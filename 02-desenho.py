from turtle import*
speed(7)
pensize(7)
def circulos_olimpiadas(x,y,crl):
 penup()
 color(crl)
 goto(x,y)
 pendown()
 circle(80)

#circulos_preto
circulos_olimpiadas (0,0, "black")

#circulo_vermelho
circulos_olimpiadas (200, 0, "red")

#circulo_azual
circulos_olimpiadas (-200, 0, "blue")

#circulo_amarelo
circulos_olimpiadas (-100, -90, "yellow")

#circulo_verde
circulos_olimpiadas (100, -90, "green")

done()