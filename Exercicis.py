import math

# Conversió de graus Celsius a Fahrenheit
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
def celsius_a_fahrenheit(celsius):
    Fahrenheit = (celsius * 9/5) + 32
    return Fahrenheit

# Conversió de graus Fahrenheit a Celsius
# Fórmula: Celsius = (Fahrenheit - 32) * 5/9
def fahrenheit_a_celsius(fahrenheit):
    Celsius = (fahrenheit - 32) * 5/9
    return Celsius

# Calcula l'Índex de Massa Corporal (IMC)
# Fórmula: IMC = pes / (altura ** 2)
def calcular_imc(pes, altura):
    imc = pes / (altura ** 2)
    return imc

# Calcula la hipotenusa d'un triangle rectangle
# Utilitza el teorema de Pitàgores: hipotenusa = sqrt(catet1^2 + catet2^2)
def calcular_hipotenusa(catet1, catet2):
    hipotenusa = math.sqrt(catet1^2 + catet2^2)
    return hipotenusa

# Comprova si un nombre és parell
# Per fer-ho, fem nombre % 2 i retornem si el resultat és 0
def es_parell(nombre):
    nombre_parell = nombre % 2 == 0
    return nombre_parell

# Calcula l'àrea d'un cercle donat el radi
# Fórmula: Àrea = π * radi^2
def area_cercle(radi):
    area = math.pi * radi ** 2
    return area

# Converteix minuts a hores i minuts
# Divideix minuts entre 60 per obtenir les hores i els minuts restants
def minuts_a_hores_minuts(minuts):
    hores = minuts // 60
    minuts_rest = minuts % 60
    return hores, minuts_rest

# Calcula el perímetre i l'àrea d'un rectangle
# Perímetre = 2 * (llargada + amplada)
# Àrea = llargada * amplada
def perimetre_i_area_rectangle(llargada, amplada):
    perimetre = 2 * (llargada + amplada)
    area = llargada * amplada
    return perimetre, area

# Calcula el preu final després d'un descompte percentual
# Preu final = preu inicial - (preu inicial * descompte_percent / 100)
def preu_final(preu_inicial, descompte_percent):
    preu = preu_inicial - (preu_inicial * descompte_percent / 100)
    return preu

# Calcula l'interès simple
# Fórmula: Interès = capital * (taxa / 100) * temps
def interes_simple(capital, taxa, temps):
    interes = capital * (taxa / 100) * temps
    return interes

# Converteix velocitat de km/h a m/s
# Fórmula: m/s = km/h * 1000 / 3600
def kmh_a_ms(velocitat_kmh):
    m_s = velocitat_kmh * 1000 / 3600
    return m_s

# Exercici 1
# Fes un programa amb una variable que tingui el següent text: "La programació és com l'art de resoldre problemes"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La subcadena 'art' en majúscules
# * Les lletres inicials de cada paraula concatenades en una cadena
# * La frase completa en majúscules i després en minúscules
# * La frase invertida paraula per paraula
def exercici1():
    
    frase = "La programació és com l'art de resoldre problemes"
    
    llargada = len(frase)
    print("La llargada de la frase:", llargada)
    
    subcadena_art = 'art'.upper()
    print("La subcadena 'art' en majúscules:", subcadena_art)
    
    inicials = ''.join([word[0] for word in frase.split()])
    print("Inicials de cada paraula:", inicials)
    
    frase_majuscules = frase.upper()
    frase_minuscules = frase.lower()
    print("La frase en majúscules és:", frase_majuscules)
    print("La frase en minúscules és:", frase_minuscules)
    
    frase_invertida = ' '.join(frase.split()[::-1])
    print("La frase invertida paraula per paraula és:", frase_invertida)

# Exercici 2
# Fes un programa amb una variable que tingui el següent text: "Python és un llenguatge de programació potent i versàtil"
# Després manipula aquest text per aconseguir mostrar:
# * La posició de la paraula 'programació' dins la frase
# * Les paraules 'Python' i 'potent' concatenades en una sola paraula sense espais
# * La subcadena que comprèn des de 'un' fins a 'potent'
# * La frase amb totes les vocals reemplaçades per '*'
# * La frase amb la primera lletra de cada paraula en majúscula

# Fes servir ''.join(['*' if c in vocals else c for c in frase]) per canviar les vocals per '*'

