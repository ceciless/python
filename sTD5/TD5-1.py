# -*- coding: utf-8 -*-

import struct

class BMP():
    __init__(self,nom,grey_weight)
    f= open(nom,'rb')
    start,self.w,self.h=struct.unpack("<xxxxxxxxxxIxxxxII",f.read(0x1A))
    f.seek(start,0)
    if grey_weight == None:
        weight=ny.array([1/3.,1/3.,1/3.])
    else:
        weight = ny.array(grey_weight)
    self.nivgris=np.zero((self.h,self.w))
    for i in range (self.h * self.w):
        self.nivgris[self.h-1-i/self.w,i%self.w]=\
            int(sum(weight*struct.unpack("<BBB",file.read(0x3))))
    file.close()
    
def dump(self, filename):
    file=open(filename, "rb")
    header = struct.pack("<ccIHHI","B","M",0,0,0,54)
    bitmap_header=struct.pack("<IIIHHIIIIII",40,self.w,self.h,0,24,\
                              0,0,0,0,0,0)
    file.write(header+bitmap_header)
    for i in range (self.w*self.h):
        pixel=self.nivgris[self.h-1-i/self.w,i%self.w]
        file.write(struct.pack("<BBB", pixel, pixel, pixel))
    file.close()
    
if __name__ == "__main__":
    lena=BMP("lena512.bmp",grey_white=())
    