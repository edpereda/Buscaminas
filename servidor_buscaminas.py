######################################################################################LIBRERIAS
from socket import *
import sys
import random
import numpy as np
######################################################################################LIBRERIAS
######################################################################################STATIC MAIN
facil = b'f'
intermedio = b'i'
dificil = b'd'
destapar_mina = b'0'
fijar_mina = b'1'
fin_servidor = b'fin'

######################################################################################STATIC MAIN
######################################################################################FUNCIONES COPIADAS
# Genera el tablero como matriz [[]]
def genTablero(filas, columnas, numMinas):
  # X filas
  # Y Columnas
    tab_aux = [0] * (filas * columnas - numMinas) + [-1] * numMinas
    tab_aux = np.random.permutation(tab_aux)

    tab = [
        list(tab_aux[i:i + columnas]) for i in range(0, columnas *filas, columnas)
    ]

    count = 0

    for x in range(0, filas):
        for y in range(0, columnas):
            '''
                (x-1, y-1) (x-1, y) (x-1,y+1) , 
                (x, y-1)       .     (x , y+1)
                (x+1, y-1) (x+1. y) (x+1, y+1) 
                 '''
            if (tab[x][y] == 0):
                count = 0
                if x - 1 >= 0 and y - 1 >= 0 and tab[x - 1][y - 1] == -1:
                    count += 1
                if x - 1 >= 0 and tab[x - 1][y] == -1:
                    count += 1
                if y + 1 < columnas and x - 1 >= 0 and tab[x - 1][y + 1] == -1:
                    count += 1
                #
                if y - 1 >= 0 and tab[x][y - 1] == -1:
                    count += 1
                if y + 1 < columnas and tab[x][y + 1] == -1:
                    count += 1
                #
                if x + 1 < filas and y - 1 >= 0 and tab[x + 1][y - 1] == -1:
                    count += 1
                if x + 1 < filas and tab[x + 1][y] == -1:
                    count += 1
                if x + 1 < filas and y+1<columnas and tab[x + 1][y +1]==-1:
                    count += 1
                tab[x][y] = count
    return tab

# Genera el tablero como string 

def genTableroString(filas, columnas, numMinas):
    s = ""
  # X filas
  # Y Columnas
    tab_aux = [0] * (filas * columnas - numMinas) + [-1] * numMinas
    tab_aux = np.random.permutation(tab_aux)

    tab = [list(tab_aux[i:i + columnas]) for i in range(0, columnas *filas, columnas)]

    count = 0

    for x in range(0, filas):
        
        for y in range(0, columnas):
            '''
                (x-1, y-1) (x-1, y) (x-1,y+1) , 
                (x, y-1)       .     (x , y+1)
                (x+1, y-1) (x+1. y) (x+1, y+1) 
                 '''
            if (tab[x][y] == 0):
                count = 0
                if x - 1 >= 0 and y - 1 >= 0 and tab[x - 1][y - 1] == -1:
                    count += 1
                if x - 1 >= 0 and tab[x - 1][y] == -1:
                    count += 1
                if y + 1 < columnas and x - 1 >= 0 and tab[x - 1][y + 1] == -1:
                    count += 1
                #
                if y - 1 >= 0 and tab[x][y - 1] == -1:
                    count += 1
                if y + 1 < columnas and tab[x][y + 1] == -1:
                    count += 1
                #
                if x + 1 < filas and y - 1 >= 0 and tab[x + 1][y - 1] == -1:
                    count += 1
                if x + 1 < filas and tab[x + 1][y] == -1:
                    count += 1
                if x + 1 < filas and y+1<columnas and tab[x + 1][y +1]==-1:
                    count += 1
                #tab[x][y] = count
                s=s+str(count)+" "
            else :
                s=s+"* "
        s+='\n'
    return s

