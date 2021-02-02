from tkinter import *
from tkinter import messagebox
from tkinter import ttk, font

class cursos(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(cursos, self).__init__(parent, *args, **kwargs)
        self.ventana = parent
        self.ventana.title("Datos De Curso")
        self.ventana.geometry("1050x500")

        titulo = Label(self.ventana, text="Sistemas Datos Curso ", font=("Helvetica", 12),
                              anchor="center").pack()
        agenda_descripcion = Label(self.ventana,
                                   text="Proyecto Diseñado por Msig Carlos Pazmiño POO ",
                                   anchor="center").pack()
        lblcodigo = Label(self.ventana, text="Código:").place(x=30, y=20)
        lblcurso = Label(self.ventana, text="Nombre Del Curso:").place(x=30, y=60)
        lblestado = Label(self.ventana, text="Estado:").place(x=30, y=90)

        self.curso = StringVar()
        self.estado = StringVar()
        self.codigo=StringVar()

        self.txtcurso = Entry(self.ventana, textvariable=self.curso).place(x=200, y=60)
        self.txtcodigo = Entry(self.ventana, textvariable=self.codigo).place(x=200, y=20)
        self.combo = ttk.Combobox(self.ventana)
        self.combo.place(x=200, y=90)
        self.combo["values"] = ["Activo", "Eliminado"]
        self.combo.current(0)


        botAceptar = Button(self.ventana, text="Aceptar", command=self.grabar_persona).place(x=250, y=180)
        botsalir = Button(self.ventana, text="Cerrar", command=self.ventana.destroy).place(x=400, y=180)



       #self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        # Tabla
        self.tree = ttk.Treeview(self.ventana, columns=('CODIGO', 'CURSO','ESTADO'))
        self.tree.heading('#0', text='CODIGO')
        self.tree.heading('#1', text='CURSO')
        self.tree.heading('#2', text='ESTADO')

       #self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.tree.place(x=40,y=220)

        self.cargarTodosLosEmpleados()


    def nuevo(self):
        self.codigo.set("0")
        self.curso.set("")
        self.combo.current(0)

    def grabar_persona(self):
        if self.combo.get()=="Activo":
            estado="1"
        else:
            estado="0"

        self.tree.insert('', '0', text=self.codigo.get(), values=(str(self.curso.get()), estado))
        self.envioMensajesPantalla("Registro", "Se Grabo Con Exito")


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


    def cargarTodosLosEmpleados(self):
        self.tree.insert('', '0', text=str("Cabecera"),values=(str("FILA1"),"ESTADO"))











