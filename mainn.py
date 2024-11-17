import math
import time
from graphics import *
def checkAge(age):
    if 90.0<=age:
        return 7
    elif 75.0<=age<90:
        return 6
    elif 65.0<=age<75.0:
        return 5
    elif 55.0<=age<65.0:
        print('deaths door kathy works')
        return 4
    elif 35.0<=age<45.0:
        print('old kathy works')
        return 3
    elif 15.0<=age<25.0:
        print('adult kathy works')
        return 2
    elif 5.0<=age<10.0:
        print('teen kathy works fine')
        return 1
    elif age<5.0:
        print('baby kathy works')
        return 0


def main():
    v=0
    win = GraphWin('My Window',1000,1000)
    win.setBackground(color_rgb(19,28,62))
    

    label = Text(Point(280,290), "Speed of the Kathy mobile:")
    label.setSize(20)
    label.setTextColor("white")
    label.draw(win)

    noworkkathy = Text(Point(450,400),"The Kathy mobile cannot run at this speed, KATHY SLOW DOWN!")
    noworkkathy.setSize(20)
    noworkkathy.setTextColor("white")

    

    def buttons(x,y):
        Submitbutton = Rectangle(Point(x,y), Point (x+30,y-30))
        Submitbutton.setFill(color_rgb(255,0,0))
        Submitbutton.draw(win)
        return Submitbutton

    #buttons()
    button = buttons (500,350)
    
    



    #create our objects

    input_box = Entry(Point(520,290),30)
    input_box.draw(win)
    #txt = Text(Point(370,280),"")
    #txt.draw(win)

    while True:
       #txt.setText(input_box.getText())
       
       click_point = win.getMouse()

       if 500 <= click_point.getX() <= 530 and 320 <= click_point.getY() <=350:
            break 
       
    
    
    

    my_txt = input_box.getText()

    yesworkkathy = Text(Point(450,400), "Kathy is now speeding around the Earth at " + my_txt + " km/s")
    yesworkkathy.setSize(20)
    yesworkkathy.setTextColor("white")
    
    if int(my_txt) > 300000000:
        noworkkathy.draw(win)
    else:
        print ("The speed of the Kathy mobile is " + my_txt + " km/s")
        yesworkkathy.draw(win)
        v=int(my_txt)

    if v>0:
        allImages=['baby.png','smiley.png','man.png','old.png','skull.png','skull.png']
        moveTime=0.1 #second
        statTime=0.0
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