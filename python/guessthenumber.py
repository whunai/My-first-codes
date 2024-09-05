import random

randomValue = random.randint(1, 10) 
guessedValue = input("Estou pensando em um número de 1 à 10, tente adivinhar qual é! Palpite: ") 

def hasSingleComma(comma):
    return comma.count(',') == 1

def hasSingleDot(dot):
    return dot.count('.') == 1

letters = tuple(chr(letter) for letter in range(32, 127) if not (48 <= letter <= 57 or letter in {44, 45, 46}))
def hasSingleSymbol(symbol):
    return symbol in letters

numbers = tuple(chr(numero) for numero in range(48, 58))
def hasSingleNumber(decimalScale):
    return decimalScale in numbers

while True:
    if any(hasSingleSymbol(char) for char in guessedValue) == False and hasSingleComma(guessedValue) and any(hasSingleNumber(char) for char in guessedValue) or any(hasSingleSymbol(char) for char in guessedValue) == False and hasSingleDot(guessedValue) and any(hasSingleNumber(char) for char in guessedValue):
        guessedValue = input("O valor inserido precisa ser inteiro. Por favor, tente novamente. Palpite: ") 
    elif any(hasSingleSymbol(char) for char in guessedValue) or any(hasSingleSymbol(char) for char in guessedValue) and any(hasSingleNumber(char) for char in guessedValue):
        guessedValue = input("Valor inserido é inválido. Por favor, tente novamente. Palpite: ")
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) > 10 or int(guessedValue) < 0:
        guessedValue = input("O valor inserido deve respeitar o intervalo de 1 à 10. Por favor, tente novamente. Palpite: ")
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) == int(randomValue):
        print("Parabéns! Você acertou.")
        break
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) > int(randomValue):
        guessedValue = input("Muito alto! Tente novamente: ")
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) < int(randomValue):
        guessedValue = input("Muito baixo! Tente novamente: ")