def exercici2():
    text = "Python és un llenguatge de programació potent i versàtil"

    position_word = text.find("programació")
    print(f"La posició de la paraula 'programació' es troba: {position_word}")

    words = text.split()
    words_pyt_pot = words[0] + words[6]
    print(f"Les paraules 'Python'y 'potent' concatenades sense espais: {words_pyt_pot}")

    word_un = text.find('un')
    word_pot = text.find('potent') + len('potent')
    subcadena = text[word_un:word_pot]
    print(f"La subcadena de 'un' a 'potent':{subcadena}")

    vocals = "aeiouàèìòùáéíóúAEIOUÀÈÌÒÙÁÉÍÓÚ"
    sense_vocals = ''.join(['*' if c in vocals else c for c in text])
    print(f"Frase amb totes les vocals reemplaçades per '*': {sense_vocals}")

    text_majúscula = text.title()
    print("Frase amb la primera lletra de cada paraula en majúscula:", text_majúscula)



# Exercici 3
# Fes un programa amb una variable que tingui el següent text: "Aprendre a programar és com aprendre un nou idioma"
# Després manipula aquest text per aconseguir mostrar:
# * El nombre de vegades que apareix la paraula 'aprendre'
# * La frase amb la paraula 'idioma' reemplaçada per 'superpoder'
# * Les tres primeres paraules de la frase
# * La frase amb les paraules en ordre invers
# * La frase original però sense espais

def exercici3():
    text = "Aprendre a programar és com aprendre un nou idioma"
    
    
    minusculas = text.lower()
    vegades = minusculas.count('aprendre')
    print("El nombre de vegades que apareix 'aprendre':", vegades)
    
    idiom_super = text.replace('idioma', 'superpoder')
    print("Frase amb 'idioma' reemplaçat per 'superpoder':", idiom_super)
    
    first_three = ' '.join(text.split()[0:3])
    print("Les tres primeres paraules del text:", first_three)
    
    inversa = ' '.join(text.split()[::-1])
    print("Frase amb paraules en ordre invers:", inversa)
    
    sense_espais = text.replace(' ', '')
    print("La frase original sense espais:", sense_espais)


# Exercici 4
# Fes un programa amb una variable que tingui el següent text: "El coneixement és poder"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La paraula 'poder' en majúscules
# * La frase repetida tres vegades amb un espai entre elles
# * La frase amb les vocals eliminades
# * La posició de la primera 'e' i de la darrera 'e' en la frase

def exercici4():
    text = "El coneixement és poder"

    llargada = len(text)
    print("La llargada de la frase:", llargada)
    
    poder_majuscules = 'poder'.upper()
    print("La paraula 'poder' en majúscules:", poder_majuscules)
    
    text_repetit = (text + ' ') * 2 + text
    print("Frase repetida tres vegades:", text_repetit)
    
    vocals = "aeiouàèìòùáéíóúAEIOUÀÈÌÒÙÁÉÍÓÚ"
    sense_vocals = ''.join([c for c in text if c not in vocals])
    print("Frase sense vocals:", sense_vocals)
    
    position_first_e = text.find('e')
    position_last_e = text.rfind('e')
    print("Posició de la primera 'e':", position_first_e)
    print("Posició de la darrera 'e':", position_last_e)

# Exercici 5
# Fes un programa amb una variable que tingui el següent text: "La pràctica fa el mestre"
# Després manipula aquest text per aconseguir mostrar:
# * La frase amb cada paraula separada per un guió '-'
# * La frase amb l'ordre de les lletres de cada paraula invertit
# * La subcadena des del tercer fins al desè caràcter
# * La frase amb totes les consonants en majúscules i les vocals en minúscules
# * El nombre total de lletres sense comptar els espais

def exercici5():
    text = "La pràctica fa el mestre"
    
    text_dividit = text.split()
    amb_guions = '-'.join(text_dividit)
    print("Frase amb paraules separades per guions:", amb_guions)
    
    paraules_invertides = ' '.join([paraula[::-1] for paraula in text.split()])
    print("Las lletres de cada paraula invertides:", paraules_invertides)
    
    subcadena = text[2:11]
    print("Subcadena del tercer al desè caràcter:", subcadena)
    
    vocals = 'aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ'
    frase_transformada = ''.join([c.lower() if c in vocals else c.upper() for c in text]) #totes les vocals minusculas i els demés caràcters en majúsculas
    print("Consonants en majúscules i vocals en minúscules:", frase_transformada)
    
    # El nombre total de lletres sense comptar els espais
    sense_espais = text.replace(' ', '')
    total_lletres = len(sense_espais)
    print("Nombre total de lletres sense espais:", total_lletres)


