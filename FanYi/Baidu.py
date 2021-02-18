#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json,re



def get_post_data(query_string):
    zh_pattern = re.compile('[\u4e00-\u9fa5]+')
    if re.search(pattern=zh_pattern, string=query_string):  # 输入的内容含有中文，则判别其为中文输入
        return {
            "from": "zh",
            "to": "en"
        }
    else:
        return {
            "from": "en",
            "to": "zh"
        }

def trans(q):
    appid = '20200322000402873'  # 填写你的appid
    secretKey = 'bIKDDc66pUTJWxT83sFT'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    # fromLang = 'auto'   #原文语种
    toLang = get_post_data(q)['to']   #译文语种
    salt = random.randint(32768, 65536)
    # q= 'apple'
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=auto' + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        # print (result['trans_result'][0]['dst'])
        return  result['trans_result'][0]['dst']

    except Exception as e:
        # print (e)
        return e
    finally:
        if httpClient:
            httpClient.close()
if __name__=='__main__':
    while True:
        string=input('requests:')
        response=trans(string)
        print(response)
        print()