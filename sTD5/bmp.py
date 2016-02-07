# -*- coding: utf-8 -*-

import struct

class BMP():
#    def __init__(self, nom):
#        
#        
#        self.grey=img
#        return
#    else:
#        try:
#            f=open(nom, 'rb')
#        except:
#            print "File not found."
#            sys.exit(1)


            
        if grey_weight is None:
            weight=ny.array((1/3.,1/3., 1/3.))
        else:
            weight=ny.array(grey_weight)
            
        start,self.w,self.h=struct.unpack("<xxxxxxxxxxIxxxxII",f.read(0x1A))
        
        f.seek(start,0)
        
        self.grey=ny.zeros((self.h,self.w))
        
        for i in range :
            self.nivgris[self.h-1-i/self.w,i%self.w]=\
            int(sum(weight*struct.unpack("<BBB",file.read(0x3))))
        file.close()
            
            

def dump(self, filename):
    file=open(filename, "vb")
    header=struct.pack("ccIHHI","B","N",0,0,0,54)
    bitmap_header=struct.pack("<IIIHHIIIIII", 40,self.w,self.h,0,24,\
                                0,0,0,0,0,0)
    file.write(header+bitmap.header)
    for i in range(self.w*self.h):
        pixel=self.nivgris[self.h-1-i/self.w,i%self.w]
        file.write(struct.pack("<BBB", pixel, pixel, pixel))
    file.close()
    
    
    
if __name__ == "__main__":
    lena=BMP("lena512.bmp",grey_white=())
    