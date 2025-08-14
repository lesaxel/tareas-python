import json
import os
from contacto import Contact

class AgendaContacs:
    """ Clase que gestion coleccion de contactos.
    Attributes:
    conctacts(list): Lista de Objetos
    ruta_archivo(): Ruta al archivo de almacenamiento """
    
    def __init__(self, ruta_archivo="contacts.json"):
        
         """Inicializa una nueva agenda de contacts 
         args:
              ruta_archivo(str, optional): Ruta al archivo para guardar los contacts
         """
         self.contacts = []
         self.ruta_archivo = ruta_archivo
         # Intentar cargar contactos existentes si el archivo existe
         self.cargar()
         
    def add(self, contact):
      
        """Anade un nuevo contacto a la agenda
        Arg:
            contact(Contact): El contacto a anadir
        
        Returns:  
                bool: True si se agrego correctamente,
                False si ya existe     
        
         """
         # Verificar si ya existe un contacto con el mismo nombre
         
        for c in self.contacts:
             if c.nombre.lower() == contact.nombre.lower():
                 return False
        # Si no existe, lo anadimos
        self.contacts.append(contact)
        return True
    
    def seek(self, termino):
            """ Busca contactos con el termino de busqueda
            Args:
                 termino(str): Termino a buscar en nombre, telefono o email 
                 
            Returns:
                   List: Lista de contactos que coincidan con la busqueda.
                   
            """
            
            resultados = []
            termino = termino.lower()
            
            for contact in self.contacts:
                if (termino in contact.nombre.lower() or
                    termino in contact.telefono.lower() or
                    termino in contact.email.lower()):
                    resultados.append(contact)
        
            return resultados
    
    def update(self, nombre_actual, nombre=None, telefono=None, email=None, direccion=None):
    
     """ Actualizar un contacto existente
            Args:
                 nombre_actual(str): Nombre del contacto a actualizar.
                 nombre(str optional): Nuevo nombre   
                 telefono(str optional): Nuevo telefono
                 email(str optional): Nuevo email
                 direccion(str optional): Nueva direccion                         
            Returns:
                   List: Lista de contactos que coincidan con la busqueda.
                   
            """
     for contact in self.contacts:
       if contact.nombre.lower() == nombre_actual.lower():
          contact.update(nombre, telefono, email, direccion)
          return True
    
     return False  
    
    def delete(self, nombre):
        """ Elimina un contacto de la agenda. 
            Args:
                 nombre(str): Nombre del contacto a eliminar.
                                          
            Returns:
                   Bool: True si se elimina correctamente, False si no se encontro .
                   
            """
        for i, contact in enumerate(self.contacts):
            if contact.nombre.lower() == nombre.lower():
                del self.contacts[i]
                return True
            return False
   
    def lists(self):
             """ Devuelve la lista completa de contacts. 
                                                     
            Returns:
                   Lists: Lista todo los contactos.                  
            """
             return self.contacts
    
    def save(self):
        """ 
            Bool: True si se guardo, False en caso contrario.
                   
        """
        try:
           # Convertir ojbeto Conctact a diccionario.
         datos = []
         for contact in self.contacts:
              datos.append({
              "nombre": contact.nombre,
              "telefono": contact.telefono,
              "email": contact.email,
              "direccion": contact.direccion                  
            })             
               
            # Guardar en formato Json
         with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dumb(datos, archivo, indent=4, ensure_ascii=False)
                return True  
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False
    
    def loads(self):
         """ Va a cargar los contacts desde un archivo.json. 
                                                     
            Returns:
                   Bool: Si se cargo correctamente, False en caso contrario.                  
            """
         if not os.path.exists(self.ruta_archivo):
             return False    
         try:
             with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                 datos = json.load(archivo)
            # Convertir diccionarios a objetos contact
             self.contacts = []
             for dato in datos:
                 contact = Contact(
                     dato["nombre"],
                     dato["telefono"],
                     dato.get["email", ""],
                     dato["direccion"]
                 )
                 self.contacts.append(contact)
                 return True
         except Exception as e:
             print(f"Error al cargar: {e}")
             return False