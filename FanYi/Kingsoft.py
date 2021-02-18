from requests import post
from sys import exit
from json import loads
from pyperclip import paste
from tkinter import Tk,Entry,Text,Label,StringVar


url = "http://fy.iciba.com/ajax.php?a=fy"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
    "X-Requested-With": "XMLHttpRequest"
}
def get_data(words):
    """
    请求数据
    :param url:
    :return:
    """
    post_data = {
        "f": "auto",
        "t": "auto",
        "w": words
    }
    response = post(url, data=post_data, headers=headers)
    return response.text

def show_translation(words,t=None):
    response = get_data(words)
    json_data = loads(response, encoding='utf-8')
    if json_data['status'] == 0:
        translation = json_data['content']['word_mean']
    elif json_data['status'] == 1:
        translation = json_data['content']['out']
    else:
        translation = None
    return translation

def trans(text):
    translation=show_translation(text)
    if isinstance(translation,list):
        words=''
        for word in translation:
            words+=word+'\n'
        # print(words)
        return words.strip()
    else:
        # print(translation)
        return translation.strip()
def enterrun(t=None):
    entrywords= entry1.get()
    if entrywords:
        words=trans(entrywords.strip())
        listb.delete(1.0, "end")
        listb.insert("insert", words.strip())
        listb.insert("insert", '\n')
    else:
        clipwords = paste()
        result.set(clipwords)
        words=trans(clipwords.strip())
        listb.delete(1.0, "end")
        listb.insert("insert", words.strip())
        listb.insert("insert", '\n')
def cliprun(t=None):
    entry1.delete(0, "end")
    clipwords=paste()
    if clipwords:
        result.set(clipwords.strip())
        words=trans(clipwords.strip())
        listb.insert("insert", words.strip())
        listb.insert("insert", '\n')
    else:
        return ''

if __name__ == "__main__":
    master = Tk()
    master.title('Belong Translator')
    master.geometry('1520x260+0+540')
    master.bind('<Return>',enterrun)
    master.bind('<Control-Return>',cliprun)
    result=StringVar()
    entry1 = Entry(master, fg='black', font=('GB2312', 18),bg='light green',width=126,textvariable=result)
    entry1.grid(row=0,column=0)# 在窗口显示出来,放在第0行，第1专栏
    entry1.focus()
    listb  = Text(master,width=126,height=8, fg='black', font=('GB2312', 18))
    listb.grid(row=1,column=0)
    tips=Label(master,text='基于金山词霸    Alt键翻译clip文本    Enter键翻译内容输入框文本    Esc键退出\t',fg='green',font=('GB2312',18),width=126)
    tips.grid(row=2,column=0)
    master.bind('<Escape>',exit)
    master.mainloop()

