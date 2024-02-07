def menu():
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Buscar carrera")
    print("6. Salir")
    
def agregar(nombre):
    dicCarrera = {}
    dicCarrera = {"carrera": nombre, "clases": []}
    alterarClases=input("Desea ingresar clases(Y/N): ")
        
    while alterarClases == "Y" or alterarClases=="y":
       nombreClase = input("Nombre de la clase: ")
       dicCarrera["clases"].append(nombreClase)
       alterarClases = input("Desea ingresar otra clase (Y/N): ")
    carreras.append(dicCarrera)
    print("Creacion de Carrera y clases satisfactoriamente ")
             
def leer():
    print("Leer (mostrar) carreras")
    for carrera in carreras:
       print("- Nombre :" + carrera["carrera"])

def actualizar(carreraActualizar,nuevoValor):
    indice = 0
    for carrera in carreras:
       if carrera["carrera"] == carreraActualizar:
          carrera["carrera"] = nuevoValor
          
def borrar(carreraBorrar):
    indice = 0
    encontrado = False
    for carrera in carreras:
       if carrera["carrera"] == carreraBorrar:
          encontrado = True
          break
       else :
          indice = indice + 1

    if encontrado :
       carreras.remove(carreras[indice])
       print("Elemento borrado")
    else:
       print("No existe")    
       
def buscar(buscarCarrera):
        indice=0
        alterar=""
        noEncontrado=False
        
        for carrera in carreras:
          if carrera['carrera']== buscarCarrera:  
              print("Se ha encontrado la carrera satisfactoriamente")
              
              alterar=input("Desea alterar la carrera? Y/N: ")   
                
              if alterar=="Y" or alterar=="y":
              
                 carreraActualizar=input("Ingrese nuevo nombre de la carrera: ")
                 indice=0
                 for carrera in carreras:
                   if carrera["carrera"] ==buscarCarrera:
                       carrera["carrera"]=carreraActualizar
                       
              elif alterar=="N" or alterar=="n":
                 print("Esta bien")
                 break
           
              else:
                 print("Debe de ser Y/N no otra palabra o letra")    
                 break
              
          else:
              indice = indice + 1
              noEncontrado=True
          
        if noEncontrado:   
          print('No se ha encontrado la carrera')
      

            
carreras = []
seguir = True

while seguir:
    print(carreras)
    menu()
    opcion = int(input("Ingrese su opcion: "))
    print("----------------------------------")
    
    if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre : ")
        agregar(nombre)
     
    elif opcion == 2:
        leer()
                    
    elif opcion == 3:
        carreraActualizar = input("Ingrese nombre de la carrera : ")
        nuevoValor = input("Ingrese nuevo nombre de la carrera : ")
        actualizar(carreraActualizar,nuevoValor)
                
    elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera: ")
        borrar(carreraBorrar)

    elif opcion == 5:        
        buscarCarrera=input("Ingrese la carrera ha buscar: ")
        buscar(buscarCarrera)
        
    elif opcion == 6:
        print("Hasta la proxima")
        seguir = False
        
    print("----------------------------------")
