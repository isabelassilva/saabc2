
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

# region :: Frame de Abas

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

# region :: Aba Inicial


def iterate():
    atual = combobox.current()
    novo = atual+1
    novo = 0 if novo == 4 else novo
    combobox.current(novo)


def select():
    option = combobox.current()

    if option == 0:
        print("Ouvir novamente as instruções de uso")
    else:
        notebook.select(option)

w = 15

combobox = ttk.Combobox(aba1, width=w, state='readonly', font=f)

combobox['values'] = ('ABA INICIAL',
                    'ABA DE LETRAS',
                    'ABA DE SÍLABAS',
                    'ABA DE PALAVRAS')

combobox.pack(expand=1)

combobox.current(0)

# endregion

import pygame.mixer

mixer = pygame.mixer

mixer.init()

# region Aba de Letras


def key(event):
    char = event.char.upper()

    aba = notebook.index(notebook.select())

    if aba == 1 or aba == 2:
        if char in alphabet:
            mixer.music.load('./mp3/' + char + '_pt-br.mp3')
            mixer.music.play()
        else:
            mixer.music.load('./mp3/PK_pt-br.mp3')
            mixer.music.play()
    if aba == 2:
        if char not in alphabet:
            g = entry.get()
            entry.set(g[:-1])

# endregion

# region Aba de Sílabas

consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J',
             'K', 'L', 'M', 'N', 'P', 'Q', 'R',
             'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

vowel = ['A', 'E', 'I', 'O', 'U']

alphabet = consonant + vowel


def syllable():
    syllable = entry.get()
    size = len(syllable)
    if size == 2:
        print("possível sílava de tamanho 2")
    elif size == 3:
        print("possível sílava de tamanho 3")
    else:
        print("não é uma sílaba")
    entry.set('')

entry = tk.StringVar()
en = tk.Entry(aba3, textvariable=entry, font=f)
en.pack(expand=1)
en.focus()

# endregion

# region :: Binds


def enter(event):
    aba = notebook.index(notebook.select())
    if aba == 0:
        select()
    elif aba == 2:
        syllable()

def escape():
    notebook.select(0)


def space(event):
    aba = notebook.index(notebook.select())
    iterate() if aba == 0 else escape()


window.bind('<space>', space)

aba1.bind_all('<Return>', enter)

aba2.bind_all('<Key>', key)

# endregion

window.mainloop()
