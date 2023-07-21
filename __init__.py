import calendar
import locale
import datetime
import tkinter as tk
from centralizacion import centrar
locale.setlocale(locale.LC_ALL, '')
from tkinter import *

import mysql.connector
import config

#obtener conexion
def conectar():
    return mysql.connector.connect(**config.config)


#creamos el cursor y la database en caso de que no exista
con = conectar()
cursor = con.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS basedeprueba")
cursor.execute("USE basedeprueba")
cr_eventos="""CREATE table IF NOT EXISTS eventos (
    id_evento int NOT NULL auto_increment,
    nombre varchar(30) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    duracion TIME NOT NULL DEFAULT '01:00',
    importancia TINYINT(1) NOT NULL DEFAULT 0,
    descripcion MEDIUMTEXT,
    primary key(id_evento))
    
    ;    
    """
cr_recor=""" CREATE TABLE IF NOT EXISTS recordatorios(
    id_recordatorio INT NOT NULL auto_increment,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    primary key (id_recordatorio))
    ;
    """
cr_import="""CREATE TABLE IF NOT EXISTS importancia (
           importancia TINYINT(1) NOT NULL ,
           clasificacion varchar(8),
           primary key(importancia)
           )
    ;
    """ 

cursor.execute(cr_eventos)
cursor.execute(cr_recor)
cursor.execute(cr_import)
#cursor.execute("USE basedeprueba")
con.commit()
con.close()




#ventana principal
raiz=tk.Tk()
raiz.title("Calendario") #Cambiar el nombre de la ventana
raiz.geometry("550x430")
centrar(raiz,550,430)
#raiz.iconbitmap("calendario.ico") #Cambiar el icono
raiz.resizable(0,0) #si la ventana es manipulable de x,y 0,0=NO redimencionar
raiz.config(bg="white")
frame1 = Frame(raiz, bg="white")
frame1.pack(ipadx= 50,ipady=51, fill=X)

frame2 = Frame(raiz,bg="white")
frame2.pack(ipadx=5,ipady=1, fill=X,padx=10)

frame3 = tk.Frame(raiz,bg="white")
frame3.pack(ipadx= 50,ipady=130 ,padx=10, fill=X)



#label encabezado fecha
lunes=Label(raiz,text="Lunes",borderwidth=2,relief="ridge")
lunes.place(x=10,y=78)
lunes.config(width=8,height=1)
lunes.config(fg="black",bg="white",font=("Verdana",11))

martes=Label(raiz,text="Martes",borderwidth=2,relief="ridge")
martes.place(x=86,y=78)
martes.config(width=8,height=1)
martes.config(fg="black",bg="white",font=("Verdana",11))

Miercoles=Label(raiz,text="Miercoles",borderwidth=2,relief="ridge")
Miercoles.place(x=161,y=78)
Miercoles.config(width=8,height=1)
Miercoles.config(fg="black",bg="white",font=("Verdana",11))

Jueves=Label(raiz,text="Jueves",borderwidth=2,relief="ridge")
Jueves.place(x=237,y=78)
Jueves.config(width=8,height=1)
Jueves.config(fg="black",bg="white",font=("Verdana",11))

Viernes=Label(raiz,text="Viernes",borderwidth=2,relief="ridge")
Viernes.place(x=313,y=78)
Viernes.config(width=8,height=1)
Viernes.config(fg="black",bg="white",font=("Verdana",11))

Sabado=Label(raiz,text="Sabado",borderwidth=2,relief="ridge")
Sabado.place(x=389,y=78)
Sabado.config(width=8,height=1)
Sabado.config(fg="black",bg="white",font=("Verdana",11))

Domingo=Label(raiz,text="Domingo",borderwidth=2,relief="ridge")
Domingo.place(x=465,y=78)
Domingo.config(width=8,height=1)
Domingo.config(fg="black",bg="white",font=("Verdana",11))
#clase evento 
class Eventos():
    iniciar=0
    def __init__(self,titulo,fechayhora,importancia,fecha_recordatorio,duracion,descripcion="",etiquetas=""):
        """Se crea el objeto evento"""
        self.titulo=titulo
        self.fechayhora=fechayhora
        self.descripcion=descripcion
        self.importancia=importancia
        self.duracion=duracion
        self.fecha_recordatorio=fecha_recordatorio
        self.etiquetas=etiquetas
    
    def mostrarprincipal(n):
        if n=="1":
            return True
        
    try:
        import json
        f = open("eventos.json")
        f.close()
        ar=open("eventos.json",'r')
        l=ar.readline()
        ar.close
        if l=="{}" or l=="" or l=="[]" or l==" ":
            a=open("eventos.json",'w')
            a.write("")
            listaeventos=[]
            iniciar=0
        else:
            mostrarprincipal("1")
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            with open("eventos.json",'w') as archivo:
                json.dump(datas,archivo)
                listaeventos=datas
            iniciar=1

                
    except IOError:
        #en caso de no exister un archivo eventos.json en el directorio, lo crea
        a=open("eventos.json",'w')
        a.write("")
        listaeventos=[]
        

    listadias=[]
    repeticiones=1
    colores=["yellow","skyblue","springgreen","pink","green","blue","grey","white"]
    def agregar_evento():
        import json
        Eventos.listaeventos
        with open ("eventos.json",'w') as archivo:
            json.dump(Eventos.listaeventos,archivo)
    
    

