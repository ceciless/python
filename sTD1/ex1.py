# -*- coding: utf-8 -*-

import sys
import os

print("hello world")
#os.system("pause")
#os.system("cls")

print("Version avec for")
for i in range(20):
    print i, "x7=", i*7

print("version avec while")
c=0
while c<20:
    print str(c)+"x7"+ str(c*7)
    c=c+1
    
print("version python & for")
#result = [i*7 for i in range(20)]
#print type(result)
#print(result)
[sys.stdout.write( str(i)+"x7="+ str(i*7)+"\n") for i in range(20)]


a=[]
a=[(i,i*7) for i in range(20)] #1~19
print(a)


