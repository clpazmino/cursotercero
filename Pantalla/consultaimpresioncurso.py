from tkinter import *
from tkinter import messagebox

from tkinter import ttk, font

class cursosimpresionesCursos(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(cursosimpresionesCursos, self).__init__(parent, *args, **kwargs)
        self.ventana = parent
        self.ventana.title("Consulta de Cursos")
        self.ventana.geometry("1050x500")

        titulo = Label(self.ventana, text="Sistema Con Base Datos Curso 2F", font=("Helvetica", 12),
                              anchor="center").pack()
        agenda_descripcion = Label(self.ventana,
                                   text="Proyecto Manejo de Base Datos diseñada por Msig Carlos Pazmiño para el curso de Desarrollo Programación",
                                   anchor="center").pack()
        lblcurso = Label(self.ventana, text="Nombre Del Curso:").place(x=30, y=60)


        self.curso = StringVar()
        self.txtcurso = Entry(self.ventana, textvariable=self.curso).place(x=200, y=60)

        botbucar = Button(self.ventana, text="Buscar").place(x=350, y=60)
        botsalir = Button(self.ventana, text="Cerrar", command=self.ventana.destroy).place(x=500, y=180)




        # Tabla
        self.tree = ttk.Treeview(self.ventana, columns=('CODIGO', 'CURSO','ESTADO'))
        self.tree.heading('#0', text='CODIGO')
        self.tree.heading('#1', text='CURSO')
        self.tree.heading('#2', text='ESTADO')

       #self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.tree.place(x=40,y=220)

        self.cargarTodosLoscursos()
        # Increment counter



    def salir(self):
        self.ventana.destroy()
    def cargarTodosLoscursos(self):
        self.tree.insert('', '0', text=str("Cabecera"), values=(str("FILA1"), "ESTADO"))



    def envioMensajesPantalla(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
    def centra_ventana(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))





