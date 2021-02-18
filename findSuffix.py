import re
from os.path import splitext
from os import walk
##src="https://imgsa.baidu.com/forum/w%3D580/sign=610e48b672f0f736d8fe4c093a54b382/12de234f78f0f73665a932c80055b319e9c413da.jpg"
def matchEmail(src):
    '''Email地址'''
    Email="[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
    suffix=re.compile(Email).findall(src)
    print(suffix)
    return suffix
def matchChinese(src):
    '''单个中文字符'''
    chinese="[\u4e00-\u9fa5]"
    suffix=re.compile(chinese).findall(src)
    print(suffix)
    return suffix
def matchDoubleChar(src):
    '''双字节字符(包括中文字符)'''
    double_char="[^\x00-\xff]"
    suffix=re.compile(double_char).findall(src)
    print(suffix)
    return suffix
def matchNone(src):
    '''空白字符'''
    none="\n\s*\r"
    suffix=re.compile(none).findall(src)
    print(suffix)
    return suffix
def matchUrl(src):
    '''网址url'''
    url="[a-zA-z]+://[^\s]*"
    suffix=re.compile(url).findall(src)
    print(suffix)
    return suffix
def matchPhone(src):
    '''国内手机号码'''
    phone="\d{3}-\d{8}|\d{4}-\{7,8}"
    suffix=re.compile(phone).findall(src)
    print(suffix)
    return suffix
def matchQQnum(src):
    '''腾讯qq号'''
    QQnum="[1-9][0-9]{4,}"
    suffix=re.compile(QQnum).findall(src)
    print(suffix)
    return suffix
def matchPost(src):
    '''中国邮政编码'''
    post="[1-9]\d{5}(?!\d)"
    suffix=re.compile(post).findall(src)
    print(suffix)
    return suffix
def matchIDNum(src):
    '''18位身份证号'''
    Id_number="^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$"
    suffix=re.compile(Id_number).findall(src)
    print(suffix)
    return suffix
def matchDate(src):
    '''(年-月-日)格式日期'''
    date="([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))"
    suffix=re.compile(date).findall(src)
    print(suffix)
    return suffix
def findSuffix(src):
    suffix=re.compile(r'\.[^.\\/:*?"<>|\r\n]+$').findall(src)
    print(suffix)
    return suffix
def findsuffixfile(file_dir,suffix):
    for root, dirs, files in walk(file_dir):
        names = []
        filename=[]
        for file in files:
            if splitext(file)[1] == suffix:
                # print(splitext(file)[0])
                names.append(file)#有后缀
                filename.append(splitext(file)[0])#无后缀
    return filename,names
# r'\.[^.\\/:*?"<>|\r\n]+$'
