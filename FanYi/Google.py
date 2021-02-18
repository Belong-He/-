from requests import get
from json import loads
from re import compile,sub
from execjs import compile as Compile # 必须，需要先用pip 安装，用来执行js脚本
from urllib.parse import quote
from sys import exit
from tkinter import Tk,Entry,Text,Label,StringVar
from pyperclip import paste
from Belong import myRequests
# 用来判断是否需要打印日志
debug = True

class Py4Js:

    def __init__(self):
        self.ctx = Compile(""" 
            function TL(a) { 
                var k = ""; 
                var b = 406644; 
                var b1 = 3293161072;       
                var jd = "."; 
                var $b = "+-a^+6"; 
                var Zb = "+-3^+b+-f";    
                for (var e = [], f = 0, g = 0; g < a.length; g++) { 
                    var m = a.charCodeAt(g); 
                    128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
                    e[f++] = m >> 18 | 240, 
                    e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
                    e[f++] = m >> 6 & 63 | 128), 
                    e[f++] = m & 63 | 128) 
                } 
                a = b; 
                for (f = 0; f < e.length; f++) a += e[f], 
                a = RL(a, $b); 
                a = RL(a, Zb); 
                a ^= b1 || 0; 
                0 > a && (a = (a & 2147483647) + 2147483648); 
                a %= 1E6; 
                return a.toString() + jd + (a ^ b) 
            };      
            function RL(a, b) { 
                var t = "a"; 
                var Yb = "+"; 
                for (var c = 0; c < b.length - 2; c += 3) { 
                    var d = b.charAt(c + 2), 
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
                } 
                return a 
            }
        """)

    def get_tk(self, text):
        return self.ctx.call("TL", text)


def build_url(text, tk, tl='zh-CN'):
    """
    需要用转URLEncoder
    :param text:
    :param tk:
    :param tl:
    :return:
    """
    return 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=' + tl + '&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&source=btn&ssel=0&tsel=0&kc=0&tk=' \
           + str(tk) + '&q=' + quote(text, encoding='utf-8')


def translate(js, text, tl='zh-CN'):
    """
    tl为要翻译的语言
    de：德语
    ja：日语
    sv：瑞典语
    nl：荷兰语
    ar：阿拉伯语
    ko：韩语
    pt：葡萄牙语
    zh-CN：中文简体
    zh-TW：中文繁体
    """

    header = {
        'authority': 'translate.google.cn',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        # 'cookie': '_ga=GA1.3.110668007.1547438795; _gid=GA1.3.791931751.1548053917; 1P_JAR=2019-1-23-1; NID=156=biJbQQ3j2gPAJVBfdgBjWHjpC5m9vPqwJ6n6gxTvY8n1eyM8LY5tkYDRsYvacEnWNtMh3ux0-lUJr439QFquSoqEIByw7al6n_yrHqhFNnb5fKyIWMewmqoOJ2fyNaZWrCwl7MA8P_qqPDM5uRIm9SAc5ybSGZijsjalN8YDkxQ',
         'cookie':'_ga=GA1.3.110668007.1547438795; _gid=GA1.3.1522575542.1548327032; 1P_JAR=2019-1-24-10; NID=156=ELGmtJHel1YG9Q3RxRI4HTgAc3l1n7Y6PAxGwvecTJDJ2ScgW2p-CXdvh88XFb9dTbYEBkoayWb-2vjJbB-Rhf6auRj-M-2QRUKdZG04lt7ybh8GgffGtepoA4oPN9OO9TeAoWDY0HJHDWCUwCpYzlaQK-gKCh5aVC4HVMeoppI',
        # 'cookie': '',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'user-agent':myRequests.get_agent(),
        'x-client-data': 'CKi1yQEIhrbJAQijtskBCMG2yQEIqZ3KAQioo8oBCL+nygEI7KfKAQjiqMoBGPmlygE='
    }
    url = build_url(text, js.get_tk(text), tl)
    try:
        r = get(url, headers=header)
        result = loads(r.text)
        r.encoding = "UTF-8"
        if debug:
            return result
    except Exception as e:
        if debug:
            translate_error=url+'\n'
            translate_error+="翻译\n" + text + "\n失败\n"
            translate_error+="错误信息:\n"
            translate_error+=e
            listb.delete(1.0, "end")
            listb.insert("insert", translate_error)
            return False


