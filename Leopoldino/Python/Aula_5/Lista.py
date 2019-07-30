lista=[]
print(lista)
lista=['O carro','peixe',123,111]
print(lista)
nova_lista=["pedra",lista]
print(nova_lista)
print(lista[2])
print(len(lista))
lista.append('gato')
lista.insert(2,'Cabra')
lista.pop(1)
print(lista)
lista.remove(123)
print(lista)
nova_lista.reverse()
print(lista)
item=input("Digte um item: ")
if item in nova_lista:
    print("Item encontrado!")
else:
    print("Item não existe na lista!")