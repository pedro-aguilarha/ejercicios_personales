#importaciones y  modulos
import os

#declaracion de variables
mtzArticulos=[]
mtzMateriales=[]
mtzPVenta = []  #saldos presupuesto venta
mtzPProduccion=[]
mtzUnidadesProducir=[]
mtzRequerimientoTotal=[]
mtzPRMateriales=[]
mtzPCMateriales=[]
mtzPManoObraDirecta=[]
dicArticulos = dict(CodArticulo="",NomArticulo="")
dicArticulos["CodArticulo"] = "1"
dicArticulos["NomArticulo"] = "CL"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "2"
dicArticulos["NomArticulo"] = "CE"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "3"
dicArticulos["NomArticulo"] = "CR"
mtzArticulos.append(dicArticulos.copy())

dictMateriales= dict(Codigo="",Nombre="")
dictMateriales["Codigo"]="1"
dictMateriales["Nombre"]="MaterialA"
mtzMateriales.append(dictMateriales.copy())

dictMateriales["Codigo"]="2"
dictMateriales["Nombre"]="MaterialB"
mtzMateriales.append(dictMateriales.copy())

dictMateriales["Codigo"]="3"
dictMateriales["Nombre"]="MaterialC"
mtzMateriales.append(dictMateriales.copy())
Total2016ventas = 0
def Main():
    while True:
        os.system("cls")
        print("== SISTEMA DE CONTABILIDAD FACPYA ==\n")
        print("-"*40)
        print("1.Ventas\n2.Flujo de Entradas\n3.Produccion\n4.Requerimiento de Materiales\n5.Compra de Materiales\n6.Flujo de Salidas")
        print("7.Mano de Obra Directa\n8.Gastos Indirectos de Fabricación\n9.Gastos de Operacion\n10.Costo Unitario de Productos Terminados\n11.Valucacion de Inventarios Finales\n12.Salir del Sistema")
        print("-"*40)
        opcion= input("ingresa la opcion deseada: ")

        if opcion=="1":
            PresupuestoVentas()
        elif opcion=="2":
            while True:
                os.system("cls")
                print("== DETERMINACION DEL SALDO DE CLIENTES Y FLUJO DE ENTRADAS ==")
                print("1.- Agregar información del flujo")
                print("2.- Mostrar Reporte de saldo clientes y flujo de ventas")
                print("3.- Regresar al Menú principal")
                opcion_fe= input("Ingrese una opcion: ")
                if opcion_fe == "1":
                    TOTAL = Total2016ventas
                    SaldoClientes2015 = int(input("Dame el saldo de clientes al 31-Diciembre-2015: "))
                    while True:
                        try:
                            porcentaje2015 = float(input("\nCuanto porcentaje se cobro del 2015? (EN DECIMAL): "))
                            porcentaje2016 = float(input("\nCuanto porcentaje se cobro del 2016? (EN DECIMAL): "))
                            TotalClientes2016 = float(SaldoClientes2015+TOTAL)
                            TotalEntradas2016 = float((SaldoClientes2015*porcentaje2015)+(TOTAL*porcentaje2016))
                            SaldoClientes2016 = float(TotalClientes2016 - TotalEntradas2016)
                            break
                        except :
                            os.system("cls")
                            input("INGRESE CORRECTAMENTE LOS DATOS EN DECIMAL\nPULSA ENTER PARA CONTINUAR...")

                elif opcion_fe =="2":
                    try:
                        print(f"        DESCRIPCION           |      IMPORTE    |    TOTAL   ")
                        print(f"Saldo de clientes 31-Dic-2015 |                 | {SaldoClientes2015}")
                        print(f"Ventas 2016                   |                 | {TOTAL}")
                        print(f"TOTAL CLIENTES 2016           |                 | {(TotalClientes2016)}")
                        print(f"ENTRADAS DE EFECTIVO:         |                 |")
                        print(f"Por cobranza 2015             |  {SaldoClientes2015*porcentaje2015}          | %{porcentaje2015}")
                        print(f"Por cobranza 2016             |  {TOTAL*porcentaje2016}             | %{porcentaje2016}")
                        print(f"Total entradas 2016           |                 | {TotalEntradas2016}")
                        print(f"SALDO CLIENTES 2016           |                 | {SaldoClientes2016}")
                        input("\nPresiona enter para continuar...")
                    except:
                        os.system("cls")
                        print("¡¡Primero debe Ingresar los Valores en ''1- Agregar informacion del flujo''!!")
                        input("Presiona enter para continuar...")

                elif opcion_fe =="3":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")


        elif opcion=="3":
            Presupuesto_Produccion()
        elif opcion=="4":
            PresupuestoRMateriales()
        elif opcion=="5":
            PresupuestoCMateriales()
        elif opcion=="6":
            while True:
                os.system("cls")
                print("== DETERMINACION DEL SALDO DE PROVEEDORES Y FLUJO DE SALIDAS ==")
                print("1.- Agregar información del flujo")
                print("2.- Mostrar Reporte de saldo proveedores y flujo de salidas")
                print("3.- Regresar al Menú principal")
                opcion_fe= input("Ingrese una opcion: ")
                if opcion_fe == "1":
                    #calcular las compras de 2016
                    Semestre1=0
                    Semestre2=0
                    for diccionario in mtzPCMateriales:
                        if diccionario["Semestre"]==1:
                            Semestre1 += diccionario["ImporteTotal"]
                        else:
                            Semestre2 += diccionario["ImporteTotal"]
                    Compras2016= Semestre1+ Semestre2
                    SaldoProveedores31Dic2015= float(input("Ingresa el Saldo de Proveedores del 31 de Dic de 2015: "))
                    TotalProveedores2016= float(Compras2016+SaldoProveedores31Dic2015)
                    SalidasProveedor2015= Compras2016
                    SalidasProveedor2016= Compras2016 * .60
                    TotalSalidas2016= float(SalidasProveedor2015 + SalidasProveedor2016)
                    SaldoProveedores2016= float(TotalProveedores2016-TotalSalidas2016)
                elif opcion_fe =="2":
                    try:
                        print(f"        DESCRIPCION              |      IMPORTE    |    TOTAL   ")
                        print(f"Saldo de proveedores 31-Dic-2015 |                 | {SaldoProveedores31Dic2015}")
                        print(f"Compras 2016                     |                 | {Compras2016}")
                        print("\nSALIDAS DE EFECTIVO")
                        print(f"Por Proveedores del 2015         | {SalidasProveedor2015}             | %100")
                        print(f"Por Proveedores del 2016         | {SalidasProveedor2016}             | %60")
                        print(f"TOTAL DE SALIDAS                 |                 | {TotalSalidas2016}")
                        print(f"Saldo de Proveedores del 2016    |                 | {SaldoProveedores2016}")

                        input("\nPresiona enter para continuar...")
                    except:
                        os.system("cls")
                        print("¡¡Primero debe Ingresar los Valores en ''1- Agregar informacion del flujo''!!")
                        input("Presiona enter para continuar...")

                elif opcion_fe =="3":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")
        elif opcion=="7":
            PresupuestoManoObraDirecta()
        elif opcion=="12":
            break
        else:
            input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")



