from utilidades import*

trabajadores=[]

while True:
    print("---Analizador de datos---")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion=int(input("Seleccione una opcion del menu: "))
    if opcion == 1:
        asig_sueldos_aleatorios(trabajadores)
    elif opcion ==2:
        clasificar_sueldos(trabajadores) 
    elif opcion ==3:
        ver_estadisticas() 
    elif opcion ==4:
        report_sueldo(trabajadores)       
    elif opcion ==5:
        salir_programa()
        break 
    else:
        print("Favor seleccionar opcion de 1 a 5")

    




