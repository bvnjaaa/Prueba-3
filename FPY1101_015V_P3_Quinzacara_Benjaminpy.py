import os
os.system("cls")

Personas = []

#Definir funciones

def grabar_datos() :
    
    
    
    nif = input("Ingrese su Numero de Identificacion Fiscal (NIF) Ejemplo(12345678-XXX) : ")
    if len(nif) != 12 :
        print("NIF Invalido")
        return
            
            
    
    while True:
        nombre = input("Ingrese su nombre : ")
        validar = nombre.replace(" ", "")
        if len(validar) >= 8:
            break
        
    try:
        edad = int(input("Ingrese su edad porfavor : "))
    except:
        edad = 0
    if edad < 0 or edad == 0 :
        print("La edad debe ser igual o mayor a 0")
    
    persona = {
        'Nif' : nif,
        'Nombre' : nombre,
        'Edad' : edad
    }
    Personas.append(persona)
    print("Persona Grabada Muchas Gracias")
    
#end def

def buscar_persona() :
    persona_buscada = input("Ingrese el Numero de Identificacion Fiscal (NIF) de la persona a buscar : ")
    
            
    for numero_nif in Personas :
        if numero_nif["Nif"] == persona_buscada :
            print(numero_nif)
        else :
            print("Persona no encontrada")
        
        if persona_buscada in "sp" or "SP" :
            print("Persona Española")
        else:
            print("Persona Europea")
         
        
        
    
#end def

def imprimir_certificado() :
    try:
        valor_certificado1 = int(input("Ingrese un valor para el certificado de Nacimiento : "))
    except:
        valor_certificado1 = 0
    if valor_certificado1 < 1500 and valor_certificado1 > 5000 :
                print("Valor Invalido. Ingrese un valor entre 1500 y 5000")
    try:
        valor_certificado2 = int(input("Ingrese un valor para el certificado de estado conyugal : "))
    except:
        valor_certificado2 = 0
    if valor_certificado2 < 1500 and valor_certificado2 > 5000 :
                print("Valor Invalido. Ingrese un valor entre 1500 y 5000")
    try:
        valor_certificado3 = int(input("Ingrese un valor para el certificado de pertenencia a la union europea : "))
    except:
        valor_certificado3 = 0
    if valor_certificado3 < 1500 and valor_certificado3 > 5000 :
                print("Valor Invalido. Ingrese un valor entre 1500 y 5000")
    print('''
          Opciones:
          1.- Imprimir Certificado de Nacimiento
          2.- Imprimir Certificado de estado conyugal
          3. Imprimir Cerificado de pertenencia a la union europea
          ''')
    try:
        op = int(input("Ingrese una opcion : "))
    except:
        op = 0
        
    if op < 1 or op > 3 :
        print("Opcion Invalida")
    else:
        if op == 1:
            persona_buscada = input("Ingrese el Numero de Identificacion Fiscal (NIF) de la persona para imprimir certificado de nacimiento :" )
            for numero_nif in Personas :
                if numero_nif["Nif"] == persona_buscada :
                    print("Certificado de Nacimiento")
                    print(numero_nif)
                    print("Valor del certificado")
                    print(valor_certificado1)
                
        elif op == 2 :
            persona_buscada = input("Ingrese el Numero de Identificacion Fiscal (NIF) de la persona para imprimir certificado de estado conyugal :" )
            for numero_nif in Personas :
                if numero_nif["Nif"] == persona_buscada :
                    print("Certificado de Estado Conyugal")
                    print(numero_nif)
                    print("Valor del certificado")
                    print(valor_certificado2)
               
        elif op == 3 :
            persona_buscada = input("Ingrese el Numero de Identificacion Fiscal (NIF) de la persona para imprimir certificado de pertenencia a la union europea :" )
            for numero_nif in Personas :
                if numero_nif["Nif"] == persona_buscada :
                    print("Certificado de Pertenencia a la Union Europea")
                    print(numero_nif)
                    print("Valor del certificado")
                    print(valor_certificado3)
                
    
#end def

def salir() :
    print("Byee, Benjamin Quinzacara")
    print("Version del programa 2024")
    print("***")
    False
#end def

#Principal

while True :
    #Mostrar Opciones
    print('''
          Opciones:
          1.- Grabar Datos
          2.- Buscar una persona
          3. Imprimir Certificado
          4. Salir
          
          ''')
    #Escoger una opcion
    try:
        op = int(input("Ingrese una opcion : "))
    except:
        op = 0
    
    if op < 1 or op > 3 :
        print("Ingrese una Opcion Valida")
    else:
        if op == 1 :
            grabar_datos()
        elif op == 2 :
            buscar_persona()
        elif op == 3 :
            imprimir_certificado()
        elif op == 4 :
            salir()
        #End if
    #End if
#End while