# Fatorial de um número

ChosenValue = input("Insira aqui o número que você deseja encontrar o valor fatorial: ")

total = 1

def hasSingleComma(comma):
    return comma.count(',') == 1

def hasSingleDot(dot):
    return dot.count('.') == 1

letters = tuple(chr(letter) for letter in range(32, 127) if not (48 <= letter <= 57 or letter in {44, 45, 46}))
def hasSingleSymbol(symbol):
    return symbol in letters

numbers = tuple(chr(numero) for numero in range(48, 58)) # Mesmo esquema da de cima, mas apenas com números
def hasSingleNumber(decimalScale):
    return decimalScale in numbers

while True:
    if any(hasSingleSymbol(char) for char in ChosenValue) == False and hasSingleComma(ChosenValue) and any(hasSingleNumber(char) for char in ChosenValue) or any(hasSingleSymbol(char) for char in ChosenValue) == False and hasSingleDot(ChosenValue) and any(hasSingleNumber(char) for char in ChosenValue):
        ChosenValue = input("O valor inserido precisa ser inteiro. Por favor, insira novamente o número para descobrir seu fatorial: ")
    
    elif any(hasSingleSymbol(char) for char in ChosenValue) or any(hasSingleSymbol(char) for char in ChosenValue) and any(hasSingleNumber(char) for char in ChosenValue):
        ChosenValue = input("Valor inserido é inválido. Por favor, insira novamente o número para descobrir seu fatorial: ")
    
    elif ChosenValue.isnumeric() and float(ChosenValue).is_integer() == True and int(ChosenValue) >= 0:
        for multiplier in range(1, int(ChosenValue) + 1):
            total = total * multiplier
        print("O fatorial de "+ChosenValue+" é "+str(total)+".")
        break
    elif int(ChosenValue) < 0:
        ChosenValue = input("Não há fatorial de valores negativos. Por favor, insira novamente o número para descobrir seu fatorial: ")
    else:
        ChosenValue = input("Valor inserido é inválido. Por favor, insira novamente o número para descobrir seu fatorial: ")