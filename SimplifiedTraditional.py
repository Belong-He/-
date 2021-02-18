from Belong.lanconv import *

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence
#FamiliarTraditional
def Simplified2Traditional(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence
def AutoTrans(word):
    Traditional_sentence = Simplified2Traditional(word)
    Simplified_sentence = Traditional2Simplified(word)
    if Traditional_sentence!= word:
        return Traditional_sentence
    else:
        return Simplified_sentence
if __name__=="__main__":
    #traditional_sentence = '憂郁的臺灣烏龜'
    while True:
        chioce=input('1:Simplified to Traditional\n2:Traditional to Simplified\nPlease chioce Mode:')
        if chioce=='exit':
                    break
        if chioce=="1":
            while True:
                string=input('input:')
                if string=='exit':
                    break
                traditional_sentence = string
                simplified_sentence = Simplified2Traditional(traditional_sentence)
                print(simplified_sentence)
        else:
            while True:
                string=input('input:')
                if string=='exit':
                    break
                traditional_sentence = string
                simplified_sentence = Traditional2Simplified(traditional_sentence)
                print(simplified_sentence)
