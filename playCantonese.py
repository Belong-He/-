# from jyutping import get
import jyutping
# from re import sub,compile
from os import path, makedirs
from shutil import move
from playsound import playsound
from Belong import myRequests
# from Belong.FanYi.Baidu import trans

dirRoot = 'MyLibrary/Cantonese library'
from Belong.SimplifiedTraditional import Simplified2Traditional


if not path.exists(dirRoot):
    # 不存在，就创建
    makedirs(dirRoot)

def download(pinyin):
    url = "http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/sound/" + pinyin + ".wav"
    content = myRequests.get_content(url)
    with open(pinyin + ".wav", 'wb')as f:
        f.write(content)


def play(character1):
    result=''
    print('简：' + character1)
    character2 = Simplified2Traditional(character1)
    print('繁：' + character2)
    pinyins = jyutping.get(character2)
    print(pinyins[0])
    for pinyin in pinyins:
        if isinstance(pinyin,list):
            for pinyin1 in pinyin:
                if not path.exists(dirRoot + '/'  + pinyin1 + '.wav'):
                    download(pinyin1)
                if path.exists(pinyin1 + '.wav'):
                    move(pinyin1 + '.wav', dirRoot  + '/' + pinyin1 + '.wav')
                playsound(dirRoot + '/'+ pinyin1 + '.wav')  # 路径不能有中文，所以翻译成英文
                result += "简体：" + character1 + '\n' + "繁体：" + character2 + '\n' + pinyin1+'\n'
        else:
            if not path.exists(dirRoot  + '/' + pinyin + '.wav'):
                download(pinyin)
            if path.exists(pinyin + '.wav'):
                move(pinyin + '.wav', dirRoot+ '/' + pinyin + '.wav')
            playsound(dirRoot + '/'  + pinyin + '.wav')#路径不能有中文，所以翻译成英文
            result += "简体：" + character1 + '\n' + "繁体：" + character2 + '\n' + pinyin
    return result


if __name__ == "__main__":
    while True:
        character = input('character:')
        for c in character:
            try:
                play(c)
            except Exception as e:
                print(e)
