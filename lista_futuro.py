print("lista de desejos")

NOME_ARQUIVO = "meus_desejos.txt"

desejos = []

try:
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            desejos.append(linha.strip())
    print(f"meus desejos foram carregados com sucesso do arquivo {NOME_ARQUIVO}'!\n")
except FileNotFoundError:
    print(f"parece sua primeira vez! vamos cria uma lista de desejos para você!\n")
except Exception as e:
    print(f"ocorreu um erro ao abrir o arquivo: {e}\n")

def salvar_desejos(lista_de_desejos):
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            for desejos in lista_de_desejos:
                arquivo.write(desejos + "\n")
    except Exception as e:
        print(f"ocorreu um erro ao salvar os desejos: {e}")
        
while True:
    print("\n--- o que voce quer fazer? ---\n")
    print("1 - mostrar desejos")
    print("2 - salvar desejos")
    print("3 - remover desejos")
    print("4 - sair")

    opcao = input("escolha uma opção 1 a 4: ")

    if opcao == "1":
        novos_desejos = input("Qual e o seu desejo do futuro? ")
        if novos_desejos.strip():
            desejos.append(novos_desejos.strip())
            salvar_desejos(desejos)
        else:
            print("desejo nao pode estar vazio!")
    elif opcao == "2":
        print("\nmeus desejos para o futuro")
        if not desejos:
            print("não há desejos para o futuro, que tal adicionar um? ")
        else:
            for desejo in desejos:
                print(f"- {desejo}")
    elif opcao == "3":
        print("remover desejos")
        if not desejos:
            print("não há desejos para remover.")
        else:
            for i, desejo in enumerate(desejos):
                print(f"{i+1} - {desejo}")
            print("---------------------------")
            try:
                indice = int(input("Digite o número do desejo que deseja remover: "))
                if 1 <= indice <= len(desejos):
                    removido = desejos.pop(indice - 1)
                    salvar_desejos(desejos)
                    print(f"Desejo '{removido}' removido com sucesso.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    elif opcao == "4":
        print("até logo!")
        break
 