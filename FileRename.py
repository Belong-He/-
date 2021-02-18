from re import split
def rename(name):
    namepatter = r'\\|\/|\:|\*|\?|\"|<|>|\)'
    Sentences = split(namepatter, name)
    name = ''
    for i in Sentences: name += i
    return name,Sentences
if __name__=="__main__":
    while 1:
        # name='cachingFile system data will be read in bulk and cached in memory for certain operations ("core. fscache" is set to true). This provides a significant pertormance boost'
        name=input('please input name:')
        a=rename(name)[0]
        print(a)