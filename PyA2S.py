print("Suma de arreglos de 5 valores XD")
lista=[]
for x in range(5):
    valor=int(input("Ingrese un numero (entero) porfavor:"))
    lista.append(valor) 
print("su arreglo es",lista)
suma = 0
for valor in lista:
    suma = suma + valor

print(f"La suma de su arreglo es =",suma)