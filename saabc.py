
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

# region :: Configuraçao de Fontes

fontsize = 40
f = ("Times News Roman", fontsize)

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

# region Aba Inicial


def iterate(event):
    atual = combobox.current()
    novo = atual+1
    novo = 0 if novo == 4 else novo
    combobox.current(novo)


def select(event):
    aba = combobox.current()
    #aba = notebook.index(notebook.select())
    if aba == 0:
        print("Ouvir novamente as instruções de uso")
    elif aba == 1:
        notebook.select(1)
    elif aba == 2:
        notebook.select(2)
    elif aba == 3:
        notebook.select(3)

w = 15

combobox = ttk.Combobox(aba1, width=w, state='readonly', font=f)

combobox['values'] = ('ABA INICIAL',
                    'ABA DE LETRAS',
                    'ABA DE SÍLABAS',
                    'ABA DE PALAVRAS')

combobox.pack(expand=1)

combobox.current(0)

aba1.bind_all('<space>', iterate)

aba1.bind_all('<Return>', select)

# endregion

window.mainloop()