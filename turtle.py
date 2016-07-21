import turtle
from math import sin
s=str(input('введите почтовый индекс без пробелов (6 цифр):' ))
s1=s[0]
s2=s[1]
s3=s[2]
s4=s[3]
s5=s[4]
s6=s[5]
A = [s1, s2, s3,s4 ,s5 ,s6]

def zigzag(A, B):
    """ Рисует цифру и возвращается по нарисованному обратно"""
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def penup_down (A,B):
    t.pendown()
    zigzag (A, B)
    t.penup()
    
def digit_one(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 0, 135]
    A = [ L1, L1, L2]
    t.penup()
    t.forward(L1)
    penup_down (A,B)

def digit_two(length):
        L1 = length/2
        L2 = (length/2)*2**0.5
        B = [180, -135, 45, 90]
        A = [ L1,   L2, L1, L1]
        t.penup()
        t.forward(L1)
        penup_down (A,B)

def digit_four(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 0, 180, -90, -90]
    A = [ L1, L1, L1, L1, L1]
    t.penup()
    t.forward(L1)
    penup_down (A,B)

def digit_three(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, 135, -135, 135]
    A = [ L2, L1, L2, L1]
    t.penup()
    penup_down (A,B)
    t.forward(L1)

def digit_five(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [0, 90, 90, -90, -90]
    A = [ L1, L1, L1, L1, L1]
    t.penup()
    penup_down (A,B)
    t.forward(L1)

def digit_six(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 90, 180, -90, -90, -90, -45]
    A = [ L1, L1, L1, L1, L1, L1, L2]
    t.penup()
    t.forward(L1)
    penup_down (A,B)
    
def digit_seven(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, -45, 135]
    A = [ L1, L2, L1]
    t.penup()   
    penup_down (A,B)
    t.forward(L1) 
   
def digit_nine(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, 45, 90, 90, 90]
    A = [ L2, L1, L1, L1, L1]
    t.penup()   
    penup_down (A,B)
    t.forward(L1)  

def digit_eight(length):
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [90, 0, 90, 90, 90, 180, 90, 90]
    A = [L1, L1, L1, L1, L1, L1, L1, L1]
    t.penup()
    t.forward(L1)
    penup_down (A,B)

def draw(A):
        """выбирает изображение в зависимости от введенного
        индекса"""
        if A[i] =='1':
                t.forward(30)
                digit_one(x)
        if A[i] =='2':
                t.forward(30)
                digit_two(x)
        if A[i] =='3':
                t.forward(30)
                digit_three(x)
        if A[i] =='4':
                t.forward(30)
                digit_four(x)
        if A[i] =='5':
                t.forward(30)
                digit_five(x)
        if A[i] =='6':
                t.forward(30)
                digit_six(x)
        if A[i] =='7':
                t.forward(30)
                digit_seven(x)
        if A[i] =='8':
                t.forward(30)
                digit_eight(x)
        if A[i] =='9':
                t.forward(30)
                digit_nine(x)

x=int(input('введите высоту цифры от 50 до 300:' ))
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "red")
t.shapesize(2)
t.speed(5)            
t.penup()
t.backward(400)     
t.hideturtle()    

for i in range(len(A)):
        draw(A)


#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()
