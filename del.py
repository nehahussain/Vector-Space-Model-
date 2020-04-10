import ast


d={"neha": [1,2,3,4], 00:[1,6,9] }
f=open("checkingdict.txt","w")
f.write(str(d))
f.close()

f=open("checkingdict.txt","r")
r=f.read()
dc=ast.literal_eval(r)
f.close()
print(dc)