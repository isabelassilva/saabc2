
# region :: Configurações da Janela Principal

import tkinter as tk

from tkinter import ttk

window = tk.Tk()

window.title("SAABC: Software de Auxílio à Alfabetização Braille para Crianças")

xsize = 650
ysize = 500

window.geometry('%dx%d' % (xsize, ysize))

window.resizable(0, 0)

# endregion

# region Frame de Abas

notebook = ttk.Notebook(window)

aba1 = ttk.Frame(notebook)

notebook.add(aba1, text="         Aba Inicial           ")

notebook.pack(fill="both", expand=1)

aba2 = ttk.Frame(notebook)

notebook.add(aba2, text="         Aba de Letras         ")

aba3 = ttk.Frame(notebook)

notebook.add(aba3, text="         Aba de Sílabas        ")

notebook.pack(fill="both", expand=1)

aba4 = ttk.Frame(notebook)

notebook.add(aba4, text="         Aba de Palavras       ")

# endregion

window.mainloop()