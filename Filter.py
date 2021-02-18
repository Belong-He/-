import os
import sys
# suffix=[".jpg",".txt"] #后缀，设置过滤后的文件类型 当然可以设置多个类型
def remove_suffix_file(path,suffix):
    '''删除给定后缀的文件'''
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(path):
        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in suffix:
                result.append(apath)
                os.remove(apath)
    return result
# print(Type_Filter("E:\myTest"))

def remove_size_file(path,Size=[0,None]):
    '''
    删除指定大小的文件
    以KB算的
    :param path:
    :param Size:
    :return:
    '''
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        size = os.path.getsize(fullName)
        if Size[0]*1024< size < Size[1]*1024:
            os.remove(fullName)
            print(filename,size)
def Rename_suffix(Path,suffix):#改後綴
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
