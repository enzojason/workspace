import tkinter as tk
from tkinter import ttk

def centrar(ventana,w,h):   
    """Centrar la ventana que es recibida por parametro, dependiendo de su ancho y largo"""
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()
    wventana = w
    hventana = h
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))