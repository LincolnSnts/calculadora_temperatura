def converter_C_F(graus):
    temp_final = (9/5) * graus + 32
    print(f'{graus}°C = {temp_final:.2f}°F')

def converter_C_K(graus):
    temp_final = graus + 273.15
    print(f'{graus}°C = {temp_final:.2f}°K')

def converter_F_C(graus):
    temp_final = (5/9) * (graus - 32)
    print(f'{graus}°F = {temp_final:.2f}°C')

def converter_F_K(graus):
    temp_final = (5/9) * (graus - 32) + 273.15
    print(f'{graus}°F = {temp_final:.2f}°K')
    
def converter_K_C(graus):
    temp_final = graus - 273.15
    print(f'{graus}°K = {temp_final:.2f}°C')

def converter_K_F(graus):
    temp_final = (9/5) * (graus - 273.15) + 32
    print(f'{graus}°K = {temp_final:.2f}°F')

#Inicio da Main

while True:
    try:
        temperatura = float(input('Digite uma temperatura: '))
    except ValueError:
        print('Essa não é uma temperatura válida!')
        continue
    tipo_origem = input('Digite a unidade de medida de origem (C/F/K) ->').upper()
    tipo_destino = input('Digite a unidade de medida de destino (C/F/K) ->').upper()

    if tipo_origem == 'C':
        if tipo_destino == 'F':
            converter_C_F(temperatura)
        elif tipo_destino == 'K':
            converter_C_K(temperatura)
        elif tipo_destino == 'C':
            print('A temperatura já está em Celsius!')
            continue
        else:
            print('Digite unidades de medida válidas!')
            continue

    elif tipo_origem == 'F':
        if tipo_destino == 'C':
            converter_F_C(temperatura)
        elif tipo_destino == 'K':
            converter_F_K(temperatura)
        elif tipo_destino == 'F':
            print('A temperatura já está em Fahrenheit!')
        else:
            print('Digite unidades de medida válidas!')
            continue

    elif tipo_origem == 'K':
        if tipo_destino == 'C':
            converter_K_C(temperatura)
        elif tipo_destino == 'F':
            converter_K_F(temperatura)
        elif tipo_destino == 'K':
            print('A temperatura já está em Kelvin!')
        else:
            print('Digite unidades de medida válidas!')
            continue
    
    else:
        print('Selecione uma opção válida! (C/F/K)')
        continue

    repetir = input('Deseja converter outra temperatura? (S/N) ->').upper()
    if repetir == 'S':
        continue
    else:
        break

print('Fim do programa!')