import requests
from bs4 import BeautifulSoup
# import enchant
# checkword= enchant.Dict("en_US")#检查是否单词

def trans(word):
    try:
        # if checkword.check(word):
        r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%word)
        soup = BeautifulSoup(r.text, "lxml")
        s = soup.find(class_='trans-container')('ul')[0]('li')
        result=''
        for item in s:
            if item.text:
                result+=item.text+'\n'
        return result
        # else:
        #     return False
    except Exception as e:
        # print(e)
        return False
        # return False
        # print("Please input English!!\n")

if __name__=="__main__":
    while True:
        word=input('Please input English word!!')
        result=trans(word)
        print(result)