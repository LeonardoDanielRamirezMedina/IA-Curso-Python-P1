#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

dato=0      #Se declara variable global

def operacion():
    x=2     #variable local de la funcuión
    global y    #De esta manera la variable local "y" se convierte en global
    y=3     #variable local
    dato=x+y    #se guarda en una variable global
    print("Resultado:",dato)

operacion()         #se llama a la función operacion
print("Valore de y:",y)    #la variable "y" se puede usar fuera de la función donde se declara ya que la hicimos global
