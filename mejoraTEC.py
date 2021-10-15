print('Hola, bienvendi@ a el juego. Escoge una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Ver nivel\n0-Salir del juego')
menu=1

pciencias='preguntasCiencias.txt'
rciencias='respuestasCiencias.txt'

plectura='preguntasEspañol.txt'
rlectura='respuestasEspañol.txt'

pmate='preguntasMate.txt'
rmate='respuestasMate.txt'

listaCiencia = []
listaMate = []
listaLec = []
def menuPrincipal(x):
    if x == 1:
        reglas()
    elif x == 2:
        jugar()
    #elif x==3:
    #    recursos()
    elif x == 4:
        checarNivel()
    
def reglas():
    archivo = open('Reglas.txt', 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

def jugar():
    print('Selecciona una opción\n1-Ciencia\n2-Matematicas\n3-Lectura')
    opt = int(input())
    print('ADVERTENCIA: favor de indicar su respuesta solamente con la letra correcta y en minuscula, gracias y buena suerte.')
    if opt==1:
        materias(pciencias,rciencias,opt)
    elif opt==2:
        materias(pmate,rmate,opt)
    elif opt==3:
        materias(plectura,rlectura,opt)
    else:
        print('Opción incorrecta')   
    
def materias(x,y,z):
    archivo=open(x,'r',encoding='utf-8-sig')
    archivo1=open(y,'r',encoding='utf-8-sig') 
    cont=0
    for i in archivo:
        print(i,end='')
        respuesta=str(input())
        a=archivo1.readline()
        if respuesta==a[0]:
            cont+=3
        else:
            cont-=1
    archivo.close()
    archivo1.close()
    print('Tu puntaje fue de', cont)
    if z==1:
        listaCiencia.append(cont)
        mat='Ciencias'
    elif z==2:
        listaMate.append(cont)
        mat='Mate'
    elif z==3:
        listaLec.append(cont)
        mat='Lectura'
    print('Has completado el módulo de',mat,'.Escoge nuevamente una de las siguientes opciones:\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Checar nivel\n0-Salir del juego')

def checarNivel():
    suma=0
    for i in range(len(listaCiencia)):
        suma+=listaCiencia[i]
    for z in range(len(listaLec)):
        suma+=listaLec[z]
    for p in range(len(listaMate)):
        suma+=listaMate[p]
    print('Su puntaje total es de',suma)



while menu!=0: 
    menu=int(input())
    menuPrincipal(menu)
    

ayb = input('Deseas conocer tus resultados, selecciona una opcion: a)Si  b)No = ')
if ayb == 'a':
    if len(listaCiencia)>0:
      print('Resultados ciencia',listaCiencia)
    if len(listaMate)>0:
      print('Resultados matematicas',listaMate)
    if len(listaLec)>0:
      print('Resultados lectura',listaLec)
else: 
 print('Gracias por jugar, hasta luego')