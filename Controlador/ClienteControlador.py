import sys
import os
import time

sys.path.append("C:/xampp/htdocs/multitodo - phyton/Banco")
from Modelo.base_de_datos.Conexion import Conexion
from Modelo.Cliente import CLiente
from Modelo.CuentaWeb import CuentaWeb

cli = CLiente()
cue_web = CuentaWeb()
menu = 0

while menu != 3:
    print("----------------------------")
    print("Bienvenido a Banco multitodo")
    print("Por favor escoja una opción")
    print("1) Inicio de cesión")
    print("2) Registro")
    print("3) Salir")
    print("----------------------------")

    opcion = int(input("Digite el numero de la opción: "))


    if opcion  > 3:
        print("La opcion elegida no esta en el menu seleccione otra por favor")

    if opcion == 1:
        print("-----------------------")
        print("   INICIO DE CESIÓN    ")
        print("-----------------------")

        print("Ingrese sus credenciales de Usuario")

        usuario = input("Ingrese su ususario:").strip()
        clave = input("Ingrese su clave:").strip()
        cedula = cue_web.Loguear(usuario,clave)

        if cedula is not None :

            print("--Bienvenido a Tu banca web multitodo --")

            print("Escoge una opción")

            print("1) Realizar una transferencia bancaria ")
            print("2) Consultar estado de cuenta ")

            opcion_banca = int(input("Ingresa una opción"))

            if opcion == 1:

                cuenta_dep = input("Ingrese su numero cuenta").strip()
                
                
                ver_cue_cli =  cue_web.Verificar_datos_transferir(cuenta_dep,cedula)
                if ver_cue_cli is True:
                    cue_web.Mostrar_Datos_depositante(cuenta_dep)
                    cuenta_ben = input("Ingrese el numero de cuenta del beneficiario").strip()
                    nombre_ben = input("Ingrese el nombre del beneficiario").strip()
                    cantidad = float(input("Ingrese la cantidad a depositar").strip())
                    cue_web.Transferir(cuenta_dep,cuenta_ben,nombre_ben,cantidad,cedula)
       

    
    elif opcion == 2:

        print("-------------------------")
        print("Registro Banco Multitodo")
        print("--------------------------")
        

        cedula = input("Por favor digite su numero de cedula: ").strip()

        clave = input("por favor digite su clave de tarjeta: ").strip()

        ver_dat_cli = cli.verificar_cliente(cedula,clave)

        if ver_dat_cli is True:

            usuario = input("Digite el nombre de usuario que desea usar").strip()

            print("recuerde que debe tener entre 8 a 16 digitos con letras mayusculas, minusculas, numeros y caracteres no alfanumericos")
            
            clave1 = input("Digite la contraseña: ").strip()

            clave2 = input("Ingrese de nuevo la contraseña: ").strip()

            cli.crear_cuenta_web(usuario,clave1,clave2,cedula)

        else: 
            print("Error:")
        
        

        
        


    







