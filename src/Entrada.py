# -*- coding: utf-8 -*-
'''
Created on 06/04/2015
@author: Isaac
'''
import random
from pip._vendor.distlib.compat import raw_input

numVariables = 0
numSoluciones = 0 
numIteraciones = 0 
listaIntervalos = []

def main():
    global numVariables, numSoluciones , numIteraciones
    numVariables = int(raw_input("Numero de variables: "))
    numSoluciones = int(raw_input("Numero de soluciones a generar: "))
    numIteraciones = int(raw_input("Numero de iteraciones: "))
    limites = raw_input("Introduzca un intervalo global para las variables [Li Ls]: ")
    opc = raw_input("Generar intervalos distintos para cada variable? (s/n): ")
    opc = opc.upper()   
    if "S" in opc:
        print("Todas las variables tendran un valor aleatorio contenido en ", limites)
        crearIntervalos(limites, numVariables, 0)
    elif "N" :
        crearIntervalos(limites, numVariables, 1)
    else:
        print("Opcion incorrecta")
    generaArchivo()
    
def generarAleatorios(li, ls):
    random.randrange(li, ls, 1)
    
def crearIntervalos(limites, numVariables, modo):
    limites = limites.split(' ')
    lgi = int(limites[0]) 
    lgs = int(limites[1]) + 1  # Para incluir  el limite superior en el intervalo
    if modo == 0: 
        for i in range(numVariables):
            li = random.randrange(lgi, lgs, 1)
            ls = random.randrange(li, lgs, 1)
            # print("Nuevo limite: " , li , "," , ls)
            listaIntervalos.append(li)
            listaIntervalos.append(ls)
    else:
            li = random.randrange(lgi, lgs, 1)
            ls = random.randrange(li, lgs, 1)
            listaIntervalos.append(li)
            listaIntervalos.append(ls)
    
def generaArchivo():
    global numVariables, numSoluciones , numIteraciones , listaIntervalos
    print("Generando archivo...")
    archivo = open("entradaN.txt", "w")
    archivo.write(str(numVariables))
    archivo.write("\n")
    archivo.write(str(numSoluciones))
    archivo.write("\n")
    archivo.write(str(numIteraciones))
    archivo.write("\n")
    cont = 0
    for limite in listaIntervalos:
        if cont>1 and cont%2 == 0:
                archivo.write(";")
        archivo.write(str(limite))
        if (cont+1)%2 != 0:
            archivo.write(" ")
        cont = cont + 1
    archivo.write("\n")
    archivo.close()
    print("Archivo generado con exito.")
main()
