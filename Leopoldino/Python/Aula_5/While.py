pos=0
neg=0
num=int(input("Digite um número qualquer: "))
while num!=0:
    if num>0:
        pos=pos+1
    elif num<0:
        neg=neg+1
    print("Digite '0' para encerrar!!!")
    num=int(input("Digite um número qualquer: "))
print("Número de positivos.",pos)
print("Números de negativos.",neg)