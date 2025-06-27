### Ejercicio 2: Calculadora de Formas Geométricas
# Clase abstracta
import math
print("*" * 35)
class Forma:
    def calcularArea(self, nombre):
        pass
    def calcularPerimetro(self, nombre):
        pass
# Clase circulo    
class Circulo(Forma):
    def __init__(self, radio):
       self.radio = radio
    def calcularArea(self):
        return math.pi * self.radio ** 2
    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

# Clase Rectangulo
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def calcularArea(self):
        return self.ancho * self.alto
    def calcularPerimetro(self):
        return 2 * (self.ancho + self.alto)
    
# Clase de prueba

if __name__ == "__main__":
    formas = [
        Circulo(5),
        Rectangulo(4, 6),
        Circulo(7.2),
        Rectangulo(2.5, 3.8)]
    
    for forma in formas:
        print(f"Tipo de forma: {type(forma).__name__}")
        print(f"Area: {forma.calcularArea()}")
        print(f"Perimetro: {forma.calcularPerimetro()}")
        print("*" * 35)
         