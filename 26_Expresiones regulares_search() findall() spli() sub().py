#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

import re       #este modulo nos permitira usar métodos para encontrar coincidencias quee specifiquemos dentro de variables

mensaje="Buscar una o mas coincidencias en este mensaje para comprobar los metodos"     #se declara el string en el que buscaremos
busca = re.search("este",mensaje)                   #el metodo re.search() nos sirve para encontrar una unica coincidencia dentro de la variable
print("Resultado de coincidencia:",busca)       #se imprime el resultado de la busqueda

busca= re.findall("a",mensaje)                  #el método findall() nos muestra todas las coincidencias encontradas dentro del string
print("\nCoincidencias encontradas:",busca)       #se muestran las coincidencias

busca = re.split(" ",mensaje)           #el método split() excluye todas las coincidencias y separa el resto del string con comas
print("\nString con caracteres excluidos y separado:",busca)                    #se imrpime el string separado por comas y excluyendo espacios

busca = re.sub(" "," --X-- ",mensaje,5)     #sub() suistituye todas las coincidencias en el string con lo que le especifiquemos, el 5 es para indicar la cantidad de veces que queremos que haga esto
print("\nString con datos sustituidos:",busca)            #se imprime el resultado sustituyendo lo indicado