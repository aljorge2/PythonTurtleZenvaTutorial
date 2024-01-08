#import turtle
from turtle import *

begin_fill()
#color circles gold
color("#FFC20A")

#draw a circle radius x
circle(25)
circle(50)
circle(75)
circle(100)
end_fill()

#no line
penup()

#move forward x pixels
forward(200)

pendown()
begin_fill()
color("#E66100")
#draw a circle radius x
circle(25)
circle(50)
circle(75)
circle(100)
end_fill()
#turn right x degrees
right(180)

#move forward x pixels
#forward(200)

begin_fill()
color("#40B0A6")
#draw a circle radius x
circle(25)
circle(50)
circle(75)
circle(100)
end_fill()
#no line
penup()

#move forward x pixels
forward(200)

pendown()
#color circle blue
begin_fill()
#color circle
color("#006CD1")
#draw a circle radius x
circle(25)
circle(50)
circle(75)
circle(100)

end_fill()
#do not close window
done()