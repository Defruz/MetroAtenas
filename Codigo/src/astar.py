from graph import Graph
from math import radians, cos, sin, asin, sqrt

"""
    Algoritmo A*

"""
class AlgoritmoAstar():

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.path = []

        # Creacion de las listas para nodos abiertos y cerrados
        self.listaAbierta = [self.origen]
        self.listaCerrada = []

        # Creacion del grafo correspondiente al plano del metro
        self.g = Graph()
        self.g.nodes = self.g.getNodos()
        self.g.aristas = self.g.getAristas()
        self.g.nodes[self.origen]["F"] = 0
        self.g.nodes[self.origen]["G"] = 0
        

    # Devuelve el nodo con menor f de la lista para nodos abiertos
    def nodoMenorF(self):
        resultado = self.listaAbierta[0]
        if len(self.listaAbierta) > 1:
            for i in self.listaAbierta:
                if self.g.nodes[i]["F"] < self.g.nodes[resultado]["F"]:
                    resultado = i
        self.listaAbierta.remove(resultado)

        return resultado


    # Devuelve la distancia en linea recta entre dos puntos especificados con
    # su latitud y longitud en los parametros
    def haversine(self, lon1, lat1, lon2, lat2):
        # Convierte los datos expresados en grados decimales a radianes
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # Formula haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))

        # 6731 = radio de la tierra (Km)
        distancia = 6371 * c

        return distancia


    # Calcula la ecuacion de distancia en A*: f = g + h
    def formula(self, padre, hijo):
        # Se calcula h con la formula haversine
        lonDest = self.g.getLongitud(self.destino)
        latDest = self.g.getLatitud(self.destino)
        lonHijo = self.g.getLongitud(hijo)
        latHijo = self.g.getLatitud(hijo)
        distH = self.haversine(lonDest, latDest, lonHijo, latHijo)

        # Se obtiene g del grafo
        distG = self.g.getDistancia(padre, hijo)

        # Se añaden estos valores al nodo para una futura comparacion
        self.g.nodes[hijo]["G"] = self.g.nodes[padre]["G"] + distG
        self.g.nodes[hijo]["H"] = distH
        self.g.nodes[hijo]["F"] = self.g.nodes[hijo]["G"] + self.g.nodes[hijo]["H"]


    # Ejecuta el algoritmo A*
    def algoritmo(self):        
        while(len(self.listaAbierta) > 0):
            self.actual = self.nodoMenorF()
            self.listaCerrada.append(self.actual)

            if self.actual == self.destino:
                self.listaAbierta.clear()
            else:
                listaAdyacentes = list(self.g.getVecinos(self.actual))
                for vecino in listaAdyacentes:
                    # Si el vecino no se encuentra ya en la lista abierta ni en la cerrada, lo añadimos a la abierta
                    if self.listaAbierta.count(vecino) == 0 and self.listaCerrada.count(vecino) == 0:
                        self.formula(self.actual, vecino)
                        # Se apunta al nodo padre desde el vecino
                        self.g.nodes[vecino]["Padre"] = self.actual
                        # Se añade el nodo a la lista abierta puesto que no habia ninguno
                        self.listaAbierta.append(vecino)

                    # Si el vecino ya aparece en la lista abierta, se establecen sus pesos
                    elif self.listaAbierta.count(vecino) > 0:
                        if self.g.nodes[vecino]["G"] < self.g.nodes[self.actual]["G"]:
                            self.formula(self.actual, vecino)
                            self.g.nodes[vecino]["Padre"] = self.actual

        # Se rellena la variable path
        self.camino(self.actual, self.origen)


    # Rellena de forma recursiva la lista path para obtener el recorrido
    def camino(self, nodo1, nodo2):
        self.path.append(nodo1)
        if nodo1 != nodo2:
            self.camino(self.g.nodes[nodo1]["Padre"], nodo2)


    # Devuelve el recorrido calculado listo para añadir en la interfaz
    def getRecorrido(self):
        recorrido = []
        color = ""
        for i in range(len(self.path) - 1):
            if color == "":
                color = self.g.getLinea(self.path[i], self.path[i+1])
                recorrido.append([color, self.path[i]])

            if color != self.g.getLinea(self.path[i], self.path[i+1]):
                color = self.g.getLinea(self.path[i], self.path[i+1])
                recorrido.append([color, self.path[i]])
                        
        return recorrido


    # Devuelve el tiempo total que conlleva realizar el recorrido calculado
    def getTiempo(self):
        tiempo = 0
        linea = self.g.getLinea(self.path[0], self.path[1])

        for i in range(len(self.path) - 1):
            tiempo += self.g.getTiempoArista(self.path[i], self.path[i+1])

            if self.g.getLinea(self.path[i], self.path[i+1]) != linea:
                tiempo += self.g.getTiempoNodo(self.path[i])

        return tiempo