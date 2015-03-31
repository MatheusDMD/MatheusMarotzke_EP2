# -*- coding: utf-8 -*-
#Matheus Dias Marotzke Dib
import string
import turtle
import random
import tkinter

angulo = 90
erro2 = 0

alfabeto = list(string.ascii_lowercase) + ['ç'] # lista de itens aceitáveis
alfabeto2 = ['ã','ó','ô','í','é','ê'] #letras aceitas em lugares específicos

window = turtle.Screen()  
window.bgcolor("yellow")
window.title("Forca 2.0")

forca = turtle.Turtle()    #Define Turtles e suas cores
forca.speed(4)
forca.penup()
forca.setpos(-500,-250)
forca.pendown()
forca.color("black")
ow = turtle.Turtle()
ow.color('brown')
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
        
def fun_OW(): # Desenha o LOGO: 'OLD WEST forca'
    ow.speed(1)
    ow.penup()
    ow.setpos(180,200)
    ow.pendown()
    ow.write('OLD', font=('Arial',95,'bold'))
    ow.penup()
    ow.setpos(220,85)
    ow.pendown()
    ow.write('WEST', font=('Arial',95,'bold'))
    ow.penup()
    ow.setpos(250,80)
    ow.pendown()
    ow.write('Forca', font=('Arial',25,'normal'))
    
def fun_placar(erro2,l): #Desenha o placar e define o valor da média
    plt.clear()
    pl.penup()
    pl.setpos(-480,-290)
    pl.write('Média de Erros por Rodada:', font=('Arial',20,'normal'))
    m = erro2/(11-len(l))
    plt.penup()
    plt.setpos(-140,-290)
    plt.pendown()
    plt.write(m, font=('Arial',20,'normal'))
    
def fun_traços(p): #Desenha as letras sobre os espaços
    for i in range(len(p)):
        if letra == p[i] and letra not in alfabeto2:
            linhas.penup()
            linhas.setpos(-480+(40+9)*i,-250)
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
            
def contar_espaços(): #Conta os espaços em cada palavra
    contagem = 0
    for i in range(len(p)):
        if p[i] == ' ':
            contagem += 1
    return contagem

def fun_forca(): #Desenha a forca
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
    
def fun_erro(erro): #Desenha o boneco conforme o número de erros
    if erro == 1:
        boneco.penup()
        boneco.setposition(-275,y=90)
        boneco.pendown()
        boneco.circle(30)
    elif erro == 2:
        boneco.penup()
        boneco.setposition(-275,y=90)
        boneco.pendown()
        boneco.right(90)
        boneco.fd(190)
        boneco.right(-90)
    elif erro == 3:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.pendown()
        boneco.right(120)
        boneco.fd(75)
        boneco.right(-120)
    elif erro == 4:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.pendown()
        boneco.right(60)
        boneco.fd(75)
        boneco.right(-60)
    elif erro == 5:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.pendown()
        boneco.right(120)
        boneco.fd(120)
        boneco.right(-120)
    elif erro == 6:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.pendown()
        boneco.right(60)
        boneco.fd(120)
        boneco.right(-60)
    elif erro == 7:
        boneco.penup()
        boneco.setposition(-285,y=117)
        boneco.pendown()
        boneco.circle(5)
    elif erro == 8:
        boneco.penup()
        boneco.setposition(-265,y=117)
        boneco.pendown()
        boneco.circle(5)
    elif erro == 9:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.right(120)
        boneco.fd(120)
        boneco.right(-120)
        boneco.pendown()
        boneco.circle(5)
    elif erro == 10:
        boneco.penup()
        boneco.setposition(-275,y=-100)
        boneco.right(60)
        boneco.fd(120)
        boneco.right(-60)
        boneco.pendown()
        boneco.circle(5)
    elif erro == 11:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.pendown()
        boneco.right(60)
        boneco.fd(75)
        boneco.right(-60)
        boneco.pendown()
        boneco.circle(5)
    elif erro == 12:
        boneco.penup()
        boneco.setposition(-275,y=40)
        boneco.right(120)
        boneco.fd(75)
        boneco.right(-120)
        boneco.pendown()
        boneco.circle(5)

