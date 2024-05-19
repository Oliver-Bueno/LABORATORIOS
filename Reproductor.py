import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip
import pygame.mixer as mx
import tkinter.ttk as ttk
import pygame
from tkinter import filedialog

class Reproductor():
    def agregar_cancion(self):
        canciones = filedialog.askopenfilenames(filetypes=[("Archivos de audio", "*.mp3")])
        for cancion in canciones:
            self.canciones.append(cancion)
            self.lista_canciones.insert(END, cancion.split("/")[-1])  # Muestra solo el nombre del archivo

    def play(self, event):
        if not self.canciones:
            messagebox.showwarning("Advertencia", "No hay canciones en la lista.")
            return

        if self.indice_cancion_actual >= len(self.canciones):
            messagebox.showerror("Error", "Índice de canción fuera de rango.")
            return

        mx.music.load(self.canciones[self.indice_cancion_actual])
        mx.music.play(loops=0)
        self.lblestado.config(text="Reproduciendo... " + self.canciones[self.indice_cancion_actual])
        self.duracion_cancion_actual = pygame.mixer.Sound(self.canciones[self.indice_cancion_actual]).get_length()
        self.deslizar.config(to=self.duracion_cancion_actual)
        self.actualizar_barra_progreso()
        
        self.btnPause.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnPlay.config(state="disabled")
        self.bandera = True

    def pause(self, event):
        if(self.bandera == False):
            mx.music.pause()
            self.lblestado.config(text="Reproduccion Pausada...")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = True
        else:
            mx.music.unpause()
            self.lblestado.config(text="Reproducciendo...")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = False



    def stop(self, event):
        mx.music.stop()
        self.lblestado.config(text="Reproduccion Detenida...")
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")

        


   


    # def mideslizar(self, event):
    #     self.lbldeslizar.config(text=self.deslizar.get())
    # no funcina por el momento


    def __init__(self):
        print("Iniciando Reproductor...")

        def volumen(valor):

         pygame.mixer.music.set_volume(float(valor)/100)
        # Agrega una lista de canciones
        self.canciones = [
    "C:\\Users\\olive\\OneDrive\\Desktop\\Laboratorio1P\\sounds\\flowers.mp3",
    "C:\\Users\\olive\\OneDrive\\Desktop\\Laboratorio1P\\sounds\\boxeo.mp3",
    "C:\\Users\\olive\\OneDrive\\Desktop\\Laboratorio1P\\sounds\\roca.mp3",
    "C:\\Users\\olive\\OneDrive\\Desktop\\Laboratorio1P\\sounds\\tecno.mp3",
    "C:\\Users\\olive\\OneDrive\\Desktop\\Laboratorio1P\\sounds\\suspenso.mp3"]


        self.indice_cancion_actual = 0
        self.ventana = tk.Tk()
        self.ventana.title("Mi reproductor")
        self.ventana.config(width=850, height=480)
        self.ventana.resizable(0,0)

        self.canvas = tk.Canvas(self.ventana, width=850, height=480, background="white")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        
        self.img_fones = tk.PhotoImage(file=r"imagenes\azul.png")
        self.img_fonem = tk.PhotoImage(file=r"imagenes\negro.png")
        self.img_foneb = tk.PhotoImage(file=r"imagenes\azul.png")

        self.canvas.create_line(0, 422, 850, 422, width=3)  # linea baja
        self.canvas.create_line(0,30, 850, 30,width=3) # linea superior
        self.canvas.create_line(600, 30, 600, 420,width=3)  # fondo medio
        self.canvas.create_line(600, 60, 850, 60,width=3)


        mx.init()
        self.bandera = False

        iconoPlay = tk.PhotoImage(file=r"icons\control_play_blue.png")
        iconoPause = tk.PhotoImage(file=r"icons\control_pause_blue.png")
        iconoStop = tk.PhotoImage(file=r"icons\control_stop_blue.png")
        iconoAdelantar = tk.PhotoImage(file=r"icons\control_fastforward_blue.png")
        iconoDevolver = tk.PhotoImage(file=r"icons\control_rewind_blue.png")
        iconoAvanzar = tk.PhotoImage(file=r"icons\control_repeat_blue.png")
        iconoRetroceder = tk.PhotoImage(file=r"icons\control_repeat_blue.png")
        iconoAudifonos1 = tk.PhotoImage(file=r"imagenes\audifonos1.png")

       
        self.lblestado = tk.Label(self.ventana, text="Cargando...")
        self.lblestado.place(relx=0.5 ,rely=0.5, anchor="center")
        

        self.lblbajo = tk.Label(self.ventana, text="music...", image=self.img_foneb, border=0,background="white")
        self.lblbajo.place(x=-3, y=420)

        self.lblsuperior = tk.Label(self.ventana, text="3,2,1...", image=self.img_fones, border=0,background="white")
        self.lblsuperior.place(x=-20, y=-35)

        self.lblmedio = tk.Label(self.ventana, text="1,2,3...", image=self.img_fonem, border=0,background="white")
        self.lblmedio.place(x=0, y=29)

        self.lbltextoiz = tk.Label(self.ventana, text="Flowers", background="light blue")
        self.lbltextoiz.place(x=5, y=5)
        
        
        self.lblAudifonos= tk.Label(self.ventana, image=iconoAudifonos1, border=0, state="disabled")
        self.lblAudifonos.place(x=40, y=50)
        

        

        self.deslizar = ttk.Scale(self.ventana, from_=0, to=100, orient=HORIZONTAL, value=0)
        self.deslizar.place(x=10, y=425, width=830, height=6)

        self.sonido = ttk.Scale(self.ventana, from_=0, to=100, orient=HORIZONTAL,command=volumen)
        self.sonido.place(x=620, y=451, height=13)

        



        self.btnPlay = tk.Button(self.ventana, image=iconoPlay)
        self.btnPlay.place(relx=0.5, rely=1, y=-35, width=25, height=25)
        Tooltip(self.btnPlay,"Presione para iniciar la reproduccion...")

        self.btnPause = tk.Button(self.ventana, image=iconoPause, state="disabled")
        self.btnPause.place(relx=0.5, rely=1, y=-35, x=50 , width=25, height=25)
        Tooltip(self.btnPause,"Presione para Pausar la Reproduccion...")

        self.btnStop = tk.Button(self.ventana, image=iconoStop, state="disabled")
        self.btnStop.place(relx=0.5, rely=1, y=-35,x=-50, width=25, height=25)
        Tooltip(self.btnStop,"Presione para Detener la reproduccion...")

        self.btnPasarcancion = tk.Button(self.ventana, image=iconoAdelantar)
        self.btnPasarcancion.place(relx=0.5, rely=1, y=-35,x=100, width=25, height=25)
        Tooltip(self.btnPasarcancion,"Presione para Saltar a la siguiente cancion")

        self.btnDevolvercancion = tk.Button(self.ventana, image=iconoDevolver)
        self.btnDevolvercancion.place(relx=0.5, rely=1, y=-35,x=-100, width=25, height=25)
        Tooltip(self.btnDevolvercancion,"Presione para volver a la anterior cancion")

        self.btnAdelantar = tk.Button(self.ventana, image=iconoAvanzar)
        self.btnAdelantar.place(relx=0.5, rely=1, y=-35,x=150, width=25, height=25)
        Tooltip(self.btnAdelantar,"Presione para Adelantar 10 segundos la reproduccion...")

        self.btnRetroceder = tk.Button(self.ventana, image=iconoRetroceder)
        self.btnRetroceder.place(relx=0.5, rely=1, y=-35,x=-150, width=25, height=25)
        Tooltip(self.btnRetroceder,"Presione para Retroceder 10 segundos la reproduccion...")

        

        self.btnCuadroA= tk.Button(self.ventana, text="A")
        self.btnCuadroA.place(x=823, y=8, width=22, height=22)

        self.btnCuadroB= tk.Button(self.ventana, text="B")
        self.btnCuadroB.place(x=823, y=450, width=22, height=22)

        


           
        

        self.ventana.mainloop()


