import math
moveTime=0 #second
statTime=0
v=5830 #m/s
c=3*10**8
gamma = 1/math.sqrt(1-(v**2/c**2))


while statTime <= 100:
    moveTime+=1
    statTime+=gamma*1

print('move time ', moveTime)
print('stat time ', statTime)

