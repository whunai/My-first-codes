# Biblioteca de aleatoriedade do Python sendo inportada
import random

randomValue = random.randint(1, 10) # Variável com valor aleatório no intervalo 1-10 sendo definida
guessedValue = input("Estou pensando em um número de 1 à 10, tente adivinhar qual é! Palpite: ") # Recebendo uma entrada para a variável guessedValue

# Detector de vírgulas 
def hasSingleComma(comma): # Definindo uma função que verifica se dentro de uma string genérica tem pelo menos 1 vírgula
    return comma.count(',') == 1 # Aqui o "return" retorna o valor para o código que chamou a função

# Detector de pontos
def hasSingleDot(dot): # "dot" e "comma" São strings genéricas que são substituídas pela string especificada quando a função é chamada
    return dot.count('.') == 1

# Detector de caracteres
letters = tuple(chr(letter) for letter in range(32, 127) if not (48 <= letter <= 57)) # Aqui a variável "letter" chama uma coleção por meio do for, exceto pelos valores de 48 pra cima e 57 pra baixo (que representam os números).
# O "chr(letter)" pega cada um desses números e converte num caractere ASCII e o tuple transforma a variável em uma tupla, fazendo uma lista com cada caractere separado invidualmente
def hasSingleSymbol(symbol):
    return symbol in letters # Aqui ele verifica a variável genérica e retorna um valor para o código que chamou a função caso a string possua algum desses caracteres.

# Detector de números
numbers = tuple(chr(numero) for numero in range(48, 58)) # Mesmo esquema da de cima, mas apenas com números
def hasSingleNumber(decimalScale):
    return decimalScale in numbers

while True:
    if hasSingleComma(guessedValue) or hasSingleDot(guessedValue):
        guessedValue = input("O valor inserido precisa ser inteiro. Por favor, tente novamente. Palpite: ") # Aqui eu verifico se o valor de entrada é ou não decimal, para uma mensagem dedicada só pra essa situação
    
    elif any(hasSingleSymbol(char) for char in guessedValue) or any(hasSingleSymbol(char) for char in guessedValue) and any(hasSingleNumber(char) for char in guessedValue):
        guessedValue = input("Valor inserido é inválido. Por favor, tente novamente. Palpite: ") # Aqui eu verifico se o valor de entrada é alfanumérico ou apenas alfa, independemente não será aceito nenhum dos dois
    
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) > 10 or int(guessedValue) < 0:
        guessedValue = input("O valor inserido deve respeitar o intervalo de 1 à 10. Por favor, tente novamente. Palpite: ")
        
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) == int(randomValue):
        print("Parabéns! Você acertou.")
        break
    
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) > int(randomValue):
        guessedValue = input("Muito alto! Tente novamente: ")
    
    elif guessedValue.isnumeric() and float(guessedValue).is_integer() == True and int(guessedValue) < int(randomValue):
        guessedValue = input("Muito baixo! Tente novamente: ")