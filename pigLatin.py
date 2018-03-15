# Translate to pig latin

lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
latinAdd = 'ay'
senToConvert = str(input('What would you like to convert to pig latin? '))

def convToPl(sentence):
    senList = sentence.split()
    vowels = ['a','e','i','o','u']
    plSen = []
    for word in senList:
        if word[0] in vowels:
            plSen.append(word + 'way')
        elif word[:2] in lst:
            plSen.append(word[2:] + word[:2] + latinAdd)
        else:
            plSen.append(word[1:] + word[:1] + latinAdd)
    print(' '.join(plSen))

convToPl(senToConvert)
