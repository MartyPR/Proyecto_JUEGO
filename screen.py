




import tkinter as tk
from tkinter import ttk
from Constantes import estilo , config
from Constantes import config 

from PIL import Image, ImageTk, ImageSequence
from datetime import datetime 

from BD import *

class home(tk.Frame):
    
    
    def  __init__ (self,parent, controller):
        super().__init__(parent)
        self.configure(background=estilo.BACKGROUND)
        self.controler = controller
        self.initwidgets()
        global inicio_contador
        inicio_contador = True


    def move_to_game(self):
        self.controler.show_frame(Game)
        global inicio_contador
        inicio_contador = True
        print(self.controler.mode)

    def move_to_Score(self):
        self.controler.show_frame(score)
        print(self.controler.mode)
        

    def initwidgets(self):
        tk.Label(
            self,
            text="Quien quiere ser millonario : GAME",
            justify = tk.CENTER,
            **estilo.STYLE
            ).pack( # pack coloca el widgets
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
        )
        #subfrma
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=estilo.BACKGROUND)
        optionFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True ,
            
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionFrame,
            text="vamos a comenzar?",
            justify= tk.CENTER,
            **estilo.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11

        )
        tk.Button(optionFrame,text="Score"+"", command=self.move_to_Score,justify= tk.CENTER,activebackground= estilo.BACKGROUND,activeforeground= estilo.TEXT,relief=tk.FLAT,bg='#E2ba15',font=("Arial",16),fg="#000000").pack(side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11)
        tk.Button(
            self,
            text="Si"+(""),
            #variable=self.gameMode,
            #value = value,
            command=(self.move_to_game ),
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT,
            relief=tk.FLAT,
            bg=("#96be25" ),
            font=("Arial",16),
            fg="#000000"
        ).pack(
            side =tk.LEFT,
            fill = tk.BOTH,
            expand=True,
            padx=5,
            pady=5

            )
        tk.Button(
            self,
            text="No"+(""),
            #variable=self.gameMode,
            #value = value,
            command=(self.quit),
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT,
            relief=tk.FLAT,
            bg=( "#be4d25" ),
            font=("Arial",16),
            
            fg="#000000"
        ).pack(
            side =tk.LEFT,
            fill = tk.BOTH,
            expand=True,
            padx=5,
            pady=5

            )

class Game(tk.Frame):
    
    def  __init__ (self,parent, controller):
        super().__init__(parent)
        self.configure(background=estilo.BACKGROUND)
        self.controler = controller 
        self.currentQuestion = tk.StringVar(self,value=config.pre[1])
        self.opcion1 = tk.StringVar(self,value=config.res[1])
        self.opcion2 = tk.StringVar(self,value=config.res[2])
        self.opcion3 = tk.StringVar(self,value=config.res[3])
        self.opcion4 = tk.StringVar(self,value=config.res[4])

        self.time=tk.StringVar(self)
        self.click=tk.StringVar()
        self.click.set("None")

        self.counter=0 # contador del tiempo
        
        self.count=3 #permite la seleccion de la pregunta
        self.n=5 #define la posicion inicia de las respuestas
        self.finish=1
        self.running=True # marca el comienzo del juego
        self.score=tk.StringVar() #cambio del score en los frames
        self.Score=0 #valor entero del score
        self.initwidgets()
        
        self.counter_label()
        

    def update_question(self,value):
        #aumenta el nivel de la pregunta
        print("question update")
        print(config.res[self.n])
        print(value)
        
        #verifica si la respuesta es correcta , ademas disminuye el score cada vez mas tiempo
        if value== config.res[self.n] :
            print("true")
            self.Score =(self.Score+100)-(self.counter*1.5)
            self.score.set("Score: "+str(self.Score))

            if self.finish>=5:
                global tiempo
                global puntaje
                tiempo=self.time.get()
                puntaje=self.Score
                self.move_to_win()
                self.count=3
                self.n=5
                self.finish=1
                self.running=False
                
            if self.finish<5 :
                self.currentQuestion.set(config.pre[self.count])
                self.opcion1.set(config.res[self.n+2])
                self.opcion2.set(config.res[self.n+3])
                self.opcion3.set(config.res[self.n+4])
                self.opcion4.set(config.res[self.n+5])
                self.count=self.count+2
                self.n=self.n+6 
                self.finish=self.finish+1

        else: 
            print("false")
            Command=self.quit()

    def move_to_win(self):
        #moverse a la clase Win
        self.controler.show_frame(win)
        print(self.controler.mode)        
    
    def counter_label(self):  
        #tiempo de transcuso del juego
        def count():          
            if self.running:
                tt = datetime.fromtimestamp(self.counter) 
                
                string = tt.strftime("%M:%S") 
                display=string  

                self.after(1000, count)   
                self.counter += 1
                print(display)
                self.time.set("time: "+display)
    
        count()    
        
        

    def initwidgets(self):
        tk.Label(
            self,
            text="Responde la pregunta :",
            justify = tk.CENTER,
            **estilo.STYLE
            ).pack( # pack coloca el widgets
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
        )
        FrameTime = tk.Frame(self)
        FrameTime.configure(background=estilo.BACKGROUND)
        FrameTime.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True ,
            
            padx = 11,
            pady = 10
        )
        tk.Label(FrameTime, text="time:",textvar=self.time,**estilo.STYLE
        ).pack(side =tk.LEFT,fill = tk.BOTH,expand=True,padx=11,pady=11)
        tk.Label(FrameTime,text="score:",textvar=self.score,justify = tk.CENTER,**estilo.STYLE                  
        ).pack( side = tk.RIGHT,fill = tk.BOTH,expand = True,padx = 11,pady = 11  )   

        #subfrma
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=estilo.BACKGROUND)
        optionFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True ,
            
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionFrame,
            text=config.pre[1],
            textvar=self.currentQuestion,
            justify= tk.CENTER,
            **estilo.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11

        )
        opcion1=tk.Radiobutton(self,text=config.res[1],textvar=self.opcion1,variable=self.click,value = '[a]',activebackground= estilo.BACKGROUND,activeforeground= estilo.TEXT,bg=( "#5D8103" ),font=("Arial",16), fg="#000000"
        ).pack(
                side =tk.LEFT,
                fill = tk.BOTH,
                expand=True,
                padx=5,
                pady=5           
        )
        opcion2=tk.Radiobutton(self,text=config.res[2],textvar=self.opcion2,variable=self.click,value = '[b]',activebackground= estilo.BACKGROUND,activeforeground= estilo.TEXT,bg=( "#5D8103" ),font=("Arial",16), fg="#000000"
        ).pack(
                side =tk.LEFT,
                fill = tk.BOTH,
                expand=True,
                padx=5,
                pady=5           
        )
        opcion3=tk.Radiobutton(self,text=config.res[3],textvar=self.opcion3,variable=self.click,value = '[c]',activebackground= estilo.BACKGROUND,activeforeground= estilo.TEXT,bg=( "#5D8103" ),font=("Arial",16), fg="#000000"
        ).pack(
                side =tk.LEFT,
                fill = tk.BOTH,
                expand=True,
                padx=5,
                pady=5           
        )
        opcion4=tk.Radiobutton(self,text=config.res[4],textvar=self.opcion4,variable=self.click,value = '[d]',activebackground= estilo.BACKGROUND,activeforeground= estilo.TEXT,bg=( "#5D8103" ),font=("Arial",16), fg="#000000"
        ).pack(
                side =tk.LEFT,
                fill = tk.BOTH,
                expand=True,
                padx=5,
                pady=5           
        )     
               
            
        buton_s=tk.Button(
           self,
            text= "siguiente →",
            command=lambda: self.update_question(self.click.get()),
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side =tk.TOP,
            fill = tk.BOTH,
            expand=True,
            padx=10,
            pady=5

        )
        tk.Button(
           self,
            text= "← Home",
            command=lambda:self.controler.show_frame(home),
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side =tk.TOP,
            fill = tk.BOTH,
            expand=True,
            padx=10,
            pady=5

        )


