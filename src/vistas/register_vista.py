import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
from customtkinter import *
from src.classes_project.consultas import Consultas
from src.classes_project.cifrar import CifrarPassword
import datetime

class Registrarse(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.apariencia = set_appearance_mode('dark')
        self.temas = set_default_color_theme('blue')
        # Definir el protocolo para el cierre de la ventana
        self.protocol("WM_DELETE_WINDOW", self.on_cerrar_ventana)

        self.load_window_registrarse()
        self.registrase_interfaz()

    def load_window_registrarse(self):
        self.title("Registrarse")
        return self.geometry("800x500")
    
    def registrase_interfaz(self):

        #frame para ubicar los widgets, entry y buttons
        self.frameRegistrarse = CTkFrame(self, width=700, height=400, corner_radius=25)
        self.frameRegistrarse.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #titulo frame registrarse
        self.lblTituloRegistrarse = CTkLabel(
            self.frameRegistrarse,text="Registrate para acceder al sistema",
            font=('Century Ghotic', 25)
        )
        self.lblTituloRegistrarse.place(relx=0.5, y=45, anchor=tk.CENTER)

        #Entradas de texto para el registro
        self.lblIdentificacion = CTkLabel(
            self.frameRegistrarse,text="Identificación",
            font=('Century Ghotic', 16)
        )
        self.lblIdentificacion.place(x=50, y=110)

        #entry identificación
        self.txtIdentificacion = CTkEntry(self.frameRegistrarse, width=295, 
            placeholder_text="Ingrese identificación", font=("Century Ghotic", 14)
        )
        self.txtIdentificacion.place(x=50, y=140)

        #lbl nombre
        self.lblNombre = CTkLabel(
            self.frameRegistrarse,text="Nombre usuario",
            font=('Century Ghotic', 16)
        )
        self.lblNombre.place(x=365, y=110)

        #entry nombre usuario
        self.txtNombre = CTkEntry(self.frameRegistrarse, width=295, 
            placeholder_text="Ingrese nombre de usuario", font=("Century Ghotic", 14)
        )
        self.txtNombre.place(x=365, y=140)

        #lblcorreo
        self.lblIdentificacion = CTkLabel(
            self.frameRegistrarse,text="Correo",
            font=('Century Ghotic', 16)
        )
        self.lblIdentificacion.place(x=50, y=175)

        #entry email
        self.txtEmail = CTkEntry(self.frameRegistrarse, width=295, 
            placeholder_text="Ingrese correo electrónico", font=("Century Ghotic", 14)
        )
        self.txtEmail.place(x=50, y=205)

        #lblpassword
        self.lblIdentificacion = CTkLabel(
            self.frameRegistrarse,text="Contraseña",
            font=('Century Ghotic', 16)
        )
        self.lblIdentificacion.place(x=365, y=175)

        #entry password
        self.txtPassword = CTkEntry(self.frameRegistrarse, width=295, 
            placeholder_text="Ingrese contraseña", font=("Century Ghotic", 14)
        )
        self.txtPassword.place(x=365, y=205)

        #button para registrar
        self.btnRegistrarUsuario = CTkButton(
            self.frameRegistrarse, text="Registrarse", corner_radius=8, width=200,
            font=("Century Ghotic", 14, 'bold'), command=self.registrarUsuario,
        )
        self.btnRegistrarUsuario.place(relx=0.5, y=280, anchor=tk.CENTER)


    def registrarUsuario(self):
        #obtenemos el valor de los campos de texto y los alacenamos en varibles
        identificacion, nom = self.txtIdentificacion.get(), self.txtNombre.get()
        email, pword = self.txtEmail.get(), self.txtPassword.get()

        if len(identificacion)==0 or len(nom)==0 or len(email)==0 or len(pword)==0:
            messagebox.showwarning("Verificación campos de texto", "Debes llenar todos los campos de texto")
        else:
            consulta = Consultas()
            sql = f"SELECT COUNT(*) as contar_usuario FROM usuario WHERE identificacion='{identificacion}' OR email='{email}';"
            result_consulta = consulta.consultarDatosUsuario(sql)
            #validamos que el usuario no haya sido registrado aún
            if result_consulta['contar_usuario'] == 0:
                print('creando usuario...')
                consulta.insertar('usuario', 
                {
                'identificacion' : identificacion,
                'nombre_usuario'  : nom,
                'email' : email,
                'password' : pword,
                'password_hash' : CifrarPassword.cifrar_password(pword).decode(encoding='utf-8'),
                'ruta_imagen' : f"src/images/faces/{identificacion}.png",
                'fecha_registro' : datetime.datetime.now()
                })
                messagebox.showinfo('Exito', '!Usuario registrado satisfactoriamente!') 
                self.txtIdentificacion.delete(0, END)  
                self.txtNombre.delete(0, END)
                self.txtEmail.delete(0, END)
                self.txtPassword.delete(0, END)
                self.txtIdentificacion.focus()

            else:
                messagebox.showerror('Validación usuario', '¡Usuario existente, cambie el correo o la identificación!')
    
    def on_cerrar_ventana(self):
        # Acciones que deseas realizar antes de cerrar la ventana
        print("La ventana registrarse se está cerrando")
        self.destroy()
        

                         


        