print(genTableroString(9,9,10))
######################################################################################FUNCIONES COPIADAS
######################################################################################FUNCIONES
"""def se_encuentra(lista,valor):
	for elemento in range(len(lista)):
		if valor==lista[elemento]:

			return 0
	return 1

def generar_matriz(dificultad):
	numero_filas=0
	numero_columnas=0
	numero_minas=0
	minas_posicionesf= [0]
	minas_posicionesc= [0]

	if dificultad==facil:
		print('dificultad = facil')
		numero_filas=9
		numero_columnas=9
		numero_minas=10
	elif dificultad==intermedio:
		print('dificultad = intermedio')
		numero_filas=16
		numero_columnas=16
		numero_minas=40
	else:
		print('dificultad = dificil')
		numero_filas=16
		numero_columnas=30
		numero_minas=99

	matriz = []									#Aqui ya estamos generando una matriz tamaño depende de dificultad
	for i in range(numero_columnas):
		matriz.append([0]*numero_filas)


	for i in range(numero_minas):
		posicionf= random.randint(0,numero_filas-1)
		posicionc= random.randint(0,numero_columnas-1)	#generamos posiciones aleatorias
		
		print('randomf: ',posicionf,end="")
		print(' randomc: ',posicionc)
		FALTA UN IF QUE VALIDE SI YA SE HABIA COLOCADO UNA MINA AHI ANTES
		if (se_encuentra(minas_posicionesf,posicionf)==1)&(se_encuentra(minas_posicionesc,posicionc)==1):
			print('NO SE ENCONTRO PREVIAMENTE')
			matriz[posicionc][posicionf]=-1							#la posicion aleatorio la rellenamos con mina (-1)
			minas_posicionesf.append(posicionf)							#guardamos la primera posicion
			minas_posicionesc.append(posicionc)
		else:
			print(i)
			i=i-1
			print(i)



	for i in range(numero_columnas):
		for j in range(numero_filas):
			print(' Valor ',i,j,' : ',matriz[i][j],end="")		#Este es solo para verificar si se esta generando la matriz con 0 y -1
	print("\n")

	return matriz"""


 


######################################################################################FUNCIONES
######################################################################################MAIN
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
i=1
while  i<2:
	
	serverSocket.bind(("",serverPort))
	print("The server is ready to receive")		#Aqui creamos el servidor y que empiece en un while forever
	comando, clientAdress = serverSocket.recvfrom(2048)
	print('Comando recibido: ',comando)



	if (comando==facil)|(comando==intermedio)|(comando==dificil):
																
		#matriz=generar_matriz(comando)	#Esta funcion me genera la matriz tamaño dependiendo de la dificultad

		"""for i in range(30):
			for j in range(16):
				print('Valor ',i,j,' : ',matriz[i][j],'  ',end="")
		print(end="\n")									___________________SOLO SIRVE PARA HACER PRUEBAS"""

		#ENVIAR MATRIZ
		if comando==facil:
			matriz=genTablero(9,9,10)
			for i in range (9):
				for j in range (9):
					print('Enviando valor: ',matriz[i][j])
					valor=str(matriz[i][j])		#Convertimos el valor en cadena para ser serializado
					valor_b=valor.encode()		#Ya esta el valor serializado
					serverSocket.sendto(valor_b,clientAdress)		#Enviamos el valor

		elif comando==intermedio:
			matriz=genTablero(16,16,40)
			for i in range (16):
				for j in range (16):
					print('Enviando valor: ',matriz[i][j])
					valor=str(matriz[i][j])		#Convertimos el valor en cadena para ser serializado
					valor_b=valor.encode()		#Ya esta el valor serializado
					serverSocket.sendto(valor_b,clientAdress)		#Enviamos el valor
		else:
			matriz=genTablero(30,16,99)
			for i in range (30):
				for j in range (16):
					print('Enviando valor: ',matriz[i][j])
					valor=str(matriz[i][j])		#Convertimos el valor en cadena para ser serializado
					valor_b=valor.encode()		#Ya esta el valor serializado
					serverSocket.sendto(valor_b,clientAdress)		#Enviamos el valor
		
		"""palabra_enviar=comando
		serverSocket.sendto(palabra_enviar,clientAdress)_____________SOLO SIRVE PARA HACER PRUEBAS"""
		
	else:														#Aqui recibimos los comandos por parte del cliente
		"""if comando==destapar_mina:
			pass
		elif comando==fijar_mina:
			pass
		elif comando==fin_servidor:
			serverSocket.close()
		else:"""
		print('Comando no valido')														

	
######################################################################################MAIN