def get_translate(word, tl):
    js = Py4Js()
    translate_result = translate(js, word, tl)
    return translate_result
def isAllZh(s):
    '包含汉字的返回TRUE'
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False
def minisimplify(results,language):
    if language == 'zh-CN':
        b =''
        for i in results[0]:
            if i[0]:
                b += i[0]
        b+='\n'
        if results[1]:
            for i in results[1]:
                b +=  '\n' + i[0]+'\n'
                for t in i[2]:
                    b +=  t[0] + '：' + ','.join(t[1])+'\n'
            try:
                b+='\n'
                for i in results[5]:
                    b += i[0]+'\n'
                    for j in i[2]:
                        b += j[0]+'，'
                    b += ' \n'
            except:
                pass
        return b
    else:
        b = ''
        for i in results[0]:
            if i[0]:
                b+=i[0]
        b += '\n'
        try:
            if results[1]:
                c=''
                for i in results[1]:
                    c = '\n'+ i[0]+ '\n'
                    for t in i[2]:
                        c +=  (t[0] + '：' + ','.join(t[1]))+ '\n'
                if c:
                    b+=c
        except:
            pass
        try:
            for i in results[5]:
                num = 1
                for j in i[2]:
                    b+='\n'+(str(num)+'：'+j[0])
                    num+=1
                b+=' \n'
        except:
            pass
        return b.strip()

def simplify(results,language):
    if language == 'zh-CN':#翻译成中文
        b = '<<翻译>>'.center(125)+'-'*126
        for i in results[0]:
            if i[0]:
                b += i[0]
        b += '\n'+'<<原文>>'.center(127)+'-'*126
        for i in results[0]:
            if i[1]:
                b += i[1]
        b += '\n\n'+'<<拼音>>'.center(127)+'-'*126
        for i in results[0]:
            try:
                if i[2]:
                    b += i[2].center(126)
            except:
                pass

        a=''
        for i in results[0]:
            try:
                if i[3]:
                    a += i[3].center(126)
            except:
                pass
        if a:
            b += '\n\n' + '<<发音>>'.center(125) + '-' * 126+a

        if results[1]:
            b +=  '\n\n' + '*' * 126 + '\n'+'<<词性>>'.center(125)+'\n' + '*'*126
            for i in results[1]:
                b +=  '\n' + i[0].center(118)+'\n'+'-'*126
                b +=  ','.join(i[1])+'\n'
                # 其他单词
                for t in i[2]:
                    b +=  t[0] + '：' + ','.join(t[1])+'\n'
            try:
                b += '\n' +'*' * 126 + '<<句子更多翻译>>'.center(120)  + '*' * 126
                for i in results[5]:
                    b += i[0].center(126)
                    for j in i[2]:
                        b += j[0].center(125)
                    b += ' \n'

            except:
                pass
            try:
                c =  '\n'+'*' * 126+'<<同义词>>'.center(123)  + '*' * 126 + '\n'
                d=''
                num=1
                for i in results[11]:
                    part=str(num)+'：'+i[0]
                    d += part.center(118) +'\n'+'-'*126
                    num+=1
                    for j in i[1]:
                        d += (',  '.join(j[0])+'。').center(124) + '\n\n'
                    d+='\n'
                if d:
                    b+=c+d
            except:
                pass
            try:
                b +=  '*'*126+'\n'+'<<定义>>'.center(124) + '\n'+'*'*126+'\n'
                for t in results[12]:
                    b += t[0].center(118)+'\n'+'-'*126
                    num=1
                    for t in t[1]:
                        b += str(num)+'：'+t[0] + '\n\n'
                        num+=1
                        try:
                            b += '\t'+t[2] + '\n\n'
                        except:
                            pass
            except:
                pass
            try:
                c= '\n'+'*'*126+'\n'+'<<例句>>'.center(124) + '\n'+'*'*126+'\n'
                num=1
                d=''
                for t in results[13][0]:
                    ll = compile('<b>(.*?)</b>').findall(t[0])[0]
                    rr = sub('<b>.*?</b>', ll, t[0])
                    d +=str(num)+'：'+ rr + '\n\n'
                    num+=1
                if d:
                    b+=c+d
            except:
                pass
        return b


    else:#翻译成英文
        b = '<<翻译>>'.center(124)+'-'*126
        for i in results[0]:
            if i[0]:
                b+=i[0]
        b += '\n\n'+'<<原文>>'.center(124)+'-'*126
        for i in results[0]:
            if i[1]:
                b +=i[1]
        b += '\n\n'+'<<拼音>>'.center(124)+'-'*126
        for i in results[0]:
            if i[3]:
                b +=i[3].center(126)
        try:
            if results[1]:
                d= '\n\n' + '*' * 126 + '\n'+'<<词性>>'.center(124)+'\n' + '*' * 126
                c=''
                for i in results[1]:
                    c = '\n'+ i[0].center(124)+'-'*126
                    # 其他单词
                    for t in i[2]:
                        c +=  (t[0] + '：' + ','.join(t[1])).center(124) + '\n'
                if c:
                    b+=d+c
        except:
            pass
        try:
            b +='\n\n'+'*'*126+'<<单句翻译>>'.center(122)+'*'*126+'\n'
            for i in results[5]:
                b+=i[0].center(122)+'\n'
                num = 1
                for j in i[2]:
                    b+=(str(num)+'：'+j[0]).center(124)
                    num+=1
                b+=' \n'
        except:
            pass
        return b
