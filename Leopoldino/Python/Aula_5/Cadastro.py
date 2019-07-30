esc = 0
escolha = 3
listanome = []
listadata = []
listacpf = []
listaid = []
matricula = []
while esc != 'sair':
    print("1-Para cadastrar.")
    print("2-Para consultar.")
    print("3-Para listar todos.")
    print("4-Para excluir.")
    print()
    print("digite 'sair' para sair.")
    print()
    esc = (input("Digite sua opção: "))
    if esc == '1':
        while escolha != 0:
            nome = input("Digite um nome: ")
            listanome.append(nome)
            data = input("Digite a data de nascimento: ")
            listadata.append(data)
            cpf = input("Digite um CPF: ")
            listacpf.append(cpf)
            id = input("Digite o número de identidade: ")
            listaid.append(id)
            escolha = int(input("Digite'0' para sair do programa ou '1' para cadastrar outro número: "))
    elif esc == '2':
        busca = input("Digite aqui um CPF válido: ")
        if busca == listacpf:
           print("CPF encontrado!")
        else:
            print("CPF não cadastrado!")

    elif esc == '3':
        print("Nome: ", listanome)
        print("Data: ", listadata)
        print("CPF:  ", listacpf)
        print("ID:   ", listaid)