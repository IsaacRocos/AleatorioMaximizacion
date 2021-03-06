'''
Created on 30/03/2015
@author: Isaac
'''
import sys
import random
from pip._vendor.distlib.compat import raw_input
class PMaximizacion(object):
    
    # Atributos
    nVariables = 0
    nSoluciones = 0
    nIteraciones = 0
    listaIntervalos = ['']
    #-----------
    
    def __init__(self, params):
        # Verificando parametros de entrada
        if len(sys.argv) <= 1:
            print("No hay argumentos de entrada para el programa")
        else:
            argumento = sys.argv[1]
            print("Argumento encontrado <", argumento, "> Procesando...")
            self.procesarEntrada(argumento)
        self.imprimirAtributos()
        self.RUN()
        
    def procesarEntrada(self, nombreArchivo):
        entrada = open(nombreArchivo, 'r')
        nVar = int(entrada.readline())
        nSol = int(entrada.readline())
        nIter = int(entrada.readline())
        liInt = entrada.readline()
        entrada.close()
        #Proceso para lista de intervalos --
        liInt = liInt.replace('\n','')
        liInt = liInt.split(";")
        indice = 0
        for intervalo in liInt:
            intervalo = intervalo.split(" ")
            liInt[indice] = intervalo
            indice = indice +1
        # ----------------------------------
        self.setNVariables(nVar)
        self.setNSoluciones(nSol)
        self.setNIteraciones(nIter)
        self.setListaIntervalos(liInt)
        print("Proceso terminado. Variables de programa incializadas.")
    
    def setNVariables(self, nVar):
        global nVariables
        nVariables = nVar
    
    def setNSoluciones(self, nSol):
        global nSoluciones
        nSoluciones = nSol
    
    def setNIteraciones(self, nIter):
        global nIteraciones 
        nIteraciones = nIter
    
    def setListaIntervalos(self, liInt):
        global listaIntervalos 
        listaIntervalos = liInt
    
    def RUN(self):
        global nVariables, nSoluciones, nIteraciones , listaIntervalos
        mejoresSol = [] 
        # Algoritmo principal -----------
        print("Ejecutando algoritmo...")
        for j in range(nIteraciones):
            listaSoluciones = self.crearSoluciones(listaIntervalos,nSoluciones,nVariables)
            listaAptitudes = self.evaluarAptitudes(listaSoluciones)
            mejorAptitud = self.obtenerMejorAptitud(listaAptitudes)
            mejorAptitud.append(j)  # para saber en que iteracion se presenta
            self.evaluarMejorSolucion(mejorAptitud,mejoresSol)
            if j%50 == 0:
                mejorActual = mejoresSol[len(mejoresSol) - 1]
                print("[Itr -",j,"] Mejor solucion actual:\n >> |APTITUD|: [",mejorActual[0],"] |SOLUCION|", mejorActual[1], " en |ITERACION|",mejorActual[2],"\n")
        # FIN Algoritmo principal -----------
        print("\nFin de ejecicion.")
        self.imprimirEstadoFinal(mejoresSol)
        
                   
    def crearSoluciones(self,listaIntervalos,nSoluciones,nVariables):
        #print(listaIntervalos,nSoluciones,nVariables)
        grupoSoluciones = []
        for solucion in range(nSoluciones):
            nuevaSolucion = []
            for variable in range(nVariables):
                li = int(listaIntervalos[variable][0])
                ls = int(listaIntervalos[variable][1]) +1
                nuevaSolucion.append(random.randrange(li,ls, 1))
            grupoSoluciones.append(nuevaSolucion)
        #print("\nSoluciones Creadas:\n",grupoSoluciones)
        return grupoSoluciones
        
        
    def evaluarAptitudes(self, listaSoluciones):
        listaAptitudes = []
        for solucion in listaSoluciones:
            aptitud = 0
            for x in solucion:
                if x == 0:
                    aptitud = aptitud + 1
            listaAptitudes.append(aptitud)
        return listaAptitudes

    def obtenerMejorAptitud(self, listaAptitudes):
        mejorApt = 0
        mejorSolucion = 0
        for aptitud in listaAptitudes:
            if aptitud > mejorApt:
                mejorApt = aptitud
                mejorSolucion = listaAptitudes.index(aptitud)
        mejor = []
        mejor.append(mejorApt)
        mejor.append(mejorSolucion)
        return mejor
        
    def evaluarMejorSolucion(self, mejorAptitud,mejoresSol):
        tamanioSoluciones = len(mejoresSol)
        if tamanioSoluciones == 0:
            mejoresSol.append(mejorAptitud)
            # Comparar aptitudes de la mejor solucion en la cola y agrega mejorAptitud si se cumple la condicion
        elif mejoresSol[tamanioSoluciones - 1][0] <= mejorAptitud[0]: 
            mejoresSol.append(mejorAptitud)
        tamanioSoluciones = len(mejoresSol)
        if tamanioSoluciones > 50:  # para mantener un grupo de 50 mejores soluciones
            del mejoresSol[0]
        
    
    # Para verificar que la carga de los datos se hizo adecuadamente
    def imprimirAtributos(self):
        global nVariables, nSoluciones, nIteraciones, listaIntervalos
        print("Numero de variables: ", nVariables)
        print("Numero de soluciones: ", nSoluciones)
        print("Numero de iteraciones: ", nIteraciones)
        #print(listaIntervalos)

    def imprimirEstadoFinal(self,mejoresSol):
        mejorFinal = mejoresSol[len(mejoresSol) - 1]
        print("[FIN] MEJOR SOLUCION:\n >>> |APTITUD|: [",mejorFinal[0],"] |SOLUCION|: ", mejorFinal[1], " encontrada en |ITERACION| ",mejorFinal[2],"\n")
        opc = "s"
        opc = raw_input("Imprimir conjuto de mejores soluciones? (s/n): ")
        opc = opc.upper()   
        if "S" in opc:
            print("----------------------------------------")
            print("--------- Mejores soluciones -----------")
            print("----------------------------------------")
            contador = 0
            for solucion in mejoresSol:
                print(contador,"] |Sol|", solucion[1], "|Iter|",solucion[2],"|Aptitud|",solucion[0]," \n")
                contador = contador+1
        print("FIN de Proframa")

maximizar = PMaximizacion("") 



'''
sol1 = [1, 1, 0, 0, 1]
        sol2 = [1, 1, 1, 0, 0]
        sol3 = [0, 1, 1, 1, 0]
        sol4 = [0, 1, 1, 0, 0]
        soluciones.append(sol1)
        soluciones.append(sol2)
        soluciones.append(sol3)
        soluciones.append(sol4)

'''