# import os
# from tkinter import * 
# from tkinter import messagebox
# import tkinter as tk
# from PIL import Image, ImageTk
# import re
# from nltk.stem import WordNetLemmatizer
# import time
# import numpy as np
# import createindex

# Dictionary=createindex.listofwords()
# def stopwordlist():
#     fo=open("StopwordList.txt","r")
#     x=fo.read()
#     stoplist=x.split()
#     fo.close()
#     return stoplist

# def lisofwords():
#     # Dictionary=createindex.listofwords()
#     return list(Dictionary.keys())

# def get_df():
#     # Dictionary=createindex.listofwords() 
#     templist=[]
#     for i in Dictionary.keys():
#         templist.append( len(Dictionary[i]) )
#     return templist

# lemmatizing=WordNetLemmatizer ()
# stoplist=stopwordlist()
# N=56

# def VSMofDoc():
#     lstofword=lisofwords()    #list of the word in entire dataset
#     dict={}                      #dictionary for VSM
#     temp=[]                     #temp list for document vector
#     path = os.getcwd()          #returns the path of the current folder 
#     files=os.listdir(path+"\Trump Speechs")         #returns all the files present in the specified directory
#     qq=re.compile('\W+')                #for splitting words
#     y=re.compile("\d+")                 # for getting the int part of the file name 
#     global filelist                        # list of file name
#     filelist=[]
#     for f in files:                     # for each file present in the directory
#         for jj in range(len(lstofword)):    # initilizing the vector with zero 
#             temp.append(0.0)
#         fname=path+"\Trump Speechs\\"
#         fname+=f
#         lines=open(fname,"r")               #open a file 
#         next(lines)
#         wordslist=lines.read()              #read the deta from the file
#         x=qq.split(wordslist.casefold())        # casefolding and then splitting the words
#         name=y.findall(f)
#         name=int(name[0])
#         for i in x:
#             if i in stoplist:
#                 continue
#             i=lemmatizing.lemmatize(i)      #lemmatizing the word
#             indexofterm=lstofword.index(i)
#             if f not in dict:
#                 dict[f]=temp.copy()
#                 dict[f][indexofterm]=dict[f][indexofterm]+1.0
#             else:
#                 dict[f][indexofterm]=dict[f][indexofterm]+1.0
#         lines.close()
#         filelist.append(name)
#         fname=""
#         temp.clear()
    
#     dflist=get_df()
#     # print(len(dflist))
#     for ii,j in dict.items():
#         for iii in range(len(j)):
#             if j[iii]!=0:
#                 j[iii]=( 1+np.log ( j[iii] ) )*( np.log ( 56/dflist[iii] ) )
      
#     wordfile=open("VSM.txt","w")
#     for K in sorted(dict.keys()):
#         wordfile.write(str(K)+" "+str(dict[K])+'\n')
#     wordfile.close()
#     return dict
    

# def searchquery():
#     vsm=VSMofDoc()
#     print(len(vsm))
#     return

# searchquery()

lst=["X", "Y"]
newlst=[]
for i in lst:
    newlst.append(i.casefold())
print(newlst)


import numpy as np
x = np.array([1,2,3,4,5])
print("Original array:")
print(x)
print("Magnitude of the vector:")
print(np.linalg.norm(x))