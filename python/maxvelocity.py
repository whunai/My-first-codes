carVelocity = input("")
maxVelocity = 80
measureUnit = "km/h"

def hasSingleComma(comma):
    return comma.count(',') == 1

symbols = tuple(chr(letters) for letters in range(32, 127) if not (48 <= letters <= 57 or 46 == letters or 44 == letters))

while True:
    if hasSingleComma(carVelocity):
        input("Para valores decimais, por favor utilize ponto ao invés de vírgula. Insira novamente a velocidade do veículo: ")

    elif float(carVelocity) > maxVelocity and float(carVelocity) < (maxVelocity + 11):
        print("Você recebeu uma multa leve")

    elif float(carVelocity) > (maxVelocity + 10) and float(carVelocity) < (maxVelocity + 21):
        print("Você recebeu uma multa grave")

    elif float(carVelocity) > (maxVelocity + 20):
        print("Você recebeu uma multa gravíssima")