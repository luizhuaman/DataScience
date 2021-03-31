def exchanges(moneda,equivalencia,cantidad):
    result = 0
    # Moneda chilena
    if moneda == 1:
        result = round(float(cantidad * equivalencia),2)
        print(f'Los {cantidad} pesos chilenos equivalen a {result} dolares')
    # Moneda colombiana
    elif moneda == 2:
        result = round(float(cantidad * equivalencia),2)
        print(f'Los {cantidad} pesos colombianos equivalen a {result} dolares')
    # Moneda Argentina
    elif moneda == 3:
        result = round(float(cantidad * equivalencia),2)
        print(f'Los {cantidad} pesos argentinos equivalen a {result} dolares')
    # Moneda mexicana
    elif moneda == 4:
        result = round(float(cantidad * equivalencia),2)
        print(f'Los {cantidad} pesos mexicanos equivalen a {result} dolares')
    # Moneda Peruana
    elif moneda == 5:
        result = cantidad * equivalencia
        print(f'Los {cantidad} soles equivalen a {result} dolares')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')

def logica():
    punto_salida = 0
    while True:
        try:
            while True:
                moneda = int(input('''
                Ingresa el indice de la moneda que quieres convertira  dolar:
                    [1] Moneda chilena a Dolar
                    [2] Moneda colombiana a Dolar
                    [3] Moneda argentida a Dolar
                    [4] Moneda mexicana a Dolar
                    [5] Moneda Peru a Dolar
                    [0] Salir
                Selecciona: '''))
                print('********************************')
                if(moneda >= 0 and moneda <= 5):
                    break;
            if (moneda == 0):
                print ('Bye bye, te esperamos pronto')
                punto_salida = 1
            else:
                cantidad = round(float(input('Ingresa el monto a convertir en dolares:')),2)
                equivalencia = round(float(input('Ingresa el tipo de cambio: ')),2)
                exchanges(moneda,equivalencia,cantidad)
              
        except:
            print('* * * * * * E R R O R * * * * * *')
            print('Por favor, Ingresa solo valores numericos')
        if(punto_salida == 1):
            break;
        
if __name__ == '__main__':
    try:
        logica()
    except:
        logica()