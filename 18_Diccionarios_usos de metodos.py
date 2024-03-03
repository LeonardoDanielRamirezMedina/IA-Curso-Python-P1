#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#Se mostrará el uso de diferentes métodos aplicables en diccionarios

datosAlumno ={                  #creamos el diccionario datosAlumno 
    "nombre":"leonardo",
    "carrera":"mecatronica",
    "grado":"6",
    "grupo":"E1"
}

datosAlumno2 ={                  #creamos el diccionario datosAlumno2 
    "nombre":"daniel",
    "carrera":"mecatronica",
    "grado":"5",
    "grupo":"F1"
}

print("datosAlumno contiene",len(datosAlumno),"claves.") #se utiliza len sobre nuestra biblioteca parab contar el numero de claves que contiene
datosAlumno.pop("carrera")      #se usa pop() para eliminar una clave en especifico de la biblioteca
print("Biblioteca con una clave eliminada: ",datosAlumno)              #se muestran claves y valores

datosAlumno2.clear()        #se vacían todos los campos de la biblioteca
print("Biblioteca vaciada: ",datosAlumno2)         #se muestra la biblioteca vacia
                            #si se quiere eliminar por completo se usaría: del datosAlumno2

copiaBiblio = dict(datosAlumno) #se copia el contenido de una biblioteca y se guarda en una nueva usando dict()
print("Copia: ",copiaBiblio)    #se muestra la biblioteca con datos copiados

claves = ("nombre","carrera","grado","grupo")       #se almacenan las claves a usar en una lista
datosAlumno2 = dict.fromkeys(claves,"vacio")        #se le asignan claves y valores a la biblioteca usando dict.fromkeys()
print("Biblioteca modificada: ",datosAlumno2)     #se muestra la biblioteca modificada