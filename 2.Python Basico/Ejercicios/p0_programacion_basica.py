#Lenguajes compilados: requiere de un compilador (otro programa) para que el programa escrito pueda ejecutarse, de tal manera que arroje un archivo con un lenguaje que el computador pueda interpretarlo (codigo binario). Java C C#.

#Lenguajes interpretados: programa que traduce linea por linea a lenguaje maquina y el tiempo de ejecucion es mas lento pero es multiplataforma. php, ruby, python


#Distintas formas de realizar un comentario

# print("hello world")
# print('hello world')
print('''hello world''')
# print("""hello world""")

#Variables
CONSTANTE = "Soy una constante"
tutor = "Codi"
print(tutor)
print('Estoy sumando textos: '+CONSTANTE+","+tutor)

#No se puede utilizar las sgtes palabras por que son reservadas. false, else, if, etc.
#https://www.programiz.com/python-programming/keyword-list

print('Asignacion de variables')
valor1, valor2, valor3 = 10, "Codi", 10 * 20
print(valor1)
print(valor2)
print(valor3)

#OPERADORES DE COMPARACION
# > , < , >= , <= , == , != 
#-> ejemplo
variable1 = 10
variable2 = 20
menor_igual =  variable1 < variable2 #TRUE
print(menor_igual) #resultado -> true

#Podemos verificar si dos variables son iguales con IS
igual_is = variable1 is variable2
print(igual_is) #resultado true or falso, en este caso es FALSE

#OPERADORES LOGICOS
result_end = True and menor_igual #TRUE
result_end2 = False or menor_igual #TRUE
print(result_end) #resulta true ya que es necesario que ambos valores sean true.
print(result_end2) #resulta true ya que es necesario que ambos valores sean false para resultar false.

#Entrada de datos
# SHIFT+ALT+A = COMENTAR BLOQUES
# CTRL + } = COMETAR LINEA

nombre=input("Cual es tu nombre?\n")
edad=int(input("Cual es tu edad?\n"))
peso=float(input("Cual es tu peso?\n"))
autorizado=input("Estas autorizado?(si/no)\n")

flagAdvice=False
while flagAdvice!=True:

    booleanWork = True
    flagWork = False

    while flagWork != True:
        varWork=input("Estas trabajando?(si/no)\n")

        if varWork.upper() == "SI":
            booleanWork=True
            flagWork=True
        elif  varWork.upper() =="NO":
            booleanWork=False
            flagWork=True
        else:
            print("Dato ingresado es incorrecto")

    booleanStudy = True
    flagStudy = False

    while flagStudy != True:
        varWork=input("Estas estudiando?(si/no)\n")

        if varWork.upper() == "SI":
            booleanStudy=True
            flagStudy=True
        elif  varWork.upper() =="NO":
            booleanStudy=False
            flagStudy=True
        else:
            print("Dato ingresado es incorrecto")

    booleanResult_and = booleanStudy and booleanWork
    booleanResult_or = booleanStudy or booleanWork

    if booleanResult_and == True:
        print("Eres muy empeñoso, trabajas y estudias a la vez, enhorabuena")
    elif booleanResult_or == False:
        print("Por favor has algo por la vida, no te quedes sentado")
    elif booleanStudy == False:
        print("Si trabajas, ahorra y paga algun estudio que te servira para mejorar")
    else:
        print("Si estudias, empieza a buscar un trabajo, es el tiempo de hacerlo")

    flagAdvice2=False
    while flagAdvice2 != True:
        varAdvice=input("Quieres salir del programa?(si/no)\n")

        if varAdvice.upper() == "SI":
            flagAdvice=True
            flagAdvice2=True
        elif  varAdvice.upper() =="NO":
            flagAdvice=False
            flagAdvice2=True
        else:
            print("Dato ingresado es incorrecto")


# Formato para imprimir
print("Hola {}, tienes {} años y tu peso es {}\n¿Estas autorizado? {}".format(nombre,edad,peso,autorizado))
print("Autorizado", autorizado)

"""
Este es un comentario
en parrafo.
"""

#Lista: permite almacenar cualquier valor (int,float,string)
lista = ["Eduardo",23,True,19.5] #tamaño de 4 -> lista=[0,1,2,3]
cursos=["python","django","flask","c","c++","c#","java","php","sql"]
print('Ejm: [start:end:step]')
print(cursos[3:8:2]) 
print('Ejm: [:]')
print(lista[:]) 
print('Ejm: [start:]') 
print(cursos[2:]) 
print('Ejm: [:end]')
print(cursos[:3]) 