# Exercici 6
# Fes un programa amb una variable que tingui el següent text: "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense espais al principi ni al final
# * La frase amb un ample total de 80 caràcters, centrada, omplint amb '-'
# * La frase amb un ample total de 80 caràcters, alineada a l'esquerra, omplint amb '*'
# * La frase amb un ample total de 80 caràcters, alineada a la dreta, omplint amb '.'
# * La llargada de la frase original i de la frase després d'aplicar strip()

def exercici6():
    text = "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
    
    sense_espais = text.strip()
    print("Frase sense espais al principi ni al final:", sense_espais)
    
    text_center = sense_espais.center(80, '-')
    print("Frase centrada amb ample 80:", text_center)
    
    text_left = sense_espais.ljust(80, '*')
    print("La frase alineada a l'esquerra amb ample 80:", text_left)
    
    text_right = sense_espais.rjust(80, '.')
    print("La frase alineada a la dreta amb ample 80:", text_right)
    
    llargada_original = len(text)
    llargada_dividit = len(sense_espais)
    print("La llargada original:", llargada_original)
    print("La llargada després d'aplicar strip():", llargada_dividit)

# Exercici 7
# Fes un programa amb una variable que tingui el següent text: "****Benvinguts al curs de Python****"
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense els asteriscs del principi i del final
# * La frase sense els asteriscs només del principi
# * La frase sense els asteriscs només del final
# * La frase amb un ample total de 50 caràcters, centrada
# * La frase amb un ample total de 50 caràcters, alineada a la dreta

def exercici7():
    text = "****Benvinguts al curs de Python****"

    sense_asteriscs = text.strip('*') 
    print("La frase sense '*':", sense_asteriscs)

    left_asteriscs = text.lstrip('*')
    print("La frase sense els asteriscs del principi:" , left_asteriscs)

    right_asteriscs = text.rstrip('*')
    print("La frase sense el asteriscs de l'esquerre:" , right_asteriscs)

    text_center = text.center(50)
    print("La frase centrada amb 50 un total de 50 caràcters:" ,text_center)

    text_right = text.rjust(50)
    print("La frase alineada a la dreta amb un total de 50 caràcters:" , text_right)

# Exercici 8
# Fes un programa amb una variable que tingui el següent text: "    Python és genial    "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original amb els espais del principi eliminats
# * La frase original amb els espais del final eliminats
# * La frase amb un ample total de 30 caràcters, alineada a l'esquerra, omplint amb '-'
# * La frase amb un ample total de 30 caràcters, alineada a la dreta, omplint amb '+'
# * La frase amb un ample total de 30 caràcters, centrada, omplint amb '*'

def exercici8():
    frase = "    Python és genial    "
    
    frase_1 = frase.lstrip()
    print("Frase amb espais eliminats del principi:", frase_1)
    
    frase_2 = frase.rstrip()
    print("Frase amb espais eliminats del final:", frase_2)
    
    frase_3 = frase.strip()
    frase_3_definitiva = frase_3.ljust(30, '-')
    print("Frase alineada a l'esquerra amb ample 30 amb - :", frase_3_definitiva)
    
    frase_4 = frase.strip()
    frase_4_definitiva = frase_4.rjust(30, '+')
    print("Frase alineada a la dreta amb ample 30 amb + :", frase_4_definitiva)
    
    frase_5 = frase.strip()
    frase_5_definitiva = frase_5.center(30, '*')
    print("Frase centrada amb ample 30 amb * :", frase_5_definitiva)

# Exercici 9
# Crea un programa que mostri un menú tipus:
# *********************************Menú Principal*********************************
#             1. Veure perfil                         4. Configuració             
#          2. Canviar contrasenya                         5. Ajuda                
#                3. Sortir                            6. Tancar sessió  
# Sense utilitzar bucles 'for' ni 'while', i fent servir les funcions ljust, center, rjust, etc.
# El programa ha de mostrar el menú amb dues columnes d'opcions una al costat de l'altra.

def exercici9():
    titol = "Menú Principal"
    titol_menú = titol.center(80, '*')
    primer = "1. Veure perfil"
    segon = "2. Canviar contrasenya"
    tercer = "3. Sortir"
    quart = "4. Configuració"
    cinqué = "5. Ajuda"
    sisé = "6. Tancar sessió"
    
    first = primer.center(40)
    second = quart.center(40)
    third = segon.center(40)
    fourth = cinqué.center(40)
    fifth = tercer.center(40)
    sixth = sisé.center(40)
    
    fila1 = first + second
    fila2 = third + fourth
    fila3 = fifth + sixth
    print(titol_menú)
    print(fila1)
    print(fila2)
    print(fila3)