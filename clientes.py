import json
import os

# Caminho do arquivo JSON
dados_arquivo = 'clientes.json'

# Dicionário de clientes (será carregado do arquivo)
clientes = {}

# Funções de manipulação de arquivo
def carregar_dados():
    """Carrega os clientes do arquivo JSON."""
    if os.path.exists(dados_arquivo): # Verifica se o arquivo existe
        with open(dados_arquivo, 'r', encoding='utf-8') as arquivo: # Abre o arquivo em modo leitura
            return json.load(arquivo) # Carrega o conteúdo do arquivo JSON para um dicionário
    return {}

def salvar_dados(dados):
    """Salva o dicionário de clientes no arquivo JSON."""
    with open(dados_arquivo, 'w', encoding='utf-8') as arquivo: # Abre o arquivo em modo escrita
        json.dump(dados, arquivo, ensure_ascii=False, indent=4) # Salva o dicionário no arquivo JSON
    return True 

# Funções do sistema de cadastro
def listar_clientes(): # Função para listar clientes
    """Lista todos os clientes cadastrados."""
    if clientes: # Verifica se há clientes
        print("\nLista de clientes cadastrados:") # Verifica se há clientes cadastrados
        for nome, dados in clientes.items(): # Itera sobre os clientes
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}") # Exibe os dados do cliente
    else: # Se não houver clientes
        print("\nNenhum cliente cadastrado.") # Mensagem caso não haja clientes cadastrados

def cadastrar_cliente(nome, telefone, email): # Função para cadastrar clientes
    """Cadastra um novo cliente."""
    if nome in clientes:   # Verifica se o cliente já está cadastrado
        print(" Cliente já cadastrado!") # Verifica se o cliente já está cadastrado
    else:
        clientes[nome] = {"telefone": telefone, "email": email} # Adiciona o cliente ao dicionário
        print(f"Cliente '{nome}' cadastrado com sucesso.") # Mensagem de sucesso

def remover_cliente(nome): # Função para remover clientes
    """Remove um cliente do cadastro."""
    if nome in clientes:  # Verifica se o cliente está cadastrado
        del clientes[nome] # Remove o cliente do dicionário
        print(f" Cliente '{nome}' removido com sucesso.") # Mensagem de sucesso
    else: 
        print(" Cliente não encontrado.") # Mensagem caso o cliente não seja encontrado

# Menu principal
def sistema_principal():
    global clientes
    clientes = carregar_dados()

    while True:
        print("\n=== Sistema de Cadastro de Clientes ===")
        print("1 - Listar clientes")
        print("2 - Cadastrar cliente")
        print("3 - Remover cliente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            nome = input("Nome do cliente: ").strip()
            telefone = input("Telefone: ").strip()
            email = input("Email: ").strip()
            cadastrar_cliente(nome, telefone, email)
            salvar_dados(clientes)
        elif opcao == "3":
            nome = input("Nome do cliente a remover: ").strip()
            remover_cliente(nome)
            salvar_dados(clientes)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print(" Opção inválida! Tente novamente.")

# Execução
if __name__ == "__main__":
    sistema_principal()
