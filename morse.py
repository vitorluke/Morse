from time import sleep
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', ' ': '/ '}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char
    return morse_code.rstrip()

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in MORSE_CODE_DICT.values():
            text += [char for char, morse in MORSE_CODE_DICT.items() if morse == code][0]
        elif code == '/':
            text += ' '
        else:
            text += code
    return text
print('---Conversor Morse---')
print()
input('Aperte ENTER para continuar')
print()
sleep(1)
print('Para converter texto para morse digite 1')
print()
sleep(1)
print('Para converter morse para texto digite 2')
print()
x = input('= ')
listazinha = [1,2]
while x not in listazinha:
    x = int(input('= '))
if x == 1:
    texto_original = input('Digite o texto: ')
    print()
    print('Convertendo...')
    sleep(3)
    codigo_morse = text_to_morse(texto_original)
    print(codigo_morse)
else:
    texto_original = input('Digite o código: ')
    texto_convertido = morse_to_text(texto_original)
    print()
    print('Convertendo')
    sleep(3)
    print(texto_convertido)
