def bmm_readDict(fn):
    word_set,max_len=set(),0#集合速度快
    with open(fn,encoding='utf-8') as fo:
        for line in fo:
            line=line.strip()#去除两端空白字符
            word_set.add(line)
            if max_len<len(line):
                max_len=len(line)
    return word_set,max_len


def fmm_segment(inp,word_set,max_len):#inp即要切的字符串
    segged,res='',inp#已被切分的+未被切分
    while res:
        for i in range(max_len,0,-1):#倒序
            word=res[:i]
            if word in word_set:
                segged=segged+word+' '
                res=res[i:]
                break;
            elif i==1:
                segged=segged+word+' '
                res=res[i:]
            else:
                continue
    return segged

def bmm_segment(inp,word_set,max_len):#inp即要切的字符串
    segged,res='',inp#已被切分的+未被切分
    while res:
        for i in range(max_len,0,-1):#倒序
            word=res[-1*i::]
            if word in word_set:
                segged=word+' '+segged
                res=res[:-1*i]
                break;
            elif i==1:
                segged=word+' '+segged
                res=res[:-1*i]
            else:
                continue
    return segged

def readData(f2):
    fre_words={}
    with open(f2,encoding='utf-8') as fo2:
        for line in fo2:
            words=line.split('\t')
            if len(words)>1:
                fre_words[words[0]]=words[1]
    return fre_words

def countfre(line):
    res=0
    countfre=0
    fre_words=readData(f2)
    line=line.split('\t')
    for words in line:
        if words in fre_words:
            res+=fre_word[words]
    countfre=res/len(line)
    return countfre

def compare(fmm_line,bmm_line):
    fmm_countfre=countfre(fmm_line)
    bmm_countfre=countfre(bmm_line)
    if fmm_countfre>bmm_countfre:
        return fmm_line
    else:
        return bmm_line


fn=r"C:\Users\user\Desktop\dict.txt"
word_set,max_len=bmm_readDict(fn)
fmm_line=''
bmm_line=''
line='对语言学者来说结婚和未结婚....'
f2=r"C:\Users\user\Desktop\wordList.txt"
fmm_line=fmm_segment(line,word_set,max_len)
bmm_line=bmm_segment(line,word_set,max_len)
if fmm_line==bmm_line:
    print(fmm_line)
else:
    print(compare(fmm_line,bmm_line))

def hello_world():
    print("Hello, world!")

hello_world()

def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))
