import matplotlib.pyplot as plt #importamos matplotlib para crear unas gráficas 


print('Hola, bienvendi@ a el juego. Escoge una de las siguientes opciones (escribir solo el número):\n1- Reglas del juego\n2-Jugar\n3- Recursos de aprendizaje\n4- Ver Resultados\n0- Salir del juego')
menu = 1 #Arriba se imprime el dialogo inicial, e inicializamos la variable menu como uno para arrancar el while de nuestro main que esta más abajo en el código

pciencias = 'preguntasCiencias.txt' #damos a variables el valor de string de los nombres de los documentos que queremos abrir para simplificar el código, la explicación del porque está más adelante cuando se usa.
rciencias = 'respuestasCiencias.txt' #^^^

plectura = 'preguntasEspañol.txt' #^^^
rlectura = 'respuestasEspañol.txt'  #^^^

pmate = 'preguntasMate.txt' #^^^
rmate = 'respuestasMate.txt' #^^^

#Guardamos un string que imprimiremos varias veces para optimizar.
msjescoge='Escoge nuevamente una de las siguientes opciones (escribir solo el número):\n1-Reglas del juego\n2-Jugar\n3-Recursos de aprendizaje\n4-Checar Resultados\n0-Salir del juego'

listaCiencia = [] #Inicializamos las listas cuyó propósito es guardar los puntajes de cada respectivo tema jugado, lista común siendo todos los puntajes.
listaMate = [] 
listaLec = []
listacomun = []

def menuPrincipal(x): #Nuestra función del menu principal, la cuál recibe el valor ingresado por el usuario y corre la función correspondiente al comando.
   
    if x == 1:
        reglas()
    elif x == 2:
        jugar()
        
    elif x == 3:
        recursos()
    elif x == 4:
        checarResultados()

def recursos(): #Función que imprime links de recursos de aprendizaje para la lectura y el refuerzo de los conocimientos del usuario.
    print('Link de apoyo para Mate \nhttps://www.planyprogramasdestudio.sep.gob.mx/descargables/biblioteca/secundaria/mate/1-LPM-sec-Matematicas.pdf \nLink para Ciencias \nhttps://www.planyprogramasdestudio.sep.gob.mx/descargables/biblioteca/secundaria/ciencias/1-LpM-sec-Ciencias-y-Tecnologia.pdf \nLink para Lectura \nhttps://libros.conaliteg.gob.mx/20/S00069.htm#page/20') 
    #Se utilizá el retorno de carro \n para caber todo a un solo print y en diferentes líneas.

def reglas(): #Función que nos imprime las reglas del juego, las cuales están en un archivo de texto.
    archivo = open('Reglas.txt', 'r', encoding = 'utf-8-sig') #Abrimos un archivo de texto, en modo read para solo leerlo y con encoding para poder leer acentos.
    contenido = archivo.read() #Asignamos a la variable contenido todo el valor de tipo string del archivo.
    print(contenido) #Imprimimos nuestro reglamento
    archivo.close() #Cerramos el archivo
    print(msjescoge)

def jugar(): #Este es el submenu de juegos.
    print('Selecciona una opción\n1-Ciencia\n2-Matematicas\n3-Lectura')
    opt = int(input()) #Se ingresa el tema que se quiera reforzar
    print('ADVERTENCIA: favor de indicar su respuesta solamente con la letra correcta y en minuscula, gracias y buena suerte.')
    if opt == 1: #En este caso se escoge el tema de ciencias, asi que mandamos a llama la función que corre el juego en si con las variables que establecimos en un inicio, 
        materias(pciencias, rciencias, opt) #las cuáles representan los archivos que queremos abrir, y opt es la opción(tema)
    elif opt == 2:
        materias(pmate, rmate, opt)
    elif opt == 3:
        materias(plectura, rlectura, opt)
    else:
        print('Opción incorrecta')   #Un else para indicar al usuario que su input no es correcto.
        print(msjescoge)

def materias(x, y, z): #La función que se llama en la función anterior. x y y  son las variables que toman el valor que  le enviamos antes, z toma el valor de opt.
    archivo = open(x, 'r', encoding = 'utf-8-sig') #abrimos los archivos de acuerdo a las variables seleccionadas
    archivo1 = open(y, 'r', encoding = 'utf-8-sig') 
    cont = 0 #inicializamos la variable cont, la cual cuenta el puntaje acumulado de la jugada especifica.
    for i in archivo: #Creamos un loop el cual imprime cada linea del archivo de preguntas, el usuario ingresa una respuesta, se leen las respuestas y compara que este correcta.
        print(i, end='')
        respuesta = str(input())
        a = archivo1.readline().rstrip()
        if respuesta == a[0]: #Si  esta correcta sele suman tres puntos, si esta incorrecta se le resta uno.
            cont += 3
        else:
            cont -= 1
    archivo.close() #cerramos ambos archivos
    archivo1.close()
    print('Tu puntaje fue de', cont) #Se imprime el puntaje de esta jugada
    if z == 1:
        listaCiencia.append(cont)  #En  estos ifs se filtra con el uso del input opt a que materia se estaba jugando, y se le añade el puntaje a la lista correspondiente y a la comun.
        listacomun.append(cont)
        mat = 'Ciencias' #Establecemos mat con el string correspondiente a la materia jugada, para al final indicar que se ha completado el modulo correspondiente.
    elif z == 2:
        listaMate.append(cont) #Hacemos lo mismo pero con otro caso.
        listacomun.append(cont)
        mat='Mate'
    elif z == 3:  #Mismo pero con otro caso
        listaLec.append(cont)
        listacomun.append(cont)
        mat = 'Lectura'
    print('Has completado el módulo de', mat, msjescoge) #Imprimimos el modulo completado, y el mensaje del menu

def checarResultados(): #Funcion para pedir los resultados totales.
    listaveces= [] #Creamos una lista cuyo proposito sera servir de eje x para los puntajes totales.
    suma = 0 #Variable local para sumar los puntajes totales.
    for i in range(len(listaCiencia)): #Sumamos los valores obtenidos de Ciencias
        suma += listaCiencia[i]
    for z in range(len(listaLec)): #Los de Lectura
        suma += listaLec[z]
    for p in range(len(listaMate)): #y los de mate
        suma += listaMate[p]
    print('Su puntaje total es de', suma) #damos el puntaje total
    for yu in range(1,len(listacomun)+1): #Creamos nuestro eje x, que son los numeros del 1 al total de veces jugado.
        listaveces.append(str(yu)) #Lo guardamos como string para que en la grafica no se peguen los valores.
    #Creamos un diccionario con los valores de puntajes y su indice correspondiente
    dic={'Ciencias' : listaCiencia, 'Mate' : listaMate, 'Lectura' : listaLec, 'Puntaje total' : suma}
    print(dic) #Lo imprimimos
    print(listacomun)#imprimimos lista comun, la cual representa cada puntaje jugado.
    plt.bar(listaveces,listacomun,color='green')
    plt.xlabel('Vez jugada')
    plt.ylabel('Puntaje obtenido')
    plt.show()
    plt.title('Puntajes')
    print(msjescoge)

while menu != 0: 
    menu = int(input())
    menuPrincipal(menu)
    