import math
import time
from graphics import *


def checkAge(age):
    if 90.0<=age:
        return 9
    elif 75.0<=age<90:
        return 8
    elif 60.0<=age<75.0:
        return 7
    elif 45.0<=age<60.0:
        print('deaths door kathy works')
        return 6
    elif 35.0<=age<45.0:
        print('old kathy works')
        return 5
    elif 25.0<=age<35.0:
        return 4
    elif 15.0<=age<25.0:
        print('adult kathy works')
        return 3
    elif 10.0<=age<15.0:
        return 2
    elif 5.0<=age<10.0:
        print('teen kathy works fine')
        return 1
    elif age<5.0:
        print('baby kathy works')
        return 0


def main():
    v=0
    win = GraphWin('My Window',1200,1000)
    win.setBackground(color_rgb(19,28,62))
    

    label = Text(Point(380,100), "Speed of the Kathy mobile:")
    label.setSize(20)
    label.setTextColor("white")
    label.draw(win)
    earth=Image(Point(200,825),'earth.png')
    earth.draw(win)
    ship=Image(Point(1050,675),'kathymobile.png')
    ship.draw(win)
    noworkkathy = Text(Point(550,150),"The Kathy mobile cannot run at this speed, KATHY SLOW DOWN!")
    noworkkathy.setSize(20)
    noworkkathy.setTextColor("white")

    

    def buttons(x,y):
        Submitbutton = Rectangle(Point(x,y), Point (x+60,y-30))
        Submitbutton.setFill(color_rgb(255,0,0))
        #enter=Text(Point(x+300,y-15),'enter')
        #enter.setSize(20)
        Submitbutton.draw(win)
        #enter.draw(win)
        return Submitbutton

    #buttons()
    button = buttons (600,200)
    
    



    #create our objects

    input_box = Entry(Point(700,100),30)
    input_box.setSize(20)
    input_box.setFill('white')
    input_box.draw(win)
    #txt = Text(Point(370,280),"")
    #txt.draw(win)

    while True:
       #txt.setText(input_box.getText())
       
       click_point = win.getMouse()

       if 600 <= click_point.getX() <= 630 and 170 <= click_point.getY() <=200:
            break 
       
    
    
    

    my_txt = input_box.getText()

    yesworkkathy = Text(Point(600,150), "Kathy is now speeding around the Earth at " + my_txt + " m/s")
    yesworkkathy.setSize(20)
    yesworkkathy.setTextColor("white")
    
    if int(my_txt) > 300000000:
        noworkkathy.draw(win)
    else:
        print ("The speed of the Kathy mobile is " + my_txt + " m/s")
        yesworkkathy.draw(win)
        v=int(my_txt)

    if v>0:
        allImages=['kathybaby.PNG','kathy5.PNG','kathy10.PNG','kathy15.PNG','kathy25.PNG','kathy35.PNG','kathy45.PNG','kathy60.PNG','kathy75.PNG','kathydead.PNG']
        moveTime=0.0 #second
        statTime=0.0
        c=3.0*10**8
        gamma = 1/math.sqrt(1-(v**2/c**2))
        count=0
        efile=0
        sfile=0
        elabel=Text(Point(200,200),"Karth's age:")
        elabel.setSize(20)
        elabel.setTextColor('white')
        slabel=Text(Point(1000,200),"Kathy's age:")
        slabel.setSize(20)
        slabel.setTextColor('white')
        imgEarth=Image(Point(200,500),allImages[efile])
        imgSpace=Image(Point(1000,500),allImages[sfile])
        imgEarth.draw(win)
        imgSpace.draw(win)
        slabel.draw(win)
        elabel.draw(win)
        while statTime <= 90:
            count+=1
            time.sleep(1)
            moveTime+=1
            statTime+=gamma*1
            print(statTime)
            if count>1:
                eage.undraw()
                sage.undraw()
                eage=Text(Point(200,250),int(statTime))
                eage.setSize(20)
                eage.setTextColor('white')
                sage=Text(Point(1000,250),int(moveTime))
                sage.setSize(20)
                sage.setTextColor('white')
                eage.draw(win)
                sage.draw(win)
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
                    imgSpace=Image(Point(1000,500),allImages[sfile])
                    imgSpace.draw(win)
            else:
                eage=Text(Point(200,250),int(statTime))
                eage.setSize(20)
                eage.setTextColor('white')
                sage=Text(Point(1000,250),int(moveTime))
                sage.setSize(20)
                sage.setTextColor('white')
                eage.draw(win)
                sage.draw(win)
                efile=checkAge(statTime)
                sfile=checkAge(moveTime)
        

    win.getMouse()
    win.close()

    print('move time ', moveTime)
    print('stat time ', statTime)

    

main()