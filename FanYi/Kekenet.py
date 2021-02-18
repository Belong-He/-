from Belong import myRequests
from lxml import etree

def trans(searchname):
    # searchname = 'hulk'
    print(searchname.title())
    a = searchname.split(' ')
    if len(a) > 1:
        search_name = '+'.join(a)
    else:
        search_name = searchname
    url='http://dict.kekenet.com/en/'+search_name
    text=myRequests.get_text(url)
    html=etree.HTML(text)
    result=html.xpath('string(/html/body/div[3])')
    a=result.strip().split('\n')
    # print(a)
    a=[x.strip() for x in a]
    a=[x.strip() for x in a if x.strip()!='']
    # print(a)
    output=''
    for i in a:
        if i.strip()=='在线背单词':
            break
        # print(i)
        output+=i+'\n'
    # if output=='抱歉，没有找到与您查询的“想你”相符的字词。':
    #     url='http://fy.kekenet.com/'
    return output
if __name__=="__main__":
    while True:
        word=input('please input:')
        output=trans(word)
        print(output)