import matplotlib.pyplot as plt


print('Hola, bienvendi@ a el juego. Escoge una de las siguientes opciones (escribir solo el número):\n1- Reglas del juego\n2-Jugar\n3- Recursos de aprendizaje\n4- Ver nivel\n0- Salir del juego')
menu = 1

pciencias = 'preguntasCiencias.txt'
rciencias = 'respuestasCiencias.txt'

plectura = 'preguntasEspañol.txt'
rlectura = 'respuestasEspañol.txt'

pmate = 'preguntasMate.txt'
rmate = 'respuestasMate.txt'

listaCiencia = []
listaMate = []
listaLec = []
listacomun = []

def menuPrincipal(x):
   
    if x == 1:
        reglas()
    elif x == 2:
        jugar()
        
    elif x == 3:
        recursos()
    elif x == 4:
        checarNivel()

def recursos():
    print('Linkde apoyo para Mate \nhttps://www.planyprogramasdestudio.sep.gob.mx/descargables/biblioteca/secundaria/mate/1-LPM-sec-Matematicas.pdf \nLink para Ciencias \nhttps://www.planyprogramasdestudio.sep.gob.mx/descargables/biblioteca/secundaria/ciencias/1-LpM-sec-Ciencias-y-Tecnologia.pdf \nLink para Lectura \nhttps://libros.conaliteg.gob.mx/20/S00069.htm#page/20') 


def reglas():
    archivo = open('Reglas.txt', 'r', encoding = 'utf-8-sig')
    contenido = archivo.read()
    print(contenido)
    archivo.close()
    print('Escoge nuevamente una de las siguientes opciones (escribir solo el número):\n1- Reglas del juego\n2- Jugar\n3- Recursos de aprendizaje\n4- Checar nivel\n0- Salir del juego')

def jugar():
    print('Selecciona una opción\n1-Ciencia\n2-Matematicas\n3-Lectura')
    opt = int(input())
    print('ADVERTENCIA: favor de indicar su respuesta solamente con la letra correcta y en minuscula, gracias y buena suerte.')
    if opt == 1:
        materias(pciencias, rciencias, opt)
    elif opt == 2:
        materias(pmate, rmate, opt)
    elif opt == 3:
        materias(plectura, rlectura, opt)
    else:
        print('Opción incorrecta')   
    
def materias(x, y, z):
    archivo = open(x, 'r', encoding = 'utf-8-sig')
    archivo1 = open(y, 'r', encoding = 'utf-8-sig') 
    cont = 0
    for i in archivo:
        print(i, end='')
        respuesta = str(input())
        a = archivo1.readline().rstrip()
        if respuesta == a[0]:
            cont += 3
        else:
            cont -= 1
    archivo.close()
    archivo1.close()
    print('Tu puntaje fue de', cont)
    if z == 1:
        listaCiencia.append(cont)
        listacomun.append(cont)
        mat = 'Ciencias'
    elif z == 2:
        listaMate.append(cont)
        listacomun.append(cont)
        mat='Mate'
    elif z == 3:
        listaLec.append(cont)
        listacomun.append(cont)
        mat = 'Lectura'
    print('Has completado el módulo de', mat, '. Escoge nuevamente una de las siguientes opciones (escribir solo el número):\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Checar nivel\n0-Salir del juego')

def checarNivel():
    suma = 0
    for i in range(len(listaCiencia)):
        suma += listaCiencia[i]
    for z in range(len(listaLec)):
        suma += listaLec[z]
    for p in range(len(listaMate)):
        suma += listaMate[p]
    print('Su puntaje total es de', suma)
    dic={'Ciencias' : listaCiencia, 'Mate' : listaMate, 'Lectura' : listaLec, 'Puntaje total' : suma}
    print(dic)
    print(listacomun)
    plt.plot(listacomun,'ro')
    plt.xlabel('Vez jugada')
    plt.ylabel('Puntaje obtenido')
    plt.show()
    plt.title('Puntajes')
    print('Escoge nuevamente una de las siguientes opciones (escribir solo el número):\n1- Reglas del juego\n2- Jugar\n3- Recursos de aprendizaje\n4- Checar nivel\n0- Salir del juego')

while menu != 0: 
    menu = int(input())
    menuPrincipal(menu)
    