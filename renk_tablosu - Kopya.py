from turtle import *
colormode(255)
color(255,0,255)#cerceve ve ic renk
pensize(5)#cerceve kalınlık
def ucgen():
    for x in range(3):
        forward (200)
        left(120)

begin_fill()
ucgen()
end_fill()

        
