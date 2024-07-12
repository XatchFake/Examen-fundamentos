import random


def asig_sueldos_aleatorios(trabajadores):
    nombre = input("ingrese nombre del trabajador: ")
    sueldo=round(random.uniform(300000,2500000),)
    print("Se han generado el sueldo")
    sueldor={'nombre: ': nombre,'sueldo:': sueldo}
    trabajadores.append(sueldor)
    print(f"nombre: {nombre} sueldo: {sueldo}")


def clasificar_sueldos(trabajadores):
    print("Nombre      empleados")
    print(f"{trabajadores}")

def ver_estadisticas(trabajadores):
    promedio=sum(trabajadores['sueldo'] for trabajadores in trabajadores)
    print("el promedio de los sueldos es:")
    print("el sueldo mas alto es:")
    print("el sueldo mas bajo es:")

def report_sueldo(trabajadores):
    descuentoS=(trabajadores['sueldo'])/0.7
    descuentoAFP=(trabajadores['sueldo'])/0.12

def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por Cristian Castro")
    print("20.139.298-5")
