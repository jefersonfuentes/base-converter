# Investigación de lógica para informáticos conversor de base hexadecimal a octal.

def header():
    '''Function that displays the program header and the names of the authors.'''
    print('''
______                                                _            
| ___ \                                              | |           
| |_/ / __ _ ___  ___    ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
| ___ \/ _` / __|/ _ \  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |_/ / (_| \__ \  __/ | (_| (_) | | | \ V /  __/ |  | ||  __/ |   
\____/ \__,_|___/\___|  \___\___/|_| |_|\_/ \___|_|   \__\___|_|   

Created by             

  <Jeferson Fuentes García C34044> <Nathaly Nuñez Ulate C35630> 
  <Verónica Aguero Aguilar C30084> <Jonaikel Arias Brenes C18855>                                             
    ''')


def hex_to_oct(hex_num):
    '''Function to convert hexadecimal to octal numbers without using python built-in functions'''

    # Diccionario que enlaza los hexadecimales con su valor en binario.
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Convertir el número hexadecimal a binario
    binary_num = ''
    for digit in hex_num:
        binary_num += hex_to_bin[digit]

    # Añadir ceros a la izquierda para que la longitud del binario sea múltiplo de 3
    while len(binary_num) % 3 != 0:
        binary_num = '0' + binary_num

    # Convertir el número binario a octal
    oct_num = ''
    i = 0
    while i < len(binary_num):
        oct_digit = binary_num[i:i + 3]
        oct_num += str(int(oct_digit, 2))
        i += 3

    return oct_num

# Encabezado del programa
header()

# Bucle principal para permitir múltiples conversiones
while True:
    hexadecimal = input("Ingresa un número hexadecimal (o escribe 'salir' para terminar): ")
    hexadecimal = hexadecimal.upper() # Formateo del string a mayúscula para evitar errores con el diccionario.
    
    # Comprobar si el usuario quiere salir del programa
    if hexadecimal == "SALIR":
        break

    # Validar el número hexadecimal ingresado
    valid_hex = all(c in '0123456789ABCDEF' for c in hexadecimal)
    if not valid_hex:
        print("\n¡Error! El número ingresado no es un número hexadecimal válido.\nLos dígitos válidos son: 0-9, A-F.\n")
        continue

    # Convertir el número hexadecimal a octal
    octal = hex_to_oct(hexadecimal)
    print('El número', hexadecimal, 'octal equivalente es:', octal)
    print()  # Línea en blanco para separar las conversiones

print("\nSalida exitosa!\n")    