lista2 = [8.17, 90, 50, 1, 1.32]
print('lista2.sort(reverse=True) ordena descendentemente')
lista2.sort(reverse=True)
print(lista2[:]) 
print("El menor numero de mi lista es {} y el mayor es {}".format(min(lista2),max(lista2)))
print("La longitud de la lista es: {}".format(len(lista2)))

#capturar indice en la lista
valor=1.32
print("El indice de valor {} en la lista es {}".format(valor,lista2.index(valor)))
#lista2.count():para saber la cantidad de veces que se ha repetido un valor 
#lista.append():agrega un elemento al final
#lista.insert(index,elemento): inserta en el indice dado y corre los demas valores.
#lista.remove(elemento): elimana el primer elemento que encuentra - elemento-> input var
#return_value = languages.pop(3) elimina elemento con index 3 y returna, si no hay index, default -1.
#lista.clear() deja empty o vacia la lista
#list.reverse() voltea la lista.
#lista1.extend(list2): agrega todos los elementos de la lista2 al final de la lista1

#language list es una colección ordenada y modificable. Permite miembros duplicados. Entre corchetes
print('Language_lista')
language = ['French', 'English', 'German']
print(language[:])

print('Agrege el idioma Arabic')
language.append('Arabic')
# language.pop(2) Eliminar elemento de indice 2

print('Imprimiendo los elementos de la lista con un FOR')
for elemento in language:
    print(elemento)

# language tuple: colección ordenada e inmutable, se escriben entre parentesis. Permite miembros duplicados.
print('Language_tupla')
language_tuple = ('Spanish', 'Portuguese')
print(language_tuple[:])

print('Reasignar valores de una tupla')
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Funciones son iguales a métodos, la diferencia que las funciones dentro de una clase se le conoce como métodos, ahora las variables dentro de una clase se le conoce como propiedades.
# ___Propiedades que aplican a tuplas:
# len
# max
# min
# sum
# any
# all
# sorted
# ______Métodos que aplican a tuplas:
# index
# count

# language set: coleccion o conjunto que no esta ordenado ni indexado. No hay miembros duplicados.
print('Language_set')
language_set = {'Chinese', 'Japanese'}
print(language_set)

# Dictionary es una colección desordenada, modificable e indexada. No hay miembros duplicados.
# Operaciones:
# .keys() —> Retorna la clave de nuestro elemento
# .values()—> Retorna una lista de elementos (valores del diccionario)
# .items() —> Devuelve lista de tuplas (primero la clave y luego el valor)
# .clear() —> Elimina todos los items del diccionario
# .pop(“n”) —> Elimina el elemento ingresado
print('Imprimir Diccionario')
thisdict = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964,
    "costo": 24000,
    "made in": "Italy"
    }
print('thisdict.keys()')
print(thisdict.keys())
print('thisdict.values()')
print(thisdict.values())
print('thisdict.items()')
print(thisdict.items())

print(thisdict)
print('Imprimir Diccionario.model')
print(thisdict["model"])

# Language_lista with/extend language_tuple
language.extend(language_tuple)
print('Language_lista with/extend language_tuple')
print(language[:])
# Language_lista with/extend language_set
language.extend(language_set)
print('Language_lista with/extend language_set')
print(language[:])

#matrices
fila1 = [10,20]
fila2 = [30,40]
matriz = [fila1,fila2]
print('Imprimir Matriz')
print(matriz)

#tuplas: no se pueden modificar los elementos que almacena. Estas son mas rapidas para las consultas.
#tuple -> () ; list -> []
mi_tupla = (1,2,3,4,5,6,7,8,9,0)
lista = [10,20,30,40,50,60,70,80,90]
tupla = (100,200,300,400,500,600)
print(mi_tupla[:4:2])
uno, dos, *tres, cero = mi_tupla
# Ejemplo: primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]
#primero, segundo, *_, ultimo = tupla (obtener 1°,2° y ultimo elemento)
print("{}\n{}\n{}\n{}".format(uno,dos,tres,cero))
print(list(zip(mi_tupla,lista,tupla))) #list
print(tuple(zip(mi_tupla,lista,tupla))) #tuple


# METODOS:

# variable.upper() = 'todos los caracteres en MAYÚSCULAS'
# variable.capitalize() = 'solo la primera en MAYÚSCULA'
# variable.lower() = 'todos los caracteres en minúscula'
# variable.strip() = 'eliminar espacios basura del string'
# variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter

# FUNCIONES BILT IN

# aquellas que son propias del lenguaje y que no tenemos que crearlas, solo invocarlas.
# nombre[i]: mostrar letra alojada en el indice i de la palabra
# len()
# print()
# input()

# nombre[start,end,step] ejemplo nombre[::-1] (orden inverso)
