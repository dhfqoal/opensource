import turtle
import random

myturtle, tangle, tsize, tshape, tcolor = [None] * 5
pturtle = []
shapelist = []
swidth, sheight = 500, 500

if __name__=="__main__" :
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    shapelist = turtle.getshapes()
    for i in range(0, 5) :
        random.shuffle(shapelist)
        myturtle = turtle.Turtle(shapelist[0])
        tangle = random.randrange(1, 100)/10
        r = random.random(); g = random.random(); b = random.random()
        tsise = random.randrange(1,3)
        pturtle.append([myturtle, tangle, tsize, r, g, b])

    for tlist in pturtle :
        myturtle = tlist[0]
        myturtle.color((tlist[3], tlist[4], tlist[5]))
        myturtle.pencolor((tlist[3], tlist[4], tlist[5]))
        myturtle.turtlesize(tlist[3])
        myturtle.goto(tlist[1], tlist[2])
    turtle.done()

