from controlador import manager
from BD import*
if __name__ == "__main__":
    app=manager()
    
    #createDB()
    #createTable()
    #insertRow("prueba","0:00",0)

ancho_ventana = 1200
alto_ventana = 350

x_ventana = app.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = app.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
app.geometry(posicion)

app.mainloop()
    
