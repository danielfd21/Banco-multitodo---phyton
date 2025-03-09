
from Modelo.base_de_datos.Repositorio.CuentaWebRepositorio import CuentaWebRepositorio

repo = CuentaWebRepositorio()

class CuentaWeb():

    est = ""
    usu = ""
    cla = ""
    ced = ""
    inte = 0

    def __init_subclass__(cls):
        pass

    def __init__(self, estado, usaurio, clave, cedula, intentos ):

        self.est = estado
        self.usu = usaurio
        self.cla = clave
        self.ced = cedula
        self.inte = intentos



    
    def crear_cuenta_web(self):


        cre_cue = repo.Insertar_datos_cuentaweb(self.est,self.usu,self.cla,self.ced,self.inte)

        if cre_cue is True:

            print("Su registro ha sido exitoso")
        else:
            print("Lo sentimos ha ocurrido un error")
        