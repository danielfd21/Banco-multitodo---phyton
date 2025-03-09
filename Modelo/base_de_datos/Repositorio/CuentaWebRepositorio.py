from Modelo.base_de_datos.Conexion.Conexion import conexion




class CuentaWebRepositorio():

    

    def __init__(self):
        self.conexion = conexion()
        self.cursor = self.conexion.cursor()

    def Consultar_cuenta_web_un_campo(self,campo,objeto) -> bool:
        ok = False

        consulta = f"SELECT * FROM cuenta_web WHERE {campo} = %s "
        val = (objeto,)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchone()

        if consultado is not None:
            ok = True
        return ok
        


    def Insertar_datos_cuentaweb(self,est,usu,cla,ced,inte) -> bool:

        ok = False

        insertar = "INSERT INTO cuenta_web(`estado`, `Usuario`, `Clave`, `Cedula`, `Intentos`) VALUES(%s,%s,%s,%s,%s)"
        val = (est,usu,cla,ced,inte)
        self.cursor.execute(insertar,val)
        self.conexion.commit()
        if self.cursor.rowcount > 0:
            ok = True
        return ok

    def Consulta_Numero_de_cuenta(self,cedula):

        consulta = "SELECT Numero_cuenta FROM cuenta WHERE Cedula = %s"
        val = (cedula,)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchall()

        for imprimir in consultado:
            print(f"cuenta: {imprimir[0]}")

    def Obtener_cedula_cuenta_web(self, usuario) -> str:
        
        cedula = ""

        consulta = "SELECT Cedula From cuenta_web Where Usuario = %s"
        val = (usuario,)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchone()
        if consultado is not None:

           cedula = consultado[0] 
        
        return cedula
   

        


