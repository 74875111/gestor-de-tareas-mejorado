import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "[X]" if self.completada else "[ ]"
        return f"{estado} {self.titulo}: {self.descripcion}"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].completada = True

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            del self.tareas[index]

def agregar_tarea_gui():
    titulo = entry_titulo.get()
    descripcion = entry_descripcion.get()
    try:
        gestor.agregar_tarea(titulo, descripcion)
        actualizar_lista_tareas()
        entry_titulo.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def marcar_completada_gui():
    try:
        index = lista_tareas.curselection()[0]
        gestor.marcar_completada(index)
        actualizar_lista_tareas()
    except IndexError:
        messagebox.showerror("Error", "Seleccione una tarea para marcar como completada")

def eliminar_tarea_gui():
    try:
        index = lista_tareas.curselection()[0]
        gestor.eliminar_tarea(index)
        actualizar_lista_tareas()
    except IndexError:
        messagebox.showerror("Error", "Seleccione una tarea para eliminar")

def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)
    for tarea in gestor.tareas:
        lista_tareas.insert(tk.END, str(tarea))

# Inicializar gestor de tareas
gestor = GestorTareas()

# Configuración de la ventana de la interfaz
root = tk.Tk()
root.title("Gestor de Tareas Mejorado")
root.geometry("500x400")
root.resizable(False, False)

# Marco principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

# Etiquetas y campos de entrada
label_titulo = tk.Label(frame, text="Título de la tarea:")
label_titulo.grid(row=0, column=0, sticky="w")
entry_titulo = tk.Entry(frame, width=40)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame, text="Descripción:")
label_descripcion.grid(row=1, column=0, sticky="w")
entry_descripcion = tk.Entry(frame, width=40)
entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

# Botones para acciones
btn_frame = tk.Frame(frame)
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

btn_agregar = tk.Button(btn_frame, text="Agregar Tarea", command=agregar_tarea_gui, width=15)
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_completar = tk.Button(btn_frame, text="Marcar Completada", command=marcar_completada_gui, width=15)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar Tarea", command=eliminar_tarea_gui, width=15)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(frame, width=60, height=15)
lista_tareas.grid(row=3, column=0, columnspan=2, pady=5)

# Ejecutar la aplicación
root.mainloop()
