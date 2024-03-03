#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#Se explicará el uso de los diccionarios y como emplear el bucle for en ellos

datosAlumno ={                  #se crea el diccionario datosAlumno con sus claves y valores
    "nombre":"leonardo",
    "carrera":"mecatronica",
    "grado":"6",
    "grupo":"E1"
}
print(datosAlumno)                  #se imprime el contenido del diccionario como aparece en el codigo
mostrar = datosAlumno["nombre"]         #se muestra solo el valor que contiene la clave nombre
print("\nSe muestra un dato especifico: "+mostrar,"\n")     #se imprime

datosAlumno["Registro"]="21310138"          #de esta manera se puede agragar una clave con su rerspectivo valor en la biblioteca

for x,y in datosAlumno.items():         #se utiliza el for para mostrar las claves y valores del diccionario usando el metodo items()
    print(x+": "+y+".")                 #se imprimen los datos y se le da formato

