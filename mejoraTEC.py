print('Hola, bienvendi@ a el juego. Escoge una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Modo Administrador\n0-Para salir del juego')
menu=1

while menu!=0:
    menu=int(input())
    if menu==1:
        archivo=open('Reglas.txt', 'r')
        contenido=archivo.read()
        print(contenido)
        archivo.close()
    elif menu==2:
      print('Selecciona una opción\n1-Ciencia\n2-Matematicas\n3-Lectura')
      opt = int(input())
      print('ADVERTENCIA: favor de indicar su respuesta solamente con la letra correcta y en minuscula, gracias y buena suerte.')
      if opt == 1:
          archivo=open('preguntas.txt','r',encoding='utf-8-sig')
          archivo1=open('respuestas.txt','r',encoding='utf-8-sig') 
          cont=0
          for i in archivo:
              print(i,end='')
              respuesta=str(input())
              a=archivo1.readline()
              print(a)
              if respuesta==a:
                  cont+=3
              else:
                  cont-=1
              print(cont)
          archivo.close()
          archivo1.close()
          print('Tu puntaje fue de', cont)
          if cont <= 0:
              print('Barra de experiencia: (          )')
          elif cont<6 and cont>0:
              print('Barra de experiencia: (//        )')
          elif 11>cont and cont>5:
              print('Barra de experiencia: (////      )')
          elif 16>cont and cont>10:
              print('Barra de experiencia: (/////     )')
          elif 21>cont and cont>15:
              print('Barra de experiencia: (///////   )')
          elif 26>cont and cont>20:
              print('Barra de experiencia: (////////  )')
          elif 31>cont and cont>25:
              print('Barra de experiencia: (//////////)')
          
          print('Has completado el módulo de Ciencias. Escoge nuevamente una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Modo Administrador\n0-Para salir del juego')


      elif opt == 2:
        cont1 = 0
        archivo2 = open('preguntasMate.txt',encoding='utf-8-sig')
        archivor2 = open('respuestasMate.txt')
        for i in archivo2:
              print(i,end='')
              respuesta=input()
              a=archivor2.readline()
              if respuesta==a:
                  cont1+=3
              else:
                  cont1-=1
        archivo2.close()
        archivor2.close()
        print('Tu puntaje fue de',cont1,)
        if cont1 <= 0:
            print('Barra de experiencia: (          )')
        elif cont1<6 and cont1>0:
            print('Barra de experiencia: (//        )')
        elif 11>cont1 and cont1>5:
            print('Barra de experiencia: (////      )')
        elif 16>cont1 and cont1>10:
            print('Barra de experiencia: (/////     )')
        elif 21>cont1 and cont1>15:
            print('Barra de experiencia: (///////   )')
        elif 26>cont1 and cont1>20:
              print('Barra de experiencia: (////////  )')
        elif 31>cont1 and cont1>25:
              print('Barra de experiencia: (//////////)')
        print('Has completado el módulo de Matemáticas. Escoge nuevamente una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Modo Administrador\n0-Para salir del juego')

      elif opt == 3:
        cont2 = 0
        archivo3 = open('preguntasEspañol.txt',encoding='utf-8-sig')
        archivor3 = open('respuestasEspañol.txt')
        for i in archivo3:
              print(i,end='')
              respuesta=input()
              a=archivor3.readline()
              if respuesta==a:
                  cont2+=3
              else:
                  cont2-=1
        archivo3.close()
        archivor3.close()
        print('Tu puntaje fue de',cont2,)
        if cont2 <= 0:
              print('Barra de experiencia: (          )')
        elif cont2<6 and cont2>0:
              print('Barra de experiencia: (//        )')
        elif 11>cont2 and cont2>5:
              print('Barra de experiencia: (////      )')
        elif 16>cont2 and cont2>10:
              print('Barra de experiencia: (/////     )')
        elif 21>cont2 and cont2>15:
              print('Barra de experiencia: (///////   )')
        elif 26>cont2 and cont2>20:
              print('Barra de experiencia: (////////  )')
        elif 31>cont2 and cont2>25:
              print('Barra de experiencia: (//////////)')
        print('Has completado el módulo de Español. Escoge nuevamente una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Modo Administrador\n0-Para salir del juego')

      else:
        print('Opción incorrecta')
print('Gracias por jugar, hasta luego')