import shutil
from os.path import exists,splitext
from os import remove,makedirs,walk
from re import split
# from Belong.findSuffix import findsuffixfile

def dist_file_name(file_dir):
    file_path=[]
    file_names=[]
    dir_path = []
    dir_names=[]
    for root, dirs, files in walk(file_dir):
        # #print(root)  # 当前目录路径
        # #print(dirs)  # 当前路径下所有子目录
        # #print(files)  # 当前路径下所有非目录子文件
        for file in files:
            # #print(file)
            file_names.append(file)
            file_path.append(root+'\\'+file)
        for dir in dirs:
            # #print(dir)
            # #print(root+'\\'+dir)
            dir_names.append(dir)
            dir_path.append(root+'\\'+dir)
    # #print(file_path)
    # #print(file_names)
    return file_path,file_names,dir_path,dir_names

def Moving(to_path,file_paths_a,file_paths_b):
    for path,name in zip(file_paths_a,file_paths_b):
        if exists(to_path+'\\'+path):
            remove(to_path+'\\'+path)
        # #print(path)
        shutil.move(path, to_path)
#移动文件夹下 所有文件和文件夹
def move_all_file(frompath,to_path):
    file_paths=dist_file_name(frompath)
    Moving(to_path,file_paths[0],file_paths[1])
    Moving(to_path,file_paths[2],file_paths[3])
#移动文件夹下 所有文件(没弄好)
def move_files(frompath,to_path):
    file_paths=dist_file_name(frompath)
    # Moving(to_path, file_paths[0], file_paths[1])
#移动文件夹下 所有文件夹
def move_dirs(frompath,to_path):
    file_paths=dist_file_name(frompath)
    Moving(to_path,file_paths[2],file_paths[3])
#移动文件夹下 指定后缀文件
def move_appoint_file(frompath,to_path,suffix):
    file_paths=dist_file_name(frompath)
    for file_path,file_name in zip(file_paths[0],file_paths[1]):
        parten='\.'
        FileSuffix=split(parten,file_name)
        # if len(FileSuffix)==1 and suffix=='':
        if len(FileSuffix)==1 and suffix=='':
            if exists(to_path + '\\' + file_name):
                remove(to_path + '\\' + file_name)
            #print(file_path)
            shutil.move(file_path, to_path)
        # findsuffixfile(frompath,suffix)
        if len(FileSuffix)>1:
            if FileSuffix[-1]==suffix:
                if exists(to_path+'\\'+file_name):
                    remove(to_path+'\\'+file_name)
                #print(file_path)
                shutil.move(file_path, to_path)
#移动指定文件
def move_file(frompath,to_path):
    file_paths=dist_file_name(frompath)
    for file_path,file_name in zip(file_paths[0],file_paths[1]):
        try:
            if exists(to_path+'\\'+file_name):
                remove(to_path+'\\'+file_name)
            shutil.move(file_path, to_path)
        except Exception as e:
            print(e)
if __name__=="__main__":

    while 1:
        frompath = input('FromPath:')
        if not exists(frompath):
            # frompath=input()
            #print("路径不存在："+frompath)
            topathornot = input("是否创建路径：(y/n)" + frompath)
            if topathornot == 'y':
                makedirs(frompath)
                break
        else:
            #print('路径存在')
            break
    while 1:
        topath = input('ToPath:')
        if not exists(topath):
            #print("路径不存在："+topath)
            topathornot=input("是否创建路径：(y/n)" + topath)
            if topathornot=='y':
                makedirs(topath)
                break
        else:
            #print('路径存在')
            break
    while 1:
        movewhat = input('移动目录下 所有文件和文件夹\n移动目录下(包括子目录) 所有文件(没弄好)\n移动目录下 所有文件夹\n移动目录下(包括子目录) 指定后缀文件\n请选择：')
        if movewhat=='移动目录下 所有文件和文件夹':
            move_all_file(frompath, topath)
            break

        if movewhat=='移动目录下 所有文件夹':
            move_dirs(frompath, topath)
            break
        if movewhat=='移动目录下(包括子目录) 指定后缀文件':
            suffix=input('请输入后缀(如 txt)：')
            move_appoint_file(frompath, topath, suffix)
            break
        if movewhat=='移动目录下(包括子目录) 所有文件':
            move_files(frompath, topath)
            break
        else:
            print('请重新选择')


# G:\Python\Python项目\爬得的资料\爬blogsPython
# G:\Python\Python项目\爬得的资料\11