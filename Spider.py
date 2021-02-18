import requests
import threading


# 传入的命令行参数，要下载文件的url
# url = 'http://www.nco.ncep.noaa.gov/pmb/codes/nwprod/nosofs.v3.0.4/fix/cbofs/nos.cbofs.romsgrid.nc'

def Handler(start, end, url, filename,address):
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)

    # 写入文件对应位置
    with open(address+filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)


def download_file(address, url, num_thread=500):
    r = requests.head(url)
    try:
        file_name = url.split('/')[-1]
        file_size = int(
            r.headers['content-length'])  # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
    except:
        print("检查URL，或不支持对线程下载")
        return

    # 创建一个和要下载文件一样大小的文件
    fp = open(address+file_name, "wb")
    fp.truncate(file_size)
    fp.close()

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name,'address':address})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s 下载完成' % file_name)


# if __name__ == '__main__':
#     start = datetime.datetime.now().replace(microsecond=0)
#     download_file(url)
#     end = datetime.datetime.now().replace(microsecond=0)
#     print("用时: ", end='')
#     print(end - start)





# <-------------------链接函数-------------------------->
def get_link(page):  # 寻找链接的href
    linkData = []
    for page in page.find_all('td'):
        links = page.select("a")
        for each in links:
            # if str(each.get('href'))[:1] == '/': 过滤if代码
                data=each.get('href')
                linkData.append(data)
    return(linkData)





# <---------------------各类函数----------------->
import urllib.request

from bs4 import BeautifulSoup

from findLinks import get_link

from Download import download_file

import os
import datetime
import time
import errno


def mkdir_p(path):   #递归创建多级目录
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

# def file_Down(connet,file): #小文件下载模块
#     urllib.request.urlretrieve(connet, file, Schedule)

def decice(data): #通过判断斜杠，来进行区分文件及文件夹
    a = '/'
    if a in data:
        return 1
    else:
        return 0


def gain(url):
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')  #利用soup获取网页内容
    links = get_link(soup) #获取<a href= ? 内容
    return links

def take(links,file,file_cre,connet):
    if decice(links):
        mkdir_p(file)
    else:

        start = datetime.datetime.now().replace(microsecond=0)
        download_file(file_cre, connet)
        end = datetime.datetime.now().replace(microsecond=0)
        # Handler(start, end, connet, links[childLink],file_cre1)
        print("用时: ", end='')
        print(end - start)












# <-----------主函数------------->


from urllib.parse import urljoin

from Carriage import decice
from Carriage import gain
from Carriage import take



import os

import time




