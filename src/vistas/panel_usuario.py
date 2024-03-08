import customtkinter as ctk
from customtkinter import *
import tkinter as tk

class Sistema(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.mode = set_appearance_mode('dark')
        self.tema = set_default_color_theme('dark-blue')
        self.load_sistema()
        self.sistema_interfaz()

    def load_sistema(self):
        self.title("Sistema")
        return self.geometry("900x700")
    
    def sistema_interfaz(self):
        #frame central 
        self.frameSistema = CTkFrame(self, width=700, height=700, corner_radius=25)
        self.frameSistema.place(relx=0.5, rely=0.5, anchor=tk.CENTER)