def trans(text,t=None):
    if isAllZh(text):#全是汉字时翻译成英文
        Complication=get_translate(text, 'en')
        return simplify(Complication,'en')
    else:
        Complication=get_translate(text, 'zh-CN')
        return simplify(Complication, 'zh-CN')
def minitrans(text,t=None):
    if isAllZh(text):#全是汉字时翻译成英文
        Complication=get_translate(text, 'en')
        return minisimplify(Complication,'en')
    else:
        Complication=get_translate(text, 'zh-CN')
        return minisimplify(Complication, 'zh-CN')
def main(t=None):
    entrywords = entry1.get()
    if entrywords:
        results = trans(entrywords)
        listb.delete(1.0, "end")
        listb.insert("insert", results)
    else:
        clipwords = paste()
        result.set(clipwords)
        translation = trans(clipwords)
        listb.delete(1.0, "end")
        listb.insert("insert", translation)
def clip(t=None):
    clipwords = paste()
    result.set(clipwords)
    translation = trans(clipwords)
    listb.delete(1.0, "end")
    listb.insert("insert", translation)
if __name__=="__main__":
    master = Tk()
    master.title('Belong Translator')
    master.geometry('1520x790+0+0')
    result = StringVar()
    entry1 = Entry(master, fg='black', font=('GB2312', 18), bg='light green', width=126, textvariable=result)
    entry1.grid(row=0, column=0)  # 在窗口显示出来,放在第0行，第1专栏
    entry1.focus()
    listb = Text(master, width=126, height=30, fg='black', font=('GB2312', 18))
    listb.grid(row=1, column=0)
    tips = Label(master, text='Google翻译    Enter翻译输入框内容   Ctrl+Enter翻译Clip内容    Esc键退出', fg='green',
                 font=('GB2312', 18), width=126)
    tips.grid(row=2, column=0)
    master.bind('<Return>', main)
    master.bind('<Control-Return>', clip)
    master.bind('<Escape>', exit)
    master.mainloop()
