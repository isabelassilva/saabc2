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

vowel_ = {'A': 'a',
          'E': 'é',
          'I': 'i',
          'O': 'ó',
          'U': 'u'}

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
    # region Functions Exiting
    if not os.path.isfile(__PATH__ + 'aba_letras_saida_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Saída da Aba de Letras', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_letras_saida_' + __LANGUAGE__ + '.mp3')
    if not os.path.isfile(__PATH__ + 'aba_silabas_saida_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Saída da Aba de Sílabas', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_silabas_saida_' + __LANGUAGE__ + '.mp3')
    if not os.path.isfile(__PATH__ + 'aba_palavras_saida_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Saída da Aba de Palavras', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'aba_palavras_saida_' + __LANGUAGE__ + '.mp3')

    # region Syllable: start with Consonant, size 2
    consonant1 = consonant
    consonant1.remove('Q')
    for L1 in consonant1:
        for L2 in vowel:
            if not os.path.isfile(__PATH__ + L1 + L2 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=L1 + ' mais ' + vowel_[L2] + ' é igual a ' + L1.lower() + vowel_[L2], lang=__LANGUAGE__)
                tts.save(__PATH__ + L1 + L2 + '_' + __LANGUAGE__ + '.mp3')

    # region Syllable: start with Vowel, size 2
    for L1 in vowel:
        for L2 in ['M', 'N', 'L', 'R', 'S', 'Z']:
            if not os.path.isfile(__PATH__ + L1 + L2 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=vowel_[L1] + ' mais ' + L2 + ' é igual a ' + vowel_[L1] + L2.lower(), lang=__LANGUAGE__)
                tts.save(__PATH__ + L1 + L2 + '_' + __LANGUAGE__ + '.mp3')
    # region Syllable: start with Consonant, size 2
        for L2 in ['C', 'L', 'N']:
            if not os.path.isfile(__PATH__ + L2 + 'H' + L1 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=L2 + ' mais H, mais ' + vowel_[L1] + '. É igual a. ' + L2.lower() + 'h' + vowel_[L1], lang=__LANGUAGE__)
                tts.save(__PATH__ + L2 + 'H' + L1 + '_' + __LANGUAGE__ + '.mp3')
    # region Syllable: size 3
        for L2 in ['B', 'C', 'F', 'G', 'P', 'T', 'V']:
            if not os.path.isfile(__PATH__ + L2 + 'L' + L1 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=L2 + '. mais L. mais ' + vowel_[L1] + '. É igual a. ' + L2.lower() + 'l' + vowel_[L1], lang=__LANGUAGE__)
                tts.save(__PATH__ + L2 + 'L' + L1 + '_' + __LANGUAGE__ + '.mp3')
        for L2 in ['B', 'C', 'D', 'F', 'G', 'P', 'T']:
            if not os.path.isfile(__PATH__ + L2 + 'R' + L1 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=L2 + '. mais R. mais ' + vowel_[L1] + '. É igual a. ' + L2.lower() + 'r' + vowel_[L1],
                           lang=__LANGUAGE__)
                tts.save(__PATH__ + L2 + 'R' + L1 + '_' + __LANGUAGE__ + '.mp3')
    vowel1 = vowel
    vowel1.remove('U')
    for L1 in vowel1:
        for L2 in ['G', 'Q']:
            if not os.path.isfile(__PATH__ + L2 + 'U' + L1 + '_' + __LANGUAGE__ + '.mp3'):
                tts = gTTS(text=L2 + '. mais U. mais ' + vowel_[L1] + '. É igual a. ' + L2.lower() + 'u' + vowel_[L1],
                           lang=__LANGUAGE__)
                tts.save(__PATH__ + L2 + 'U' + L1 + '_' + __LANGUAGE__ + '.mp3')

    # region Non Syllable
    if not os.path.isfile(__PATH__ + 'NS_' + __LANGUAGE__ + '.mp3'):
        tts = gTTS(text='Não é uma sílaba', lang=__LANGUAGE__)
        tts.save(__PATH__ + 'NS_' + __LANGUAGE__ + '.mp3')

else:
    print('This procedure requires internet connection')
