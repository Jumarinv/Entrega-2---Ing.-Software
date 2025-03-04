import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))


from src.gestorAplicacion.administrativo.Cambio import Cambio
from datetime import date
from PIL import Image, ImageTk

from tkinter import messagebox



class InterfazQuimico:
    def __init__(self, root):
        self.root = root
        self.root.title("Quimico")
        self.root.geometry("1000x800")

        self.imagen_fondo = Image.open("descarga1.jpg")
        self.imagen_fondo = self.imagen_fondo.resize((1000, 800))
        self.fondo = ImageTk.PhotoImage(self.imagen_fondo)

        # Crear un label con la imagen
        self.label_fondo = tk.Label(self.root, image=self.fondo)
        self.label_fondo.place(relwidth=1, relheight=1)
        self.label_fondo.image = self.fondo  # Evitar que la imagen sea eliminada por el recolector de basura

        self.crear_interfaz_quimico()

    def crear_interfaz_quimico(self):


        self.bienvenida = tk.Label(self.root, text="Bienvenido quimico", font=("Arial", 22, "bold"))
        self.bienvenida.pack(pady=20)

        self.boton_asignar_ingredientes = tk.Button(self.root,text="Asignar ingredientes a producto", font=("Arial", 12), width=25, height=2, bg="#0056b3", fg="white", 
        command=lambda :self.asignar_ingredientes())

        self.boton_asignar_ingredientes.pack(pady=20)

        botonVolver = tk.Button(self.root, text="Volver al login", font=("Arial", 12), bg="#0056b3", fg="white", command= lambda: self.reingresar(self.root))
        botonVolver.pack(pady=5)


    def eliminar_elementos(self):
        for widget in self.root.winfo_children():
            if widget != self.label_fondo:
                widget.destroy()

    def asignar_ingredientes2(self, producto):
        self.eliminar_elementos()

        self.out_upper_frame = tk.Frame(self.root, bd=2,bg="lightblue")
        self.out_upper_frame.pack(fill="both",expand=True)

        self.upper_frame = tk.Frame(self.out_upper_frame,bd=2,bg="lightblue")
        self.upper_frame.place( relx=0.5,rely=0.5, anchor="center")
        

        self.name_product_label = tk.Label(self.upper_frame,padx=10, pady=10, text="Nombre del producto",bd=2,bg="lightblue")
        self.name_product_label.grid(row = 0,column=0, columnspan=2)

        self.name_product_entry = tk.Entry(self.upper_frame,bd=2,bg="lightblue")
        self.name_product_entry.grid(row=0,column=2, columnspan=3)
        self.name_product_entry.insert(0,producto.nombre)
        self.name_product_entry.config(state="disabled")

        self.quantity_product_label = tk.Label(self.upper_frame, text="Cantidad de producto",bd=2,bg="lightblue")
        self.quantity_product_label.grid(row = 1, column=0, columnspan=2)

        self.quantity_product_entry = tk.Entry(self.upper_frame,bd=2,bg="lightblue")
        self.quantity_product_entry.grid(row = 1, column=2, columnspan=3)
        self.quantity_product_entry.insert(0,str(producto.cantidad))
        self.quantity_product_entry.config(state="disabled")



    def asignar_ingredientes(self):
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        from src.gestorAplicacion.usuarios.quimico import Quimico
        productos = Quimico.productos_pendientes()

        if productos[2] == 0:

            messagebox.showinfo("Informacion","No hay productos pendientes a los cuales asignarles ingredientes")
        else:

            self.eliminar_elementos()


            self.ingredients = []

            # Selección de Producto
            self.product_label = tk.Label(self.root, text="Seleccionar Producto:")
            self.product_label.pack(pady=5)

            self.productos_pendientes = []


            for i in AgenteComercial.Pedidos:
                print(i.cliente)
                print(i.nombre)
                print(i.estado)
                print(i.ingredientes)
                print(i.cantidad)


            
            self.product_combobox = ttk.Combobox(self.root, values=productos[0])
            self.product_combobox.pack(pady=5)
            
            self.select_button = tk.Button(self.root, text="Seleccionar", command=lambda : self.select_product(productos))
            self.select_button.pack(pady=5)

            # Botón para volver
            botonVolver = tk.Button(self.root, text="Volver al login", command= lambda: self.reingresar(self.root) )
            botonVolver.pack(pady=5)
            
            
    def select_product(self,productos):
        selected_product = self.product_combobox.get()

        if selected_product:
            indice = self.product_combobox.current()
            objeto_seleccionado = productos[1][indice]

            self.asignar_ingredientes2(objeto_seleccionado)

            # Frame para contener los elementos que deben aparecer después de seleccionar el producto
            self.content_frame = tk.Frame(self.root, bd=2,bg="lightblue")

            # Entrada de Ingredientes
            self.ingredient_label = tk.Label(self.content_frame, text="Ingrediente:",bd=2,bg="lightblue")
            self.ingredient_entry = tk.Entry(self.content_frame)
            
            self.quantity_label = tk.Label(self.content_frame, text="Cantidad:",bd=2,bg="lightblue")
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
            
            self.send_button = tk.Button(self.content_frame, text="Asignar Ingredientes", command=lambda:self.send_data(objeto_seleccionado))
                                                                #"Asignar Ingredientes y Enviar al Asesor Comercial"

            self.cancel_button = tk.Button(self.content_frame, text="Cancelar", command=self.clear_all)
        



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
            self.cancel_button.pack(pady=10)

    def add_ingredient(self):
        ingredient = self.ingredient_entry.get()
        quantity = self.quantity_entry.get()
        
        if ingredient and quantity:
            frame = tk.Frame(self.scrollable_frame,bd=2,relief="ridge")
            frame.pack(fill=tk.X, pady=2, expand=True)
            
            label = tk.Label(frame, text=f"{ingredient} - {quantity}", anchor="w", font=("Arial", 13))
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            delete_button = tk.Button(frame, text="❌", command=lambda: self.remove_ingredient(frame))
            delete_button.pack(side=tk.RIGHT)
            
            self.ingredients.append((ingredient, quantity, frame))
            
            self.ingredient_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)

        else:

            messagebox.showerror("Error","Por favor ingrese el nombre y cantidad del ingrediente")

    def remove_ingredient(self, frame):
        for item in self.ingredients:
            if item[2] == frame:
                self.ingredients.remove(item)
                frame.destroy()
                break

    def send_data(self,producto):
        from src.gestorAplicacion.usuarios.agenteComercial import AgenteComercial
        
        from src.gestorAplicacion.usuarios.quimico import Quimico


        data = [(producto, item[0], item[1]) for item in self.ingredients]
        print("Datos enviados:", data)

        
        for k in data:
            Quimico.asociar_ingredientes(k[1],k[2],producto)

        Cambio("Ingredientes", "Quimico", producto.nombre, date.today() )
        messagebox.showinfo("Informacion","Se han asociado los ingredientes correctamente")

        for item in self.ingredients:
            item[2].destroy()
        self.ingredients.clear()
        self.ingredient_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.content_frame.pack_forget()

        self.root.destroy()

        new_root = tk.Toplevel()

        h = InterfazQuimico(new_root)




        

    def clear_all(self):
        for item in self.ingredients:
            item[2].destroy()
        self.ingredients.clear()
        self.ingredient_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.content_frame.pack_forget()

        messagebox.showinfo("Informacion","Se ha cancelado el diligenciamiento de ingredientes")    

        self.eliminar_elementos()

        self.crear_interfaz_quimico()

    def reingresar (self, ventana):
        from src.gestorAplicacion.administrativo.login import LoginApp,Login
        LoginApp(Login.root1)   
        ventana.destroy()    
