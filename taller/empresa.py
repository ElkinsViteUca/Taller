from abc import ABC,abstractclassmethod,abstractmethod
from calendar import c
from helpers import Helper
import os
class ADMINISTRACION:
  pass
      
class USUARIO():
  def __init__(self,nombre,direccion,cedula,email):
    self.nombre = nombre
    self.direccion = direccion
    self.cedula = cedula
    self.email = email
    
  @abstractmethod
  def mostrarCleinte(self):
    print(self.nombre,self.cedula,self.direccion,self.email)
        

    
class OPC_SISTEMA:
  def __init__(self,certi_usuario,verificar_datos,modificar_datos):
    self.certi_usuario = certi_usuario
    self.verificar_datos = verificar_datos
    self.modificar_datos = modificar_datos
    pass 
      
class MODIFICARDATOS(USUARIO):
  def __init__(self, nombre, direccion, cedula, email):
    super().__init__(nombre, direccion, cedula, email)
  def CertificarUsuario(self):
    print("*"*20,"Certificado Usuario","*"*20)
    print("Nombre"," "*10,"Cedula"," "*10,"Email"," "*10,"Direccion")
    print("{:15} {:13} {:23} {}".format(self.nombre,self.cedula,self.email,self.direccion) )
  
  def VerificarDatos(self):
    da = input("Ingrese el nombre")
    while da.isnumeric() == True :
      print("tiene que ingresar sólo caracteres")
      
  def ModificarDatos():
    
    pass
      
      
    
class VERIFICAR_DATOS(USUARIO):
  def __init__(self, nombre, direccion, cedula, email):
    super().__init__(nombre, direccion, cedula, email)
    
  def CantidadCaracteres(self):
    n=len(nombre)
    c=len(cedula)
    d=len(direccion)
    e=len(email)
    print("{} tiene:{} caracteres".format(nombre,n))
    print("{} tiene:{} caracteres".format(cedula,c))
    print("{} tiene:{} caracteres".format(direccion,d))
    print("{} tiene:{} caracteres".format(email,e))
    
  def ValidarCampoLleno(self):
    if len(nombre)==0:
      print ("Campo Nombre Vacio")
    else:
      print("Campo Nombre lleno ")
    #cedula  
    if len(cedula)==0:
      print ("Campo Cedula Vacio")
    else:
      print("Campo Cedula lleno ")
    ######
    if len(direccion)==0:
      print ("Campo Dirección Vacio")
    else:
      print("Campo Dirección lleno ")
    ###
    if len(email)==0:
      print ("Campo Correo Vacio")
    else:
      print("Campo Coreo lleno ")
      
  def IdUnico(self):
    id = input("ingrese el id:")
    if id == cedula:
      print("su id no es unico")
      print("la cedula: {} es igual a su id:{}".format(cedula,id))
    else:
      print("su id es unico")
      
  
  
  
      
class CERTI_USUARIO(USUARIO):
  def __init__(self, nombre, direccion, cedula, email,contra=0):
    super().__init__(nombre, direccion, cedula, email)
  
  def Certificado(self):
    contra=input("Ingrese contraseña:")
    contra=cedula
    n=nombre
    if (n == nombre)and(cedula==contra):
      print("El usario {} se encuentra certificado".format(nombre))
    else:
      print("El usario {} no se encuentra certificado".format(nombre))
      
helper = Helper()
lista=["1) Usuario","2) Administrador","3) Salir"]
opcion=""
while opcion != "3":
  os.system("clear")
  opcion = helper.menu(lista,"Menu Principal")
  if opcion == "1":
    opc1=""
    while opc1 != "5":
      os.system("clear")
      print("*"*20,"Mantenimento De Usuario","*"*20)
      opc1 = helper.menu(["1) Caracteres","2) Validar Campo","3) ID Unico","4) Certificado","5) Salir"],"")
      os.system("clear")
      if opc1 == "1":
        print("*"*20,"Verificar Usuario","*"*20)
        nombre=input("Nombre del Usuario:")
        direccion=input("Dirección del Usuario:")
        cedula=input("Cedula del Usuario:")
        email=input("Correo del Usuario:")
        car=VERIFICAR_DATOS(nombre,direccion,cedula,email)
        car.CantidadCaracteres()
        input("presiona cualquier tecla para regresar")
      
      if opc1 == "2":
        print("*"*20,"Verificar Campo LLeno","*"*20)
        car=VERIFICAR_DATOS(nombre,direccion,cedula,email)
        car3=VERIFICAR_DATOS(nombre,direccion,cedula,email)
        car3.CantidadCaracteres()
        car.ValidarCampoLleno()
        input("presiona cualquier tecla para regresar")
        
      if opc1 == "3":
        print("*"*20,"ID Unico","*"*20)
        car=VERIFICAR_DATOS(nombre,direccion,cedula,email)
        car.IdUnico()
        input("presiona cualquier tecla para regresar")
        
      if opc1 == "4":
        print("*"*20,"Certificado Usuario","*"*20)
        car=CERTI_USUARIO(nombre,direccion,cedula,email,c)
        car3=VERIFICAR_DATOS(nombre,direccion,cedula,email)
        car.Certificado()
        input("presiona cualquier tecla para regresar")
        
  
        
      
        