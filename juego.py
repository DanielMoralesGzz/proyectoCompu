print('Hola, bienvendi@ a el juego. Escoge una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Modo Administrador\n0-Paras salir del juego')
menu=1

while menu!=0:
    menu=int(input())
    if menu==1:
        archivo=open('Reglas.txt', 'r')
        contenido=archivo.read()
        print(contenido)
        archivo.close()
    elif menu==2:
        archivo=open('preguntas.txt',encoding='utf-8-sig')
        archivo1=open('respuestas.txt')
        cont=0
        for i in archivo:
            print(i,end='')
            respuesta=input()
            a=archivo1.readline()
            if respuesta==a:
                cont+=3
            else:
                cont-=1
        archivo.close()
        archivo1.close()
        print('Tu puntaje fue de',cont,)
print('Gracias por jugar, hasta luego')
print('l;lkas')
