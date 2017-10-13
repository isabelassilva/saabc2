
import tkinter as tk

from tkinter import ttk

import enchant

import os.path

import pyttsx3

import pygame.mixer

from audio_generator import record

engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', rate-50)

engine.setProperty('voice', 'brazil')

mixer = pygame.mixer

mixer.init()

# region :: Configurações da Janela Principal

window = tk.Tk()

window.title("SAABC: Software de Auxílio à Alfabetização Braille para Crianças")

xsize = 650
ysize = 500

window.geometry('%dx%d' % (xsize, ysize))

window.resizable(0, 0)

# endregion

# region :: Configuração de Fontes

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

audio_option = ['./mp3/aba_inicial_pt.mp3',
                './mp3/aba_letras_pt.mp3',
                './mp3/aba_silabas_pt.mp3',
                './mp3/aba_palavras_pt.mp3']

audio_option_exiting = ['./mp3/aba_inicial_saida_pt.mp3',
                        './mp3/aba_letras_saida_pt.mp3',
                        './mp3/aba_silabas_saida_pt.mp3',
                        './mp3/aba_palavras_saida_pt.mp3']


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
            sy_entry.set('')
            syl.focus()
        if option == 3:
            wo_entry.set('')
            wor.focus()

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
            g = sy_entry.get()
            sy_entry.set(g[:-1])

# endregion

# region Aba de Sílabas

consonant = ['B', 'C', 'D', 'F', 'G', 'H',
             'J', 'L', 'M', 'N', 'P', 'Q',
             'R', 'S', 'T', 'V', 'X', 'Z']

special_consonant = ['K', 'W', 'Y']

vowel = ['A', 'E', 'I', 'O', 'U']

alphabet = consonant + special_consonant + vowel


def syllable():
    sy = sy_entry.get().upper()
    size = len(sy)
    if size == 2:
        if (sy[1] in vowel and (sy[0] in consonant and sy[0] not in ['Q'])) or \
                (sy[1] in ['M', 'N', 'L', 'R', 'S', 'Z'] and sy[0] in vowel):
            mixer.music.load('./mp3/' + sy + '_pt.mp3')
            mixer.music.play()
        else:
            mixer.music.load('./mp3/NS_pt.mp3')
            mixer.music.play()
    elif size == 3:
        if sy[2] in vowel:
            if (sy[1] == 'H' and sy[0] in ['C', 'L', 'N']) or \
                    (sy[1] == 'L' and sy[0] in ['B', 'C', 'F', 'G', 'P', 'T', 'V']) or \
                    (sy[1] == 'R' and sy[0] in ['B', 'C', 'D', 'F', 'G', 'P', 'T']) or \
                    (sy[1] == 'U' and sy[0] in ['G', 'Q'] and sy[2] in ['A', 'E', 'I', 'O']):
                    mixer.music.load('./mp3/' + sy + '_pt.mp3')
                    mixer.music.play()
            else:
                mixer.music.load('./mp3/NS_pt.mp3')
                mixer.music.play()
        else:
            mixer.music.load('./mp3/NS_pt.mp3')
            mixer.music.play()
    else:
        mixer.music.load('./mp3/NS_pt.mp3')
        mixer.music.play()
    sy_entry.set('')

sy_entry = tk.StringVar()
syl = tk.Entry(aba3, textvariable=sy_entry, font=f)
syl.pack(expand=1)

# endregion

# region Aba de Palavras


def say(msg):
    engine.say(msg)
    engine.runAndWait()

dictionary = enchant.request_pwl_dict("pt-BR_out.dic")


def word():
    wo = wo_entry.get().lower()
    if wo != '':
        b = dictionary.check(wo)
        file = './mp3/' + wo + '_pt.mp3'
        if b:
            if os.path.isfile(file):
                mixer.music.load(file)
                mixer.music.play()
            elif record(wo, 'pt'):
                mixer.music.load(file)
                mixer.music.play()
            else:
                say(wo)
        else:
            mixer.music.load('./mp3/NW_pt.mp3')
            mixer.music.play()

    wo_entry.set('')

wo_entry = tk.StringVar()
wor = tk.Entry(aba4, textvariable=wo_entry, font=f)
wor.pack(expand=1)

# endregion

# region :: Binds


# noinspection PyUnusedLocal
def enter(event):
    aba = notebook.index(notebook.select())
    if aba == 0:
        select()
    elif aba == 2:
        syllable()
    elif aba == 3:
        word()


def escape():
    notebook.select(0)
    mixer.music.load(audio_option_exiting[combobox.current()])
    mixer.music.play()


# noinspection PyUnusedLocal
def space(event):
    aba = notebook.index(notebook.select())
    iterate() if aba == 0 else escape()


window.bind('<space>', space)

aba1.bind_all('<Return>', enter)

aba2.bind_all('<Key>', key)

# endregion

# region Welcome


def welcome():
    file = './mp3/welcome.mp3'
    mixer.music.load(file)
    mixer.music.play()

window.after(100, welcome)

# endregion

window.mainloop()
