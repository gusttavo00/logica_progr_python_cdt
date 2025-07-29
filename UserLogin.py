"É um sistema simples com login e cálculo de média de notas. "
"Ele valida o usuário e senha, permite cadastrar um novo usuário se não existir"
"recebe notas de um aluno, calcula a média e mostra se foi aprovado, em recuperação ou reprovado."

usuarios = {
    "admin": "admin123",
    "aluno1": "senha1",
}

def validar_usuario(usuario, senha):
    return usuario in usuarios and usuarios[usuario] == senha

def cadastrar_usuario(usuario, senha):
    usuarios[usuario] = senha
    print(f"Usuário '{usuario}' cadastrado com sucesso!")

def saudacoes(nome):
    nome = nome.strip().title()
    if nome:
        print(f"Olá, {nome}! Bem-vindo(a)!")
        return nome
    return None

def obter_notas():
    entrada = input("Digite as notas do aluno separadas por vírgula: ")
    try:
        notas = [float(nota.strip()) for nota in entrada.split(",")]
        return notas
    except ValueError:
        return []

def validar_notas(notas):
    return all(0 <= nota <= 10 for nota in notas)

def calcular_media(notas):
    if not validar_notas(notas):
        return None
    return sum(notas) / len(notas)

def verificar_se_passou(media):
    if media is None:
        return "Média inválida."
    elif media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def maior_menor_nota(notas):
    if not validar_notas(notas):
        print("Notas inválidas. Por favor, insira notas entre 0 e 10.")
        return
    print(f"Maior nota: {max(notas):.2f}")
    print(f"Menor nota: {min(notas):.2f}")

def main():
    print("=== Login ===")
    usuario = input("Usuário: ").strip()

    if usuario not in usuarios:
        print("Usuário não encontrado.")
        escolha = input("Deseja cadastrar este usuário? (s/n): ").lower()
        if escolha == 's':
            nova_senha = input("Digite a nova senha: ").strip()
            cadastrar_usuario(usuario, nova_senha)
        else:
            print("Encerrando o programa.")
            return

    senha = input("Senha: ").strip()

    if not validar_usuario(usuario, senha):
        print("Usuário ou senha inválidos.")
        return

    print(f"Login bem-sucedido! Bem-vindo(a), {usuario}.")

    nome = saudacoes(input("Digite seu nome: "))
    notas = obter_notas()
    media = calcular_media(notas)
    resultado = verificar_se_passou(media)

    if nome:
        print(f"Vamos calcular sua média, {nome}.")

    if media is not None: 
        print(f"A média das notas é: {media:.2f}") 
        print(f"Resultado: {resultado}")
        maior_menor_nota(notas)
    else:
        print("Notas inválidas. Por favor, insira valores entre 0 e 10.")

if __name__ == "__main__":
    main()
