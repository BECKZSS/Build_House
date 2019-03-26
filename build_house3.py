from mcpi.minecraft import Minecraft
import time
import math
import random as rd

print("teacher hahah")

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

pos=mc.player.getTilePos()
pos1=mc.player.getTilePos()
block_id1=mc.getBlock(pos.x,pos.y-1,pos.z)
block_id2=mc.getBlock(pos.x+1,pos.y-1,pos.z)
print(block_id2)

def house(x,y,z,m,n,u,h,s):
    pos.x=x
    pos.y=y
    pos.z=z
    print('hello')
    L=m
    W=n
    H=u
    M=h
    MR=s
    roof=[0]
    for e in range (L-1):
        x=e+1
        R=L/2  

        if L%2 == 0:
            center=(L-1)/2
            if x>center:
                x0=int(x-center+1)
            else:
                x0=int(center-x+1)*(-1)
        else:
            center=L/2
            if x>center:
                x0=x-center+1
            else:
                x0=(center-x)*(-1)

class House():
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        print("turehahhahhah")
    def build_wall(self,x,y,z,M):
        pos.x=x
        pos.y=y
        pos.z=z
        self.x=x
        self.y=y
        self.z=z
        for i in range (4):
            mc.setBlock(pos.x,pos.y+i,pos.z,M)
    def change_material(self,MR):
        self.build_wall(self.x,self.y,self.z,MR)
house1=House()
house1.build_wall(pos1.x,pos1.y,pos1.z,89)


for i in range(100000):
    house1.change_material(1+i%100)
    time.sleep(1)
print(house1)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x<=-201 x>=-202 y=0 z<=-6 z>=-8 for 10s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x<=-201 and pos.x>=-202 and pos.z<=-6 and pos.z>=-8:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-201,10,-7)
            stayed_time=0
    else:
        stayed_time=0
        
     
