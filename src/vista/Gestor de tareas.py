import tkinter as tk
from tkinter import messagebox, ttk

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
        label_status.config(text="Tarea agregada correctamente.", fg="green")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def marcar_completada_gui():
    try:
        index = lista_tareas.curselection()[0]
        gestor.marcar_completada(index)
        actualizar_lista_tareas()
        label_status.config(text="Tarea marcada como completada.", fg="blue")
    except IndexError:
        messagebox.showerror("Error", "Seleccione una tarea para marcar como completada")

def eliminar_tarea_gui():
    try:
        index = lista_tareas.curselection()[0]
        gestor.eliminar_tarea(index)
        actualizar_lista_tareas()
        label_status.config(text="Tarea eliminada correctamente.", fg="red")
    except IndexError:
        messagebox.showerror("Error", "Seleccione una tarea para eliminar")

def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)
    for tarea in gestor.tareas:
        if tarea.completada:
            lista_tareas.insert(tk.END, f"{tarea.titulo} - COMPLETADA")
        else:
            lista_tareas.insert(tk.END, tarea)

# Inicializar gestor de tareas
gestor = GestorTareas()

# Configuración de la ventana de la interfaz
root = tk.Tk()
root.title("Gestor de Tareas Mejorado")
root.geometry("500x450")
root.resizable(False, False)

# Colores y tema
root.config(bg="#f0f0f0")

# Marco principal
frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
frame.pack(expand=True, fill=tk.BOTH)

# Etiquetas y campos de entrada
label_titulo = tk.Label(frame, text="Título de la tarea:", bg="#f0f0f0", font=("Arial", 10))
label_titulo.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_titulo = tk.Entry(frame, width=40, font=("Arial", 10))
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame, text="Descripción:", bg="#f0f0f0", font=("Arial", 10))
label_descripcion.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_descripcion = tk.Entry(frame, width=40, font=("Arial", 10))
entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

# Botones para acciones
btn_frame = tk.Frame(frame, bg="#f0f0f0")
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

btn_agregar = tk.Button(btn_frame, text="Agregar Tarea", command=agregar_tarea_gui, width=15, bg="#4CAF50", fg="white", font=("Arial", 10))
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_completar = tk.Button(btn_frame, text="Marcar Completada", command=marcar_completada_gui, width=15, bg="#2196F3", fg="white", font=("Arial", 10))
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(btn_frame, text="Eliminar Tarea", command=eliminar_tarea_gui, width=15, bg="#F44336", fg="white", font=("Arial", 10))
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Lista de tareas con scrollbar
lista_frame = tk.Frame(frame, bg="#f0f0f0")
lista_frame.grid(row=3, column=0, columnspan=2, pady=5)

scrollbar = tk.Scrollbar(lista_frame, orient=tk.VERTICAL)
lista_tareas = tk.Listbox(lista_frame, width=60, height=10, selectmode=tk.SINGLE, font=("Arial", 10), yscrollcommand=scrollbar.set, bg="#ffffff")
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_tareas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Etiqueta de estado
label_status = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 10), fg="black")
label_status.grid(row=4, column=0, columnspan=2, pady=5)

# Ejecutar la aplicación
root.mainloop()
