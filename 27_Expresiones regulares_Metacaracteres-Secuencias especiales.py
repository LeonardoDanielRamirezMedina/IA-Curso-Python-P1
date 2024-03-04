#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#-----SECUENCIAS ESPECIALES------

import re       #se importa el modulo re para utilizar sus metodos

texto="este texto va a ser utilizado para comprobar diferentes metodos 1 2 3" #se declara string con la que comprobaremos los metodos
buscar = re.findall("\Aeste",texto)                                           #se utiliza \A para buscar coincidencias solo al inicio del string
if buscar:
    print("Se encontró una coincidencia al inicio del string: ",buscar)       #se imprime si hay coincidencias
else:
    print("No hay coincidencias al inicio del texto")                         #Se imprime si no hay coincidencias

buscar = re.findall("\D",texto)                                               #se utiliza \D para omitir todos los numeros y mostrar las letras
print("Caracteres que no son numeros: ",buscar)                                                                 #se muestran las letras omitiendo numeros

#-----METACARACTERES-------
texto2= "palo pala pelo"
buscar = re.findall("p.l.",texto2)        #se utiliza para buscar coincidencias aceptando los puntos por cualquier caracter en el string
print("Coincidencias:",buscar)                                    #imprime coincidencias

buscar = re.findall("palo|pelo",texto2)        # se utiliza || para establecer una o mas palabras para buscar coincidencias
print("Coincidencias:",buscar)                              #imprime coincidencias

buscar = re.findall("[a-m]",texto2)        #se utiliza [] para bucar caracteres especificos o un rango de caracteres con coincidencias
print("Coincidencias:",buscar)                                   #imprime coincidencias