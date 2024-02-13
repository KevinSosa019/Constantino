ordenes=[]
seguir=True    
numeroOrden=1


def validarReferencia(fechaClienteRetiroOrden):
    from datetime import datetime
    
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Solicitar al usuario que ingrese una fecha
    fechaRetiroOrden = datetime.strptime(fechaClienteRetiroOrden, "%Y-%m-%d")

    # Calcular la diferencia de fechas
    diferencia = fecha_actual-fechaRetiroOrden
    
    if 0<diferencia.days<=15:
        print("Su garantia aun esta Activa")
        referenciaOrden="Activa"
    else:
        print("Su garantia ya ha expirado XD")
        referenciaOrden="Desactivada"
    return referenciaOrden
            
while seguir:
    print("\n""Se iniciara a ingresar su orden para el taller de Reparaciones Electronicas: ")
    print("El numero de su Orden es: ["+str(numeroOrden)+"]")    
    fechaOrden=input("Ingrese la fecha de la Orden (YYYY-MM-DD): ")
    clienteOrden=input("Ingrese el nombre del cliente: ")
    fechaInicioReparacionOrden=input("ingrese la fecha de inicio de reparacion (YYYY-MM-DD): ")
    fechaOrdenListaOrden=input("La fecha de orden lista sera (YYYY-MM-DD):")
    fechaClienteRetiroOrden=input("La fecha del retiro del Cliente sera (YYYY-MM-DD): ")
   
    dicOrden={} 
    dicOrden["fecha"]=fechaOrden
    dicOrden["cliente"]=clienteOrden
    dicOrden["fecha de inicio de reparacio: "]=fechaInicioReparacionOrden
    dicOrden["fecha de orden lista"]=fechaOrdenListaOrden
    dicOrden["fecha cliente de retiro"]=fechaClienteRetiroOrden
 
    print("\n""Ingrese el tipo de Orden")
    print("1. Orden Normal")
    print("2. Orden Garantia")
    tipoOrden=int(input("Seleccione una opcion: "))
    if tipoOrden==1:
        precioOrden=input("Ingrese el Precio de la orden: ")
        dicOrden["precio"]=precioOrden
    elif tipoOrden==2:
        referenciaOrden=validarReferencia(fechaClienteRetiroOrden)
        dicOrden["referencia"] = referenciaOrden
        
    print("\n""Ingrese los Detalles de la Orden")
    descripcionOrden=input("Ingrese la descripcion de su vehiculo: ")
    fallaOrden=input("Ingrese la falla del vehiculo: ")
    reparadoOrden=input("Ingrese como se reparara el vehiculo: ")
    noReparadoOrden=input("Ingrese la razon porque no se reparo: ")
    tecnicoOrden=input("Ingrese el nombre del Tecnico: ")
    
    dicOrden["decripcion"]=descripcionOrden
    dicOrden["falla"]=fallaOrden
    dicOrden["reparado"]=reparadoOrden
    dicOrden["noReparado"]=noReparadoOrden
    dicOrden["tecnico"]=tecnicoOrden
       
    ordenes.append(dicOrden)
    
    print("\n""Informacion completa de las Ordenes")
    for orden in ordenes:
        print("\n""["+str(numeroOrden)+"]. Numero de Orden")
        print("Datos de la Orden")
        print("La fecha de la Orden es: "+fechaOrden)
        print("El nombre del Cliente es: "+clienteOrden)
        print("La fecha de inicio de reparacion es: "+fechaInicioReparacionOrden)
        print("La fecha que se completo la lista: "+fechaOrdenListaOrden)
        print("La fecha que retiro el cliente: "+fechaClienteRetiroOrden)
        if tipoOrden==1:
           print("El precio de la orden es: "+precioOrden+" Lps.")
        else:
            print("Estado de la garantia: "+referenciaOrden)
        print("\n""Datos del vehiculo")
        print("La descripcion del vehiculo: "+descripcionOrden)
        print("La falla del vehiculo es: "+fallaOrden)
        print("La reparacion del vehiculo es: "+reparadoOrden)
        print("La razon la cual no se reparo es: "+noReparadoOrden)
        print("El nombre del tecnico es: "+tecnicoOrden)
        print("-----------------------------------------------")

    
    salir=input("\n""Desea ingresar otra orden (Y/N): ""\n").lower
    if salir=="n":
        seguir=False
     
