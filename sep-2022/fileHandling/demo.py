##file=open("text.txt","w")
##file.write("Hello world")
##file=open("text.txt","r")
##for i in file:
##    print(i)
##file.close()

f=open("demo.txt","a")
f.write("\nhello world2")
f=open("demo.txt","r")
for i in f:
    print(i)
f.close()

##import os
##os.remove("demo.txt")
import os
