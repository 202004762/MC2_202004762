import tkinter as tk
import networkx as nx
from graphviz import Digraph
from PIL import Image, ImageTk

vertices = []
aristas = []

def agregar_vertice():

    vertice = vertice_entry.get()
    vertices.append(vertice)
    vertice_entry.delete(0, tk.END)
    actualizar_resumen()

def agregar_arista():

    arista = arista_entry.get()
    aristas.append((arista))
    arista_entry.delete(0, tk.END)
    actualizar_resumen()

def generar_grafo():

    G = Digraph(comment='Grafo generado')
    G.node_attr.update(shape='circle')
    for vertice in vertices:
        G.node(vertice)

    for arista in aristas:
        a, b = arista.split(">")
        G.edge(a, b)

    G.render('grafo.gv', view=False, format='png')
    imagen = Image.open('grafo.gv.png')
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.grid(row=0, column=6, rowspan=3)
    
def actualizar_resumen():

    resumen.delete("1.0", tk.END)
    resumen.insert(tk.END, "Vértices:\n")
    for vertice in vertices:
        resumen.insert(tk.END, "- " + vertice + "\n")

    resumen.insert(tk.END, "\nAristas:\n")
    for arista in aristas:
        resumen.insert(tk.END, "- " + arista)

def analizar_grafo():

    visitados = []
    cola = []

    origen = origen_entry.get()
    print("\nLista de recorrido en anchura\n")
    cola.append(origen)
    while cola:
        actual = cola.pop(0)
        if actual not in visitados:
            print("Vertice actual -> ", actual)
            visitados.append(actual)
            
        for vertice in vertices[actual]:
            if vertice not in visitados:
                cola.append(vertice)

    print()

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto 1")

# Crear los elementos de la interfaz
vertice_label = tk.Label(root, text="Vértice:")
vertice_entry = tk.Entry(root)
agregar_vertice_button = tk.Button(root, text="Agregar", command=agregar_vertice)

arista_label = tk.Label(root, text="Arista (A>B):")
arista_entry = tk.Entry(root)
agregar_arista_button = tk.Button(root, text="Agregar", command=agregar_arista)

origen_label = tk.Label(root, text="Origen:")
origen_entry = tk.Entry(root)
generar_anchura_button = tk.Button(root, text="Generar", command=analizar_grafo)

generar_grafo_button = tk.Button(root, text="Generar grafo", command=generar_grafo)

resumen = tk.Text(root)

# Ubicar los elementos en la interfaz
vertice_label.grid(row=0, column=0, sticky="E")
vertice_entry.grid(row=0, column=1)
agregar_vertice_button.grid(row=0, column=2)

arista_label.grid(row=1, column=0, sticky="E")
arista_entry.grid(row=1, column=1)
agregar_arista_button.grid(row=1, column=2)

origen_label.grid(row=2, column=0, sticky="E")
origen_entry.grid(row=2, column=1)
generar_anchura_button.grid(row=2, column=2)

generar_grafo_button.grid(row=3, column=1)

resumen.grid(row=0, column=6, rowspan=4)

root.mainloop()