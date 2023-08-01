phrase = str(input('Digite uma frase: '))

phrase_lower = phrase.lower()

def remove(phrase_lower):
    return phrase_lower.replace(' ', '')

def inverse(phrase_lower):
    return phrase_lower[::-1]


if remove(phrase_lower) == remove(inverse(phrase_lower)):
    print('A frase "{}" forma um políndromo.'.format(phrase_lower))
else:
    print('Não é um políndromo.')







