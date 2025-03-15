from Modelo.base_de_datos.Conexion.Conexion import conexion
import datetime

class RepositorioCliente():

    def __init__(self):
        self.conexion = conexion()
        self.cursor = self.conexion.cursor()

    def consulta_verificar_cliente_un_campo(self , campo, objeto) -> bool :
        
        ok = False



        consultar = f"SELECT * FROM cliente WHERE {campo} = %s"
        val = (objeto,) 

        self.cursor.execute(consultar,val)

        if self.cursor.fetchone() :

            ok = True

        
        return ok
    
    def consultar_datos_Cuenta_dos_campos(self, campo1, campo2, objeto1, objeto2) -> bool :
        
        ok = False
        
        consulta = f"SELECT * FROM cuenta WHERE {campo1} = %s AND {campo2} = %s"
        val = (objeto1,objeto2)
        self.cursor.execute(consulta,val)
        
        if self.cursor.fetchone() :

            ok = True
        
        return ok
    
    
    def Consulta_Saldo_depositante(self, cuenta) -> float:

        saldo = 0.0

        consulta = "SELECT Saldo FROM cuenta WHERE Numero_cuenta = %s"
        val = (cuenta,)
        self.cursor.execute(consulta,val)
        consultado = self.cursor.fetchone()
        if(consultado):
            saldo = float(consultado[0])

        return saldo  
    
    def Insertar_transferencia(self,cuenta_dep,cuenta_ben,cant)-> int:

        id_tra = 0

        fecha = datetime.date.today()
        hora = datetime.datetime.now().strftime('%H:%M:%S')

        insertar = "INSERT INTO transaccion(`fecha_tra`, `Hora_tra`, `Cantidad`, `Cuenta_rem`, `Cuenta_ben`) VALUES(%s,%s,%s,%s,%s)"
        val = (fecha,hora,cant,cuenta_dep,cuenta_ben)
        self.cursor.execute(insertar,val)
        self.conexion.commit()
        
        if self.cursor.rowcount > 0:

            id_tra = self.cursor.lastrowid
        
        return id_tra

    


    def LLamar_Procedimiento_Transferencia(self,cuenta_dep,cuenta_ben,cant)-> int:

        id_tra = 0

        Transferir = "CALL Transferir(%s,%s,%s)"
        val = (cuenta_dep,cuenta_ben,cant)
        self.cursor.execute(Transferir,val)
        self.conexion.commit()

        if self.cursor.rowcount > 0:
            print("Registro exitoso")
            id_tra =  self.Insertar_transferencia(cuenta_dep,cuenta_ben,cant)
        return id_tra
    
            
    def Consulta_cliente_JOIN_cuenta_dos_campos(self,campo1, campo2, objeto1, objeto2) -> bool:
        
        ok = False

        consultar = f"SELECT * FROM cliente INNER JOIN cuenta ON cliente.cedula = cuenta.cedula WHERE {campo1} = %s AND {campo2} = %s"
        val = (objeto1,objeto2)
        self.cursor.execute(consultar,val)
        consultado = self.cursor.fetchone()
        if consultado is not None:
            ok = True

        return ok
    
      


             






        

            









