import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))



import tkinter as tk
from tkinter import ttk

class InterfazQuimico:
    def __init__(self, root):
        self.root = root
        self.root.title("Asignar Ingredientes a Producto")
        self.root.geometry("1000x800")
        self.ingredients = []

        # Selección de Producto
        self.product_label = tk.Label(root, text="Seleccionar Producto:")
        self.product_label.pack(pady=5)
        
        self.product_combobox = ttk.Combobox(root, values=["Producto A", "Producto B", "Producto C"])
        self.product_combobox.pack(pady=5)
        
        self.select_button = tk.Button(root, text="Seleccionar", command=self.select_product)
        self.select_button.pack(pady=5)
        
        # Frame para contener los elementos que deben aparecer después de seleccionar el producto
        self.content_frame = tk.Frame(root)

        # Entrada de Ingredientes
        self.ingredient_label = tk.Label(self.content_frame, text="Ingrediente:")
        self.ingredient_entry = tk.Entry(self.content_frame)
        
        self.quantity_label = tk.Label(self.content_frame, text="Cantidad:")
        self.quantity_entry = tk.Entry(self.content_frame)
        
        self.add_button = tk.Button(self.content_frame, text="Agregar Ingrediente", command=self.add_ingredient)
        
        # Frame con Scroll para lista de ingredientes
        self.frame_container = tk.Frame(self.content_frame)
        
        self.canvas = tk.Canvas(self.frame_container)
        self.scrollbar = tk.Scrollbar(self.frame_container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.send_button = tk.Button(self.content_frame, text="Asignar Ingredientes y Enviar al Asesor Comercial", command=self.send_data)
        
    def select_product(self):
        selected_product = self.product_combobox.get()
        if selected_product:
            self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            self.ingredient_label.pack()
            self.ingredient_entry.pack()
            self.quantity_label.pack()
            self.quantity_entry.pack()
            self.add_button.pack(pady=5)
            self.frame_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.send_button.pack(pady=10)

    def add_ingredient(self):
        ingredient = self.ingredient_entry.get()
        quantity = self.quantity_entry.get()
        
        if ingredient and quantity:
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(fill=tk.X, pady=2)
            
            label = tk.Label(frame, text=f"{ingredient} - {quantity}", anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            delete_button = tk.Button(frame, text="X", command=lambda: self.remove_ingredient(frame))
            delete_button.pack(side=tk.RIGHT)
            
            self.ingredients.append((ingredient, quantity, frame))
            
            self.ingredient_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)

    def remove_ingredient(self, frame):
        for item in self.ingredients:
            if item[2] == frame:
                self.ingredients.remove(item)
                frame.destroy()
                break

    def send_data(self):
        product = self.product_combobox.get()
        data = [(product, item[0], item[1]) for item in self.ingredients]
        print("Datos enviados:", data)
        
        # Limpiar la interfaz
        self.product_combobox.set("")
        for item in self.ingredients:
            item[2].destroy()
        self.ingredients.clear()
        self.ingredient_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.content_frame.pack_forget()