class CalendarioPrincipal():
    def __init__(self,numero): 
        self.numero=numero
    x=datetime.datetime.now()
    diax=x.strftime("%d")
    dia_actual=int(diax)
    m=x.strftime("%m")
    mes_actual=int(m)
    a=x.strftime("%Y")
    anio=int(a)
    
    #LABEL FECHA ACTUAL
    fecha=x.strftime("%A %d de %B %Y")
    labelfecha=Label(raiz,text=fecha,bg="white")
    labelfecha.place(x=310,y=15)
    labelfecha.config(fg="black",font=("Verdana",12))

    calendario=calendar.Calendar()
    mes = calendario.monthdayscalendar(anio,mes_actual)
    for a in range(len(mes)):
        semana=mes[a]
        for dias in semana:
            if dias==dia_actual:
                numero_de_semana=a  
                semana_actual=a

    numero_de_mes=mes_actual-1
    
    mesesnombre=list()
    for y in range(13):
        if y==0:
            pass
        else:
            mesesnombre.append(calendar.month_name[y])
    
    aniocompleto=list()
    aniocompleto.append(calendario.monthdayscalendar(2023,1))
    aniocompleto.append(calendario.monthdayscalendar(2023,2))
    aniocompleto.append(calendario.monthdayscalendar(2023,3))
    aniocompleto.append(calendario.monthdayscalendar(2023,4))
    aniocompleto.append(calendario.monthdayscalendar(2023,5))
    aniocompleto.append(calendario.monthdayscalendar(2023,6))
    aniocompleto.append(calendario.monthdayscalendar(2023,7))
    aniocompleto.append(calendario.monthdayscalendar(2023,8))
    aniocompleto.append(calendario.monthdayscalendar(2023,9))

    numero_de_mes=mes_actual-1
    opciones = {
    "Enero": ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'), 
    "Febrero": ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'),
    "Marzo":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Abril":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Mayo":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Junio":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Julio":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Agosto":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Septiembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Octubre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    "Noviembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'),
    "Diciembre":('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'),
    }

    

#funcion que muestra el calendario SEMANAL
def mostrar_calendario_mensual():
    class Mes():
        numero=int()

    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    raizm = Toplevel(raiz)
    #raizm.iconbitmap("calendario.ico") #Cambiar el icono
    raizm.resizable(0,0)
    raizm.focus_set()
    raizm.title("Calendario Mensual")
    raizm.geometry("500x350")
    raizm.config(bg="white")
    centrar(raizm,500,350)
    mif=Frame(raizm)
    mif.pack(padx=5,pady=60)
    mif.config(width="550",height="720")
    mif.config(bg="white")

    def mostrar(mes):
        Label(raizm,text="L          M         M         J          V         S          D",font=("verdana","11"),bg="white").place(x=70,y=40)
        nm=str(CalendarioPrincipal.mesesnombre[mes-1])
        nome=Label(raizm,text=nm.capitalize(),font=("verdana","14"),bg="white",width="12")
        nome.place(x=180,y=5)
        calendario=calendar.monthcalendar(2023,mes)
        Mes.numero=mes

        importselect=[]
        dataseleccionada=[]
        diasconseguidos=[]
        mesconseguidos=[]
        nsconseguido=[]
        import json
        f = open("eventos.json")
        f.close()
        ar=open("eventos.json",'r')
        l=ar.readline()
        ar.close
        if l=="{}" or l=="" or l=="[]" or l==" ":
            for f in range(len(calendario)):
            #crea los labels del calendario mensual y los asigna sus posiciones y colores
                for c in range(0, 7):
                    diac=calendario[f][c]
                    if calendario[f][c]==0:
                        celda = Label(mif,height=2,width=6,text="-",bg="white")
                        celda.config(fg="black",font=("Verdana",9))
                        celda.grid(padx=2, pady=2, row=f, column=c)
                    else:
                        if diac==CalendarioPrincipal.dia_actual and Mes.numero==CalendarioPrincipal.numero_de_mes+1:
                            celda = Label(mif,height=2,width=6,text=calendario[f][c],bg="white",borderwidth="2",relief="solid")
                            celda.config(fg="black",font=("Verdana",9))
                            celda.grid(padx=2, pady=2, row=f, column=c)
            pass
        else:
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python

            for a in range(len(datas)):
                aa=datas[a]
                for b in aa:
                    c=aa[b]
                    if b =="Fecha y hora":
                        import datetime
                        datetime_object = datetime.datetime.strptime(c,'%d/%m/%Y,%H:%M:%S')
                        di=datetime_object.strftime("%d")#conseguir dia
                        d=int(di)
                        diasconseguidos.append(d)
                        me=datetime_object.strftime("%m")#conseguir mes 1-12
                        m=int(me)
                        mesconseguidos.append(m)
                        dataseleccionada.append(aa)

            #selecciona la importancia de los datos seleccionados anteriormente
            for af in range(len(dataseleccionada)):
                aaf=dataseleccionada[af]
                for bf in aaf:
                    c=aaf[bf]
                    if bf =="Importancia":
                        importselect.append(c)

        for f in range(len(calendario)):
            #crea los labels del calendario mensual y los asigna sus posiciones y colores
            for c in range(0, 7):
                diac=calendario[f][c]
                if calendario[f][c]==0:
                    celda = Label(mif,height=2,width=6,text="-",bg="white")
                    celda.config(fg="black",font=("Verdana",9))
                    celda.grid(padx=2, pady=2, row=f, column=c)
                else:
                    if diac==CalendarioPrincipal.dia_actual and Mes.numero==CalendarioPrincipal.numero_de_mes+1:
                        celda = Label(mif,height=2,width=6,text=calendario[f][c],bg="white",borderwidth="2",relief="solid")
                        celda.config(fg="black",font=("Verdana",9))
                        celda.grid(padx=2, pady=2, row=f, column=c)
                    else:
                        celda = Label(mif,height=2,width=6,text=calendario[f][c],bg="white")
                        celda.config(fg="black",font=("Verdana",9))
                        celda.grid(padx=2, pady=2, row=f, column=c)
                    for k in range(len(diasconseguidos)):
                        if diac==diasconseguidos[k] and Mes.numero==mesconseguidos[k]:
                            if importselect[k]=="Importante":
                                celda.config(fg="black",bg="red")
                            else:
                                celda.config(fg="black",bg=Eventos.colores[k])                
                    

                    
                

    
    
    mostrar(CalendarioPrincipal.mes_actual)
    def mes_siguiente():
        n=Mes.numero + 1
        mostrar(n)

    def mes_anterior():
        ne=Mes.numero - 1
        mostrar(ne)

    mes_s=ttk.Button(raizm,text="Mes Anterior",command=mes_anterior)
    mes_s.place(x=15,y=300)
    mes_a=ttk.Button(raizm,text="Mes Siguiente",command=mes_siguiente)
    mes_a.place(x=405,y=300)
