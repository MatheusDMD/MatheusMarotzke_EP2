import turtle
window = turtle.Screen()
window.bgcolor("yellow")
window.title("Forca")
y=('sim')
x=window.textinput(('Um ou Dois?','Escolha entre: Um jogador ou Dois Jogadores:').lower())
while y==('sim') or y==('quero'):
    while x==('um') or x==('um jogador'):
        if 
        palavra = input(" ")
            
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
        linhas.pendown()
        linhas.color("black")
        
        dist=500
        dist1=100
        dist2=200
        dist3=100
        dist4=50
        dist5=150
        dist6=300
        dist7=50
        dist8=550
        angulo = 90
        
        for i in range(1):
            forca.left(angulo)
            forca.forward(dist)
            forca.right(angulo)
            forca.fd(dist2)
            forca.right(angulo)
            forca.fd(dist3)
            forca.left(angulo)
            forca.fd(dist4)
            forca.left(angulo)
            forca.fd(dist5)
            forca.left(angulo)
            forca.fd(dist6)
            forca.left(angulo)
            forca.fd(dist8)
            forca.left(angulo)
            forca.fd(dist7)
            linhas.penup()
            linhas.setpos(-300,-250)
            for i in range(len(palavra)):
                #linhas.write('_',font=('Arial',100,'normal'))
                linhas.pendown()
                linhas.forward(40)
                linhas.penup()
                linhas.forward(10)
    y=window.textinput(('Jogar novamente?', 'Quer jogar novamente?').lower())
            
window.exitonclick()
    
    
