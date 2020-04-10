import os
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import re
from nltk.stem import WordNetLemmatizer
import time
import numpy as np
import createindex
import math
import operator
import ast
Dictionary=createindex.returndict()

def stopwordlist():
    fo=open("StopwordList.txt","r")
    x=fo.read()
    stoplist=x.split()
    fo.close()
    return stoplist

def listofwords():
    lst=list(Dictionary.keys())
    lst.sort()
    return lst

lemmatizing=WordNetLemmatizer ()
stoplist=stopwordlist()
lstofword=listofwords()    #list of the word in entire dataset

def get_df(): 
    templist=[]
    for i in range(len(lstofword) ):
        templist.append(0)
    for i in lstofword:
        templist[lstofword.index(i)]=( len(Dictionary[i]))
    return templist

dflist=get_df()

N=56

def VSMofDoc():
    dict={}                      #dictionary for VSM
    temp=[]                     #temp list for document vector
    path = os.getcwd()          #returns the path of the current folder 
    files=os.listdir(path+"\Trump Speechs")         #returns all the files present in the specified directory
    qq=re.compile('\W+')                #for splitting words
    y=re.compile("\d+")                 # for getting the int part of the file name 
    global filelist                        # list of file name
    filelist=[]
    for f in files:                     # for each file present in the directory
        for jj in range(len(lstofword)):    # initilizing the vector with zero 
            temp.append(0)
        fname=path+"\Trump Speechs\\"
        fname+=f
        lines=open(fname,"r")               #open a file 
        next(lines)
        wordslist=lines.read()              #read the deta from the file
        x=qq.split(wordslist.casefold())        # casefolding and then splitting the words
        name=y.findall(f)
        name=int(name[0])
        for i in x:
            if i in stoplist:
                continue
            i=lemmatizing.lemmatize(i)      #lemmatizing the word
            indexofterm=lstofword.index(i)
            temp[indexofterm]+=1
        dict[f]=temp.copy()
        lines.close()
        filelist.append(name)
        fname=""
        temp.clear()
    
    for ii,j in dict.items():
        for iii in range(len(j)):
            if j[iii]!=0:
                product=( j[iii] )*( math.log( 56/dflist[iii] ,10 ) )
                j[iii]=product
      
    wordfile=open("VSM.txt","w")
    wordfile.write(str(dict))
    wordfile.close()
    # return dict
    return
VSMofDoc()

f=open("VSM.txt","r")
r=f.read()
dict=ast.literal_eval(r)
f.close()


def calculateranking(query):
    qq=re.compile('\W+')
    weightlist=[]
    query=qq.split(query.casefold())
    parsedquery=[]
    queryvector=[]
    for i in query:
        if i in stoplist:
            continue
        i=lemmatizing.lemmatize(i.casefold())
        if i in lstofword:
            parsedquery.append(i)
        else:
            continue 
        
    for jj in range(len(lstofword)):    # initilizing the vector with zero 
        queryvector.append(0)  
             
    for x in parsedquery:
        queryvector[lstofword.index(x)]+=1
    
    for ii in range(len(queryvector)):
        idf=( math.log( 56/dflist[ii] ,10) )
        queryvector[ii]=queryvector[ii]*idf
        
    for x in parsedquery:
        print(queryvector[lstofword.index(x)])
        
    for key,docvector in dict.items():
        numerator=np.dot(queryvector,docvector)
        magnitude_of_Query_vector=np.linalg.norm(queryvector)
        magnitude_of_Doc_vector=np.linalg.norm(docvector)
        denominator=(magnitude_of_Query_vector)*(magnitude_of_Doc_vector)
        # ans=math.cos(numerator/denominator)
        ans=numerator/denominator
        answer=(key,ans)
        weightlist.append(answer)
        del answer
        
    weightlist.sort(key=operator.itemgetter(1),reverse=True)
    templist=[]
    alpha=0.0005
    for y in weightlist:
        if y[1]<alpha:
            break
        t=(y[0],y[1])
        templist.append(t)
        # templist.append(y[0])
    return templist
        
        
def searchquery():
    t0=time.time()
    strr=entry.get()
    global answer_value
    answer.delete(1.0,END)
    answer_value=calculateranking(strr)
    # elif c=="error":
    #     messagebox.showerror("QUERY ERROR", "For Positional Query : Query must be of the form : word1 word2 /distance(in int) \n For Boolean Query (AND OR NOT must be in caps, every word must be seperated by a space) :")
    t1=time.time()
    for i in answer_value:
        answer.insert(END,'')
        answer.insert(END,i)
        answer.insert(END,'\n')
    
    finaltime=t1-t0
    ft="{0:.8f}".format(finaltime)
    r.delete(1.0,END)
    r.insert(END,"About "+str(len(answer_value)) +" result(s)  ("+str(ft)+" seconds)")
    answer.pack()

def showinformation():
    messagebox.showinfo("HELP","For Positional Query : Query must be of the form : word1 word2 /distance(in int) \n For Boolean Query (AND OR NOT must be in caps, every word must be seperated by a space) :")
    
root=tk.Tk() 
root.geometry("900x700")
root.resizable(0,0)
root.title("Retrieve Information")
root.configure(background="steel blue")
canvas=Canvas(root,width=900, height=246)
path = os.getcwd()
image=ImageTk.PhotoImage(Image.open(path+"/bgg.jpg"))
canvas.create_image(0,0,anchor=NW, image=image)
canvas.pack()

topframe=Frame(root, borderwidth=2)
entry=Entry(topframe,justify=CENTER,width=65,bd=10,font=("Arial",12,"bold"))
entry.pack(side=LEFT)
button=Button(topframe,text="SEARCH", command=searchquery,width=10,bd=4, font=("Arial",12,"bold"))
button.pack(side=RIGHT)
img=ImageTk.PhotoImage(Image.open(path+"/info.png"))
info=Button(topframe,image=img, command=showinformation,width=25, bd=3)
info.pack(side=RIGHT)
topframe.pack(side=TOP,pady=20)

bottomframe=Frame(root)
r=Text(bottomframe,width = 100,height=1, font=("Helvetica", 15, "bold", "italic"), bg="steel blue",bd=0,insertborderwidth=0,fg="white")
r.pack( side=TOP )
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottomframe,yscrollcommand=scroll.set,insertborderwidth=3, bd=5,width = 40, height=4, font=("Helvetica", 15, "bold"))
scroll.config(command=answer.yview)
answer.pack(expand=TRUE, fill=BOTH )
bottomframe.pack(side=BOTTOM, fill=BOTH, expand=TRUE,pady=20, padx=55)
l1=Label()

root.mainloop()