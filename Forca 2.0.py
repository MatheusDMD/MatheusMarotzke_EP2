# -*- coding: utf-8 -*-
#Matheus Dias Marotzke Dib
import string
import turtle
import random
import tkinter

angulo = 90

alfabeto = list(string.ascii_lowercase) + ['ç']
alfabeto2 = ['ã','ó','ô','í']

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
plt = turtle.Turtle()
pl = turtle.Turtle()
pl.color('brown')
linhas = turtle.Turtle()
linhas.color("black")

l=[]
letras=[]
letra=''
f = open('entrada.txt', encoding = "utf-8")
lista = f.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip().lower()
    if lista[i] != '':
        l.append(lista[i])
        
def fun_placar(pnt,erro):
    plt.clear()
    pl.penup()
    pl.setpos(-480,-290)
    pl.write('Média de Erros/Rodadas:', font=('Arial',20,'normal'))
    m = erro2/(11-len(p))
    plt.penup()
    plt.setpos(-150,-290)
    plt.pendown()
    plt.write(m, font=('Arial',20,'normal'))
    
def fun_traços(p):
    for i in range(len(p)):
        if letra == p[i] and letra not in alfabeto2:
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
            linhas.setpos(-480+(40+9)*i,-250)
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
        elif letra == 'e' and (p[i] == 'é' or p[i] == 'ê'):
            linhas.penup()
            linhas.setpos(-480+(40+10)*i,-250)
            linhas.pendown()
            linhas.write(p[i], font=('Arial',25,'normal'))
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

plt.hideturtle()
pl.hideturtle()
boneco.hideturtle()
linhas.hideturtle()
forca.hideturtle()
fun_forca()
y = True
erro2 = 0
while y == True:
    palavra = (random.choice(l))
    pnt = 0
    p = list(palavra)
    print(p) #apagar!
    boneco.clear()
    linhas.clear()
    fun_linhas()
    contagem = contar_espaços()
    l.remove(palavra)
    letras.clear()
    erro = 0
    pnt = len(p) - contagem
    while erro < 6 and pnt > 0:
        letras.append(letra)
        letra = window.textinput('Letra','Escreva uma letra').lower()
        if letra not in alfabeto:
            tkinter.messagebox.showwarning('Letra inválida','Letra inválida')
        elif letra in letras:
            tkinter.messagebox.showwarning('Letra inválida','Letra já utilizada')
        elif letra in p:
                for i in range(len(p)):
                    if letra == p[i]:
                        pnt-=1
                    elif letra == 'a' and p[i] == 'ã':
                        pnt-=1
                    elif letra == 'o' and p[i] == 'ô':
                        pnt-=1
                    elif letra == 'o' and p[i] == 'ó':
                        pnt-=1
                    elif letra == 'i' and p[i] == 'í':
                        pnt-=1                
                    elif letra == 'e' and (p[i] == 'é' or p[i] == 'ê'):
                        pnt-=1
        else:
            erro+=1
            erro2+=1
            for i in range(len(p)):
                if letra == 'a' and p[i] == 'ã':
                    pnt-=1
                    erro-=1
                    erro-=1
                elif letra == 'o' and (p[i] == 'ô' or p[i] == 'ó' or p[i] == 'õ'):
                    pnt-=1
                    erro-=1
                    erro2-=1
                elif letra == 'i' and p[i] == 'í':
                    pnt-=1
                    erro-=1
                    erro2-=1
                elif letra == 'e' and (p[i] == 'é' or p[i] == 'ê'):
                    pnt-=1
                    erro-=1
                    erro2-=1
        fun_erro(erro)
        fun_traços(p)
        fun_placar(pnt,erro)
    y = tkinter.messagebox.askyesno('GAME OVER','Quer Jogar Novamente?')
if l == []:
    tkinter.messagebox.showinfo('Game Over!','Você esgotou todas as opções de Palavras')
    tkinter.messagebox.showinfo('Obrigado!','Obrigado por Jogar!')
window.exitonclick()