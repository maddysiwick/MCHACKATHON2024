import math
import time
from graphics import *
def checkAge(age):
        if 90.0<=age:
            return 5
        elif 70.0<=age<90.0:
            print('deaths door kathy works')
            return 4
        elif 50.0<=age<70.0:
            print('old kathy works')
            return 3
        elif 30.0<=age<50.0:
            print('adult kathy works')
            return 2
        elif 10.0<=age<30.0:
            print('teen kathy works fine')
            return 1
        elif age<10.0:
            print('baby kathy works')
            return 0


def main():
    win = GraphWin('My Window',1000,1000)
    win.setBackground('black')
    allImages=['baby.png','smiley.png','man.png','old.png','skull.png','skull.png']
    moveTime=0.1 #second
    statTime=0.0
    v=250000000.0
    c=3.0*10**8
    gamma = 1/math.sqrt(1-(v**2/c**2))
    count=0
    efile=0
    sfile=0
    imgEarth=Image(Point(200,500),allImages[efile])
    imgSpace=Image(Point(800,500),allImages[sfile])
    imgEarth.draw(win)
    imgSpace.draw(win)
    while statTime <= 100:
        count+=1
        time.sleep(1)
        moveTime+=1
        statTime+=gamma*1
        print(statTime)
        if count>1:
            eprev=efile
            sprev=sfile
            efile=checkAge(statTime)
            sfile=checkAge(moveTime)
            if eprev!=efile:
                imgEarth.undraw()
                imgEarth=Image(Point(200,500),allImages[efile])
                imgEarth.draw(win)
            if sprev!=sfile:
                imgSpace.undraw()
                imgSpace=Image(Point(800,500),allImages[sfile])
                imgSpace.draw(win)
        else:
            efile=checkAge(statTime)
            sfile=checkAge(moveTime)

    win.getMouse()
    win.close()

    print('move time ', moveTime)
    print('stat time ', statTime)

    

main()