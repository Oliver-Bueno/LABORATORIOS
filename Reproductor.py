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
        if self.bandera:
            mx.music.pause()
            self.lblestado.config(text="Pausado...")
            self.btnPause.config(state="disabled")
            self.btnPlay.config(state="normal")
            self.bandera = False
    
    def stop(self, event):
        mx.music.stop()
        self.lblestado.config(text="Reproduccion Detenida...")
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")
        self.deslizar.set(0)
    
    def Adelantar(self, event):
        if mx.music.get_busy():
            nueva_posicion = self.obtener_posicion_actual() + 10
            self.reproducir_desde_posicion(nueva_posicion)
        else:
            print("No hay música reproduciéndose en este momento.")
    
    def Retroceder(self, event):
        if mx.music.get_busy():
            nueva_posicion = self.obtener_posicion_actual() - 10
            self.reproducir_desde_posicion(nueva_posicion)
        else:
            print("No hay música reproduciéndose en este momento.")
    
    def obtener_posicion_actual(self):
        if mx.music.get_busy():
            return mx.music.get_pos() / 1000
        else:
            return self.deslizar.get()
    
    def reproducir_desde_posicion(self, nueva_posicion):
        if nueva_posicion < 0:
            nueva_posicion = 0
        elif nueva_posicion > self.duracion_cancion_actual:
            nueva_posicion = self.duracion_cancion_actual

        mx.music.stop()
        mx.music.play(start=nueva_posicion)
        self.deslizar.set(nueva_posicion)
    
    def Pasarcancion(self, event):
        mx.music.stop()
        self.indice_cancion_actual += 1
        if self.indice_cancion_actual >= len(self.canciones):
            self.indice_cancion_actual = 0
        self.play(event)
    
    def DevolverCancion(self, event):
        mx.music.stop()
        self.indice_cancion_actual -= 1
        if self.indice_cancion_actual < 0:
            self.indice_cancion_actual = len(self.canciones) - 1
        self.play(event)
    
    def actualizar_barra_progreso(self):
        if mx.music.get_busy():
            self.deslizar.set(self.obtener_posicion_actual())
            self.ventana.after(1000, self.actualizar_barra_progreso)

if __name__ == "__main__":
    Reproductor()

        
        


           
        