from tkinter import ttk

#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual",command=mostrar_calendario_mensual)
cambiar.place(x=5,y=10)


#BOTON CAMBIAR EL CALENDARIO A MENSUAL
cambiar=ttk.Button(raiz,text="Calendario Mensual",command=mostrar_calendario_mensual)
cambiar.place(x=5,y=10)
def mostrar_calendario(numero_semana):
    mes=CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes]
    semana=mes[numero_semana]
    CalendarioPrincipal.numero_de_semana=numero_semana

    y=0
    for x in semana:
        if x==0:
            celda=Label(frame2,height=2,width=6,text="-",bg="white",anchor="center")
        
        elif x==CalendarioPrincipal.dia_actual and CalendarioPrincipal.numero_de_mes==CalendarioPrincipal.mes_actual - 1:
                celda=Label(frame2,height=2,width=6,text=x,bg="white",anchor="center",borderwidth=2,relief="solid")
        else:
            celda=Label(frame2,height=2,width=6,text=x,bg="white",anchor="center",relief="groove")
        y=y+1
        celda.config(fg="black",bg="white",font=("Verdana",13))
        celda.grid(padx=1,pady=1,row=0,column=y,ipadx=1)

    #crea los labels de los dias de  semana    
    for c in range(len(semana)):
            cell =Label(frame3, width=10,height=3,bg="white")
            cell.grid(row=0, column=c)

    for d in range(len(semana)):
            cell =Label(frame3, width=10,height=3,bg="white")
            cell.grid(row=1, column=d)


    #labels calendario    
    import json
    f = open("eventos.json")
    f.close()
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]" or l==" ":
        pass
    else:
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python

        importselect=[]
        dataseleccionada=[]
        diasconseguidos=[]
        mesconseguidos=[]
        nsconseguido=[]
        tituloselect=[]

        for a in range(len(datas)):
            aa=datas[a]
            for b in aa:
                c=aa[b]
                if b =="Fecha y hora":
                    import datetime
                    datetime_object = datetime.datetime.strptime(c,'%d/%m/%Y,%H:%M:%S')
                    di=datetime_object.strftime("%d")#conseguir dia
                    d=int(di)
                    diasconseguidos.append(d)
                    dss=datetime_object.strftime("%w")#conseguir dia de la semana,0-6, 0 es domingo
                    ds=int(dss)
                    if ds==0:
                        ds=6
                    else:
                        ds=ds-1
                    nsconseguido.append(ds)
                    me=datetime_object.strftime("%m")#conseguir mes 1-12
                    m=int(me)
                    mesconseguidos.append(m)
                    dataseleccionada.append(aa)

        for af in range(len(dataseleccionada)):
                aaf=dataseleccionada[af]
                for bf in aaf:
                    c=aaf[bf]
                    if bf =="Importancia":
                        importselect.append(c)
                    if bf=="Titulo":
                        tituloselect.append(c)

     
        mms=CalendarioPrincipal.numero_de_mes+1


        r=0
        
        for i in range(len(semana)):
            
            for j in range(len(diasconseguidos)):
                c=diasconseguidos.count(diasconseguidos)    
                if diasconseguidos[j]==semana[i] and mesconseguidos[j]==mms:
                    
                    if c==1:
                        if importselect[j]=="Importante":
                            cell =Label(frame3, width=10,height=2,text=tituloselect[j],bg="red")
                            cell.grid(row=0, column=nsconseguido[j])
                        else:
                            cell =Label(frame3, width=10,height=2,text=tituloselect[j],bg=Eventos.colores[j])
                            cell.grid(row=0, column=nsconseguido[j])
                    else:
                
                        if importselect[j]=="Importante":
                            cell =Label(frame3, width=10,height=2,text=tituloselect[j],bg="red")
                            cell.grid(row=r, column=nsconseguido[j])
                            r+=1
                        else:
                            cell =Label(frame3, width=10,height=3,text=tituloselect[j],bg=Eventos.colores[j])                         
                            cell.grid(row=r, column=nsconseguido[j])
                            r+=1


     
       


