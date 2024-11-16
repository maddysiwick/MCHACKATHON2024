import math
import time
moveTime=0.1 #second
statTime=0.0
v=float(input('input velocity /n'))
print(v)
print(type(v))
c=3.0*10**8
gamma = 1/math.sqrt(1-(v**2/c**2))

def checkAge(age):
    if 90.0<=age:
        print('on the brink of death')
    elif 70.0<=age>90.0:
        print('getting old grandma')
    elif 50.0<=age>70.0:
        print('reirement is on the horizon')
    elif 30.0<=age>50.0:
        print('middle age approaches')
    elif 10.0<=age>30.0:
        print('shes growing up')
    elif 0.0<=age>10.0:
        print('shes a little babyy')


while statTime <= 100:
    moveTime+=1
    statTime+=gamma*1
    print('moving:')
    checkAge(moveTime)
    print(moveTime)
    print('stationary:')
    checkAge(statTime)
    print(statTime)

print('move time ', moveTime)
print('stat time ', statTime)

x=94.07153950826232

if x in range(90,100):
    print('works')