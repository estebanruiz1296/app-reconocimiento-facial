from src.classes_project import conexion
from src.classes_project.consultas import Consultas
from datetime import date
from datetime import datetime
import bcrypt
from src.classes_project.cifrar import CifrarPassword

#bibliotecas
import cv2
import numpy as np
import mediapipe as mp
import os
from PIL import Image, ImageTk
from tkinter import (
    Frame, Tk, Label, Entry, font, Button, END, messagebox 
)
from src.utils.constantes import RUTA_BASE_SETUP

if __name__ == '__main__':
    print('iniciando...')
    #para encriptar strings

    #funciones interfaz
    def Ingresar():
        correo, password = txt_correo_login.get(), txt_password_login.get()

        if (len(correo) == 0):
            messagebox.showwarning("Comprobación", "¡Debes ingresar tu correo!")
        elif(len(password) == 0):
            messagebox.showwarning("Comprobación", "¡Debes ingresar tu contraseña!")
        else:
            usuario = Consultas()

            sql = F"""
                SELECT email, password_hash FROM usuario WHERE 
                email='{correo}' LIMIT 1;
            """
            result_consulta = usuario.consultarDatosUsuario(sql)
            if not result_consulta:
                messagebox.showwarning('Validación credenciales', 'Usuario incorrecto')
            else: 
                if result_consulta['email'] == correo and CifrarPassword.validar_password(password, result_consulta['password_hash']):
                    print('ingresando...')
                else:
                    messagebox.showwarning('Validación credenciales', '¡Contraseña incorrecta!')

            

            txt_correo_login.delete(0, END)
            txt_password_login.delete(0, END)
            txt_correo_login.focus()

    def Registrarse():
        global pantallaRegistro
    

    # crear ventana
    pantallaLogin = Tk()
    pantallaLogin.title('Ingreso-reconocimiento-facial')
    pantallaLogin.geometry("1280x720")


    # fondo pantalla login
    imagenFondoLogin = ImageTk.PhotoImage(
        Image.open(f"{RUTA_BASE_SETUP}/fondo_login.png").resize(
            (pantallaLogin.winfo_screenwidth(), pantallaLogin.winfo_screenheight()), Image.ADAPTIVE)
    )
    labelFondoLogin = Label(image=imagenFondoLogin, text='inicio')
    labelFondoLogin.place(x=0, y=0, relheight=1, relwidth=1)

    #Ingresar texto
    tipografia = font.Font(family="Century Gothic", size=16) 

    txt_correo_login = Entry(pantallaLogin, font=tipografia)
    txt_correo_login.place(x=535, y=260, width=300, height=40)

    txt_password_login = Entry(pantallaLogin, show="*", width=20, font=tipografia)
    txt_password_login.place(x=535, y=380, width=300, height=40)

    ## botones
    #ingresar
    imagenBotonIngresar = ImageTk.PhotoImage(
        Image.open(f"{RUTA_BASE_SETUP}/boton_ingresar.png").resize(
            (260, 64), Image.ADAPTIVE)
    )
    btnIngresarLogin = Button(
        pantallaLogin, image=imagenBotonIngresar, 
        width=260, height=64, command=Ingresar, bd=0)
    btnIngresarLogin.place(x=380, y=619)

    #registrarse
    imagenBotonRegistrarse = ImageTk.PhotoImage(
        Image.open(f"{RUTA_BASE_SETUP}/boton_registrarse.png").resize(
            (260, 64), Image.ADAPTIVE)
    )
    btnRegitrarseLogin = Button(
        pantallaLogin, image=imagenBotonRegistrarse, 
        width=260, height=64, command=Registrarse,bd=0)
    btnRegitrarseLogin.place(x=670, y=619)



    pantallaLogin.mainloop()

    print('Finalizo.')

    


  
    



    
        
        
