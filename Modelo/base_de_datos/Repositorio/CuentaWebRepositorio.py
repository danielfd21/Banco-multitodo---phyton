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
    
    def Consulta_Estado_Cuenta(self,cuenta):

        consulta = "SELECT transaccion.fecha_tra, transaccion.Hora_tra, transaccion.Cantidad ,  cli_rem.Nombres  AS 'Remitente'  , transaccion.Cuenta_rem, cli_ben.Nombres AS 'Beneficiario'  , transaccion.Cuenta_ben FROM transaccion  INNER JOIN cuenta as cu_rem ON transaccion.Cuenta_rem = cu_rem.Numero_cuenta INNER JOIN cliente as cli_rem ON cu_rem.Cedula = cli_rem.Cedula  INNER JOIN cuenta AS cu_ben ON transaccion.Cuenta_ben = cu_ben.Numero_cuenta INNER JOIN cliente AS cli_ben ON cu_ben.Cedula = cli_ben.Cedula WHERE cu_rem.Numero_Cuenta = %s"
        val = (cuenta,)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchall()


       

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

    def Consulta_Filtro_Estado_Cuenta_Dos_Campos(self,cuenta,campo1,campo2,objeto1,objeto2):

        consulta = f"SELECT transaccion.fecha_tra, transaccion.Hora_tra, transaccion.Cantidad ,  cli_rem.Nombres  AS 'Remitente'  , transaccion.Cuenta_rem, cli_ben.Nombres AS 'Beneficiario'  , transaccion.Cuenta_ben FROM transaccion  INNER JOIN cuenta as cu_rem ON transaccion.Cuenta_rem = cu_rem.Numero_cuenta INNER JOIN cliente as cli_rem ON cu_rem.Cedula = cli_rem.Cedula  INNER JOIN cuenta AS cu_ben ON transaccion.Cuenta_ben = cu_ben.Numero_cuenta INNER JOIN cliente AS cli_ben ON cu_ben.Cedula = cli_ben.Cedula WHERE cu_rem.Numero_Cuenta = %s AND {campo1} = %s AND {campo2} = %s"
        val = (cuenta,objeto1,objeto2)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchall()


       

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

        

            
            


            
            



   

        


