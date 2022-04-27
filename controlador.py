#contiene el control de varias ventanas , es escalable para añadir varias ventanas
from textwrap import fill
import tkinter as tk 
from tkinter import * 
from typing import Container
from Constantes import estilo
from screen import *
from Constantes import estilo , config


class manager(tk.Tk):

    def __init__(Self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        Self.title ("¿Quien quiere ser millonario? : Game")
        Container =tk.Frame(Self) #contiene el resto de frames
        Self.mode="Si" 
        Container.pack(

            side = tk.TOP,
            fill = tk.BOTH,
            expand = True 
        )
        Container.configure(background = estilo.BACKGROUND)
        Container.grid_columnconfigure(0, weight = 1)#indice de la fila y la columna , weith el peso
        Container.grid_rowconfigure(0, weight = 1)
        
        
        Self.frames =  { }
        for F in (home,Game,win,score):
            frame = F(Container, Self)
            Self.frames[F]=frame
            frame.grid(row=0, column=0,sticky= tk.NSEW)

        Self.show_frame(home)
        


    def show_frame(self,container):
        frame= self.frames[container]
        frame.tkraise()



