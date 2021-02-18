from os import path,makedirs
from urllib.request import urlretrieve
from playsound import playsound
# from enchant import Dict
from Belong.BaiduAip import VoiceBroadcast
from shutil import move
# checkword= Dict("en_US")
# dirRoot = 'F:\Python3.6.4\Lib\site-packages\Belong\FanYi\SpeechLibrary'
dirRoot = 'MyLibrary'

class youdao():
    def __init__(self, type=0, word='hellow'):
        word = word.lower()  # 小写
        self._type = type  # 发音方式
        self._word = word  # 单词

        self._dirRoot = dirRoot
        if 0 == self._type:
            self._dirSpeech = path.join(self._dirRoot, 'Speech_US')  # 美音库
        else:
            self._dirSpeech = path.join(self._dirRoot, 'Speech_EN')  # 英音库
        # 判断是否存在美音库
        if not path.exists(self._dirRoot+'\Speech_US'):
            # 不存在，就创建
            makedirs(self._dirRoot+'\Speech_US')
        # 判断是否存在英音库
        if not path.exists(self._dirRoot+'\Speech_EN'):
            # 不存在，就创建
            makedirs(self._dirRoot+'\Speech_EN')

    def setAccent(self, type=0):
        '''
        type = 0：美音
        type = 1：英音
        '''
        self._type = type  # 发音方式

        if 0 == self._type:
            self._dirSpeech = path.join(self._dirRoot, 'Speech_US')  # 美音库
        else:
            self._dirSpeech = path.join(self._dirRoot, 'Speech_EN')  # 英音库

    def getAccent(self):
        '''
        type = 0：美音
        type = 1：英音
        '''
        return self._type

    def down(self, word):
        '''
        下载单词的MP3
        判断语音库中是否有对应的MP3
        如果没有就下载
        '''
        word = word.lower()  # 小写
        tmp = self._getWordMp3FilePath(word)
        if tmp is None:
            self._getURL()  # 组合URL
            # 调用下载程序，下载到目标文件夹
            # print('不存在 %s.mp3 文件\n将URL:\n' % word, self._url, '\n下载到:\n', self._filePath)
            # 下载到目标地址
            # urllib.request.urlretrieve(self._url, filename=self._filePath)
            urlretrieve(self._url, filename=self._filePath)
            # print('%s.mp3 下载完成' % self._word)
        # else:
            # print('已经存在 %s.mp3, 不需要下载' % self._word)

        # 返回声音文件路径
        return self._filePath

    def _getURL(self):
        '''
        私有函数，生成发音的目标URL
        http://dict.youdao.com/dictvoice?type=0&audio=
        '''
        self._url = r'http://dict.youdao.com/dictvoice?type=' + str(
            self._type) + r'&audio=' + self._word

    def _getWordMp3FilePath(self, word):
        '''
        获取单词的MP3本地文件路径
        如果有MP3文件，返回路径(绝对路径)
        如果没有，返回None
        '''
        word = word.lower()  # 小写
        self._word = word
        self._fileName = self._word + '.mp3'
        self._filePath = path.join(dirRoot, self._fileName)

        # 判断是否存在这个MP3文件
        if path.exists(self._filePath):
            # 存在这个mp3
            return self._filePath
        else:
            # 不存在这个MP3，返回none
            return None
def downloadEN(word):
    if word:
        sp = youdao(type=1)
        sp.down(word)
        return True
    else:
        print('error')
        return False
def downloadUS(word):
    if word:
        sp = youdao(type=0)
        sp.down(word)
        return True
    else:
        print('error')
        return False
def isAllZh(s):
    '包含汉字的返回TRUE'
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False
def PlayENSound(word):
    try:
        if path.exists(dirRoot + '\Speech_EN\\' + word.strip() + '.mp3'):
            playsound(dirRoot + '\Speech_EN\\' + word.strip() + '.mp3')
            print(word.strip() + '.mp3'+':已处在')
            return True
        if not path.exists(dirRoot + '\Speech_EN\\' + word.strip() + '.mp3'):
            downloadEN(word)
        if path.exists(dirRoot + '\\' + word.strip() + '.mp3'):
            move(dirRoot + '\\' + word.strip() + '.mp3', dirRoot + '\Speech_EN\\' + word.strip() + '.mp3')
        playsound(dirRoot + '\Speech_EN\\' + word.strip() + '.mp3')
    except:
        # while True:
        try:
            result=VoiceBroadcast.Voice_broadcast(dirRoot,word.strip(),person=3)
            return result
        except Exception as e:
            words = word.split(' ')
            for wor in words:
                if not path.exists(dirRoot + '\Speech_EN\\' + wor + '.mp3'):
                    downloadEN(wor)
            for wor in words:
                playsound(dirRoot + '\Speech_EN\\' + wor + '.mp3')
            return e
def PlayUSSound(word):
    try:
        if path.exists(dirRoot + '\Speech_US\\' + word.strip() + '.mp3'):
            playsound(dirRoot + '\Speech_US\\' + word.strip() + '.mp3')
            print(word.strip() + '.mp3' + ':已处在')
            return True
        if not path.exists(dirRoot + '\Speech_US\\' + word.strip() + '.mp3'):
            downloadUS(word.strip())
        if path.exists(dirRoot + '\\' + word.strip() + '.mp3'):
            move(dirRoot +'\\'+ word.strip() + '.mp3',dirRoot + '\Speech_US\\' + word.strip() + '.mp3')
        playsound(dirRoot + '\Speech_US\\' + word.strip() + '.mp3')
        # remove(dirRoot + '\Speech_US\\' + word.strip() + '.mp3')
    except:
        # while True:
        try:
            result = VoiceBroadcast.Voice_broadcast(dirRoot,word.strip(),person=4)
            # print(result)
            return result
        except Exception as e:
            # print(e)
            words = word.strip().split(' ')
            for wor in words:
                if not path.exists(dirRoot + '\Speech_US\\' + wor + '.mp3'):
                    downloadUS(wor)
            for wor in words:
                playsound(dirRoot + '\Speech_US\\' + wor + '.mp3')
            return e
if __name__ == "__main__":
    # #Speech library
    sp = youdao()
    dirRoot = 'MyLibrary'

    while True:
        words=input('input word:')
        # downloadEN(words)
        # playsound(dirRoot + '\Speech_EN\\' + words + '.mp3')
        PlayENSound(words)
        words = input('input word:')
        # downloadEN(words)
        # playsound(dirRoot + '\Speech_EN\\' + words + '.mp3')
        PlayUSSound(words)
