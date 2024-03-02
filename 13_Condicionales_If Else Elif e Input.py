#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este código se explicará el uso de los condicionales if, else y elif

print("Consulta de fecha para selección de servicio social: \nLase fechas para seleccion de servicio son las siguientes:\n")    #Se muestra encabezado
print("91 a 100 --- 10 de Marzo\n81 a 90 --- 11 de Marzo\n71 a 80 --- 12 de Marzo\n60 a 70 ---13 de Marzo\n")   #Se muestra tabal de fechas
promedio = int(input("Ingrese su pormedio:\t"))     #por medio de int(input()) se pide que ingrese un dato tipo entero que se guardará en promedio

if promedio < 0 or promedio >100:       #Se inicia con el if para el caso de que promedio sea mayor a 100 o menor a 0
    print("Promedio no válido")             #Si se cumple el if entonces se muestra este mensaje    
elif promedio <= 100 and promedio >=91:                              #condicion para promedios de 91 a 100
    print("Tu fecha para elegir servicio social es: 10 de Marzo")           #si se cumple esta condición para la variable promedio se muestra el mensaje
elif promedio <= 90 and promedio >=81:                               #condicion para promedios de 81 a 90
    print("Tu fecha para elegir servicio social es: 11 de Marzo")
elif promedio <= 80 and promedio >=71:                               #condicion para promedios de 71 a 80
    print("Tu fecha para elegir servicio social es: 12 de Marzo")
elif promedio <= 70 and promedio >=60:                               #condicion para promedios de 60 a 70
    print("Tu fecha para elegir servicio social es: 13 de Marzo")
else:                                                                   #condicion en caso que no se cumpla ninguno de los anteriores
    print("No puedes inscribirte al servicio social con un promedio menor a 60")