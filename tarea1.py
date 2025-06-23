### Ejercicio 1: Definir una Clase
class Animal:
    def __init__(self, raza, genero):
        
        self.raza = raza
        self.genero = genero
        
    def informacion(self):
        print(f"Hola, Es un {self.raza}, y es un {self.genero}.")
        
        
gen = Animal("Doberman", "Perro de Cuido")

gen.informacion()

### Ejercicio 2: Trabajar con Atributos y Métodos

class Coche:
    def __init__(self, marca):
        self.marca = marca
    
    def acelerar(self):
        print(f"El coche esta Acelerando, {self.marca}.")
        
mi_carro = Coche("Toyota")
mi_carro.marca = "Honda"

mi_carro.acelerar()


### Ejercicio 3: Crear una Clase con Múltiples Métodos

class Calculadora:
    def __init__(self):
        self.resultado = 0
        
        
    def suma(self, num1):
        self.resultado += num1
    def resta(self, num2):
        self.resultado -= num2        
    def mostrar_resultado(self):
        print("El Resultado es:", self.resultado)
        

calculadora = Calculadora()

calculadora.suma(540)
calculadora.resta(40)
calculadora.suma(50)

calculadora.mostrar_resultado()