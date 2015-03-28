# -*- coding: utf-8 -*-
#Matheus Dias Marotzke Dib
import string
import turtle
import random
import tkinter

angulo = 90

alfabeto = list(string.ascii_lowercase)

window = turtle.Screen()
window.bgcolor("yellow")
window.title("Forca 2.0")

forca = turtle.Turtle()
forca.speed(4)
forca.penup()
forca.setpos(-500,-250)
forca.pendown()
forca.color("black")

boneco = turtle.Turtle()

linhas = turtle.Turtle()
linhas.color("black")

l=[]
f = open('entrada.txt', encoding = "utf-8")
lista = f.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip().lower()
    if lista[i] != '':
        l.append(lista[i])

def contar_espaços():
    contagem = 0
    for i in range(len(p)):
        if p[i] == ' ':
            contagem += 1
    return contagem

def fun_forca():
    linhas.penup()
    linhas.setpos(-500,-250)
    forca.begin_fill()
    forca.fillcolor('brown')
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
    forca.end_fill()
    
def fun_erro(erro):
    if erro == 1:
        boneco.penup()
        boneco.setposition(-275,y=90)
        boneco.pendown()
        boneco.circle(30)
    if erro == 2:
        boneco.penup()
        boneco.setposition(-275,y=90)
        boneco.pendown()
        boneco.right(90)
        boneco.fd(190)
        boneco.right(-90)
    if erro == 3:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.pendown()
        boneco.right(120)
        boneco.fd(75)
        boneco.right(-120)
    if erro == 4:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.pendown()
        boneco.right(60)
        boneco.fd(75)
        boneco.right(-60)
    if erro == 5:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.pendown()
        boneco.right(120)
        boneco.fd(120)
        boneco.right(-120)
    if erro == 6:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.pendown()
        boneco.right(60)
        boneco.fd(120)
        boneco.right(-60)

def fun_linhas():
    linhas.penup()
    linhas.setpos(-480,-250)
    linhas.color("black")
    for i in range(len(palavra)):
        if p[i]!=(' '):
            linhas.pendown()
            linhas.forward(40)
            linhas.penup()
            linhas.forward(10)
        else:
            linhas.penup()
            linhas.forward(40)
            linhas.pendown()

boneco.hideturtle()
linhas.hideturtle()
forca.hideturtle()
fun_forca()
y = True
while y == True:
    palavra = (random.choice(l))
    pnt = 0
    p = list(palavra)
    print(p) #apagar!
    boneco.clear()
    linhas.clear()
    fun_linhas()
    contagem = contar_espaços()
    erro = 0
    pnt = len(p) - contagem
    while erro < 6 and pnt > 0:
        letra = window.textinput('Letra','Escolha uma letra').lower()
        if letra not in alfabeto:
            tkinter.messagebox.showwarning('Letra inválida','Letra inválida')
        elif letra in p and letra in alfabeto:
            for i in range(len(p)):
                if letra == p[i]:
                    if letra == 'a' and p[i] == 'ã':
                        pnt-=1
                    if letra == 'o' and p[i] == 'ô':
                        pnt-=1
                pnt-=1 #TERMINAR!!! outras letras...
        elif letra not in p:
            erro+=1
            fun_erro(erro)
        for i in range(len(p)):
            if letra == p[i]:
                linhas.penup()
                linhas.setpos(-480+(40+10)*i,-250)
                linhas.pendown()
                linhas.write(letra, font=('Arial',25,'normal'))
            elif letra == 'a' and p[i] == 'ã':
                linhas.penup()
                linhas.setpos(-480+(40+9)*i,-250)
                linhas.pendown()
                linhas.write(p[i], font=('Arial',25,'normal'))
            elif letra == 'i' and p[i] == 'í':
                linhas.penup()
                linhas.setpos(--480+(40+9)*i,-250)
                linhas.pendown()
                linhas.write(p[i], font=('Arial',25,'normal'))
            elif letra == 'o' and p[i] == 'ó':
                linhas.penup()
                linhas.setpos(-480+(40+9)*i,-250)
                linhas.pendown()
                linhas.write(p[i], font=('Arial',25,'normal'))
            elif letra == 'o' and p[i] == 'ô':
                linhas.penup()
                linhas.setpos(-480+(40+10)*i,-250)
                linhas.pendown()
                linhas.write(p[i], font=('Arial',25,'normal'))
                #IMPLEMENTAR PLACAR E CONTAGEM DE ACERTOS E ERROS
                #FAZER MENSAGEM DE DERROTA E VITÓRIA
    y = tkinter.messagebox.askyesno('GAME OVER','Quer Jogar Novamente?')
window.exitonclick()