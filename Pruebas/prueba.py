pais = "Argentina"
print(pais)
#asi se puede comentar tambien
dia = input ("ingrese un dia: ")
numero = int(input("ingrese un numero: "))
suma = 2+ numero
print(suma)
print("hola, ha ingresado el dia: ", dia, "y el numero: ", numero,"y todo suma: ", suma)

saludo = "Hola_Mundo"
print(saludo[3::3])

print(pais.index("e", 0))

print(pais*3)
print(len(pais))
print(min(pais))
print(max(pais))
print(pais.upper())
print(pais.lower())
print(pais.strip())
print(pais.replace("a", "A"))

frase= "esto es una prueba de strings en esto que es python"

print(frase.find("prueba"))
print(frase.count("esto"))

lista = [1,2,3,4,5]
print(lista)
lista.append(6)
print(lista)
lista.remove(2)
print(lista)
print(lista.pop())
lista.sort()
print(lista)

diccionario={
    "numero": 1,
    "pais": "Argentina",
    "ciudad": "Buenos Aires"
}

print(diccionario)
print(diccionario["pais"])
print("aca imprimo keys ", diccionario.keys())
print("aca imprimo values ", diccionario.values())

diccionario["pais"] = "Uruguay"
print(diccionario)
print(diccionario["pais"])