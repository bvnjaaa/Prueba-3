#Import ...

#Variables globales

lista = []



#Funciones

def guardar() :
    print("Leer datos y guardar")
    
    patente = input("Ingrese una patente (4 Letras y un Numero : Ejemplo XXZZ12): ")
    anio = int(input("Ingrese el año del Vehiculo"))
    
    #Opcion 1 : Crear una tupla
   # objeto = (patente,anio)
    # lista.append(objeto)
    
    #Opcion 2 : Crear un diccionario
    objeto = {'Patente' : patente, 'Año' : anio }
    lista.append(objeto)
#End def

def mostrar() :
    for cosa in lista :
        print(cosa)
    
def buscar() :
    print("Buscar un dato y mostrar")
    patente_buscada = input("Ingrese una patente para buscar (4 Letras y un Numero : Ejemplo XXZZ12): ")
    for cosa in lista :
        if cosa['Patente'] == patente_buscada :
            print(cosa)
            return
    print("No encontrada")    
#End def
def salir() :
    print("Chao")
#End def






#Principal
while True:
    #Mostrar opciones
    print('''
          1.-Guardar
          2.-Mostrar todos
          3.-Buscar Uno
          4.-Salir''')
    
    #Escoger una
    try:
        op = int(input("Ingrese una opcion : "))
    except:
        op = 0
        
    #Hacer algo
    if op < 1 or op > 3 :
        print("Opcion no valida")
    else:
        if op == 1 :
            guardar()
        elif op == 2 :
            mostrar()
        elif op == 3 :
            buscar()
        else:
            salir()
            break
        #End if
    #End if