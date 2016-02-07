# -*- coding: utf-8 -*-

print("version classique")
s = 1 
while s<=16384:
    print s, "euro(s) =", s *1.65, "dollar(s)" 
    s = s *2


print("version python")
[sys.stdout.write( str(2**i)+"euro(s)="+ str(2**i*1.65)+"dollar(s)"+"\n") for i in range(15)]