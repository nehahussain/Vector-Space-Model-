import ast
import math
# d={"neha": [1,2,3,4], 00:[1,6,9] }
# f=open("checkingdict.txt","w")
# f.write(str(d))
# f.close()

# f=open("checkingdict.txt","r")
# r=f.read()
# dc=ast.literal_eval(r)
# f.close()
# print(dc)

# lst=sort(dc.keys())
# print(lst)

f=open("invertedindex.txt","r")
r=f.read()
dc=ast.literal_eval(r)
f.close()
lst=list(dc.keys())
lst.sort()
ind=lst.index("peaceful")
 
templist=[]
lengthoflist=len(lst)
for i in range(lengthoflist):
    templist.append(0)
for i in lst:
    templist[lst.index(i)]=( len(dc[i]))
print(lst[ind])
print (templist[ind])

f=open("VSM.txt","r")
r=f.read()
dict=ast.literal_eval(r)
f.close()

print (dict["speech_30.txt"][lst.index("peaceful")])
print (dict["speech_30.txt"][lst.index("change")])
print (dict["speech_7.txt"][lst.index("peaceful")])
print (dict["speech_7.txt"][lst.index("change")])


# # for i, j in dict.items():
# #     print ("key: ", i , ": ", j[ind])
# for ii,j in dict.items():
#     for iii in range(len(j)):
#         if j[iii]!=0:
#             product=( j[iii] )*( math.log( 56/templist[iii] ,10 ) )
#             j[iii]=product

# print (dict["speech_30.txt"][ind])
    
