from tkinter import *

e=Tk()
e.title("Registro")
e.geometry("600x300")
e.config(bg="#B4C7E7")
e.resizable(0,0)
#------------------------------------------------

etiqueta = Label (e,font=('century',18,'bold'),text='Base de Datos',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000")
etiqueta.place(x=120,y=30)

#--------------------------------------------

boton_registro = Button(e,font=("arial",12,"bold"),text="Resgistro",width=20,height=2,bg="#0077AC",)
boton_registro.place(x=70,y=130)

boton_login = Button(e,font=("arial",12,"bold"),text="Login",width=20,height=2,bg="#0077AC",).place(x=300,y=130)

#-------------ventana_usuario---------------#
def registro_u():
    u=Tk()
    u.title("Registro")
    u.geometry("900x700")
    u.config(bg="#B4C7E7")
    u.resizable(0,0)

    #-------------Label_usuario-----------------------------------#

    etiqueta=Label(u,font=("arial",18,"bold"),text="identificacion:",bg="#B4C7E7").place(x=25,y=100)

    etiqueta=Label(u,font=("arial",18,"bold"),text="nombre y apellido:",bg="#B4C7E7").place(x=25,y=200)

    etiqueta=Label(u,font=("arial",18,"bold"),text="puesto de trabajo:",bg="#B4C7E7").place(x=25,y=300)

    etiqueta=Label(u,font=("arial",18,"bold"),text="usuario:",bg="#B4C7E7").place(x=25,y=400)

    etiqueta=Label(u,font=("arial",18,"bold"),text="contraseña:",bg="#B4C7E7").place(x=25,y=500)

    #-------------txt_usuario------------------------#

    txt_identificacion=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
    txt_identificacion.place(x=260,y=100)

    txt_nombre=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
    txt_nombre.place(x=260,y=200)

    txt_trabajo=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
    txt_trabajo.place(x=260,y=300)

    txt_usuario=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
    txt_usuario.place(x=260,y=400)

    txt_contraseña=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
    txt_contraseña.place(x=260,y=500)

    #-------------botones_usuario------------------------#

    boton_u1=Button(u,font=("arial",12,"bold"),text="consultar",width=20,height=2,bg="#0077AC",).place(x=600,y=100)

    boton_u2=Button(u,font=("arial",12,"bold"),text="agregar usuario",width=20,height=2,bg="#0077AC").place(x=50,y=600)

    boton_u3=Button(u,font=("arial",12,"bold"),text="modificar usuario",width=20,height=2,bg="#0077AC").place(x=300,y=600)

    boton_u4=Button(u,font=("arial",12,"bold"),text="eliminar usuario",width=20,height=2,bg="#0077AC").place(x=550,y=600)


def login_j():
        #----------------------------------------------------#
     j = Tk()
     j.title('Registro')
     j.geometry('750x300')
     j.resizable(0,0)
     j.config(bg='#B4C7E7')

     #-------------------------------------------------------------#
     j_usuario = Label (j,font=('century',18,'bold'),text='Usuario',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000")
     j_usuario.place(x=10,y=45)
    
     j_contraseña = Label (j,font=('century',18,'bold'),text='Contraseña',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000")
     j_contraseña.place(x=1,y=150)

     #------------------------------------------------------------------#
     txt_usuario = Entry(j,font=('century',18,'bold'),width=20)
     txt_usuario.place(x=240,y=50)

     txt_contraseña = Entry(j,font=('century',18,'bold'),width=20)
     txt_contraseña.place(x=250,y=150)

     #-----------------------------------------------------------------#
     boton_inventario = Button(j,text="Agregar Libro",width=20,height=2,)#command=agregar_libro)
     boton_inventario.place(x=530,y=45)

     boton_inventario = Button(j,text="Agregar Libro",width=20,height=2,)#command=agregar_libro)
     boton_inventario.place(x=540,y=145)

e.mainloop()