def siguiente_semana():
    mm=len(CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes])

    if CalendarioPrincipal.numero_de_semana + 1 == mm:
        c=CalendarioPrincipal.numero_de_mes + 1
        CalendarioPrincipal.numero_de_mes=c
        CalendarioPrincipal.numero_de_semana=0

        mostrar_calendario(CalendarioPrincipal.numero_de_semana)

    else:
        s=CalendarioPrincipal.numero_de_semana + 1

        mostrar_calendario(s)

def anterior_semana():
    
    
    if CalendarioPrincipal.numero_de_semana - 1 == 0:
        c=CalendarioPrincipal.numero_de_mes - 1
        CalendarioPrincipal.numero_de_mes=c
        
        mr=CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes]
        
        ns=len(mr) - 1
        CalendarioPrincipal.numero_de_semana=ns

        mostrar_calendario(CalendarioPrincipal.numero_de_semana)
        
    if CalendarioPrincipal.numero_de_semana==0:
        c=CalendarioPrincipal.numero_de_mes - 1
        CalendarioPrincipal.numero_de_mes=c
        mr=CalendarioPrincipal.aniocompleto[CalendarioPrincipal.numero_de_mes]
        ss=len(mr) - 1
        mostrar_calendario(ss)
    
    else:
        s=CalendarioPrincipal.numero_de_semana - 1
        CalendarioPrincipal.numero_de_semana=s
        mostrar_calendario(s)


                            
    
def mostrar_recordatorios():
    
    import tkinter as tk
    from tkinter import messagebox,ttk
    f = open("eventos.json")
    f.close()
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]" or l==" ":
        messagebox.showwarning("Error", "No existen eventos")
    else:  
        ventanamr = Toplevel(raiz)
        ventanamr.focus_set()
        ventanamr.title("Recordatorios")
        ventanamr.geometry("270x350")
        ventanamr.config(bg="white")
        centrar(ventanamr,270,350)
        ventanamr.resizable(0,0)
        fr=Frame(ventanamr)
        fr.config(bg="white")
        fr.pack(ipadx=0,ipady=0, fill=X,pady=30,padx=2)
        import json

        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python 
        tits=list()
        fechayhorar=list()

        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b =="Fecha Recordatorio":
                    fechayhorar.append(c)
                elif b=="Titulo":
                    tits.append(c)

        #funcion que muestra info del boton tocado
        def mostrarinfo():
            hola=Toplevel(fr)
            hola.config(bg="white")
            from centralizacion import centrar
            centrar(hola,300,230)
            hola.focus_set()
            i=str(datas[a])
            inf=i.replace(",","\n")
            info=inf.replace("'"," ")
            infos=info.replace("{"," ")
            infor=infos.replace("}"," ")
            information=Label(hola,text=infor,font=("Verdana", 12),bg="white")
            information.place(x=5,y=10)
        for a in range(len(tits)):
            if a%2==0:
                color="#CDCDB7"
            else:
                color="#FFFFD3"

            cell =Label(fr,width=15,height=3,text=tits[a],bg=color,font=("Verdana", 8)) 
            cell.grid(row=a, column=0)

        for b in range(len(tits)):
            if b%2==0:
                color="#CDCDB7"
            else:
                color="#FFFFD3"
            celld =Label(fr,width=25,height=3,text=fechayhorar[b],bg=color,font=("Verdana",8))
            celld.grid(row=b, column=2)
        
        t=Label(ventanamr,text="Titulo",bg="white",font=("Verdana", 10)).place(x=40,y=5)
        Label(ventanamr,text="Fecha Recordatorio",bg="white",font=("Verdana", 10)).place(x=130,y=5)

      
mostrar_calendario(CalendarioPrincipal.semana_actual)

from tkinter import ttk
#boton siguiente semana
sigue=ttk.Button(raiz,text="Semana Siguiente",command=siguiente_semana)
sigue.pack()
sigue.place(x=430,y=295)

#boton anterior semana
ante=ttk.Button(raiz,text="Semana Anterior",command=anterior_semana)
ante.pack()
ante.place(x=15,y=295)     

