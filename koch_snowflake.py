#Draw Koch snowflakes with turtle
#Neville Varney-Horwitz
#14 April 2015
import turtle,time,random

def koch(order,size):
    """draws a snowflake recursively"""
    if order == 0:
        turtle.forward(size)
    else:
        colour = (round(random.random(),2),round(random.random(),2),round(random.random(),2))
        turtle.pencolor(colour)        
        koch(order-1,size/3)
        turtle.left(60)
        koch(order-1,size/3)
        turtle.right(120)
        koch(order-1,size/3)
        turtle.left(60)
        koch(order-1,size/3)
                 
def main():
    turtle.screensize(1000) 
        
    for i in range(1,5):
        turtle.speed = 2*i
        turtle.penup()
        turtle.goto(-340,-200)  #move to left hand side
        turtle.pendown()
        
        koch(i,i*250)           #draw a koch snowflake of ordwer i
        
        time.sleep(1)
        turtle.bye()            #close current window
        
        
if __name__ == '__main__':
    main()
