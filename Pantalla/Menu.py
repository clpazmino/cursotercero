from tkinter import *
from EstructuraProyecto.Pantalla.cursos import *
from EstructuraProyecto.Pantalla.consultaimpresioncurso import *
import tkinter as tk


class menu_vista():
        def __init__(self):
                self.ventana1 = Tk()
                self.ventana1.config(bg="green")
                menubar = Menu(self.ventana1)
                self.ventana1.config(menu=menubar)
                self.ventana1.geometry("2000x2000")
                contenedor = Frame(self.ventana1, width="600", height="600", bg="#2E8B57")
                contenedor.pack()


                filemenu = Menu(menubar, tearoff=0)
                menubar.add_cascade(label="Ingresos", menu=filemenu)
                filemenu.add_command(label="Cursos",command=self.menudatocursos)
                filemenu.add_separator()


                filemenu.add_command(label="Salir", command=quit)

                editmenu = Menu(menubar, tearoff=0)
                menubar.add_cascade(label="Consultas y Reportes", menu=editmenu)
                editmenu.add_command(label="Cursos",command=self.consultaImpresion)

                self.ventana1.mainloop()

        def menudatospersonales(self):

                top_level = Tk.Toplevel(self.ventana1)
                #app = datospersonales(top_level)
        def menudatocursos(self):
                top_level = tk.Toplevel(self.ventana1)
                app = cursos(top_level)

        def consultaImpresion(self):
                top_level = tk.Toplevel(self.ventana1)
                app = cursosimpresionesCursos(top_level)




