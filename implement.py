import datetime
from sistemaVet import *

def main():
    servicio_hospitalario = sistemaV()
    while True:
    menu=int(input('''\nIngrese una opción: 
                    \n1- Ingresar una mascota 
                    \n2- Ver fecha de ingreso 
                    \n3- Ver número de mascotas en el servicio 
                    \n4- Ver medicamentos que se están administrando
                    \n5- Eliminar mascota 
                    \n6- Salir 
                    \nUsted ingresó la opción: ''' ))
    if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio, vuelva después..")
                continue
            if historia!=int:
                print('Usted ha ingresado datos incorrectos. Intente de nuevo: ')
            historia = int(input("Ingrese # de la historia: "))

            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipos=input("Ingrese el tipo de mascota 1. Felino  2.Canino): ")
                if tipos=='1':
                    tipo="Felino"
                else:
                    tipo="Canino"
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                x=datetime.fecha(fecha)
                medicamento=input("Ingrese nombre del medicamento: ")
                cant=input(int("Ingrese la cantidad de medicamento de la mascota: "))
                lista_med=[]
                for i in range(0,cant):
                    nombre_medicamentos= input("Ingrese el nombre: ")
                    dosis=input(int("Ingrese la dosis: "))
                    medicamento= Medicamento()
                    medicamento.asignarDosis(dosis)
                    medicamento.asignarNombre(nombre_medicamentos)
                    lista_med.append(medicamento)
                mas =  Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarlista_medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                if r :
                    print ("Se ingresó exitosamente la mascota..")
                else:
                    print ("No se ingresó la mascota.. ya está en el sistema")

            else:
                print("Ya existe una mascota con el número de historia clínica ingresado.")

        elif menu == 2:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:  
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.") 

        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q)
            if medicamento != None: 
                print(f"El medicamento suministrado es: {medicamento} ")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")


if __name__ == '__main__':
    main()