class win(tk.Frame):
    def  __init__ (self,parent, controller):
        super().__init__(parent)
        self.configure(background=estilo.BACKGROUND)
        self.controler = controller
        self.name=tk.StringVar()
        self.initwidgets()
        
    def Guardar(self):
        #fuarda los datos en la base de datos 'jugadores'
        global puntaje
        global tiempo
        global nombre
        nombre = self.name.get()
        print(nombre)
        print(tiempo)
        
        insertRow(nombre,tiempo,puntaje)
        self.quit()



    def initwidgets(self):
 
        #subfrma
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=estilo.BACKGROUND)
        optionFrame.configure(width="400", height="200")
        optionFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True ,
            
            padx = 22,
            pady = 11
        )
        
    
        tk.Label(
            optionFrame,
            text="Felicidades",
            justify= tk.CENTER,
            **estilo.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11

        )

        self.play_gif()

        tk.Entry(self,
            justify=tk.RIGHT, textvar=self.name
        ).pack(side =tk.TOP,padx=22,pady=11


        )
        buton_s=tk.Button(
           self,
            text= "salir →",
            command=lambda: self.quit(),
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side=tk.RIGHT,
            fill= tk.BOTH,
            expand=True,
            padx=22,
            pady=11

        )
        tk.Button(
           self,
            text= "GUARDAR",
            command=self.Guardar,
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side =tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11

        )

    def play_gif(optionframe):
        # colocar gif en la pantalla cuando se gana pero retrasa la aparicion del home, la funcion esta en 382
        
        img = Image.open(".\Ficheros\Aplauso.gif")
        lbl = tk.Label(optionframe, justify= tk.CENTER)
        
        lbl.place(x=520,y=80)
        for img in ImageSequence.Iterator(img):
            img=img.resize((150,150))
            img=ImageTk.PhotoImage(img)
            lbl.config(image=img)
            optionframe.update()
            
        optionframe.after(0,optionframe.play_gif) 


class score(tk.Frame):
    def  __init__ (self,parent, controller):
        super().__init__(parent)
        self.configure(background=estilo.BACKGROUND)
        self.controler = controller

        self.lst=readOrdered("Score")
        self.total_rows=(len(self.lst))
        self.total_columns=('first_name', 'last_name', 'email')
        
        self.initwidgets()
        

        print("columnas: "+ str(self.total_rows))
    def initwidgets(self):
        tk.Label(
            self,
            text="Quien quiere ser millonario : GAME",
            justify = tk.CENTER,
            **estilo.STYLE
            ).pack( # pack coloca el widgets
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
        )


        tk.Button(
           self,
            text= "← Home",
            command=lambda:self.controler.show_frame(home),
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side =tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11

        )        
        tk.Button(
           self,
            text= " ver Tabla",
            command=self.table,
            **estilo.STYLE,
            relief=tk.FLAT, 
            activebackground= estilo.BACKGROUND,
            activeforeground= estilo.TEXT

        ).pack(
            side =tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11

        )
    
    def table(self):                  
        root = tk.Tk()
        root.title('Treeview demo')
        root.geometry('620x200')
        # define columns
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(root, columns=columns, show='headings')
        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')
        # add data to the treeview
        for contact in self.lst:
            tree.insert('', tk.END, values=contact)


        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # run the app
        root.mainloop()

        
