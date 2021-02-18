import playsound
from os import path,makedirs,remove
from aip import AipSpeech

# string1='Building EXE from EXE-00.toc completed successfully.'
# string2='那只敏捷的棕色狐狸跳过了那条懒狗。'
# dirRoot = 'SpeechLibrary'
APP_ID = '19075685'
API_KEY = 'GigBBFyuQ4U95GD9N6iPDynr'
SECRET_KEY = 'ABGVFEAcN2t0s5pmf7DhL2cPba9lWZVp'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# def winCommand(*command):
#     buf= c_buffer(255)
#     command=' '.join(command).encode(getfilesystemencoding())
#     errorCode-int(windll.winmm.mciSendStringA(command,buf,254,0))
#     if errorCode:
#         errorBuffer=c_buffer(255)
#         windll.winmm.mciSendStringA(errorCode,errorBuffer,254)
#         exceptionMessage=('\n  Error'+str(errorCode)+'for command:'
#                           '\n       '+command.decode()+
#                           '\n       '+errorBuffer.value.decode()
#                           )
#         raise PlaysoundException(exceptionMessage)
#     return buf.value

def Voice_broadcast(dirRoot,weather_forcast_txt,lang='zh',volume=5,speed=None,intonation=None,person=3):
    weather_forecast_txt = weather_forcast_txt
    # print('BaiduSpeaking：', weather_forecast_txt)
    #百度语音合成
    if weather_forcast_txt:
        result = client.synthesis(
            weather_forecast_txt,  # text:合成的文本,使用UTF-8编码,请注意文本长度必须小于1024字节
            lang,  # lang:语言,中文:zh,英文:en
            1,  # ctp:客户端信息这里就写1,写别的不好使,至于为什么咱们以后再解释
            {
                'vol': volume,  # 合成音频文件的准音量
                'spd': speed,  # 语速取值0-9,默认为5中语速
                'pit': intonation,  # 语调音量,取值0-9,默认为5中语调
                'per': person  # 发音人选择,0为女声,1为男生,3为情感合成-度逍遥,4为情感合成-度丫丫,默认为普通女
            }  # options:这是一个dict类型的参数,里面的键值对才是关键.
        )
    else:
        return False
    cahce1=dirRoot+'\BaiduSpeaking\BaiduSpeaking1.mp3'
    cahce2 = dirRoot+'\BaiduSpeaking\BaiduSpeaking2.mp3'
    if not isinstance(result, dict):
        if not path.exists(dirRoot+'\BaiduSpeaking'):
            makedirs(dirRoot+'\BaiduSpeaking')
        try:
            # if block:
            #     sleep(float(durationInMS)/1000.0)
            #     winCommand('close',alias)
            if path.exists(cahce1):
                remove(cahce1)
            with open(cahce1, 'wb') as f:
                f.write(result)
                f.close()
            if path.exists(cahce1):
                playsound.playsound(cahce1)

        except Exception as e:
            if path.exists(cahce1):
                remove(cahce1)
            print('sound_error:',e)
            with open(cahce2, 'wb') as f:
                f.write(result)
                f.close()
            try:
                if path.exists(cahce2):
                    playsound.playsound(cahce2)

            except Exception as e:
                return e
                playsound.playsound('VoiceBroadcastLibrary\ERROR.mp3')
    else:
        if result:
            # print(result['err_detail'])
            return result

if __name__=="__main__":
    while True:
        string=input('broadcast_string:')
        try:
            Voice_broadcast(string,lang='zh')
            # Voice_broadcast(string,lang='en',volume=5,speed=5,intonation=5,person=3)
        except Exception as e:
            print(e)
            continue

