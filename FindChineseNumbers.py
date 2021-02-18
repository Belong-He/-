import re
def FindChineseNumbers(str_str):
    '''
    import re
    匹配中文数字
    :param str_str: 目标字符串
    :return: 匹配结果列表
    '''
    # 零 一 二 三 四 五 六 七 八 九 十 百  千 万
    reg = '[\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u4e07]'
    res = re.findall(reg, str_str)
    num=''
    for n in res:num+=n
    return num
num=FindChineseNumbers('两秒')
print(num)