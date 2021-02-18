from tkinter import Tk,Label,Text,Entry,StringVar
from requests import post
from json import loads
from pyperclip import paste
from sys import exit
from Belong.FanYi import YoudaoDictionary
# import enchant
# checkword= enchant.Dict("en_US")
wid=20

def trans(content=None):
    global wid
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data={
        'i': content,
        'doctype': 'json'
    }
    resul = YoudaoDictionary.trans(content.strip())
    if resul:
        # if resul:
        return resul
    else:
        response=post(url,data=data).text
        ret=loads(response)['translateResult']
        ts=''
        # print(ret)
        for text in ret:
            for i in text:
                ts=ts+i['tgt']
        if isinstance(ts, list):
            words=''
            for word in ts:
                words+=word
            return words.strip()
        else:
            return ts.strip()

def enterrun(t=None):
    entrywords = entry1.get()
    if entrywords:
        words=trans(entrywords)
        listb.delete(1.0, "end")
        listb.insert("insert", words.strip())
    else:
        clipwords = paste()
        result.set(clipwords)
        words =trans(clipwords)
        listb.delete(1.0, "end")
        listb.insert("insert", words.strip())


def cliprun(t=None):
    entry1.delete(0, "end")
    clipwords = paste()
    if clipwords:
        result.set(clipwords.strip())
        words =trans(clipwords)
        listb.delete(1.0, "end")
        listb.insert("insert", words.strip())
    else:
        return ''
if __name__=="__main__":
    master = Tk()
    master.title('Belong Translator')
    master.geometry('1520x260+0+540')
    master.bind('<Return>',enterrun)
    master.bind('<Control-Return>',cliprun)
    result=StringVar()
    entry1 = Entry(master, fg='black', font=('GB2312', 18),bg='light green',width=126,textvariable=result)
    entry1.grid(row=0,column=1)
    entry1.focus()
    listb  = Text(master,width=126,height=8, fg='black', font=('GB2312', 18))
    listb.grid(row=1,column=1)
    tips=Label(master,text='基于有道翻译    Alt键翻译clip文本    Enter键翻译内容输入框文本    Esc键退出\t',fg='red',font=('GB2312',18),width=92)
    tips.grid(row=2,column=1)
    master.bind('<Escape>',exit)
    master.mainloop()
