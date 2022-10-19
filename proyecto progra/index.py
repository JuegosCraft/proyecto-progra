from tkinter import *
from tkinter import messagebox
import mysql.connector

e=Tk()
e.title("Registro")
e.geometry("600x300")
e.config(bg="#B4C7E7")
e.resizable(0,0)
#-------------------------------------------------------------#
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

#------------------------------------------------#

etiqueta = Label (e,font=('century',18,'bold'),text='Base de Datos',bg='#B4C7E7',width=20,height=1,bd=5,fg="#000000")
etiqueta.place(x=120,y=30)

#-------------ventana_usuario---------------#
def registro():
     def agregar_usuario():
            cur=conexion.cursor()
            ide=txt_identificacion.get()
            nom=txt_nombre.get()
            cur.execute("update registro set nombre_y_apellidos=%s, puesto_de_trabajo=%s, usuario=%s, contraseña=%s where identificacion=%s",modificar_usuario)
            conexion.commit()
            cur.close()
            messagebox.showinfo(message="los datos se modificaron",title="informacion")     
            limpiar()
     def eliminar_usuario():
             cur=conexion.cursor()
             cod=txt_codigo.get()
             cur.execute("delete from inventario where codigo ='{}'".format(cod))
             conexion.commit()
             cur.close()
             messagebox.showinfo(message="se elimino el libro exitosamente",title="informacion")
             txt_identificacion.delete(0,END)
             txt_nombre_y_apellido.delete(0,END)
             txt_puesto_de_trabajo.delete(0,END)
             txt_usuario.delete(0,END)
             txt_contraseña.delete(0,END)
                    
     u= Tk()
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

     boton_u1=Button(u,font=("arial",12,"bold"),text="consultar",width=20,height=2,bg="#0077AC",).place(x=600,y=100,)

     boton_u2=Button(u,font=("arial",12,"bold"),text="agregar usuario",width=20,height=2,bg="#0077AC",command=agregar_usuario).place(x=50,y=600)

     boton_u3=Button(u,font=("arial",12,"bold"),text="modificar usuario",width=20,height=2,bg="#0077AC",command=modificar_usuario).place(x=300,y=600)

     boton_u4=Button(u,font=("arial",12,"bold"),text="eliminar usuario",width=20,height=2,bg="#0077AC").place(x=550,y=600)
#------------------------------------------------------------------#
def login():
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
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="ingresar sistema",)
    boton_inventario.place(x=530,y=45)

    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="cancelar",)#command=cancelar)
    boton_inventario.place(x=540,y=145)
#---------------------------------E--------------------------------------------------#
boton_re = Button(e,font=("arial",12,"bold"),text="Resgistro",command=registro,width=20,height=2,bg="#0077AC",)
boton_re.place(x=70,y=130)

boton_log = Button(e,font=("arial",12,"bold"),text="Login",command=login,width=20,height=2,bg="#0077AC",).place(x=300,y=130)

e.mainloop()     
            tra=txt_trabajo.get()
            usu=txt_usuario.get()
            con=txt_contraseña.get()
            cur.execute("insert into registro(identificacion,nombre_y_apellidos,puesto_de_trabajo,usuario,contraseña)values('{}','{}','{}','{}','{}')".format(ide,nom,tra,usu,con))
            conexion.commit()#actualizar el envio de datos
            cur.close()
            messagebox.showinfo(message="El se agrego un nuevo usuario",title="informacion")
            txt_identificacion.delete(0,END)
            txt_trabajo.delete(0,END)
            txt_usuario.delete(0,END)
            txt_contraseña.delete(0,END)
            txt_identificacion.focus()
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
             cod=txt_codigo.get()
             cur.execute("delete from inventario where codigo ='{}'".format(cod))
             conexion.commit()
             cur.close()
             messagebox.showinfo(message="se elimino el libro exitosamente",title="informacion")
             txt_identificacion.delete(0,END)
             txt_nombre_y_apellido.delete(0,END)
             txt_puesto_de_trabajo.delete(0,END)
             txt_usuario.delete(0,END)
             txt_contraseña.delete(0,END)
                    
     u= Tk()
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

     boton_u1=Button(u,font=("arial",12,"bold"),text="consultar",width=20,height=2,bg="#0077AC",).place(x=600,y=100,)

     boton_u2=Button(u,font=("arial",12,"bold"),text="agregar usuario",width=20,height=2,bg="#0077AC",command=agregar_usuario).place(x=50,y=600)

     boton_u3=Button(u,font=("arial",12,"bold"),text="modificar usuario",width=20,height=2,bg="#0077AC",command=modificar_usuario).place(x=300,y=600)

     boton_u4=Button(u,font=("arial",12,"bold"),text="eliminar usuario",width=20,height=2,bg="#0077AC").place(x=550,y=600)
#------------------------------------------------------------------#
def login():
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
    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="ingresar sistema",)
    boton_inventario.place(x=530,y=45)

    boton_inventario = Button(j,font=("arial",12,"bold"),width=20,height=2,bg="#0077AC",text="cancelar",)#command=cancelar)
    boton_inventario.place(x=540,y=145)
#---------------------------------E--------------------------------------------------#
boton_re = Button(e,font=("arial",12,"bold"),text="Resgistro",command=registro,width=20,height=2,bg="#0077AC",)
boton_re.place(x=70,y=130)

boton_log = Button(e,font=("arial",12,"bold"),text="Login",command=login,width=20,height=2,bg="#0077AC",).place(x=300,y=130)

e.mainloop()