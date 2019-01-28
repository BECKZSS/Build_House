from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

pos=mc.player.getTilePos()
L=7
W=3
H=6
roof=[]
for k in range (L):
    if k<int(L/2):
        roof.append(k+1)
    else:
        roof.append(L-k)
print(roof)

for n in range (L):
    for m in range (W):
        mc.setBlock(pos.x+n,pos.y,pos.z+m,2)#a platform
for c in range (L):
    for p in range (W):
        mc.setBlock(pos.x+c,pos.y+H-1,pos.z+p,20)#a platform
for a in range (H):#an empty square
    for i in range (L):
        mc.setBlock(pos.x+i,pos.y+a,pos.z,1)
    for j in range (W):
        mc.setBlock(pos.x,pos.y+a,pos.z+j,1)
    for i in range (L):
        mc.setBlock(pos.x+i,pos.y+a,pos.z+W-1,1)
    for j in range (W):
        mc.setBlock(pos.x+L-1,pos.y+a,pos.z+j,1)
for f in range (3):
    mc.setBlock(pos.x+int(L/2),pos.y+f+1,pos.z,0)#a door
for e in range (int(H/5)):
    mc.setBlock(pos.x+L,pos.y+e+3,pos.z+int(W/2),20)#a window
    print('window1')
for e in range (int(H/5)):
    mc.setBlock(pos.x+L,pos.y+e+3,pos.z+int(W/2)+1,20)#a window
    print('window2')
for s in range (L):
    for l in range (W):
        if s<=int(L/2):
            mc.setBlock(pos.x+s,pos.y+H-1+roof[s],pos.z+l,135)
        else:
            mc.setBlock(pos.x+s,pos.y+H-1+roof[s],pos.z+l,135,1)


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
        
     
