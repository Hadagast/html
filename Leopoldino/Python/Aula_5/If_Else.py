# Média dos alunos

nome = input("Digite o nome do aluno:")
n1 = float (input('Digite a 1º nota:'))
n2 = float (input('Digite a 2º nota:'))
n3 = float (input('Digite a 3º nota:'))
n4 = float (input('Digite a 4º nota:'))
media = (n1+n2+n3+n4)/4
if media >=7:
 print ("A média do Aluno:",nome,"é de:",media," - Aprovado")
elif media >4 and media <7:
 print ("A média do Aluno:",nome,"é de:",media," - Recuperação")
elif media <4:
 print ("A média do Aluno:",nome,"é de:",media," - Reprovado")
else:
 print("Aluno sem nota")