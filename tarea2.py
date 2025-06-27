

class Animal:
     #Clase base Animal.
    def __init__(self, nombre, edad):
        #Constructor de la clase Animal.
        self.__nombre = nombre # Privado
        self.__edad = edad      # Privado
        
    def getNombre(self):
        # Get para el nombre.
        return self.__nombre
    
    def getEdad(self):
        # Get para la edad.
        return self.__edad
    
    def setNombre(self, nombre):
        # Set para el Nombre
        self.__nombre = nombre
    def setEdad(self, edad):
        # Set para la Edad.
        self.__edad = edad       
        

    def hacerSonido(self):
        # Metodo abstracto para hacer sonido (debe ser sobreescrito o reutilizado).
        pass
    
    def comer(self):
        # Metodo concreto para comer y realiza una impresion.
        print("El animal esta comiendo")
        

class Perro(Animal):
    # Clase para Perro
    def __init__(self, nombre, edad):
        # Constructor del metodo Perro
        super().__init__(nombre, edad)
    
    def hacerSonido(self):
        # Sobreescritura del metodo hacerSonido para Perro.
        print("Guau guau!")
     
class Gato(Animal):
    # Clase para Gato
    def __init__(self, nombre, edad):
        # Constructor del metodo Gato
        super().__init__(nombre, edad)
    
    def hacerSonido(self):
        # Sobreescritura del metodo hacerSonido para Gato.
        print("Miau miau!")
        
def Main():
    # Funcion principal para probar las clases.
    perro = Perro("Max", 4) 
    gato = Gato("Apo", 2)
    
    print(f"Nombre del Perro: {perro.getNombre()}")
    print(f"Edad del Perro: {perro.getEdad()}")
    perro.comer() 
    perro.hacerSonido()
    
    print(f"Nombre del Gato: {gato.getNombre()}")
    print(f"Edad del Gato: {gato.getEdad()}")
    gato.comer()
    gato.hacerSonido() 
    
    print() 
    
    # Polimorfismo  
    animales = [perro, gato]
    
    for animal in animales:
       animal.hacerSonido()

if __name__ == "__main__":
    Main() 
# Este if la final lo coloco VSCODE.