def PresupuestoVentas():
    #declaracion de variables
    lstValArticulo = []
    global mtzPVenta
    global Total2016ventas
    dicPVenta = dict(CodArticulo="", UndVender = 0, PVenta = 0, Semestre = 0,ImporteVenta=0 )

    while True:
        os.system("cls")
        print("\n== PRESUPUESTO DE VENTA ==")
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de venta")
        print("3.- Regresar al Menú principal")
        opcion_pv= input("Ingrese una opcion: ")
        print(opcion_pv)
        if opcion_pv== "1":
            while True:
                os.system("cls")
                print("==Catálogo de artículos==")
                for Diccionario in mtzArticulos: #imprimir opciones
                    print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                    lstValArticulo.append(Diccionario["CodArticulo"])
                print("4 - Regresar a Menu Presupuesto de Ventas")
                Opcion= input("ingresa la opcion deseada: ")
                if(Opcion in lstValArticulo):

                    for Cont in range(0,2):
                        for Campo in dicPVenta:
                            if(Campo == "CodArticulo"):
                                dicPVenta[Campo] = Opcion
                            elif(Campo == "Semestre"):
                                dicPVenta[Campo] = (Cont + 1)
                            elif Campo != "ImporteVenta":
                                dicPVenta[Campo] = float(input("Ingresa la cantidad de " + Campo + " para el " + str(Cont + 1) + "° semestre: "))

                        print(" ")
                        dicPVenta["ImporteVenta"]= (dicPVenta["UndVender"] * dicPVenta["PVenta"])
                        mtzPVenta.append(dicPVenta.copy())
                elif Opcion=="4":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

        elif opcion_pv=="2": #reporte
            os.system("cls")
            print("--REPORTE PRESUPUESTO DE VENTAS--")
            for dicc in mtzPVenta:
                if dicc["CodArticulo"]== "1":
                    print("-"*50 )
                    print( "CODIGO: 1   |   PRODUCTO: CL    |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nPRECIO DE VENTA :"+str(dicc["PVenta"])+"\nIMPORTE :"+str(dicc["ImporteVenta"]))
                elif dicc["CodArticulo"]== "2":
                    print("-"*50 )
                    print( "CODIGO: 2  |   PRODUCTO: CE   |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nPRECIO DE VENTA :"+str(dicc["PVenta"])+"\nIMPORTE :"+str(dicc["ImporteVenta"]))
                else:
                    print("-"*50 )
                    print( "CODIGO: 3  |   PRODUCTO: CR    |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nPRECIO DE VENTA :"+str(dicc["PVenta"])+"\nIMPORTE :"+str(dicc["ImporteVenta"]))
            print("-"*50 )
            print("---RESUMEN DEL AÑO---")
            #se suman todos los importes de ventas para hacer el resumen del año
            TotalSemestre2=0
            TotalSemestre1=0
            for dicc in mtzPVenta:
                if dicc["Semestre"]==1:
                    TotalSemestre1+= dicc["ImporteVenta"]
                if dicc["Semestre"]==2:
                    TotalSemestre2+=dicc["ImporteVenta"]
            Total2016ventas = (float(TotalSemestre1) + float(TotalSemestre2))

            print(f"Total de ventas del Semestre1: {TotalSemestre1}\nTotal de ventas del semestre 2: {TotalSemestre2}\nTotal del año :{TotalSemestre1+TotalSemestre2}")
            input("\nPULSA ENTER PARA CONTINUAR.....")
        elif opcion_pv=="3":
            break
        else:
            input("\n¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

def Presupuesto_Produccion():
    #acceder y  modificar la matriz de produccion
    global mtzPProduccion
    global mtzUnidadesProducir
    lstValArticulo=[]
    dicPProduccion= dict(CodArticulo="",Semestre=0,UndVender=0,InventInicial=0,InventFinal=0,TotalUnidades=0,UndProducir=0)
    while True:
        os.system("cls")
        print("\t ==PRESUPUESTO DE PRODUCCION==")
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("3.- Regresar al Menú principal")
        opcion= input("Ingresa la opcion deseada: ")

        if opcion =="1":
            while True:
                os.system("cls")
                print("==Catálogo de artículos==")
                for Diccionario in mtzArticulos: #imprimir opciones
                    print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                    lstValArticulo.append(Diccionario["CodArticulo"])

                print("4 - Regresar a Menu Presupuesto de Produccion")
                Opcion= input("ingresa la opcion deseada: ")
                if(Opcion in lstValArticulo):

                    for Cont in range(0,2):
                        for Campo in dicPProduccion:
                            if(Campo == "CodArticulo"):
                                dicPProduccion[Campo] = Opcion
                            elif(Campo == "Semestre"):
                                dicPProduccion[Campo] = (Cont + 1)
                            elif Campo == "UndVender":
                                #accedemos a la matriz de venta para extraer las unidades a vender
                                for dicc in mtzPVenta:
                                    if dicc["CodArticulo"]== Opcion:
                                        if dicc["Semestre"]== (Cont+1):
                                            dicPProduccion[Campo]= dicc["UndVender"]

                            elif Campo=="InventInicial" or Campo=="InventFinal":
                                dicPProduccion[Campo] = float(input("Ingresa la cantidad de " + Campo + " para el " + str(Cont + 1) + "° semestre: "))
                            else: #se calcula las unidades totales y unidades a producir

                                dicPProduccion["TotalUnidades"]= float(dicPProduccion["UndVender"]+ dicPProduccion["InventFinal"])
                                dicPProduccion["UndProducir"]= float(dicPProduccion["TotalUnidades"]- dicPProduccion["InventInicial"])
                        #se agrega a la matriz
                        mtzPProduccion.append(dicPProduccion.copy())
                        print(" ")

                elif Opcion=="4":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")
        elif opcion=="2":
            os.system("cls")
            print("\n--REPORTE PRESUPUESTO DE PRODUCCION--")
            for dicc in mtzPProduccion:
                if dicc["CodArticulo"]== "1":
                    print("-"*50 )
                    print( "CODIGO: 1   |   PRODUCTO: CL    |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nINVENTARIO FINAL: "+str(dicc["InventFinal"])+"\nTOTAL DE UNIDADES:"+str(dicc["TotalUnidades"]))
                    print("INVENTARIO INICIAL: "+str(dicc["InventInicial"])+"\nUNIDADES A PRODUCIR "+str(dicc["UndProducir"]))
                elif dicc["CodArticulo"]== "2":
                    print("-"*50 )
                    print( "CODIGO: 2  |   PRODUCTO: CE   |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nINVENTARIO FINAL: "+str(dicc["InventFinal"])+"\nTOTAL DE UNIDADES:"+str(dicc["TotalUnidades"]))
                    print("INVENTARIO INICIAL: "+str(dicc["InventInicial"])+"\nUNIDADES A PRODUCIR "+str(dicc["UndProducir"]))
                else:
                    print("-"*50 )
                    print( "CODIGO: 3  |   PRODUCTO: CR    |   SEMESTRE:" + str(dicc["Semestre"]))
                    print("UNIDADES: "+str(dicc["UndVender"])+"\nINVENTARIO FINAL: "+str(dicc["InventFinal"])+"\nTOTAL DE UNIDADES:"+str(dicc["TotalUnidades"]))
                    print("INVENTARIO INICIAL: "+str(dicc["InventInicial"])+"\nUNIDADES A PRODUCIR "+str(dicc["UndProducir"]))

            diccUnidadesProducir= dict(Codigo="",Producto="",TotalUnidades=0)
            for diccs in mtzPProduccion:
                if diccs["CodArticulo"]=="1":
                    diccUnidadesProducir["Codigo"]="1"
                    diccUnidadesProducir["Producto"]="CL"
                    diccUnidadesProducir["TotalUnidades"]+= diccs["UndProducir"]
            mtzUnidadesProducir.append(diccUnidadesProducir.copy())
            for diccs in mtzPProduccion:
                if diccs["CodArticulo"]=="2":
                    diccUnidadesProducir["Codigo"]="2"
                    diccUnidadesProducir["Producto"]="CE"
                    diccUnidadesProducir["TotalUnidades"]+= diccs["UndProducir"]
            mtzUnidadesProducir.append(diccUnidadesProducir.copy())
            for diccs in mtzPProduccion:
                if diccs["CodArticulo"]=="3":
                    diccUnidadesProducir["Codigo"]="3"
                    diccUnidadesProducir["Producto"]="CR"
                    diccUnidadesProducir["TotalUnidades"]+= diccs["UndProducir"]
            mtzUnidadesProducir.append(diccUnidadesProducir.copy())

            print("-"*50 )
            print("---RESUMEN DEL AÑO---")
            for Dicc in mtzUnidadesProducir:
                if Dicc["Codigo"]=="1":
                    print("TOTAL DE UNIDADES A PRODUCIR DE "+  Dicc["Producto"]+": "+str(Dicc["TotalUnidades"]))
                elif Dicc["Codigo"]=="2":
                    print("TOTAL DE UNIDADES A PRODUCIR DE "+  Dicc["Producto"]+": "+str(Dicc["TotalUnidades"]))
                elif Dicc["Codigo"]=="3":
                    print("TOTAL DE UNIDADES A PRODUCIR DE "+  Dicc["Producto"]+": "+str(Dicc["TotalUnidades"]))
            input("\nPULSA ENTER PARA CONTINUAR.....")
        elif opcion=="3":
            break
        else:
            input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

def PresupuestoRMateriales():
    global mtzPRMateriales
    global mtzRequerimientoTotal
    diccPRMateriales= dict(CodArticulo="",Semestre=0,UndProducir=0,RequerimientoA=0,TotalMaterialA=0,RequerimientoB=0,TotalMaterialB=0,RequerimientoC=0,TotalMaterialC=0)
    diccRequerimiento= dict(Codigo="",Nombre="",Semestre=0,Total=0)
    lstValArticulo=[]
    while True:
        os.system("cls")
        print("\t ==PRESUPUESTO DE REQUERIMIENTO DE MATERIALES==")
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de requerimiento de materiales")
        print("3.- Regresar al Menú principal")
        opcion= input("Ingresa la opcion deseada: ")

        if opcion =="1":
            while True:
                os.system("cls")
                print("==Catálogo de artículos==")
                for Diccionario in mtzArticulos: #imprimir opciones
                    print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                    lstValArticulo.append(Diccionario["CodArticulo"])
                print("4 - Regresar al Menu Anterior")
                Opcion= input("ingresa la opcion deseada: ")

                if(Opcion in lstValArticulo):

                    for Cont in range(0,2):
                        for Campo in diccPRMateriales:
                            if (Campo== "CodArticulo"):
                                diccPRMateriales["CodArticulo"] = Opcion

                            elif(Campo == "Semestre"):
                                diccPRMateriales["Semestre"] = (Cont + 1)
                             #accedemos a la matriz de produccion para extraer las unidades a producir
                            elif (Campo== "UndProducir"):
                                for dicc in mtzPProduccion:
                                    if dicc["CodArticulo"]== Opcion:
                                        if dicc["Semestre"]== (Cont+1):
                                            diccPRMateriales["UndProducir"]= dicc["UndProducir"]
                                # MATERIAL A
                            elif(Campo=="RequerimientoA"):
                                print("-"*50)
                                print("Codigo del Producto: "+Opcion+"\nSemestre: "+str(Cont + 1))
                                diccPRMateriales["RequerimientoA"]= float(input(f"Ingrese el requerimiento de {Campo[5:]}: "))
                            elif Campo=="TotalMaterialA":
                                for dicc in mtzPProduccion:
                                    if dicc["CodArticulo"]== Opcion:
                                        if dicc["Semestre"]== (Cont+1):
                                            diccPRMateriales["TotalMaterialA"] =  diccPRMateriales["RequerimientoA"] * dicc["UndProducir"]
                                #MATERIAL B
                            elif(Campo=="RequerimientoB"):
                                print("-"*50)
                                print("Codigo del Producto: "+Opcion+"\nSemestre: "+str(Cont + 1))
                                diccPRMateriales["RequerimientoB"]= float(input(f"Ingrese el requerimiento de {Campo[5:]}: "))
                            elif Campo=="TotalMaterialB":
                                for dicc in mtzPProduccion:
                                    if dicc["CodArticulo"]== Opcion:
                                        if dicc["Semestre"]== (Cont+1):
                                            diccPRMateriales["TotalMaterialB"] =  diccPRMateriales["RequerimientoB"] * dicc["UndProducir"]
                                #MATERIAL C
                            elif(Campo=="RequerimientoC"):
                                print("-"*50)
                                print("Codigo del Producto: "+Opcion+"\nSemestre: "+str(Cont + 1))
                                diccPRMateriales["RequerimientoC"]= float(input(f"Ingrese el requerimiento de {Campo[5:]}: "))
                            elif Campo=="TotalMaterialC":
                                for dicc in mtzPProduccion:
                                    if dicc["CodArticulo"]== Opcion:
                                        if dicc["Semestre"]== (Cont+1):
                                            diccPRMateriales["TotalMaterialC"] =  diccPRMateriales["RequerimientoC"] * dicc["UndProducir"]
                        #se agrega a la matriz
                        print(" ")
                        mtzPRMateriales.append(diccPRMateriales.copy())
                elif Opcion=="4":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

        elif opcion=="2":
            #Material A
            for count in range(0,2):
                for dicc in mtzPRMateriales:
                    if dicc["Semestre"]== (count+1):
                        diccRequerimiento["Codigo"]="1"
                        diccRequerimiento["Nombre"]= "MaterialA"
                        diccRequerimiento["Semestre"]= (count+1)
                        diccRequerimiento["Total"]+= dicc["TotalMaterialA"]
                mtzRequerimientoTotal.append(diccRequerimiento.copy())
            #Material B
            for count in range(0,2):
                for dicc in mtzPRMateriales:
                    if dicc["Semestre"]== (count+1):
                        diccRequerimiento["Codigo"]="2"
                        diccRequerimiento["Nombre"]= "MaterialB"
                        diccRequerimiento["Semestre"]= (count+1)
                        diccRequerimiento["Total"]+= dicc["TotalMaterialB"]
                mtzRequerimientoTotal.append(diccRequerimiento.copy())
            #Material C
            for count in range(0,2):
                for dicc in mtzPRMateriales:
                    if dicc["Semestre"]== (count+1):
                        diccRequerimiento["Codigo"]="3"
                        diccRequerimiento["Nombre"]= "MaterialC"
                        diccRequerimiento["Semestre"]= (count+1)
                        diccRequerimiento["Total"]+= dicc["TotalMaterialC"]
                mtzRequerimientoTotal.append(diccRequerimiento.copy())

            os.system("cls")
            print("\t==DATOS INGRESADOS==")
            for dicc in mtzPRMateriales:
                print("-"*60)
                print("CODIGO: "+dicc["CodArticulo"]+"  |   SEMESTRE: "+str(dicc["Semestre"]))
                print("Unidades a Producir: "+str(dicc["UndProducir"]))
                print("| Requerimiento: "+str(dicc["RequerimientoA"])+"\t| Total de Material A: "+str(dicc["TotalMaterialA"]))
                print("| Requerimiento: "+str(dicc["RequerimientoB"])+"\t| Total de Material C: "+str(dicc["TotalMaterialB"]))
                print("| Requerimiento: "+str(dicc["RequerimientoC"])+"\t| Total de Material B: "+str(dicc["TotalMaterialC"]))
            print("\n\t==REPORTE PRESUPUESTO DE REQUERIMIENTOS DE MATERIALES")
            for dicc in mtzRequerimientoTotal:
                if dicc["Nombre"]=="MaterialA":
                    print("--"*40)
                    print(dicc["Nombre"]+"\nSemestre: "+str(dicc["Semestre"])+"\nTotal de Material Requerido: "+str(dicc["Total"]))
                elif dicc["Nombre"]=="MaterialB":
                    print("--"*40)
                    print(dicc["Nombre"]+"\nSemestre: "+str(dicc["Semestre"])+"\nTotal de Material Requerido: "+str(dicc["Total"]))
                elif dicc["Nombre"]=="MaterialC":
                    print("--"*40)
                    print(dicc["Nombre"]+"\nSemestre: "+str(dicc["Semestre"])+"\nTotal de Material Requerido: "+str(dicc["Total"]))

            input("\nPulsa enter para continuar...")
        elif opcion=="3":
            break

        else:
            input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

def PresupuestoCMateriales():
    global mtzPCMateriales
    diccPCMateriales= dict(Codigo="",Material="",Semestre=0,Requerimiento=0,InventFinal=0,InventInicial=0,PrecioCompra=0,MaterialTotal=0,MaterialComprar=0,ImporteTotal=0)

    while True:
        os.system("cls")
        print("\t ==PRESUPUESTO DE COMPRA DE MATERIALES==")
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de compra de materiales")
        print("3.- Regresar al Menú principal")
        opcion= input("Ingresa la opcion deseada: ")

        if opcion =="1":
            while True:
                os.system("cls")
                print("==Catálogo de artículos==")
                print("1 - Material A")
                print("2 - Material B")
                print("3 - Material C")
                print("4 - Regresar al Menu Anterior")
                Opcion= input("ingresa la opcion deseada: ")

                if(Opcion in ["1","2","3"]):
                    for Cont in range(0,2):
                        for Campo in diccPCMateriales:
                            if Campo== "Codigo":
                               diccPCMateriales["Codigo"]= Opcion
                            elif Campo== "Material":
                                for dicc in mtzMateriales:
                                    if dicc["Codigo"]== Opcion:
                                        diccPCMateriales["Material"] = dicc["Nombre"]
                            elif Campo=="Semestre":
                                diccPCMateriales["Semestre"]=(Cont+1)
                            elif Campo=="Requerimiento":
                                for diccionario in mtzRequerimientoTotal:
                                    if diccionario["Codigo"]== Opcion:
                                        if diccionario["Semestre"]== (Cont+1):
                                            diccPCMateriales["Requerimiento"]= float(diccionario["Total"])

                            elif Campo== "InventFinal":
                                print("--"*30)
                                for dicc in mtzMateriales:

                                    if dicc["Codigo"]== Opcion:
                                        print("|    Codigo: "+ Opcion +"  |   Nombre: " +dicc["Nombre"]+ "  |   Semestre: "+str(Cont+1))
                                diccPCMateriales["PrecioCompra"]= float(input("Ingresa el Inventario Final:  "))

                            elif Campo=="InventInicial":
                                print("--"*30)
                                for dicc in mtzMateriales:
                                    if dicc["Codigo"]== Opcion:
                                        print("|    Codigo: "+ Opcion +"  |   Nombre: " +dicc["Nombre"]+ "  |   Semestre: "+str(Cont+1))
                                diccPCMateriales["InventInicial"]= float(input("Ingresa el Inventario Inicial:  "))
                            elif Campo=="PrecioCompra":
                                print("--"*30)
                                for dicc in mtzMateriales:
                                    if dicc["Codigo"]== Opcion:
                                        print("|    Codigo: "+ Opcion +"  |   Nombre: " +dicc["Nombre"]+ "  |   Semestre: "+str(Cont+1))
                                diccPCMateriales["PrecioCompra"]= float(input("Ingresa el Precio de Compra:  "))
                            else:
                                diccPCMateriales["MaterialTotal"]= float(diccPCMateriales["Requerimiento"]+ diccPCMateriales["InventFinal"])
                                diccPCMateriales["MaterialComprar"]= float(diccPCMateriales["MaterialTotal"]- diccPCMateriales["InventInicial"])
                                diccPCMateriales["ImporteTotal"]= float(diccPCMateriales["MaterialComprar"] * diccPCMateriales["PrecioCompra"])
                        print(" ")
                        mtzPCMateriales.append(diccPCMateriales.copy())



                elif Opcion=="4":
                    break
                else:
                    input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")

        elif opcion=="2":
            os.system("cls")
            print("\t==DATOS INGRESADOS==")
            for dicc in mtzPCMateriales:
                print("-"*60)
                print("CODIGO: "+dicc["Codigo"]+"  |   Material: "+str(dicc["Material"])+"  |   Semestre: "+str(dicc["Semestre"])+" |")
                print("Requerimiento: "+str(dicc["Requerimiento"])+"\nInventario Final"+str(dicc["InventFinal"])+"\nInventario Inicial"+str(dicc["InventInicial"]))
                print("Precio Compra: "+str(dicc["PrecioCompra"])+"\nTotal de Materiales: "+str(dicc["MaterialTotal"])+"\nMaterial a Comprar: "+str(dicc["MaterialComprar"]))
                print("Material a Comprar(en $): "+str(dicc["ImporteTotal"]))

            print("\n\n\t==REPORTE PRESUPUESTO DE COMPRA DE MATERIALES")
            Semestre1=0
            Semestre2=0
            for diccionario in mtzPCMateriales:
                if diccionario["Semestre"]==1:
                    Semestre1 += diccionario["ImporteTotal"]
                else:
                    Semestre2 += diccionario["ImporteTotal"]


            print("\n\t==TOTALES==")
            print(" Compras Totales Semestre 1: "+str(Semestre1))
            print(" Compras Totales Semestre 2: "+str(Semestre2))
            print(" Compras Totales  Año 2016: "+str(Semestre1+Semestre2))

            input("\nPulsa enter para continuar...")
        elif opcion=="3":
            break

        else:
            input("¡¡¡OPCION INVALIDA!!!\tINGRESE UNA OPCION VALIDA")



Main()

