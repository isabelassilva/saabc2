
import tkinter as tk

from tkinter import ttk

import enchant

import os.path

import pyttsx3

from audio_generator import record

import vlc

# region :: init()

engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 50)

engine.setProperty('voice', 'brazil')

# endregion()

# region :: Configurações da Janela Principal

window = tk.Tk()

window.title("SAABC: Software de Auxílio à Alfabetização Braille para Crianças")

window.attributes('-zoomed', True)

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

audio_option = ['./mp3/func_inicial_pt.mp3',
                './mp3/func_letras_pt.mp3',
                './mp3/func_silabas_pt.mp3',
                './mp3/func_palavras_pt.mp3',
                './mp3/func_sair_pt.mp3']

audio_option_exiting = ['./mp3/func_inicial_saida_pt.mp3',
                        './mp3/func_letras_saida_pt.mp3',
                        './mp3/func_silabas_saida_pt.mp3',
                        './mp3/func_palavras_saida_pt.mp3']

audio_option_accessing = [' ',
                          './mp3/func_letras_entrada_pt.mp3',
                          './mp3/func_silabas_entrada_pt.mp3',
                          './mp3/func_palavras_entrada_pt.mp3']


def iterate():
    current = combobox.current()
    new = current + 1
    new = 0 if new == 5 else new
    combobox.current(new)
    global file
    file = audio_option[new]
    global track
    track.stop()
    track = vlc.MediaPlayer(file)
    track.play()


def select():
    option = combobox.current()

    if option == 0:
        welcome()
    elif option == 4:
        sair()
    else:
        notebook.select(option)
        global track
        track.stop()
        track = vlc.MediaPlayer(audio_option_accessing[option])
        track.play()
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

track = vlc.MediaPlayer('./mp3/A_pt.mp3')


def letter1(char):
    global track
    track.stop()
    if char in alphabet:
        track = vlc.MediaPlayer('./mp3/' + char + '_pt.mp3')
        track.play()
    else:
        track = vlc.MediaPlayer('./mp3/NL_pt.mp3')
        track.play()


# endregion

# region Aba de Sílabas

consonant = ['B', 'C', 'D', 'F', 'G', 'H',
             'J', 'L', 'M', 'N', 'P', 'Q',
             'R', 'S', 'T', 'V', 'X', 'Z']

special_consonant = ['K', 'W', 'Y']

vowel = ['A', 'E', 'I', 'O', 'U']

alphabet = consonant + special_consonant + vowel


def letter2(char):
    global track
    track.stop()
    if char in alphabet:
        track = vlc.MediaPlayer('./mp3/letra_' + char + '_pt.mp3')
        track.play()
    else:
        track = vlc.MediaPlayer('./mp3/NL_pt.mp3')
        track.play()
        g = sy_entry.get()
        sy_entry.set(g[:-1])


def syllable():
    global track
    track.stop()
    sy = sy_entry.get().upper()
    size = len(sy)
    if size == 2:
        if (sy[1] in vowel and (sy[0] in consonant and sy[0] not in ['Q'])) or \
                (sy[1] in ['M', 'N', 'L', 'R', 'S', 'Z'] and sy[0] in vowel):
            track = vlc.MediaPlayer('./mp3/' + sy + '_pt.mp3')
            track.play()
        else:
            track = vlc.MediaPlayer('./mp3/NS_pt.mp3')
            track.play()
    elif size == 3:
        if sy[2] in vowel:
            if (sy[1] == 'H' and sy[0] in ['C', 'L', 'N']) or \
                    (sy[1] == 'L' and sy[0] in ['B', 'C', 'F', 'G', 'P', 'T', 'V']) or \
                    (sy[1] == 'R' and sy[0] in ['B', 'C', 'D', 'F', 'G', 'P', 'T']) or \
                    (sy[1] == 'U' and sy[0] in ['G', 'Q'] and sy[2] in ['A', 'E', 'I', 'O']):
                    track = vlc.MediaPlayer('./mp3/' + sy + '_pt.mp3')
                    track.play()
            else:
                track = vlc.MediaPlayer('./mp3/NS_pt.mp3')
                track.play()
        else:
            track = vlc.MediaPlayer('./mp3/NS_pt.mp3')
            track.play()
    else:
        track = vlc.MediaPlayer('./mp3/NS_pt.mp3')
        track.play()
    sy_entry.set('')

sy_entry = tk.StringVar()
syl = tk.Entry(aba3, textvariable=sy_entry, font=f)
syl.pack(expand=1)

# endregion

# region Aba de Palavras


def letter3(char):
    global track
    track.stop()
    if char in alphabet:
        track = vlc.MediaPlayer('./mp3/letra_' + char + '_pt.mp3')
        track.play()
    else:
        track = vlc.MediaPlayer('./mp3/NL_pt.mp3')
        track.play()
        g = wo_entry.get()
        wo_entry.set(g[:-1])


def say(msg):
    engine.say(msg)
    engine.runAndWait()

dictionary = enchant.request_pwl_dict("pt-BR_out.dic")


def word():
    wo = wo_entry.get().lower()
    if wo != '':
        b = dictionary.check(wo)
        word_file = './mp3/' + wo + '_pt.mp3'
        global track
        track.stop()
        if b:
            if os.path.isfile(word_file):
                track = vlc.MediaPlayer(word_file)
                track.play()
            elif record(wo, 'pt'):
                track = vlc.MediaPlayer(word_file)
                track.play()
            else:
                say(wo)
        else:
            track = vlc.MediaPlayer('./mp3/NW_pt.mp3')
            track.play()

    wo_entry.set('')

wo_entry = tk.StringVar()
wor = tk.Entry(aba4, textvariable=wo_entry, font=f)
wor.pack(expand=1)

# endregion

# region :: Binds


def key(event):
    char = event.char.upper()

    aba = notebook.index(notebook.select())

    if aba == 1:
        letter1(char)
    elif aba == 2:
        letter2(char)
    elif aba == 3:
        letter3(char)


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
    global track
    track.stop()
    notebook.select(0)
    track = vlc.MediaPlayer(audio_option_exiting[combobox.current()])
    track.play()


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

# region :: Welcome

file = ' '


def welcome():
    global file
    file = './mp3/welcome.mp3'
    global track
    track.stop()
    track = vlc.MediaPlayer(file)
    track.play()

window.after(100, welcome)

# endregion

# region :: Função Sair


def sair():
    window.destroy()

# endregion

window.mainloop()
