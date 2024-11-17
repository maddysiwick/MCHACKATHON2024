from graphics import *

def main():
    win = GraphWin('window', 1000, 700)

    #dont code above this

    win.setBackground(color_rgb(0,255,0))

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
    
    if int(my_txt) > 300000:
        noworkkathy.draw(win)
    else:
        print ("The speed of the Kathy mobile is " + my_txt + " km/s")
        yesworkkathy.draw(win)

    
    
    win.getMouse()
    win.close()
    
    
    #dont code below this

    

main()