def abrir_ventana():
    
    from centralizacion import centrar
    import tkinter as tk
    from tkinter import messagebox,ttk
    ventananueva = Toplevel(raiz)
    ventananueva.focus_set()
    ventananueva.title("Agregar evento")
    ventananueva.geometry("250x450")
    centrar(ventananueva,250,450)
    #ventananueva.iconbitmap("calendario.ico")
    ##radioValue = tk.IntVar()
    radio = tk.IntVar()
    radio.set(1)
    varfecha = tk.IntVar()
    varfecha.set(2)
    #CREACION DE HORAS,DIAS Y MESES EN LISTA
    x=datetime.datetime.now()
    d=x.strftime("%d")
    dia_actual=int(d)            
    m=x.strftime("%m")
    a=x.strftime("%Y")
    h=x.strftime("%H")

    meses=list()
    horas=list()
    minutos=list()
    diass=list()
    for y in range(13):
        if y==0:
            pass
        else:
            meses.append(calendar.month_name[y])

    for z in range(24):
        if z==0:
            pass 
        else:
            horas.append(z)

    for r in range(60):
        if r==0:
            pass
        else:
            minutos.append(r)    

    for j in range(31):
        if j == 0:
            pass
        else:
            diass.append(j)

    #Label nuevo evento
    ne=Label(ventananueva,text="Nuevo Evento")
    ne.place(x=25,y=15)
    ne.config(font=("Verdana",17))
    
    #Label titulo
    titulol=Label(ventananueva,text="Titulo:")
    titulol.place(x=20,y=75)

    #Entrada titulo
    tituloe=ttk.Entry(ventananueva)
    tituloe.focus_set()
    tituloe.config(width=25)
    tituloe.place(x=65,y=75)
    


    

    #Label fecha 
    fecha=Label(ventananueva,text="Fecha:")
    fecha.place(x=20,y=115)
    fechan=x.strftime("%x")
    Label(ventananueva,text=fechan).place(x=65,y=115)
    #Label hora
    horal=Label(ventananueva,text="Hora:")
    horal.place(x=20,y=140)
    horaln=x.strftime("%X")
    Label(ventananueva,text=horaln).place(x=65,y=140)
    

    #label duracion
    duracionl=Label(ventananueva,text="Duración --->")
    duracionl.place(x=20,y=180)
    #entrada duracion horas
    horaed =ttk.Combobox(ventananueva,values=horas)
    horaed.place(x=95,y=180)
    horaed.config(width="3")
    horaed.insert(0,1)
    #entrada minutos
    minutosed =ttk.Combobox(ventananueva,values=minutos)
    minutosed.place(x=147,y=180)
    minutosed.config(width="3")
    minutosed.insert(0,"00")
    Label(ventananueva,text="hs").place(x=130,y=180)
    Label(ventananueva,text="min").place(x=185,y=180)
    
    #BOTONES importante y normal
    
    Radiobutton(ventananueva,
            text="Normal",
            variable=radio,
            value=1,
            ).place(x=10,y=215)

    Radiobutton(ventananueva,
            text="Importante",
            variable=radio,
            value=2,
            ).place(x=10,y=240)
    
    
    #LABEL RECORDATORIO
    Label(ventananueva,text="---------------Recordatorio---------------").place(x=10,y=270)
    dias=list()
    for a in range(dia_actual):
        dd=dia_actual-a
        dias.append(dd)

    #dias combox recordatorio
    diar= ttk.Combobox(
    ventananueva,
    state="readonly",
    values=dias,
    width="3",
    )
    diar.pack()
    diar.place(x=40,y=300)
    Label(ventananueva,text="Dia:").place(x=15,y=300)
    horasr=list()
    for x in range(24):
        if x==0:
            pass
        else:
            horasr.append(x)

    #entrada horas combobox
    horaer=ttk.Combobox(
    ventananueva,
    state="readonly",
    values=horasr,
    width=3,
    )
    horaer.pack
    horaer.place(x=120,y=300)
    Label(ventananueva,text="Hora:").place(x=90,y=300)

    #entrada minutos
    minutoser =ttk.Combobox(ventananueva,values=minutos)
    minutoser.place(x=190,y=300)
    minutoser.config(width="3")
    Label(ventananueva,text="Min:").place(x=165,y=300)

    #label descripcion
    Label(ventananueva,text="Descripción:").place(x=4,y=327)
    #texto descripcion
    descripcion_texto = Text(ventananueva, height=3,width=32)
    descripcion_texto.pack()
    descripcion_texto.place(x=4,y=350)
    
    def agregado():
        import json
        import datetime
        import tkinter as tk
        from tkinter import messagebox,ttk
        titulo=tituloe.get()
        
        #fecha y hora actuales
        fechayhora=(fechan+","+horaln)



        #duracion
        horaf=horaed.get()
        minutof=minutosed.get()
        duracion='{}:{}'.format(horaf,minutof)

        #dia hora min recordatorio
        hora_recor=horaer.get()
        dia_recor=diar.get()
        mier=minutoser.get()

        diare=dia_recor+"/"+"3"+"/"+"2023"
        horar = hora_recor+":"+mier
        fecha_recordatorio=(diare+","+horar)

        descripcion=descripcion_texto.get("1.0","end")
        des=descripcion.rstrip()

        im=str(radio.get())
        if im=="1":
            importancia="Normal"
        elif im=="2":
            importancia="Importante"
       
        ar=open("eventos.json",'r')
        le=ar.readline()
        ar.close()

        if le=="{}" or le=="" or le=="[]" or le==" ":
            listafechas=[]
            import json
            entry={"Descripcion":des,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha y hora":fechayhora,"Titulo":titulo,"Duracion":duracion}
            Eventos.listaeventos.append(entry)
            Eventos.agregar_evento()
            Eventos.listadias.append(dia_actual)
            messagebox.showinfo(message="Evento Agregado", title="Calendario")
            mostrar_calendario(CalendarioPrincipal.semana_actual)
            ventananueva.destroy()
        else:
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)

            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python

            listafechas=list()
            listadiasfechas=list()
            listahorasfechas=list()
            listamesfechas=list()

            for a in range(len(datas)):
                aa=(datas[a])
                for b in aa:
                    c=aa[b]
                    if b =="Fecha y hora":
                        listafechas.append(c)


            for f in listafechas:
                n=datetime.datetime.strptime(f, '%d/%m/%Y,%H:%M:%S')
                dn=n.strftime("%d")
                dnn=int(dn)
                listadiasfechas.append(dnn)
                hn=n.strftime("%H")
                hnn=int(hn)
                listahorasfechas.append(hnn)
                mn=n.strftime("%m")
                mnn=int(mn)
                listamesfechas.append(mnn)
                
            desfechayhora=datetime.datetime.strptime(fechayhora,'%d/%m/%Y,%H:%M:%S')
            desd=desfechayhora.strftime("%d")
            desdd=int(desd)
            desm=desfechayhora.strftime("%m")
            desmm=int(desm)
            desh=desfechayhora.strftime("%H")
            deshh=int(desh)


            for l in range(len(listafechas)):
                    if int(listadiasfechas[l])==desdd and int(listamesfechas[l])==desmm and int(listahorasfechas[l])==deshh:
                        messagebox.showerror("Error", "ya existe un evento con el mismo dia y hora")
                        repite=True
                        ventananueva.destroy()
                        break
                    else:
                        repite=False
            if repite==False:
                entry={"Descripcion":des,"Fecha Recordatorio":fecha_recordatorio,"Importancia":importancia,"Fecha y hora":fechayhora,"Titulo":titulo,"Duracion":duracion}
                Eventos.listaeventos.append(entry)
                Eventos.agregar_evento()
                Eventos.listadias.append(dia_actual)
                messagebox.showinfo(message="Evento Agregado", title="Calendario")
                mostrar_calendario(CalendarioPrincipal.semana_actual)
                ventananueva.destroy()


    #BOTON AGREGAR LISTO
    boton_listo=ttk.Button(ventananueva,text="Agregar",command=agregado)
    boton_listo.pack()
    boton_listo.place(x=160,y=415)

    #funcion del boton salir
    def salir_vn():
        ventananueva.destroy()

    #BOTON SALIR
    boto_salir=ttk.Button(ventananueva,text="Salir",command=salir_vn)
    boto_salir.pack()
    boto_salir.place(x=20,y=415)   

