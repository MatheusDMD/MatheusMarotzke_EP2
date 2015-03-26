# -*- coding: utf-8 -*-
#Matheus Dias Marotzke Dib
import turtle
import random

'''
FAZER TOCAR:

turtle.onscreenclick(t)
def t(x,y)
    if __ < x < __ and ___> y > __
    ... 
    '''
def fun_forca():
    forca.left(angulo)
    forca.forward(500)
    forca.right(angulo)
    forca.fd(200)
    forca.right(angulo)
    forca.fd(100)
    forca.left(angulo)
    forca.fd(50)
    forca.left(angulo)
    forca.fd(150)
    forca.left(angulo)
    forca.fd(300)
    forca.left(angulo)
    forca.fd(550)
    forca.left(angulo)
    forca.fd(50)
    linhas.penup()
    linhas.setpos(-300,-250)
def fun_erro(erro):
    if erro==1:
        forca.setposition(-50,y=-50)
        forca.circle(30)
    if erro==2:
        forca.setposition(-50,y=-100)
        forca.bk(200)
    if erro==3:
        forca.setposition(-50,y=-120)
        forca.right(120)
        forca.fd(75)
    if erro==4:
        forca.setposition(-50,y=-120)
        forca.right(180)
        forca.fd(75)
    if erro==5:
        forca.setposition(-50,y=-300)
        forca.right(120)
        forca.fd(75)
    if erro==6:
        forca.setposition(-50,y=-300)
        forca.right(120)
        forca.fd(75)
    if erro==7:
        print('End')
angulo = 90
window = turtle.Screen()
window.bgcolor("yellow")
window.title("Forca")
y='sim'
f=open('entrada.txt', encoding="utf-8")
l= f.readlines()
for i in range(len(l)):
    l[i]=l[i].strip().lower()

x=str(window.textinput('Um ou Dois?','Escolha entre: Um jogador ou Dois Jogadores:')).lower()
while y=='sim' or y=='quero':
    palavra2=(random.choice(l))
    p=list(palavra2)
    print(p)
    erro=0
    if x=='dois' or x=='dois jogadores' or x=='2':
        palavra=(window.textinput('Jogador 1 coloque sua Palavra:','P1 - SEM DEIXAR P2 VER! Digite Palavra:').lower())
        forca=turtle.Turtle()
        forca.speed(4)
        forca.penup()
        forca.setpos(-500,-250)
        forca.pendown()
        forca.color("black")
        linhas=turtle.Turtle()
        linhas.speed(4)
        linhas.penup()
        linhas.setpos(-500,-250)
        linhas.color('yellow')
        linhas.pendown()
        linhas.fd(1000)
        linhas.penup()
        linhas.setpos(-500,-250)
        linhas.pendown()
        linhas.color("black")
        fun_forca()
        linhas.penup()
        linhas.setpos(-300,-250)
        for i in range(len(palavra)):
            linhas.pendown()
            linhas.forward(40)
            linhas.penup()
            linhas.forward(10)
    else:
        linhas=turtle.Turtle()
        forca=turtle.Turtle()
        forca.speed(4)
        forca.penup()
        forca.setpos(-500,-250)
        forca.pendown()
        forca.color("black")
        fun_forca()
        linhas.speed(4)
        linhas.penup()
        linhas.penup()
        linhas.setpos(-500,-250)
        linhas.color('yellow')
        linhas.pendown()
        linhas.fd(1000)
        linhas.penup()
        linhas.setpos(-500,-250)
        linhas.pendown()
        linhas.color("black")
        angulo = 90
        for i in range(len(palavra2)):
            if p[i]!=(' '):
                linhas.pendown()
                linhas.forward(40)
                linhas.penup()
                linhas.forward(10)
            else:
                linhas.penup()
                linhas.forward(40)
                linhas.pendown()
        while erro < 6:
            letra=window.textinput('Letra','Escolha uma letra').lower()
            if letra not in p:
                    erro+=1
            for i in range(0,len(p)):
                if letra==p[i]:
                    linhas.penup()
                    linhas.setpos(-500+(40+10)*i,-250)
                    linhas.pendown()
                    linhas.write(letra, font=('Arial',25,'normal'))
                elif(letra)=='a' and p[i]=='ã':
                    linhas.penup()
                    linhas.setpos(-500+(40+10)*i,-250)
                    linhas.pendown()
                    linhas.write(letra, font=('Arial',25,'normal'))
                elif(letra)=='i' and p[i]=='í':
                    linhas.penup()
                    linhas.setpos(-500+(40+10)*i,-250)
                    linhas.pendown()
                    linhas.write(letra, font=('Arial',25,'normal'))
                elif(letra)=='o' and p[i]=='ó':
                    linhas.penup()
                    linhas.setpos(-500+(40+10)*i,-250)
                    linhas.pendown()
                    linhas.write(letra, font=('Arial',25,'normal'))
                elif(letra)=='o' and p[i]=='ô':
                    linhas.penup()
                    linhas.setpos(-500+(40+10)*i,-250)
                    linhas.pendown()
                    linhas.write(letra[i], font=('Arial',25,'normal'))
                fun_erro(erro)
    y=window.textinput('Jogar novamente?', 'Quer jogar novamente?').lower()
            
window.exitonclick()
