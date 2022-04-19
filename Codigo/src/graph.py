import networkx as nx

"""
    Grafo equivalente al plano de metro dado de Atenas

"""
class Graph():

    def __init__(self):

        # Creacion del grafo que contendra la informacion del plano
        self.G = nx.Graph()

        # Adiccion de las estaciones del mapa como nodos, donde se guardan las propiedades de latitud,
        # longitud y tiempo del transbordo si se hiciese
        self.G.add_node("Aghia Paraskevi", latitud = 38.01740965821040, longitud = 23.8123227150724000, tiempo = 0)
        self.G.add_node("Aghios Antonios", latitud = 38.00661747564150, longitud = 23.699581953675100, tiempo = 0)
        self.G.add_node("Aghios Dimitrios", latitud = 37.94046741270470, longitud = 23.740698453057600, tiempo = 0)
        self.G.add_node("Aghios Eleftherios", latitud = 38.02005527840040, longitud = 23.731858265461400, tiempo = 0)
        self.G.add_node("Aghios Ioannis", latitud = 37.95664775317310, longitud = 23.734706010409700, tiempo = 0)
        self.G.add_node("Aghios Nikolaos", latitud = 38.00692547935300, longitud = 23.727687812983400, tiempo = 0)
        self.G.add_node("Airport", latitud = 37.93672535036870, longitud = 23.944595773268900, tiempo = 0)
        self.G.add_node("Akropoli", latitud = 37.96874034111180, longitud = 23.729627966197500, tiempo = 0)
        self.G.add_node("Ambelokipi", latitud = 37.98735138885830, longitud = 23.756987969209600, tiempo = 0)
        self.G.add_node("Ano Patissia", latitud = 38.02427150161050, longitud = 23.735872326962400, tiempo = 0)
        self.G.add_node("Attiki", latitud = 38.00009678149000, longitud = 23.722818362942800, tiempo = 3)
        self.G.add_node("Dafni", latitud = 37.94941261287580, longitud = 23.737194671277300, tiempo = 0)
        self.G.add_node("Doukissis Plakentias", latitud = 38.02424024805810, longitud = 23.833707873378900, tiempo = 0)
        self.G.add_node("Egaleo", latitud = 37.99194682835210, longitud = 23.681904457703100, tiempo = 0)
        self.G.add_node("Eleonas", latitud = 37.98773546228400, longitud = 23.693766309164700, tiempo = 0)
        self.G.add_node("Ethniki Amyna", latitud = 38.00021095515000, longitud = 23.785686510965300, tiempo = 0)
        self.G.add_node("Evangelismos", latitud = 37.97620946367170, longitud = 23.746699480852200, tiempo = 0)
        self.G.add_node("Faliro", latitud = 37.94568486541900, longitud = 23.665137416298300, tiempo = 0)
        self.G.add_node("Halandri", latitud = 38.02241870800220, longitud = 23.821477718803900, tiempo = 0)
        self.G.add_node("Holargos", latitud = 38.00655461821750, longitud = 23.795055554102000, tiempo = 0)
        self.G.add_node("Iraklio", latitud = 38.04619118054800, longitud = 23.766138212922400, tiempo = 0)
        self.G.add_node("Irini", latitud = 38.04375132708200, longitud = 23.782722127717800, tiempo = 0)
        self.G.add_node("Kallithea", latitud = 37.96047737234800, longitud = 23.697280078107100, tiempo = 0)
        self.G.add_node("KAT", latitud = 38.06609411473510, longitud = 23.804032297543900, tiempo = 0)
        self.G.add_node("Katehaki", latitud = 37.99345784216750, longitud = 23.776168720214700, tiempo = 0)
        self.G.add_node("Kato Patissia", latitud = 38.01157933905770, longitud = 23.728751668641800, tiempo = 0)
        self.G.add_node("Kerameikos", latitud = 37.97837883780690, longitud = 23.712225807252300, tiempo = 0)
        self.G.add_node("Kifissia", latitud = 38.07388222960260, longitud = 23.808402082717000, tiempo = 0)        
        self.G.add_node("Koropi", latitud = 37.91352096635980, longitud = 23.895878569297500, tiempo = 0)
        self.G.add_node("Larissa Station", latitud = 37.99221126143500, longitud = 23.721100883243000, tiempo = 0)
        self.G.add_node("Maroussi", latitud = 38.05616664983900, longitud = 23.804957842267100, tiempo = 0)
        self.G.add_node("Megaro Moussikis", latitud = 37.97921608945980, longitud = 23.752892274663500, tiempo = 0)
        self.G.add_node("Metaxourghio", latitud = 37.98628610646960, longitud = 23.721129356029300, tiempo = 0)
        self.G.add_node("Moschato", latitud = 37.95583068090450, longitud = 23.665137416298300, tiempo = 0)
        self.G.add_node("Monastiraki", latitud = 37.97605964564880, longitud = 23.725609100061900, tiempo = 5)
        self.G.add_node("Neo Ionia", latitud = 38.04161552930390, longitud = 23.755203742985600, tiempo = 0)
        self.G.add_node("Neos-Kosmos", latitud = 37.95758990477510, longitud = 23.728448853480300, tiempo = 0)
        self.G.add_node("Neratziotissa", latitud = 38.04483832271780, longitud = 23.792837792391700, tiempo = 0)
        self.G.add_node("Nomismatokopio", latitud = 38.00942534350420, longitud = 23.805683617931800, tiempo = 0)
        self.G.add_node("Omonia", latitud = 37.98415061182990, longitud = 23.728680352643500, tiempo = 3)
        self.G.add_node("Paiania-Kantza", latitud = 37.98504840373140, longitud = 23.870092786854400, tiempo = 0)
        self.G.add_node("Pallini", latitud = 38.00589134989510, longitud = 23.869608913797000, tiempo = 0)
        self.G.add_node("Panepistimio", latitud = 37.98416642140640, longitud = 23.728718151662900, tiempo = 0)
        self.G.add_node("Panormou", latitud = 37.99412869296420, longitud = 23.763520478891300, tiempo = 0)
        self.G.add_node("Pefkakia", latitud = 38.03714668565720, longitud = 23.750208304291900, tiempo = 0)
        self.G.add_node("Perissos", latitud = 38.03291294798850, longitud = 23.744701869067800, tiempo = 0)
        self.G.add_node("Petralona", latitud = 37.96858181266130, longitud = 23.709297857304200, tiempo = 0)
        self.G.add_node("Piraeus", latitud = 37.94793429430930, longitud = 23.643349181873900, tiempo = 0)
        self.G.add_node("Sepolia", latitud = 38.00264982282370, longitud = 23.713515495852900, tiempo = 0)
        self.G.add_node("Sygrou-Fix", latitud = 37.96466217996560, longitud = 23.726531249560400, tiempo = 0)
        self.G.add_node("Syntagma", latitud = 37.97538256047030, longitud = 23.735713958304500, tiempo = 2)
        self.G.add_node("Tavros", latitud = 37.96275292744730, longitud = 23.703372582659200, tiempo = 0)
        self.G.add_node("Thissio", latitud = 37.97694229344330, longitud = 23.720719074844900, tiempo = 0)
        self.G.add_node("Victoria", latitud = 37.99373877683740, longitud = 23.730457293563500, tiempo = 0)        


        
        # Adiccion de las vias entre estaciones como aristas, donde se guardan las propiedades de linea,
        # distancia y tiempo

        # LINEA 1
        self.G.add_edge("Piraeus", "Faliro", linea = "Linea 1", distancia = 2.10, tiempo = 3)
        self.G.add_edge("Faliro", "Moschato", linea = "Linea 1", distancia = 1.79, tiempo = 3)
        self.G.add_edge("Moschato", "Kallithea", linea = "Linea 1", distancia = 1.67, tiempo = 3)
        self.G.add_edge("Kallithea", "Tavros", linea = "Linea 1", distancia = 0.585, tiempo = 1)
        self.G.add_edge("Tavros", "Petralona", linea = "Linea 1", distancia = 0.870, tiempo = 2)
        self.G.add_edge("Petralona", "Thissio", linea = "Linea 1", distancia = 1.58, tiempo = 3)
        self.G.add_edge("Thissio", "Monastiraki", linea = "Linea 1", distancia = 0.458, tiempo = 1)
        self.G.add_edge("Monastiraki", "Omonia", linea = "Linea 1", distancia = 0.946, tiempo = 3)
        self.G.add_edge("Omonia", "Victoria", linea = "Linea 1", distancia = 1.01, tiempo = 2)
        self.G.add_edge("Victoria", "Attiki", linea = "Linea 1", distancia = 1.10, tiempo = 3)
        self.G.add_edge("Attiki", "Aghios Nikolaos", linea = "Linea 1", distancia = 0.961, tiempo = 2)
        self.G.add_edge("Aghios Nikolaos", "Kato Patissia", linea = "Linea 1", distancia = 0.538, tiempo = 2)
        self.G.add_edge("Kato Patissia", "Aghios Eleftherios", linea = "Linea 1", distancia = 1.01, tiempo = 2)
        self.G.add_edge("Aghios Eleftherios", "Ano Patissia", linea = "Linea 1", distancia = 0.569, tiempo = 2)
        self.G.add_edge("Ano Patissia", "Perissos", linea = "Linea 1", distancia = 1.31, tiempo = 2)
        self.G.add_edge("Perissos", "Pefkakia", linea = "Linea 1", distancia = 0.655, tiempo = 2)
        self.G.add_edge("Pefkakia", "Neo Ionia", linea = "Linea 1", distancia = 0.715, tiempo = 1)
        self.G.add_edge("Neo Ionia", "Iraklio", linea = "Linea 1", distancia = 1.30, tiempo = 3)
        self.G.add_edge("Iraklio", "Irini", linea = "Linea 1", distancia = 1.54, tiempo = 2)
        self.G.add_edge("Irini", "Neratziotissa", linea = "Linea 1", distancia = 1.02, tiempo = 2)
        self.G.add_edge("Neratziotissa", "Maroussi", linea = "Linea 1", distancia = 1.66, tiempo = 3)
        self.G.add_edge("Maroussi", "KAT", linea = "Linea 1", distancia = 1.18, tiempo = 3)
        self.G.add_edge("KAT", "Kifissia", linea = "Linea 1", distancia = 1.03, tiempo = 2)
        
        # LINEA 2
        self.G.add_edge("Aghios Antonios", "Sepolia", linea = "Linea 2", distancia = 1.32, tiempo = 2)
        self.G.add_edge("Sepolia", "Attiki", linea = "Linea 2", distancia = 0.865, tiempo = 2)
        self.G.add_edge("Attiki", "Larissa Station", linea = "Linea 2", distancia = 0.822, tiempo = 1)
        self.G.add_edge("Larissa Station", "Metaxourghio", linea = "Linea 2", distancia = 0.631, tiempo = 1)
        self.G.add_edge("Metaxourghio", "Omonia", linea = "Linea 2", distancia = 0.732, tiempo = 2)
        self.G.add_edge("Omonia", "Panepistimio", linea = "Linea 2", distancia = 0.627, tiempo = 1)
        self.G.add_edge("Panepistimio", "Syntagma", linea = "Linea 2", distancia = 0.595, tiempo = 2)
        self.G.add_edge("Syntagma", "Akropoli", linea = "Linea 2", distancia = 0.901, tiempo = 1)
        self.G.add_edge("Akropoli", "Sygrou-Fix", linea = "Linea 2", distancia = 0.565, tiempo = 2)
        self.G.add_edge("Sygrou-Fix", "Neos-Kosmos", linea = "Linea 2", distancia = 0.781, tiempo = 1)
        self.G.add_edge("Neos-Kosmos", "Aghios Ioannis", linea = "Linea 2", distancia = 0.558, tiempo = 2)
        self.G.add_edge("Aghios Ioannis", "Dafni", linea = "Linea 2", distancia = 0.880, tiempo = 1)
        self.G.add_edge("Dafni", "Aghios Dimitrios", linea = "Linea 2", distancia = 1.01, tiempo = 2)
        
        # LINEA 3
        self.G.add_edge("Egaleo", "Eleonas", linea = "Linea 3", distancia = 1.21, tiempo = 2)
        self.G.add_edge("Eleonas", "Kerameikos", linea = "Linea 3", distancia = 1.81, tiempo = 2)
        self.G.add_edge("Kerameikos", "Monastiraki", linea = "Linea 3", distancia = 1.27, tiempo = 2)
        self.G.add_edge("Monastiraki", "Syntagma", linea = "Linea 3", distancia = 0.922, tiempo = 2)
        self.G.add_edge("Syntagma", "Evangelismos", linea = "Linea 3", distancia = 1.16, tiempo = 1)
        self.G.add_edge("Evangelismos", "Megaro Moussikis", linea = "Linea 3", distancia = 0.628, tiempo = 2)
        self.G.add_edge("Megaro Moussikis", "Ambelokipi", linea = "Linea 3", distancia = 0.990, tiempo = 1)
        self.G.add_edge("Ambelokipi", "Panormou", linea = "Linea 3", distancia = 0.906, tiempo = 2)
        self.G.add_edge("Panormou", "Katehaki", linea = "Linea 3", distancia = 1.12, tiempo = 1)
        self.G.add_edge("Katehaki", "Ethniki Amyna", linea = "Linea 3", distancia = 1.14, tiempo = 2)
        self.G.add_edge("Ethniki Amyna", "Holargos", linea = "Linea 3", distancia = 0.955, tiempo = 2)
        self.G.add_edge("Holargos", "Nomismatokopio", linea = "Linea 3", distancia = 1.13, tiempo = 2)
        self.G.add_edge("Nomismatokopio", "Aghia Paraskevi", linea = "Linea 3", distancia = 1.05, tiempo = 1)
        self.G.add_edge("Aghia Paraskevi", "Halandri", linea = "Linea 3", distancia = 0.920, tiempo = 2)
        self.G.add_edge("Halandri", "Doukissis Plakentias", linea = "Linea 3", distancia = 1.29, tiempo = 2)
        self.G.add_edge("Doukissis Plakentias", "Pallini", linea = "Linea 3", distancia = 4.14, tiempo = 4)
        self.G.add_edge("Pallini", "Paiania-Kantza", linea = "Linea 3", distancia = 2.45, tiempo = 3)
        self.G.add_edge("Paiania-Kantza", "Koropi", linea = "Linea 3", distancia = 8.51, tiempo = 6)
        self.G.add_edge("Koropi", "Airport", linea = "Linea 3", distancia = 5.89, tiempo = 5)


    # Devuelve la latitud del nodo pasado como parametro
    def getLatitud(self, node):
        return self.G.nodes[node]["latitud"]


    # Devuelve la longitud del nodo pasado como parametro
    def getLongitud(self, node):
        return self.G.nodes[node]["longitud"]
    

    # Devuelve el tiempo de transbordo del nodo pasado como parametro
    def getTiempoNodo(self, node):
        return self.G.nodes[node]["tiempo"]


    # Devuelve la linea de la arista que une los nodos pasados como parametro
    def getLinea(self, eFrom, eTo):
        return self.G[eFrom][eTo]["linea"]


    # Devuelve la distancia de la arista que une los nodos pasados como parametro
    def getDistancia(self, eFrom, eTo):
        return self.G[eFrom][eTo]["distancia"]


    # Devuelve el tiempo de la arista que une los nodos pasados como parametro
    def getTiempoArista(self, eFrom, eTo):
        return self.G[eFrom][eTo]["tiempo"]


    # Devuelve una lista con todas las aristas correspondientes al nodo pasado como parametro
    def getNodo(self, node):
        return self.G.nodes[node]
    

    # Devuelve una lista con todos los nodos (estaciones) del grafo
    def getNodos(self):
        return self.G.nodes
    

    # Devuelve una lista con todas las aristas (vias) del grafo
    def getAristas(self):
        return self.G.edges


    # Devuelve una lista con todos los nodos adyacentes al nodo pasado como parametro
    def getVecinos(self, node):
        return self.G.adj[node]