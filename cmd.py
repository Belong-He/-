from subprocess import Popen,PIPE,STDOUT
def runCmd(cmd) :
    res = Popen(cmd, shell=True,stdout=PIPE,stderr=STDOUT)
    while True:
        line = res.stdout.readline()
        if line:
            try:
                print(str(line, 'utf-8'))
            except UnicodeDecodeError:
                print(str(line, 'gbk'))
            except Exception as e:
                print(e)
            if Popen.poll(res) == 0:  # 判断子进程是否结束
                break
        else:
            break
