from tkinter import ttk
from tkinter import *
from astar import AlgoritmoAstar as al
from graph import Graph as G
import sys, os, math

# Funciones
#-------------------------------------------------------------------------------------------------
def hallarTrayecto():
    if len(origen.get()) == 0 or len(destino.get()) == 0:
        message["text"] = "Es necesario insertar destino y origen"
        time["text"] = ""
        
        # Cleaning Table 
        records = tree.get_children()
        for element in records:
            tree.delete(element)

    elif origen.get() == destino.get():
        message["text"] = "Destino y origen tienen que ser distintos"
        time["text"] = ""
        
        # Cleaning Table 
        records = tree.get_children()
        for element in records:
            tree.delete(element)

    else:
        message["text"] = ""
        time["text"] = ""

        # Cleaning Table
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        
        # Algoritmo
        a = al(origen.get(), destino.get())
        a.algoritmo()
        recorrido = a.getRecorrido()

        # Filling data
        for i in range(len(recorrido)):
           tree.insert('', 0, text = recorrido[i][0], values = recorrido[i][1])

        time["text"] = "Tiempo total: " + str(a.getTiempo()) + " minutos"

def respath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Raíz
#-------------------------------------------------------------------------------------------------
root = Tk()
root.title('Guía metro Atenas')
root.iconbitmap(respath("icono.ico"))
root.config(bg = "#076BD7")
root.resizable(0,0)


# Título
#-------------------------------------------------------------------------------------------------
label0 = Label(root, text ="")
label0.grid(row = 0, column = 0, columnspan = 3, )
label0.config(bg = "#076BD7")

label1 = Label(root, text ="Atenas")
label1.grid(row = 1, column = 0, columnspan = 3)
label1.config(fg = "white", bg = "#076BD7", font = ("Bahnschrift", 32))

label2 = Label(root, text ="Guía de metro")
label2.grid(row = 2, column = 0, columnspan = 3)
label2.config(fg = "white", bg = "#076BD7", font = ("Bahnschrift", 16))

label3 = Label(root, text ="")
label3.grid(row = 3, column = 0, columnspan = 3)
label3.config(bg = "#076BD7")

label4 = Label(root, text ="")
label4.grid(row = 5, column = 0, columnspan = 3, )
label4.config(bg = "#076BD7")


# Frame mapa
#-------------------------------------------------------------------------------------------------
frameMapa = Frame(root)
frameMapa.grid(row = 0, column = 4, rowspan = 20)
frameMapa.config(width = "625", height = "622")

mapa = PhotoImage(file = respath('mapa.png'))
Label(frameMapa, image = mapa, width = "625", height = "622").place(x = "0", y = "0")


# Frame Inputs
#-------------------------------------------------------------------------------------------------
frame = LabelFrame(root, text = 'Seleccione sus preferencias de viaje')
frame.grid(row = 4, column = 0, columnspan = 3, pady = 25)

# Origen Input
Label(frame, text = '* Origen: ').grid(row = 1, column = 0, pady = 7)
style = ttk.Style()
style.configure('my.TCombobox', arrowsize=30)
style.configure('my.TCombobox.Vertical.TScrollbar', arrowsize=28)

grafo = G()
nodos = grafo.getNodos()
values1 = []
for idx in nodos:
    values1.append(f'{idx}')

origen = ttk.Combobox(frame, values=values1, style='my.TCombobox')
origen.grid(row = 1, column = 1, padx = 5)

# Destino Input
Label(frame, text = '* Destino: ').grid(row = 2, column = 0)
style = ttk.Style()
style.configure('my.TCombobox', arrowsize=30)
style.configure('my.TCombobox.Vertical.TScrollbar', arrowsize=28)

values2 = []
for idx in nodos:
    values2.append(f'{idx}')

destino = ttk.Combobox(frame, values=values2, style='my.TCombobox')
destino.grid(row = 2, column = 1, padx  = 5)

# Button "Hallar trayecto óptimo" 
ttk.Button(frame, text = 'Hallar trayecto óptimo', command = hallarTrayecto).grid(row = 5, columnspan = 2, sticky = W + E, pady = 5)


# Frame Ouputs
#-------------------------------------------------------------------------------------------------
# Output Messages 
message = Label(text = '', fg = 'red')
message.grid(row = 10, column = 0, columnspan = 2, sticky = W + E)

# Time Output 
time = Label(text = '')
time.grid(row = 12, column = 0, columnspan = 2, sticky = W + E)

# Table
tree = ttk.Treeview(height = 12, columns = 2)
tree.grid(row = 11, column = 0, columnspan = 2)
tree.heading('#0', text = 'Linea a recorrer:', anchor = CENTER)
tree.heading('#1', text = 'Hasta:', anchor = CENTER)

root.mainloop()