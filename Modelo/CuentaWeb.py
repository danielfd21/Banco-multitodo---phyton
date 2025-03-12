from Modelo.base_de_datos.Repositorio.CuentaWebRepositorio import CuentaWebRepositorio
from Modelo.base_de_datos.Repositorio.ClienteRepositorio import RepositorioCliente

import hashlib

repo_cue_web = CuentaWebRepositorio()
repo_cli = RepositorioCliente()

class CuentaWeb():


    def Loguear(self,usuario, clave) -> str:

        cedula = None

        if usuario is None or clave is None :

            print("Por favor ingrese las credenciales de la cuenta")
        else:
            ver_usu = repo_cue_web.Consultar_cuenta_web_un_campo("Usuario",usuario)
            if ver_usu is True:

                clave = str(clave)

                cla_has = hashlib.sha256(clave.encode()).hexdigest()

                ver_cla = repo_cue_web.Consultar_cuenta_web_un_campo("Clave",cla_has)

                if ver_cla is True:

                    cedula = repo_cue_web.Obtener_cedula_cuenta_web(usuario)

                else:
                    print("La contraseña es incorrecta ")

                
            
            else:
                print("El usuario es incorrecto")
        return cedula



    def Verificar_datos_transferir(self, cuenta_depositante, cedula) -> bool:

        continuar = False

        if cuenta_depositante is None :

            print("Por favor ingrese todos los datos para la transacción")
        else:

            ver_dat_dep = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta", "Cedula", cuenta_depositante, cedula)

            if ver_dat_dep is True:

                continuar = True



            else:
                print("El numero de cuenta del depositante no pertenece al usuario de esta pagina")            

        return continuar
    

    def Mostrar_Datos_depositante(self, cuenta_dep):

        print("El numero de cuenta es: " + cuenta_dep)

        print("Su saldo actual es: " + str(repo_cli.Consulta_Saldo_depositante(cuenta_dep)))

    

    def Transferir(self,cuenta_dep, cuenta_ben, nombre_ben, cant,cedula):

        if cuenta_dep is None and cuenta_ben is None:

            print("Ingrese todos los rqueridos para la transferencia")
        else:
             

            
                 ver_cuen = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta","Cedula",cuenta_ben,cedula)
                 ver_cuen_ben = repo_cli.Consulta_cliente_JOIN_cuenta_dos_campos("Numero_cuenta", "Nombres", cuenta_ben, nombre_ben)
                 saldo = repo_cli.Consulta_Saldo_depositante(cuenta_dep)
                 if cuenta_dep == cuenta_ben :
                   print("Lo sentimos la cuenta del beneficiario es la misma cuenta del depositante")
                 elif ver_cuen is True:
                   print("Lo sentimos no se puede hacer transferencias entre cuentas pertenecientes al mismo cliente")       
                 elif cant > saldo :
                   print("La cantidad que desea transferir es mayor al saldo que posee en su cuenta")
                 elif ver_cuen_ben is False:
                   print("Los datos de la cuenta del beneficiario son incorrectos")
                 else:
                   repo_cli.LLamar_Procedimiento_Transferencia(cuenta_dep,cuenta_ben,cant)


    def Consultar_Estado_Cuenta(self,cuenta,cedula):

        if cuenta is None:
            print("Por favor ingrese su numero de cuenta")
        else:

            ver_cue  = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta","Cedula",cuenta,cedula)

            if ver_cue is True:
                repo_cue_web.Consulta_Estado_Cuenta(cuenta)
            else:
                print("El numero de cuenta ingresado no pertenece al Usuario")
    
    def Filtrar_Estado_Cuenta(self,cuenta,cedula,Mes,Año):

        if cuenta is None:
            print("Por favor ingrese su numero de cuenta")
        else:

            ver_cue  = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta","Cedula",cuenta,cedula)

            if ver_cue is True:
                repo_cue_web.Consulta_Filtro_Estado_Cuenta_Dos_Campos(cuenta,"MONTH(transaccion.fecha_tra)","YEAR(transaccion.fecha_tra)",Mes,Año)
            else:
                print("El numero de cuenta ingresado no pertenece al Usuario")



            

            




             
                 

             

                 
                 
                    


        










    
