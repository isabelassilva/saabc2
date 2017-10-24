
import tkinter as tk

from tkinter import ttk

import os.path

import pyttsx3

import playsound

from audio_generator import record

import platform

# region :: init()

engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 50)

engine.setProperty('voice', 'brazil')

so = platform.system()

__PATH__ = ''
attribute = ''

if so == 'Windows':
    __PATH__ = r'C:/Users/isabela/Anaconda3/Scripts/mp3/'
    attribute = '-fullscreen'
elif so == 'Linux':
    __PATH__ = './mp3/'
    attribute = '-zoomed'
else:
    print('Operational System not detected')

# endregion()

# region :: Configurações da Janela Principal

window = tk.Tk()

window.title("SAABC: Software de Auxílio à Alfabetização Braille para Crianças")

window.attributes(attribute, True)

window.attributes("-topmost", True)

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

audio_option = [__PATH__ + 'func_inicial_pt.mp3',
                __PATH__ + 'func_letras_pt.mp3',
                __PATH__ + 'func_silabas_pt.mp3',
                __PATH__ + 'func_palavras_pt.mp3',
                __PATH__ + 'func_sair_pt.mp3']

audio_option_exiting = [__PATH__ + 'func_inicial_saida_pt.mp3',
                        __PATH__ + 'func_letras_saida_pt.mp3',
                        __PATH__ + 'func_silabas_saida_pt.mp3',
                        __PATH__ + 'func_palavras_saida_pt.mp3']

audio_option_accessing = [' ',
                          __PATH__ + 'func_letras_entrada_pt.mp3',
                          __PATH__ + 'func_silabas_entrada_pt.mp3',
                          __PATH__ + 'func_palavras_entrada_pt.mp3']


def iterate():
    current = combobox.current()
    new = current + 1
    new = 0 if new == 5 else new
    combobox.current(new)
    file = audio_option[new]
    playsound.playsound(file)


def select():
    option = combobox.current()

    if option == 4:
        sair()
    else:
        notebook.select(option)
        playsound.playsound(audio_option_accessing[option])
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
                      'ABA DE PALAVRAS',
                      'SAIR')

combobox.pack(expand=1)

combobox.current(0)

# endregion

# region Aba de Letras


def letter(char):
    if char in alphabet:
        playsound.playsound(__PATH__ + char + '_pt.mp3')
    else:
        playsound.playsound(__PATH__ + 'NL_pt.mp3')
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
            playsound.playsound(__PATH__ + sy + '_pt.mp3')
        else:
            playsound.playsound(__PATH__ + 'NS_pt.mp3')
    elif size == 3:
        if sy[2] in vowel:
            if (sy[1] == 'H' and sy[0] in ['C', 'L', 'N']) or \
                    (sy[1] == 'L' and sy[0] in ['B', 'C', 'F', 'G', 'P', 'T', 'V']) or \
                    (sy[1] == 'R' and sy[0] in ['B', 'C', 'D', 'F', 'G', 'P', 'T']) or \
                    (sy[1] == 'U' and sy[0] in ['G', 'Q'] and sy[2] in ['A', 'E', 'I', 'O']):
                    playsound.playsound(__PATH__ + sy + '_pt.mp3')
            else:
                playsound.playsound(__PATH__ + 'NS_pt.mp3')
        else:
            playsound.playsound(__PATH__ + 'NS_pt.mp3')
    else:
        playsound.playsound(__PATH__ + 'NS_pt.mp3')
    sy_entry.set('')

sy_entry = tk.StringVar()
syl = tk.Entry(aba3, textvariable=sy_entry, font=f)
syl.pack(expand=1)

# endregion

# region Aba de Palavras


def say(msg):
    engine.say(msg)
    engine.runAndWait()

with open("pt-BR_out.dic", encoding='utf-8') as word_file:
    portuguese_words = set(word.strip().lower() for word in word_file)


def is_portuguese_word(word):
    return word.lower() in portuguese_words


def word():
    wo = wo_entry.get().lower()
    if wo != '':
        b = is_portuguese_word(wo)
        wo_file = __PATH__ + wo + '_pt.mp3'
        if b:
            if os.path.isfile(wo_file):
                playsound.playsound(wo_file)
            elif record(wo, 'pt'):
                playsound.playsound(wo_file)
            else:
                say(wo)
        else:
            playsound.playsound(__PATH__ + 'NW_pt.mp3')
    wo_entry.set('')

wo_entry = tk.StringVar()
wor = tk.Entry(aba4, textvariable=wo_entry, font=f)
wor.pack(expand=1)

# endregion

# region :: Binds


def key(event):
    char = event.char.upper()

    aba = notebook.index(notebook.select())

    if aba == 1 or aba == 2:
        letter(char)


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
    playsound.playsound(audio_option_exiting[combobox.current()])


# noinspection PyUnusedLocal
def space(event):
    aba = notebook.index(notebook.select())
    if aba == 0:
        iterate()
    else:
        escape()

window.bind('<space>', space)

window.bind_all('<Return>', enter)

window.bind_all('<Key>', key)

# endregion


# region :: Função Sair


def sair():
    window.destroy()

# endregion

window.mainloop()