from tkinter import messagebox
def error_archivo():
    messagebox.showwarning("Error", "No existen eventos")

def eliminar_evento():
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]":
        error_archivo()
    else:
        from centralizacion import centrar
        import tkinter as tk
        from tkinter import messagebox,ttk

        ventanam = Toplevel(raiz)
        ventanam.focus_set()
        ventanam.title("Eliminar evento")
        ventanam.geometry("200x200")
        centrar(ventanam,200,200)
            
        import json
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python
        
        listats=[]
        
        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b == "Titulo":
                    listats.append(c) 

        combotitulo=ttk.Combobox(ventanam,values=listats)
        combotitulo.place(x=50,y=80)
        combotitulo.config(width="12")

        

        def eliminar():
            #eliminar un evento
            from tkinter import messagebox
            messagebox.showinfo(message="Se ha eliminado un evento", title="Eliminar Evento")
            with open("eventos.json",'r') as archivo:
                datos=json.load(archivo)
            datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
            datas = json.loads(datajs)#objeto python
            
            for i in range(len(listats)):
                if listats[i] == combotitulo.get():
                        numero=i
            datas.pop(numero)
            Eventos.listaeventos.pop(numero)
            with open("eventos.json",'w') as archivo:
                json.dump(datas,archivo)
            mostrar_calendario(CalendarioPrincipal.semana_actual)

        #funcion del boton salir
        def salir_vm():
            ventanam.destroy()

        #boton salir
        bs=ttk.Button(ventanam,text="Salir",command=salir_vm)
        bs.pack()
        bs.place(x=10,y=140)

        #boton guardar
        bg=ttk.Button(ventanam,text="Elimnar",command=eliminar)
        bg.pack()
        bg.place(x=100,y=140)

        #Label 
        Label(ventanam,text="Seleccione el Evento \n a eliminar:").place(x=10,y=25)   
            

