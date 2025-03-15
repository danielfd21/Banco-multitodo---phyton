from Modelo.base_de_datos.Repositorio.ClienteRepositorio import RepositorioCliente
import re

from Modelo.Entidad.Cuenta_web_Entidad import CuentaWeb

from Modelo.base_de_datos.Repositorio.CuentaWebRepositorio import CuentaWebRepositorio

import hashlib



repo_cue_web = CuentaWebRepositorio()

repo = RepositorioCliente()


class CLiente():

    def verificar_cliente(self,cedula, clave) -> bool:
        
        acceso = False
        
        if(cedula is None or clave is None):
            print("Por favor llene todos los campos") 
        else:
            verificar_ced = repo_cue_web.Consultar_cuenta_web_un_campo("Cedula",cedula)
            if verificar_ced is False:

                  ver_dat_cli = repo.consultar_datos_Cuenta_dos_campos("Cedula","CLave",cedula,clave)

                  if ver_dat_cli is True:
                      
                      acceso = True
                        

                  else:
                      
                      print("Los datos de la cuenta bancaria son erroneos")
                      

            
            else:
                print("El cliente ya tiene una cuenta creada previamente, vuelva a Inicio de cesión o comuniquese con asistencia en linea")
        return acceso
            


    def crear_cuenta_web(self, usuario, clave_cuen_web, clave_cuen_web2, cedula):
        ver_usu = repo_cue_web.Consultar_cuenta_web_un_campo("Usuario",usuario)
        if ver_usu is False :
                          
            minusculas = r"[a-z]"
            mayusculas = r"[A-Z]"
            numeros = r"[0-9]"
            caracteres = r"[@#_-]"
            if re.search(minusculas,clave_cuen_web) and re.search(mayusculas,clave_cuen_web) and re.search(numeros,clave_cuen_web) and re.search(caracteres,clave_cuen_web) and len(clave_cuen_web) >= 8 and len(clave_cuen_web) <= 16 :
                if clave_cuen_web == clave_cuen_web2 :

                    
                    est = "Activo"
                    inte = 0

                    clave_cuen_web = str(clave_cuen_web)

                    cla_has = hashlib.sha256(clave_cuen_web.encode()).hexdigest()
                    nueva_cuenta = CuentaWeb(est,usuario,cla_has,cedula,inte)
                    nueva_cuenta.crear_cuenta_web()
                    

                    
                else:
                    print("Las claves son distintas")
            else:
                print("La contraseña debe contener como minimo entre 8 a 16 digitos con una letra en mayuscula, una letra en minuscula, un numero y un caracter no alfanumerico")
        else:
            print("El nombre de usuario ya se encuentra en uso, elija otro")
                      

        
