
import pygame.mixer

mixer = pygame.mixer

mixer.init()

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

audio_option = ['./mp3/aba_inicial_pt-br.mp3',
                './mp3/aba_letras_pt-br.mp3',
                './mp3/aba_silabas_pt-br.mp3',
                './mp3/aba_palavras_pt-br.mp3']


def iterate():
    current = combobox.current()
    new = current+1
    new = 0 if new == 4 else new
    combobox.current(new)
    mixer.music.load(audio_option[new])
    mixer.music.play()


def select():
    option = combobox.current()

    if option == 0:
        print("Ouvir novamente as instruções de uso")
    else:
        notebook.select(option)
        if option == 2:
            entry.set('')

w = 15

combobox = ttk.Combobox(aba1, width=w, state='readonly', font=f)

combobox['values'] = ('ABA INICIAL',
                    'ABA DE LETRAS',
                    'ABA DE SÍLABAS',
                    'ABA DE PALAVRAS')

combobox.pack(expand=1)

combobox.current(0)

# endregion

# region Aba de Letras


def key(event):
    char = event.char.upper()

    aba = notebook.index(notebook.select())

    if aba == 1 or aba == 2:
        if char in alphabet:
            mixer.music.load('./mp3/' + char + '_pt.mp3')
            mixer.music.play()
        else:
            mixer.music.load('./mp3/NL_pt.mp3')
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
    syl = entry.get().upper()
    size = len(syl)
    if size == 2:
        if syl[1] in vowel:
            if syl[0] in consonant and syl[0] not in ['K', 'W', 'Y']:
                print("é um sílaba de tamanho 2 que começa com consoante")
            else:
                print("não é uma sílaba válida")
        elif syl[1] in ['M', 'N', 'L', 'R', 'S', 'Z']:
            if syl[0] in vowel:
                print("é um sílaba de tamanho 2 que começa com vogal")
            else:
                print("não é uma sílaba válida")
        else:
            print("não é uma sílaba válida")
    elif size == 3:
        if syl[2] in vowel:
            if syl[1] == 'H':
                if syl[0] in ['C', 'L', 'N']:
                    print("sílava de tamanho 3 do formato CH, LH ou NH")
                else:
                    print("não é uma sílaba")
            elif syl[1] == 'L':
                if syl[0] in ['B', 'C', 'D', 'F', 'G', 'P', 'T', 'V']:
                    print("sílava de tamanho 3 do formato BL, CL, DL, FL,GL, PL, TL, ou VL")
                else:
                    print("não é uma sílaba")
            elif syl[1] == 'R':
                if syl[0] in ['B', 'C', 'D', 'F', 'G', 'P', 'T']:
                    print("sílava de tamanho 3 do formato BR, CR, DR, FR, GR, PR ou TR")
                else:
                    print("não é uma sílaba")
            elif syl[1] == 'U':
                if syl[0] in ['G', 'Q']:
                    if syl[2] in ['A', 'E', 'I', 'O']:
                        print("sílava de tamanho 3 do formato GU ou QU")
                    else:
                        print("não é uma sílaba")
                else:
                    print("não é uma sílaba")
            else:
                print("não é uma sílaba")
        else:
            print("não é uma sílaba")
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
