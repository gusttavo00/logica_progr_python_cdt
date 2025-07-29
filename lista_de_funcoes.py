# Listas e dicionários usados pelas funções
lista_compras = [] # lista para armazenar itens de compras
aluno = {} # dicionário para armazenar dados do aluno
agenda = {} # dicionário para armazenar contatos

# Função principal de menu
def menu_principal(): # função para exibir o menu principal
    print("\n=== MENU PRINCIPAL ===") # printa o título do menu
    print("1. Lista de Compras") # opções do menu
    print("2. Dados de Aluno") # opção para inserir dados de aluno
    print("3. Separar Pares e Ímpares") # opção para separar números pares e ímpares
    print("4. Agenda de Contatos") # opção para gerenciar contatos
    print("5. Sair")

# Função Lista de Compras
def lista_de_compras(): # função para gerenciar a lista de compras
    while True: # loop para manter o menu ativo
        print("\n=== LISTA DE COMPRAS ===") # printa o título da lista de compras
        print("1. Adicionar item") # opção para adicionar item
        print("2. Remover item") # opção para remover item
        print("3. Ver lista") # opção para ver a lista de compras
        print("4. Voltar ao menu principal") # opção para voltar ao menu principal  
        opcao = input("Escolha uma opção: ") # recebe a opção do usuário

        if opcao == "1": # se a opção for 1, adiciona um item
            item = input("Digite o item para adicionar: ").strip() # recebe o item a ser adicionado
            lista_compras.append(item) # adiciona o item à lista de compras
            print(f"'{item}' adicionado.") # confirma a adição do item
        elif opcao == "2": # se a opção for 2, remove um item
            item = input("Digite o item para remover: ").strip() # recebe o item a ser removido 
            if item in lista_compras: # verifica se o item está na lista
                lista_compras.remove(item) # remove o item da lista de compras
                print(f"'{item}' removido.") # confirma a remoção do item
            else: # se o item não estiver na lista
                print("Item não encontrado.") # informa que o item não foi encontrado
        elif opcao == "3": # se a opção for 3, exibe a lista de compras
            print("\nItens na lista:") # printa os itens na lista de compras
            for i, item in enumerate(lista_compras, 1): # itera sobre a lista de compras
                print(f"{i}. {item}") # exibe cada item com seu índice
        elif opcao == "4": # se a opção for 4, volta ao menu principal
            break # sai do loop e volta ao menu principal
        else: # se a opção for inválida
            print("Opção inválida.") 

# Função Dados de Aluno
def dados_de_aluno():
    print("\n=== DADOS DO ALUNO ===") # printa o título da seção de dados do aluno
    aluno.clear() # limpa os dados do aluno para evitar duplicação
    aluno['nome'] = input("Nome do aluno: ").strip().title() # recebe o nome do aluno
    if not aluno['nome']: # verifica se o nome foi inserido
        print("Nome não pode ser vazio. Tente novamente.") 
    aluno['idade'] = int(input("Idade do aluno: ")) # recebe a idade do aluno
    if aluno['idade'] <= 0: # verifica se a idade é válida
        print("Idade inválida. Tente novamente.") 
        return
    notas = input("Digite as notas separadas por vírgula: ") # recebe as notas do aluno
    if not notas: # verifica se as notas foram inseridas
        print("Notas não podem ser vazias. Tente novamente.") 
        return 
    aluno['notas'] = [float(n.strip()) for n in notas.split(",")] # converte as notas para float e remove espaços
    if not aluno['notas']: # verifica se as notas são válidas
        print("Nenhuma nota válida foi inserida. Tente novamente.") 
        return

    media = sum(aluno['notas']) / len(aluno['notas']) # calcula a média das notas
    if media < 0 or media > 10: # verifica se a média é válida
        print("Média inválida. As notas devem estar entre 0 e 10.")
        return

    print("\n--- RESUMO ---")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}") # formata a média com duas casas decimais

# Função Separar Pares e Ímpares
def separar_pares_impares():
    print("\n=== PARES E ÍMPARES ===")
    numeros = input("Digite números separados por vírgula: ")
    numeros = [int(n.strip()) for n in numeros.split(",")]

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print(f"\nPares: {pares}")
    print(f"Ímpares: {impares}")

# Função Agenda de Contatos
def agenda_de_contatos():
    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Ver todos os contatos")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do contato: ").strip().title()
            telefone = input("Telefone: ").strip()
            agenda[nome] = telefone
            print(f"Contato '{nome}' adicionado.")
        elif opcao == "2":
            nome = input("Nome a remover: ").strip().title()
            if nome in agenda:
                del agenda[nome]
                print(f"Contato '{nome}' removido.")
            else:
                print("Contato não encontrado.")
        elif opcao == "3":
            nome = input("Nome para buscar: ").strip().title()
            if nome in agenda:
                print(f"{nome}: {agenda[nome]}")
            else:
                print("Contato não encontrado.")
        elif opcao == "4":
            if agenda:
                print("\nContatos salvos:")
                for nome, tel in agenda.items():
                    print(f"- {nome}: {tel}")
            else:
                print("Agenda vazia.")
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

# Execução principal
while True:
    menu_principal()
    escolha = input("Escolha uma opção (1 a 5): ")

    if escolha == "1":
        lista_de_compras()
    elif escolha == "2":
        dados_de_aluno()
    elif escolha == "3":
        separar_pares_impares()
    elif escolha == "4":
        agenda_de_contatos()
    elif escolha == "5":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
