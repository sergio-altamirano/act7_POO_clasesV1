print("Introduccion a clases")
class Animal:
    edad=3
    raza="chihuahua"
    comida="croquetas"
    def come(self):
        print(f"El perro come "+self.comida)

print(Animal)
print("creado el objeto de la clase Animal")
perro=Animal()
print(f"edad del perro {perro.edad}")
print(f"raza del perro {perro.raza}")
lacomida=perro.come()