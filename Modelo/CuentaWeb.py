from Modelo.base_de_datos.Repositorio.CuentaWebRepositorio import CuentaWebRepositorio
from Modelo.base_de_datos.Repositorio.ClienteRepositorio import RepositorioCliente

import hashlib

from fpdf import FPDF

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

    

    def Transferir(self,cuenta_dep, cuenta_ben, nombre_ben, cant,cedula)-> int:

        id_tra = 0

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
                   id_tra = repo_cli.LLamar_Procedimiento_Transferencia(cuenta_dep,cuenta_ben,cant)
        
        return id_tra


    def Consultar_Estado_Cuenta(self,cuenta,cedula):

        if cuenta is None:
            print("Por favor ingrese su numero de cuenta")
        else:

            ver_cue  = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta","Cedula",cuenta,cedula)

            if ver_cue is True:
               consultado = repo_cue_web.Consulta_Estado_Cuenta(cuenta)
               for imprimir in consultado :
                        print("----------------------")
                        print("----------------------")
                        print("----------------------")
                        print(f"Fecha:  {imprimir[0]}")
                        print(f"Hora: {imprimir[1]}")
                        print(f"Cantidad {imprimir[2]} $")
                        print(f"Remitente: {imprimir[3]}")
                        print(f"Cuenta del remitente: {imprimir[4]}")
                        print(f"Beneficiario: {imprimir[5]}")
                        print(f"Cuenta del beneficiario: {imprimir[6]}")
                        print("----------------------")
                        print("----------------------")
                        print("----------------------")

            else:
                print("El numero de cuenta ingresado no pertenece al Usuario")
    
    def Filtrar_Estado_Cuenta(self,cuenta,cedula,Mes,Año):

        if cuenta is None:
            print("Por favor ingrese su numero de cuenta")
        else:

            ver_cue  = repo_cli.consultar_datos_Cuenta_dos_campos("Numero_cuenta","Cedula",cuenta,cedula)

            if ver_cue is True:
              consultado =  repo_cue_web.Consulta_Filtro_Estado_Cuenta_Dos_Campos(cuenta,"MONTH(transaccion.fecha_tra)","YEAR(transaccion.fecha_tra)",Mes,Año)
              for imprimir in consultado :
                        print("----------------------")
                        print("----------------------")
                        print("----------------------")
                        print(f"Fecha:  {imprimir[0]}")
                        print(f"Hora: {imprimir[1]}")
                        print(f"Cantidad {imprimir[2]} $")
                        print(f"Remitente: {imprimir[3]}")
                        print(f"Cuenta del remitente: {imprimir[4]}")
                        print(f"Beneficiario: {imprimir[5]}")
                        print(f"Cuenta del beneficiario: {imprimir[6]}")
                        print("----------------------")
                        print("----------------------")
                        print("----------------------")
            else:
                print("El numero de cuenta ingresado no pertenece al Usuario")
    
    def Crear_Pdf(self,cuenta,id_tra):

        Array =  repo_cue_web.Consulta_Estado_Cuenta_PDF(cuenta,id_tra)
        saldo = repo_cli.Consulta_Saldo_depositante(cuenta)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        
        
       
        for imprimir in Array:

            fecha =  imprimir[0]
            hora =  imprimir[1]
            cantidad =  imprimir[2]
            remitente =  imprimir[3]
            cuenta_rem =  imprimir[4]
            beneficiario = imprimir[5]
            cuenta_ben =  imprimir[6]

            pdf.cell(200,10,txt="Comprobante de transferencia - Banco Multitodo",ln=True,align="C")
            pdf.cell(200,10,txt="---------------------------------------------------------------------",ln=True,align="L")
            formatted_fecha = fecha.strftime("%Y-%m-%d")
            pdf.cell(200,10,txt=f"Fecha:  {formatted_fecha}",ln=True,align="L")
        
      
            total_segundos = int(hora.total_seconds())
            horas = total_segundos  // 3600
            minutos = (total_segundos % 3600) // 60
            segundos = total_segundos  % 60
            formatted_hora = f"{horas:02}:{minutos:02}:{segundos:02}"

            pdf.cell(200,10,txt=f"Hora: {formatted_hora}",ln=True,align="L")
            pdf.cell(200,10,txt=f"Cantidad: {cantidad} $",ln=True,align="L")
            pdf.cell(200,10,txt=f"Nombre del remitente:  {remitente}",ln=True,align="L")
            pdf.cell(200,10,txt=f"Cuenta del remitente:  {cuenta_rem}",ln=True,align="L")
            pdf.cell(200,10,txt=f"Nombre del Beneficiario: {beneficiario}",ln=True,align="L")
            pdf.cell(200,10,txt=f"Cuenta del remitente:  {cuenta_ben}",ln=True,align="L")
            pdf.cell(200,10,txt=f"Saldo restante: {saldo} $",ln=True,align="L")

            pdf.cell(200,10,txt="---------------------------------------------------------------------",ln=True,align="L")



        
        
        


        

        

        pdf.output("Archivo.pdf")
        






            

            




             
                 

             

                 
                 
                    


        










    