def findAll(): #主函数
    url='http://www.nco.ncep.noaa.gov/pmb/codes/nwprod/nosofs.v3.0.4/'
    links=gain(url)
    print('扒取网址:'+url)

    for childLink in range(len(links)-1):
        childLink =childLink +1
        connet = urljoin(url, links[childLink]) #拼接网址路径


        file = os.path.join('D:\\Info\\Index' + "/" + links[childLink]) #拼接绝对路径
        file_cre1 = os.path.join('D:\\Info\\Index' + "/")

        print(connet)
        if os.path.isfile(file):
           print('文件已存在')
        else:
          take(links[childLink], file, file_cre1, connet)   #建立文件夹和下载操作



        if decice(links[childLink]):
            link_next = gain(connet)  # 第2次链接内的<a href=?
        else:
            continue

        print("Start : %s" % time.ctime())
        time.sleep(2)
        print("End : %s" % time.ctime())

        for child_next in range(len(link_next)-1):
            child_next =child_next +1
            connet_next=urljoin(connet,link_next[child_next]) #拼接网址路径


            fileF = os.path.join(file,link_next[child_next]) #拼接路径
            file_cre2 = file

            print(connet_next)
            if os.path.isfile(fileF):
                print('文件已存在')
            else:
                take(link_next[child_next], fileF, file_cre2, connet_next)

            if decice(link_next[child_next]):
                link_nextF = gain(connet_next)  # 第3次链接内的<a href=?
            else:
                continue

            print("Start : %s" % time.ctime())
            time.sleep(2)
            print("End : %s" % time.ctime())


            for child_nextT in range(len(link_nextF )-1):
                child_nextT = child_nextT + 1
                connet_nextT = urljoin(connet_next, link_nextF[child_nextT])



                fileT = os.path.join(fileF,link_nextF[child_nextT] )
                file_cre3=fileF

                print(connet_nextT)
                if os.path.isfile(fileT):
                    print('文件已存在')
                else:
                    take(link_nextF[child_nextT], fileT, file_cre3, connet_nextT)

                if decice(link_nextF[child_nextT]):
                    link_nextT = gain(connet_nextT)
                else:
                    continue



                for child_nextTh in range(len(link_nextT )-1):
                    child_nextTh = child_nextTh + 1
                    connet_nextTh = urljoin(connet_nextT, link_nextT[child_nextTh])

                    fileTh = os.path.join(fileT,link_nextT[child_nextTh] )
                    file_cre4=fileT

                    print(connet_nextTh)
                    if os.path.isfile(fileTh):
                        print('文件已存在')
                    else:
                        take(link_nextT[child_nextTh], fileTh, file_cre4, connet_nextTh)

                    if decice(link_nextT[child_nextTh]):
                        link_nextTh = gain(connet_nextTh)
                    else:
                        continue



                    for child_nextFo in range(len(link_nextTh) - 1):
                        child_nextFo = child_nextFo + 1
                        connet_nextFo = urljoin(connet_nextTh, link_nextTh[child_nextFo])

                        fileFo = os.path.join(fileTh, link_nextTh[child_nextFo])
                        file_cre5 = fileTh

                        print(connet_nextFo)
                        if os.path.isfile(fileFo):
                            print('文件已存在')
                        else:
                            take(link_nextTh[child_nextFo], fileFo, file_cre5, connet_nextFo)


                        if decice(link_nextTh[child_nextFo]):
                            link_nextFo = gain(connet_nextFo)
                        else:
                            continue

                        for child_nextFi in range(len(link_nextFo) - 1):
                            child_nextFi = child_nextFi + 1
                            connet_nextFi = urljoin(connet_nextFo, link_nextFo[child_nextFi])

                            fileFi = os.path.join(fileFo, link_nextFo[child_nextFi])
                            file_cre6 = fileFo

                            print(connet_nextFi)
                            if os.path.isfile(fileFi):
                                print('文件已存在')
                            else:
                                take(link_nextFo[child_nextFi], fileFi, file_cre6, connet_nextFi)



                            if decice(link_nextFo[child_nextFi]):
                                link_nextFi = gain(connet_nextFi)
                            else:
                                continue
                            for child_nextSi in range(len(link_nextFi) - 1):
                                child_nextSi = child_nextSi + 1
                                connet_nextSi = urljoin(connet_nextFi, link_nextFi[child_nextSi])

                                fileSi = os.path.join(fileFi, link_nextFi[child_nextSi])
                                file_cre7 = fileFi

                                print(connet_nextSi)
                                if os.path.isfile(fileSi):
                                    print('文件已存在')
                                else:
                                    take(link_nextFi[child_nextSi], fileSi, file_cre7, connet_nextSi)


                                if decice(link_nextFi[child_nextSi]):
                                    link_nextSi = gain(connet_nextSi)
                                else:
                                    continue
                                for child_nextSe in range(len(link_nextSi) - 1):
                                    child_nextSe = child_nextSe + 1
                                    connet_nextSe = urljoin(connet_nextSi, link_nextSi[child_nextSe])

                                    fileSe = os.path.join(fileSi, link_nextSi[child_nextSe])
                                    file_cre8 = fileSi

                                    print(connet_nextSe)
                                    if os.path.isfile(fileSe):
                                        print('文件已存在')
                                    else:
                                        take(link_nextSi[child_nextSe], fileSe, file_cre8, connet_nextSe)



                                    if decice(link_nextSi[child_nextSe]):
                                        link_nextSe = gain(connet_nextSe)
                                    else:
                                        continue

                                    for child_nextEi in range(len(link_nextSe) - 1):
                                        child_nextEi = child_nextEi + 1
                                        connet_nextEi = urljoin(connet_nextSe, link_nextSe[child_nextEi])

                                        fileEi = os.path.join(fileSe, link_nextSe[child_nextEi])
                                        file_cre9 = fileSe

                                        print(connet_nextEi)
                                        if os.path.isfile(fileEi):
                                            print('文件已存在')
                                        else:
                                            take(link_nextSe[child_nextEi], fileEi, file_cre9, connet_nextEi)


                                        if decice(link_nextSe[child_nextEi]):
                                            link_nextEi = gain(connet_nextEi)
                                        else:
                                            continue

                                        for child_nextNi in range(len(link_nextEi) - 1):
                                            child_nextNi = child_nextNi + 1
                                            connet_nextNi = urljoin(connet_nextEi, link_nextEi[child_nextNi])

                                            fileNi = os.path.join(fileEi, link_nextEi[child_nextNi])
                                            file_cre10 = fileEi

                                            print(connet_nextNi)
                                            if os.path.isfile(fileNi):
                                                print('文件已存在')
                                            else:
                                                take(link_nextEi[child_nextNi], fileNi, file_cre10, connet_nextNi)


                                            if decice(link_nextEi[child_nextNi]):
                                                link_nextNi = gain(connet_nextNi)
                                            else:
                                                continue






#<————————————————————main函数——————————————————————>
from way import findAll



if __name__ == '__main__':
    findAll()