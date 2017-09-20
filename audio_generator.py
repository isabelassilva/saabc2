import urllib.request

from gtts import gTTS
import os.path


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError:
        return False

__LANGUAGE__ = 'pt'
__LETTER__ = 'Letra'
__DOT__ = 'ponto'
__AND__ = 'e'

consonant = ['B', 'C', 'D', 'F', 'G', 'H',
             'J', 'L', 'M', 'N', 'P', 'Q',
             'R', 'S', 'T', 'V', 'X', 'Z']

special_consonant = ['K', 'W', 'Y']

vowel = ['A', 'E', 'I', 'O', 'U']

__PATH__ = './mp3/'

braille = {'A': __LETTER__ + ' a. ' + __DOT__ + ' 1.',
           'B': __LETTER__ + ' b. ' + __DOT__ + 's 1 ' + __AND__ + ' 2.',
           'C': __LETTER__ + ' c. ' + __DOT__ + 's 1 ' + __AND__ + ' 4.',
           'D': __LETTER__ + ' d. ' + __DOT__ + 's 1, 4 ' + __AND__ + ' 5.',
           'E': __LETTER__ + ' é. ' + __DOT__ + 's 1 ' + __AND__ + ' 5.',
           'F': __LETTER__ + ' f. ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 4.',
           'G': __LETTER__ + ' g. ' + __DOT__ + 's 1, 2, 4 ' + __AND__ + ' 5.',
           'H': __LETTER__ + ' h. ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 5.',
           'I': __LETTER__ + ' i. ' + __DOT__ + 's 2 ' + __AND__ + ' 4.',
           'J': __LETTER__ + ' j. ' + __DOT__ + 's 2, 4 ' + __AND__ + ' 5.',
           'K': __LETTER__ + ' k. ' + __DOT__ + 's 1 ' + __AND__ + ' 3.',
           'L': __LETTER__ + ' l. ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 3.',
           'M': __LETTER__ + ' m. ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 4.',
           'N': __LETTER__ + ' n. ' + __DOT__ + 's 1, 3, 4 ' + __AND__ + ' 5.',
           'O': __LETTER__ + ' ó. ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 5.',
           'P': __LETTER__ + ' p. ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 4.',
           'Q': __LETTER__ + ' q. ' + __DOT__ + 's 1, 2, 3, 4 ' + __AND__ + ' 5.',
           'R': __LETTER__ + ' r. ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 5.',
           'S': __LETTER__ + ' s. ' + __DOT__ + 's 2, 3 ' + __AND__ + ' 4.',
           'T': __LETTER__ + ' t. ' + __DOT__ + 's 2, 3, 4 ' + __AND__ + ' 5.',
           'U': __LETTER__ + ' u. ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 6.',
           'V': __LETTER__ + ' v. ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 6.',
           'W': __LETTER__ + ' w. ' + __DOT__ + 's 2, 4, 5 ' + __AND__ + ' 6.',
           'X': __LETTER__ + ' x. ' + __DOT__ + 's 1, 3, 4 ' + __AND__ + ' 6.',
           'Y': __LETTER__ + ' y. ' + __DOT__ + 's 1, 3, 4, 5 ' + __AND__ + ' 6.',
           'Z': __LETTER__ + ' z. ' + __DOT__ + 's 1, 3, 5 ' + __AND__ + ' 6.',
           }


if internet_on():
    # region Letters
    for letter in consonant + special_consonant + vowel:
        if not os.path.isfile(__PATH__ + letter + '_' + __LANGUAGE__ + '.mp3'):
            tts = gTTS(text=braille[letter], lang=__LANGUAGE__)
            tts.save(__PATH__ + letter + '_' + __LANGUAGE__ + '.mp3')
    # region Non Letter
    if not os.path.isfile(__PATH__ + 'NL_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Esta tecla não é uma letra.', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'NL_' + __LANGUAGE__ + '.mp3')
    # region Combobox Options
    if not os.path.isfile(__PATH__ + 'aba_inicial_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Aba Inicial', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_inicial_' + __LANGUAGE__ + '.mp3')
    if not os.path.isfile(__PATH__ + 'aba_letras_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Aba de Letras', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_letras_' + __LANGUAGE__ + '.mp3')
    if not os.path.isfile(__PATH__ + 'aba_silabas_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Aba de Sílabas', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_silabas_' + __LANGUAGE__ + '.mp3')
    if not os.path.isfile(__PATH__ + 'aba_palavras_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Aba de Palavras', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_palavras_' + __LANGUAGE__ + '.mp3')

else:
    print('This procedure requires internet connection')
