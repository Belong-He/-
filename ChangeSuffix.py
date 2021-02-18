#!/usr/bin/env python
#coding:utf8
#! python3
#批量修改一个文件下的文件后缀
import sys
import os
def Rename(Path,suffix):
    # Path = input("请输入你需要操作的目录(格式如'F:\\test')：")
    filelist = os.listdir(Path)
    for files in filelist:
        Olddir = os.path.join(Path,files)
        print(files)  #打印出老的文件夹里的目录和文件
        if os.path.isdir(Olddir):  #判断是否是文件夹，是文件夹，跳过
            continue
        filename = os.path.splitext(files)[0]
        #filetype = os.path.splitext(files)[1]
        print(filename)
        Newdir = os.path.join(Path,filename + suffix)  #只要修改后缀名就可以更改成任意想要的格式
        os.rename(Olddir,Newdir)
Rename(r'F:\我的资源\Photo\AA\Storys\BlackWhite','.jpg')