def fun_linhas(): # Desenha as linhas da palavra escondida
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
ow.hideturtle()
fun_forca()
fun_OW()
y = True

tkinter.messagebox.showinfo('Bem Vindo! ao OLD WEST FORCA!','Bem vindo ao jogo de Forca! Boa sorte!')

while y == True:
    j = window.textinput('1P? ou 2P?','Digite 1P ou 2P').lower()
    if j == '1p' or j == '1 jogador' or j == 'um jogador' or j == '1 player':
        x = window.textinput('Dificuldade:','Fácil ou Médio ou O.W. style').lower()
        if x == 'fácil' or x == 'facil' or x == 'easy':
            e = 12
        elif x == 'medio' or x == 'medium' or x == 'médio':
            e = 8
        elif x == 'o.w. style' or x == 'ow style' or x == 'difícil' or x == 'dificil' or x == 'hard':
            e = 6
        else:
            x = window.textinput('Dificuldade:','por favor, digite uma destas opções: Fácil ou Médio ou O.W. style').lower()
    elif j == '2p' or j == '2 jogadores' or j == 'dois jogadores' or j == '2 players':
        palavra = window.textinput('Palavra','Jogador!, Digite uma palavra (SEM O outro VEJA!) para que ele adivinhe').lower()
    else:
        tkinter.messagebox.showinfo('Escreveu errado?','Agora vai jogar no 1P!')
        j = '1p'
    if l == []:
        tkinter.messagebox.showinfo('Game Over!','Você esgotou todas as opções de Palavras')
        tkinter.messagebox.showinfo('Obrigado!','Obrigado por Jogar!')
        #Exclama, caso tenha esgotado suas palavras, que o jogo acabou
    elif j == '1p' or j == '1 jogador' or j == 'um jogador' or j == '1 player':
        palavra = (random.choice(l))
        l.remove(palavra)    # Remove a palavra sorteada da lista 
    else:
        e = 8
    p = list(palavra)
    pnt = 0
    boneco.clear()
    linhas.clear()
    fun_linhas()
    contagem = contar_espaços()
    letras.clear()
    erro = 0
    pnt = len(p) - contagem
    #Cria um valor que desconta os espaços;
    #visando contar os pontos a partir do número de letras (SEM ESPAÇOS);
    #Estabelecendo uma pontuação condizente com o número de Letras
    while erro < e and pnt > 0:
        letras.append(letra)
        letra = window.textinput('Letra','Escreva uma letra').lower()
        if letra == 'deus': # Comando por diversão
            tkinter.messagebox.showinfo('Deus?','Ok Ok... você o salvou')
            break
        elif letra == 'matheus marotzke': # Comando de Admin (por diversão)
            x = tkinter.messagebox.askyesno('Oooh! Criador!','Você deseja poupá-lo oh! poderoso criador?')
            if x == True:
                break
            else:
                for i in range(erro,7):
                    fun_erro(i)
                break
        elif letra not in alfabeto:
            tkinter.messagebox.showwarning('Letra inválida','Letra inválida')
        elif letra in letras:
            tkinter.messagebox.showwarning('Letra inválida','Letra já utilizada')
        elif letra in p:
                for i in range(len(p)):
                    if letra == p[i]: # +Pontuação acertos
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
        else: # +Pontuação de erros
            erro+=1
            erro2+=1
            for i in range(len(p)):
                 #Subtrai pontuação erros caso não seja realmente erro
                if letra == 'a' and p[i] == 'ã':
                    pnt-=1
                    erro-=1
                    erro2-=1
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
    y = tkinter.messagebox.askyesno('GAME OVER','Quer Jogar Novamente?')
    if j == '1p' or j == '1 jogador' or j == 'um jogador' or j == '1 player':
        fun_placar(erro2,l)
else:
    tkinter.messagebox.showinfo('Obrigado!','Obrigado por Jogar!')
window.exitonclick()