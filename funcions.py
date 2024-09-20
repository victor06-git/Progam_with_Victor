def calcul_trig(base, altura):
    return base * altura

area = calcul_trig(3, 4)
print(f"La base és: {area}")

def suma (num_1, num_2):
    suma = num_1 + num_2
    return suma

suma_num = suma(2, 3)
print(f"La suma és: {suma_num}")

#Exercici 3

def transformar_km_a_milles(kilom):
    kil_mill = kilom*0.62
    return kil_mill
def transformar_milles_a_km(mill):
    mill_kil = mill/0.62
    return mill_kil

kilom = input("Entra una distancia en kilòmetres: ") #Resultat en str
kilom = float(kilom) #Cambiar a int or float
mill = transformar_km_a_milles(kilom)
print(f"La distància {kilom:.3f} kilòmetres en milles és {mill:.3f}.")

milles = transformar_milles_a_km(mill)
print(f"El resultat de tornar a calcular els kilòmetres és : {milles:.3f}")

def operacions_aritmetiques(a, b):
    suma = a + b
    resta = a - b
    multiplicacio = a * b
    divisio = a / b
    return suma , resta, multiplicacio, divisio

def mostra_resultats(a, b, suma, resta, multiplicacio, divisio):
    print(f"{a} + {b} = {suma}, {a} - {b} = {resta}, {a} * {b} = {multiplicacio}, {a} / {b} = {divisio} ")
    return a, b, suma, resta, multiplicacio, divisio
     
a = 2
b = 4
suma, resta, multiplicacio, divisio = operacions_aritmetiques(a, b)
mostra_resultats(a, b, suma, resta, multiplicacio, divisio)

 