import os
nombre_mascotas=[""]*3
edad_mascotas=[0]*3
def insertar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]=input(f"ingrese nombre de la mascota: ")
        edad_mascotas[i]=int(input(f"ingrese edad mascota: "))
def mostrar():
    for i in range(len(nombre_mascotas)):
        print(f"nombre: {nombre_mascotas[1]}, edad: {edad_mascotas[i]}")
def main():
    global nombre_mascotas, edad_mascotas
    nombre_mascotas=[""]*3
    edad_mascotas=[0]*3

    opcion = 0
    while opcion != 4:
        os.system('cls' if os.name=='nt' else 'clear')
        print("1.insertar mascotas (nombre | edad)")
        print("2.mostrar mascotas (nombre | edad)")
        print("3.eliminar mascotas por nombre")
        print("4.salir")
        opcion=int(input("elija una opcion: "))
        if opcion ==1:
            insertar()
        elif opcion==2:
            mostrar()
        elif opcion==3:
            print("eliminar")
        elif opcion==4:
            print("saliendo....")
        else: print("opcion invalida")
        if opcion !=4: int("presione para continuat..")
main()
