#bibliotecas
from src.vistas.login_vista import Login
import cv2
import imutils
from PIL import Image, ImageTk
from tkinter import Label

if __name__ == '__main__':
    print('iniciando...')
    import tkinter as tk

    def visualizar():
        global captura, lblVideo
        if captura is not None:
            ret, frame = captura.read()
            #si hay una correcta captura de video
            if ret == True:
                #redimensionamiento video
                frame = imutils.resize(frame, width=640)
                # se convierte el video
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)

                #mostrar video en el frame -> labelvideo
                lblVideo.configure(image=img)
                lblVideo.image = img
                lblVideo.after(10, visualizar)

            else:
                captura.release()
                cv2.destroyAllWindows()
                print('fin captura video')




    pantalla_cv = tk.Tk()
    #propiedades ventana
    pantalla_cv.title("prueba con opencv")
    #tamaño de la ventana ancho y alto
    pantalla_cv.geometry("1280x720")

    #creamos label
    lblVideo = Label(pantalla_cv)
    lblVideo.place(x=320, y=50)

    #captura video cv2
    #Camara seleccionada la principal de mi pc
    
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    #evaluamos si hay captura
    visualizar()

    
    pantalla_cv.mainloop()

    

    print('Finalizo.')

    


  
    



    
        
        
