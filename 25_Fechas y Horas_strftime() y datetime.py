#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#---Se mostrará como trabajar con fechas y horas----

import datetime     #modulo que nos permite trabajar con fechas y horas
import locale       #modulo que nos permite trabajar con fechas y horas mostradas en diferentes formatos
locale.setlocale(locale.LC_ALL, "es-ES")        #se utiliza para mostrar fechass del modulo locale en español

#-------USO DE datetime------

date= datetime.datetime.now()   #guardamos en una variable la fecha y hora actual gracias a datetime.now() gracias al modulo datetime
print("Fecha:",date)    #se imprime fecha y hora actual

date= datetime.datetime(2023,3,3,18,20)   #se adignan poarametros personalizados
print(date)     #se imrpime fecha personalizada


date= datetime.datetime.now()   #se guarda la fecha actual en la variable date
print("Año:",date.year,"Mes:",date.month,"Dia:",date.day)       #imprimimos unicamente año, mes y dia

#-------USO DE locale------
#Algunos de los usos de este modulo son:

print(date.strftime("Día: %A "))        #se usa el metodo strftime() y %A para mostrar el dia de la semana con letras
print(date.strftime("Fecha: %c "))          #se usa el metodo strftime() y %c la fecha y hora -- Dia/Mes/Año Hora:min:seg
print(date.strftime("Día/Mes/año: %D "))        #se usa el metodo strftime() y %D para mostrar la fecha en formato Dia/Mes/Año
