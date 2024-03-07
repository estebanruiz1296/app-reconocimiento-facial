import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import *
from PIL import Image
from src.utils.constantes import RUTA_BASE_SETUP
from src.classes_project.consultas import Consultas
from src.classes_project.cifrar import CifrarPassword

class Login(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        #atributos de clase
        self.apariencia = set_appearance_mode("dark") # parametros: system, dark, light
        self.temas = set_default_color_theme("dark-blue") # temas: blue, dark-blue or green
        self.x, self.y = 600, 440
        self.configuracion_ventana_login()
        self.panel_login()

    def configuracion_ventana_login(self):
        self.title("Login")
        # self.iconbitmap(f"{DIRECTORIO_BASE_IMAGES}/icono.ico")

        ancho_window = self.winfo_screenwidth()
        alto_window = self.winfo_screenheight()
        print('ancho window', ancho_window)

        # Calculos para centrar la interfaz en pantalla
        x_local = int((ancho_window / 2) - (self.x / 2))
        y_local = int((alto_window /  2) - (self.y / 2))

        return self.geometry(f"{self.x}x{self.y}+{x_local}+{y_local}")



    def panel_login(self):
        # creamos login
        # imagen de fondo
        self.image_fondo_login = CTkImage(Image.open(f"{RUTA_BASE_SETUP}/fondo_login.png"), size=(self.x, self.y))
        self.lblFondoLogin = CTkLabel(self, image=self.image_fondo_login)
        self.lblFondoLogin.pack()

        #frame central 
        self.frameLogin = CTkFrame(self, width=320, height=360, corner_radius=25)
        self.frameLogin.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #etiqueta para el frame titulo login
        self.lblTituloFrame = CTkLabel(self.frameLogin, text='Accede a tu cuenta', font=('Century Ghotic', 25))
        self.lblTituloFrame.place(x=50, y=45)

        #text input para el correo
        self.txtEmail = CTkEntry(
            self.frameLogin, width=220, placeholder_text="Ingrese su correo electrónico",
            font=("Century Ghotic", 14)
        )
        self.txtEmail.place(x=50, y=110)

        #text input para contraseña
        self.txtPassword = CTkEntry(
            self.frameLogin, width=220, placeholder_text="Ingrese su contraseña",
            font=("Century Ghotic", 14), show="*"
        )
        
        self.txtPassword.place(x=50, y=165)
    
        #etiqueta para olvidar contraseña
        self.lblForgotPassword = CTkLabel(self.frameLogin, text='Olvido su contraseña', font=('Century Ghotic', 12))
        self.lblForgotPassword.place(x=155, y=195)

        #boton ingresar
        self.btnIngresar = CTkButton(
            self.frameLogin, width=220, text='Ingresar', corner_radius=8, font=("Century Ghotic", 12, 'bold'),
            command=self.Ingresar
        )
        self.btnIngresar.place(x=50, y=240)

        #botones registrarse e Ingreso biométrico 
        
        self.btnRegistrarse = CTkButton(
            self.frameLogin, width=90, height=30,text='Registrarse', corner_radius=8,
            compound='left', font=("Century Ghotic", 12, 'bold'), fg_color="#3c912d", hover_color='#94e386',
            text_color='#1f211f'
        )
        self.btnRegistrarse.place(x=50, y=290)

        self.btnIngresoBiometrico = CTkButton(
            self.frameLogin, width=90, height=30,text='Ingreso biométrico', corner_radius=8,
            font=("Century Ghotic", 12, 'bold'), fg_color="#3c912d", hover_color='#94e386',
            text_color='#1f211f'
        )
        self.btnIngresoBiometrico.place(x=150, y=290)

    def Ingresar(self):
        # instanciamos la clase consulta
        consulta = Consultas()
        #obtenemos los valores de los campos de texto
        email, password = self.txtEmail.get(), self.txtPassword.get()
        #validamos que ambos campos de textos del login esten llenos
        if len(email) == 0:
            messagebox.showwarning('Verificación campos de texto', '¡El correo es obligatorio!')
        elif len(password) == 0:
            messagebox.showwarning('Verificación campos de texto', '¡La contraseña es obligatoria!')
        else:
            #creamos consulta para verificar si el usuario con correo ingresado existe y comprobamos credenciales
            sql = f"SELECT email, password_hash FROM usuario WHERE email='{email}';"
            resultado_consulta = consulta.consultarDatosUsuario(sql)
            

            # comprobamos si la consulta nos trajo resul
            if not resultado_consulta:
                messagebox.showwarning('Validación credenciales', '¡Usuario incorrecto!')
            else:
                if resultado_consulta['email'] == email and CifrarPassword.validar_password(password, resultado_consulta['password_hash']):
                    print('ingresando...')
                else:
                    messagebox.showwarning('Validación credenciales', "¡Usuario o contraseña incorrectos!")
        
            

        