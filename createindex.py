import os
import re
from nltk.stem import WordNetLemmatizer
import time
import numpy as np

lemmatizing=WordNetLemmatizer ()

def listofwords():
    dict={}
    path = os.getcwd()
    files=os.listdir(path+"\Trump Speechs")
    qq=re.compile('\W+')
    y=re.compile("\d+")
    global filelist
    filelist=[]
    fo=open("StopwordList.txt")
    x=fo.read()
    stoplistt=x.split()
    fo.close()
    for f in files:
        fname=path+"\Trump Speechs\\"
        fname+=f
        lines=open(fname,"r")
        next(lines)
        wordslist=lines.read()
        x=qq.split(wordslist.casefold())
        name=y.findall(f)
        name=int(name[0])
        for i in x:
            if i in stoplistt:
                continue
            i=lemmatizing.lemmatize(i)
            if i not in dict:
                dict[i]=[]
                dict[i].append(name)
            else:
                if name not in dict[i]:
                    dict[i].append(name)
        lines.close()
        filelist.append(name)
        fname=""
    
    tempdict={}
    wordfile=open("invertedindex.txt","w")
    for key in sorted(dict.keys()):
        wordfile.write(str(key)+" "+str(dict[key])+'\n')
        tempdict[key]=dict[key]
    wordfile.close()   
    return tempdict

if __name__ == "__main__":
    listofwords()