def modificar_evento():
    ar=open("eventos.json",'r')
    l=ar.readline()
    ar.close
    if l=="{}" or l=="" or l=="[]":
        error_archivo()
    else:
        from centralizacion import centrar
        import tkinter as tk
        from tkinter import messagebox,ttk

        ventanamod = Toplevel(raiz)
        ventanamod.focus_set()
        ventanamod.title("Modificar evento")
        ventanamod.geometry("180x180")
        centrar(ventanamod,180,180)
        #listas para combox de titulos y items para modificar
        import json
        with open("eventos.json",'r') as archivo:
            datos=json.load(archivo)
        datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
        datas = json.loads(datajs)#objeto python
        #mostrar y añadir a lista Titulos
        listatitulos=[]
        listaitems=[]
        for a in range(len(datas)):
            aa=(datas[a])
            for b in aa:
                c=aa[b]
                if b == "Titulo":
                    listatitulos.append(c)
            

        def selecciontitulo():
            f=Frame(ventanamod)
            f.pack()
            f.config(width="270",height="450")

            Label(f,text="Seleccione item a modificar").place(x=15,y=40)

            items=['Descripcion', 'Duracion', 'Fecha Recordatorio', 'Fecha y hora', 'Importancia', 'Titulo']
            #combox modificar
            comboitem=ttk.Combobox(ventanamod,values=items)
            comboitem.place(x=40,y=80)
            comboitem.config(width="14")

            #boton seleccionar item a modifica
            def mostrar_casillero():
                fe = Toplevel(raiz)
                fe.focus_set()
                fe.title("Modificar evento")
                fe.geometry("250x250")
                centrar(fe,250,250)
                
                Label(fe,text="Ingrese el nuevo valor de \n"+comboitem.get()).place(x=50,y=20)
                horas=list()
                minutos=list()

                for z in range(24):
                    if z==0:
                        pass 
                    else:
                        horas.append(z)

                for r in range(60):
                    if r==0:
                        pass
                    else:
                        minutos.append(r)   
                     

                if comboitem.get()=="Fecha y hora" or comboitem.get()=="Fecha Recordatorio":
                    #combo fecha
                    #label dias
                    Label(fe,text="Mes:").place(x=40,y=80)
                    Label(fe,text="Dias:").place(x=40,y=120)
                    def on_combobox_select(event):
                        combobox1.set("")
                        combobox1.config(values=CalendarioPrincipal.opciones[combobox.get()])

                    combobox = ttk.Combobox(
                    fe, width="11", state="readonly", values=tuple(CalendarioPrincipal.opciones.keys()))
                    combobox.place(x="80", y="80")
                    combobox.bind("<<ComboboxSelected>>", on_combobox_select)  
                    combobox1 = ttk.Combobox(
                    fe, width="4", state="readonly") 
                    combobox1.place(x="80",y="120")

                    #label horas
                    Label(fe,text="Hora:").place(x=40,y=160)

                    #horas
                    combohorafyh =ttk.Combobox(fe,values=horas)
                    combohorafyh.place(x=80,y=160)
                    combohorafyh.config(width="3")
                    combohorafyh.insert(0,1)
                    #minutos
                    combominutofyh =ttk.Combobox(fe,values=minutos)
                    combominutofyh.place(x=147,y=160)
                    combominutofyh.config(width="3")
                    combominutofyh.insert(0,"00")
                    Label(fe,text="hs").place(x=120,y=160)
                    Label(fe,text="min").place(x=185,y=160)                    
                   
     
                elif comboitem.get()=="Importancia":
                    nuevo=Entry(fe,width="35")
                    nuevo.pack()
                    nuevo.place(x=22,y=100)
                    nuevo.focus_set()
                    nuevo.insert(END,"Normal/Importante")

                else:
                    nuevo=Entry(fe,width="35")
                    nuevo.pack()
                    nuevo.place(x=22,y=100)
                    nuevo.focus_set()

                #guardar cambios del elemento modificado
                def guardarcambios():

                    from tkinter import messagebox
                    import json
                    import datetime
                    with open("eventos.json",'r') as archivo:
                        datos=json.load(archivo)
                    datajs = json.dumps(datos, indent=4, sort_keys=True)#list json
                    datas = json.loads(datajs)#objeto python
                    if comboitem.get()=="Fecha y hora":
                        listafechas=list()
                        listadiasfechas=list()
                        listahorasfechas=list()
                        listamesfechas=list()

                        for a in range(len(datas)):
                            aa=(datas[a])
                            for b in aa:
                                c=aa[b]
                                if b =="Fecha y hora":
                                    listafechas.append(c)


                        for f in listafechas:
                            n=datetime.datetime.strptime(f, '%d/%m/%Y,%H:%M:%S')
                            dn=n.strftime("%d")
                            dnn=int(dn)
                            listadiasfechas.append(dnn)
                            hn=n.strftime("%H")
                            hnn=int(hn)
                            listahorasfechas.append(hnn)
                            mn=n.strftime("%m")
                            mnn=int(mn)
                            listamesfechas.append(mnn)

                        mesget=combobox.get()
                        mesgett=mesget.lower()
                        mesnumero=CalendarioPrincipal.mesesnombre.index(mesgett) + 1
      
                        
                        for p in range(len(listafechas)):
                            if int(listadiasfechas[p])==int(combobox1.get()) and int(listamesfechas[p])==int(mesnumero) and int(listahorasfechas[p])==int(combohorafyh.get()):
                                messagebox.showerror("Modificar Calendario", "Error - Ya existe un evento con el mismo dia y hora")
                                fe.destroy()
                                break
                            
                        fechayhora=str(combobox1.get())+"/"+str(mesnumero)+"/"+"2023"+","+str(combohorafyh.get())+":"+combominutofyh.get()+":"+"00"
            

                        for i in range(len(listatitulos)):
                            if listatitulos[i] == combotitulo.get():
                                tituloelegido=i
                        
                        aa=(datas[tituloelegido])

                        for b in aa:
                            if b=="Fecha y hora":
                                aa[b]=fechayhora
                        with open("eventos.json",'w') as archivo:
                            #guardar la modificacion
                            json.dump(datas,archivo, indent=4)
                            Eventos.listaeventos=[]
                            Eventos.listaeventos=[datas]
                        messagebox.showinfo(message="Cambios Guardados", title="Modificar Calendario")
                        mostrar_calendario(CalendarioPrincipal.semana_actual)



                    elif comboitem.get()=="Fecha Recordatorio":
               
                        mesget=combobox.get()
                        mesgett=mesget.lower()
                        mesnumero=CalendarioPrincipal.mesesnombre.index(mesgett) + 1
                            
                        fechayhorar=str(combobox1.get())+"/"+str(mesnumero)+"/"+"2023"+","+str(combohorafyh.get())+":"+combominutofyh.get()+":"+"00"
            

                        for i in range(len(listatitulos)):
                            if listatitulos[i] == combotitulo.get():
                                tituloelegido=i
                        
                        aa=(datas[tituloelegido])

                        for b in aa:
                            if b=="Fecha Recordatorio":
                                aa[b]=fechayhorar
                        with open("eventos.json",'w') as archivo:
                            #guardar la modificacion
                            json.dump(datas,archivo, indent=4)
                            Eventos.listaeventos=[]
                            Eventos.listaeventos=[datas]
                        messagebox.showinfo(message="Cambios Guardados", title="Modificar Calendario")
                        mostrar_calendario(CalendarioPrincipal.semana_actual)
                    else:    
                        from tkinter import messagebox
                        messagebox.showinfo(message="Cambios Guardados", title="Modificar Calendario")
                        
                        import json
                        #elegir titulo a modificar y modificarlo
                        for i in range(len(listatitulos)):
                            if listatitulos[i] == combotitulo.get():
                                tituloelegido=i

                        #modifica el titulo en el entry nuevo
                        aa=(datas[tituloelegido])

                        for b in aa:
                            if b==comboitem.get():
                                aa[b]=nuevo.get()
                            #if b == comboitem.get():
                                #Aqui se pone en a el nuevo titulo a cambiar ejemplo puse un input
                            #    aa[b]=nuevo.get()

                        with open("eventos.json",'w') as archivo:
                            #guardar la modificacion
                            json.dump(datas,archivo, indent=4)
                        Eventos.listaeventos=[]
                        Eventos.listaeventos=[datas]
                        mostrar_calendario(CalendarioPrincipal.semana_actual)

                def salirfe():
                    fe.destroy()
                    ventanamod.destroy()
                #boton salir
                bs=ttk.Button(fe,text="Salir",command=salirfe)
                bs.pack()
                bs.place(x=40,y=220)

                #boton guardar
                bg=ttk.Button(fe,text="Guardar",command=guardarcambios)
                bg.pack()
                bg.place(x=130,y=220)

            ci=ttk.Button(ventanamod,text="Aceptar",command=mostrar_casillero)
            ci.place(x=50,y=140)

        
        #Label modifcar evento
        Label(ventanamod,text="Seleccione el Evento \n a modificar:").place(x=10,y=25)   
        combotitulo=ttk.Combobox(ventanamod,values=listatitulos)
        combotitulo.place(x=50,y=80)
        combotitulo.config(width="12")
        #boton seleccionar
        bc=ttk.Button(ventanamod,text="Seleccionar",command=selecciontitulo)
        bc.place(x=50,y=140)

#boton modificar evento
boton2=ttk.Button(raiz,text="Modificar\n Evento",command=modificar_evento)
boton2.place(x=120,y=335)

#boton eliminar evento
boton3=ttk.Button(raiz,text="Eliminar\n Evento",command=eliminar_evento)
boton3.place(x=350,y=335)

    
#boton agregar evento
from tkinter import ttk
boton1=ttk.Button(raiz,text="Agregar\n Evento",command=abrir_ventana)
boton1.pack()
boton1.place(x=235,y=335)

#boton mostrar recordatorios
botonr=ttk.Button(raiz,text="Recordatorios",command=mostrar_recordatorios)
botonr.pack()
botonr.place(x=5,y=40)

col=Label(raiz,bg="red")
col.config(width=1,height=1)
col.place(x=25,y=400)
Label(raiz,text="Importante",bg="white").place(x=40,y=400)

coh=Label(raiz,bg="white",borderwidth=2,relief="solid")
coh.config(width=1,height=1)
coh.place(x=150,y=400)
Label(raiz,text="Dia Actual",bg="white").place(x=165,y=400)
raiz.mainloop()
