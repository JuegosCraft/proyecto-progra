from tkinter import *
from xml.dom.minidom import Identified
import mysql.connector
from tkinter import messagebox
#-----------------------------ventana menu dimenciones-----------------------------------
e=Tk()
e.title("Registro")
e.geometry("700x300")
e.config(bg="#B4C7E7")
e.resizable(0,0)
#-------------------------------base-----------------------------------
conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="")
bd=conexion.cursor()
bd.execute("CREATE DATABASE IF NOT EXISTS proyecto")
bd.close()
conexion.close()
conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="proyecto")
bd=conexion.cursor()
bd.execute("CREATE TABLE IF NOT EXISTS login(usuario VARCHAR(25),contraseña VARCHAR(55))")
bd.execute("CREATE TABLE IF NOT EXISTS registro(identificacion VARCHAR(25),nombre_y_apellidos VARCHAR(55),puesto_de_trabajo VARCHAR(55),usuario VARCHAR(55),contraseña VARCHAR(55))")
bd.close()
#----------------------ventana registro-------------------------------------
def registro():
#-----------------fuciones---------------------------    
    def agregar_usuario():
            cur=conexion.cursor()
            ide=txt_identificacion.get()
            nom=txt_nombre.get()
            cur.execute("update registro set nombre_y_apellidos=%s, puesto_de_trabajo=%s, usuario=%s, contraseña=%s where identificacion=%s",modificar_usuario)
            conexion.commit()
            cur.close()
            messagebox.showinfo(message="los datos se modificaron",title="informacion")     
            limpiar()
        
    def modificar_usuario():
          cur = conexion.cursor()
          modificar_usuario = txt_identificacion.get(), txt_nombre.get(), txt_trabajo.get(), txt_usuario.get(), txt_contraseña.get()
          cur.execute("update registro set nombre_y_apellidos=%s, puesto_de_trabajo=%s, usuario=%s, contraseña=%s where identificacion=%s",modificar_usuario)
          conexion.commit()
          cur.close()
          messagebox.showinfo(message="los datos se modificaron",title="informacion")     
          limpiar()
    def eliminar_usuario():
             cur=conexion.cursor()
             cod=txt_usuario.get()
             cur.execute("delete from inventario where codigo ='{}'".format(cod))
             conexion.commit()
             cur.close()
             messagebox.showinfo(message="se elimino el libro exitosamente",title="informacion")
             txt_usuario.delete(0,END)
             txt_contraseña.delete(0,END)
    u= Tk()
    u.title("Registro")
    u.geometry("850x680")
    u.config(bg="#B4C7E7")
    u.resizable(0,0)
#-----------------------------etiqueta registro-------------------------------------------------------------
    etiqueta=Label(u,font=("arial",18,"bold"),text="identificacion:",bg="#B4C7E7").place(x=25,y=100)
    etiqueta=Label(u,font=("arial",18,"bold"),text="nombre y apellido:",bg="#B4C7E7").place(x=25,y=200)
    etiqueta=Label(u,font=("arial",18,"bold"),text="puesto de trabajo:",bg="#B4C7E7").place(x=25,y=300)
    etiqueta=Label(u,font=("arial",18,"bold"),text="usuario:",bg="#B4C7E7").place(x=25,y=400)
    etiqueta=Label(u,font=("arial",18,"bold"),text="contraseña:",bg="#B4C7E7").place(x=25,y=500)
#------------------------txt registro-----------------------------------------------------------------------------------------------
    txt_identificacion=Entry(u,font=("arial",18,"bold"),bg="#D0CECE").place(x=260,y=100)
    txt_nombre=Entry(u,font=("arial",18,"bold"),bg="#D0CECE").place(x=260,y=200)
    txt_trabajo=Entry(u,font=("arial",18,"bold"),bg="#D0CECE").place(x=260,y=300)
    txt_usuario=Entry(u,font=("arial",18,"bold"),bg="#D0CECE").place(x=260,y=400)
    txt_contraseña=Entry(u,font=("arial",18,"bold"),bg="#D0CECE").place(x=260,y=500)
#-------------------------------botones registro-------------------------------------------------
    boton_u1=Button(u,font=("arial",12,"bold"),text="consultar",width=20,height=2,bg="#0077AC",).place(x=600,y=100,)
    boton_u2=Button(u,font=("arial",12,"bold"),text="agregar usuario",width=20,height=2,bg="#0077AC",command=agregar_usuario).place(x=50,y=600)
    boton_u3=Button(u,font=("arial",12,"bold"),text="modificar usuario",width=20,height=2,bg="#0077AC",command=modificar_usuario).place(x=300,y=600)
    boton_u4=Button(u,font=("arial",12,"bold"),text="eliminar usuario",width=20,height=2,bg="#0077AC",command=eliminar_usuario).place(x=550,y=600)
#--------------------------------ventana login----------------------------------
def login():
#------------------------------------funciones de login-------------------------------------------------------
    def agregar_libro():
        cur=conexion.cursor()
        usu=txt_usuario.get()
        con=txt_contraseña.get()
        cur.execute("insert into inventario(usuario,contraseña)values('{}','{}')".format(usuario,contraseña))
        conexion.commit()#actualizar el envio de datos
        cur.close()
        messagebox.showinfo(message="login exitosos",title="informacion")
        txt_usuario.delete(0,END)
        txt_contraseña.delete(0,END)

    def cancelar_login():
        txt_usuario.delete(0,END)
        txt_contraseña.delete(0,END)
        messagebox.showinfo(message="se canselo el login",title="informacion")
#-------------------------------------------------------------------------     
    j = Tk()
    j.title('Registro')
    j.geometry('800x300')
    j.resizable(0,0)
    j.config(bg='#B4C7E7')
#-------------------etiquesta login-------------------------------------------------------------------------
    etiquetas_usuario = Label (j,font=('century',18,'bold'),text='Usuario',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000").place(x=10,y=45)
    etiquetas_contraseña = Label (j,font=('century',18,'bold'),text='Contraseña',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000").place(x=1,y=150)
#----------------------------txt login-------------------------------------------------------------------------------------------
    txt_usuario = Entry(j,font=('century',18,'bold'),width=20,bg="#D0CECE").place(x=240,y=50)
    txt_contraseña = Entry(j,font=('century',18,'bold'),width=20,bg="#D0CECE").place(x=250,y=150)
#----------------------------------------------------------------------
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="ingresar sistema",).place(x=530,y=45)
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="cancelar",).place(x=540,y=145)
#---------------------------ventana menu--------------------------------------------------
boton_re = Button(e,font=("arial",12,"bold"),text="Resgistro",command=registro,width=20,height=2,bg="#0077AC").place(x=70,y=130)
boton_log = Button(e,font=("arial",12,"bold"),text="Login",width=20,command=login,height=2,bg="#0077AC",).place(x=300,y=130)

#------------------------etiqueta menu-----------------------------
etiqueta = Label (e,font=('century',18,'bold'),text='Base de Datos',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000").place(x=120,y=30)

#--------------------------------------------------------------------
e=mainloop()