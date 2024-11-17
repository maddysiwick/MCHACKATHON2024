from graphics import *
def main():
    win = GraphWin('My Window',500,500)
    win.setBackground('black')
    img = Image(Point(250,250,),'smiley.png')
    img.draw(win)
    win.getMouse()
    win.close()

main()