# Fatorial de um número

ChosenValue = input('Insira aqui o número que você deseja encontrar o valor fatorial: ')

total = 1

def hasSingleComma(comma):
    return comma.count(',') == 1

if str(ChosenValue).isalpha():
    print("Valor inserido é inválido.")

elif hasSingleComma(ChosenValue):
    print("Não há fatorial de valores decimais.")

elif ChosenValue.isnumeric() and float(ChosenValue).is_integer() == True:
    if int(ChosenValue) >= 0:
        for multiplier in range(1, int(ChosenValue) + 1):
            total = total * multiplier
        print("O fatorial de "+ChosenValue+" é "+str(total)+".")
    elif int(ChosenValue) < 0:
        print("Não há fatorial de números negativos.")
elif float(ChosenValue).is_integer() == False:
    print("Não há fatorial de valores decimais.")
else:
    print("Valor inserido é inválido.")