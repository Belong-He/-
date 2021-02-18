from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '18427191'  # '何炳良的App ID'
API_KEY = 'rAcMd57NMhBTU7xSEl55ijeP'  # '你的 Api Key'
SECRET_KEY = 'fIkxQZYtUVwYZKH3DayMK1tjoGkDHFpk'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
# filepath = r'E:\我的资源\Python\Python项目\项目\百度aip\语音技术\\command.wav'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
languages = {
    '普通话(支持简单的英文识别)': '1536',
    '普通话(纯中文识别)': '1537',
    '英语': '1737',
    '粤语': '1637',
    '四川话': '1837',
    '普通话远场': '1936'
}


# for language in languages:print(language)
# lang=input('please input language:')
# 3300	用户输入错误	输入参数不正确	请仔细核对文档及参照demo，核对输入参数
# 3301	用户输入错误	音频质量过差	请上传清晰的音频
# 3302	用户输入错误	鉴权失败	token字段校验失败。请使用正确的API_KEY 和 SECRET_KEY生成。或QPS、调用量超出限额。或音频采样率不正确（可尝试更换为16k采样率）。
# 3303	服务端问题	语音服务器后端问题	请将api返回结果反馈至论坛或者QQ群
# 3304	用户请求超限	用户的请求QPS超限	请降低识别api请求频率 （qps以appId计算，移动端如果共用则累计）
# 3305	用户请求超限	用户的日pv（日请求量）超限	请“申请提高配额”，如果暂未通过，请降低日请求量
# 3307	服务端问题	语音服务器后端识别出错问题	目前请确保16000的采样率音频时长低于30s。如果仍有问题，请将api返回结果反馈至论坛或者QQ群
# 3308	用户输入错误	音频过长	音频时长不超过60s，请将音频时长截取为60s以下
# 3309	用户输入错误	音频数据问题	服务端无法将音频转为pcm格式，可能是长度问题，音频格式问题等。 请将输入的音频时长截取为60s以下，并核对下音频的编码，是否是16K， 16bits，单声道。
# 3310	用户输入错误	输入的音频文件过大	语音文件共有3种输入方式： json 里的speech 参数（base64后）； 直接post 二进制数据，及callback参数里url。 分别对应三种情况：json超过10M；直接post的语音文件超过10M；callback里回调url的音频文件超过10M
# 3311	用户输入错误	采样率rate参数不在选项里	目前rate参数仅提供16000，填写4000即会有此错误
# 3312	用户输入错误	音频格式format参数不在选项里	目前格式仅仅支持pcm，wav或amr，如填写mp3即会有此错误
def EMandarin(path):  # 普通话(支持简单的英文识别)
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1536,
    })
    try:
        str = text['result'][0]
        return str
    except Exception as e:
        print(e)
        return ''


def PureMandarin(path):  # 普通话(纯中文识别)
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1537,
    })
    try:
        str = text['result'][0]
        return str
    except Exception as e:
        print(e)
        return ''


def English(path):  # 英语
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1737,
    })
    try:
        str = text['result'][0]
        print(text)
        return str
    except Exception as e:
        print(e)
        return ''


def Cantonese(path):  # 粤语
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1637,
    })
    try:
        str = text['result'][0]
        return str
    except Exception as e:
        print(e)
        return ''


def Sichuan(path):  # 四川话
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1837,
    })
    try:
        str = text['result'][0]
        return str
    except Exception as e:
        print(e)
        return ''


def FarMandarin(path):  # 普通话远场
    # path=filepath
    text = client.asr(get_file_content(path), 'pcm', 16000, {
        'dev_pid': 1936,
    })
    try:
        str = text['result'][0]
        print(text)
        return str
    except Exception as e:
        print(e)
        return ''
