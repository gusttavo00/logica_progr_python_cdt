import re

class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"


class Cadastro:
    def __init__(self):
        self.usuarios = []

    def validar_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        if len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        return nome

    def validar_idade(self, idade):
        try:
            idade = int(idade)
            if idade <= 0:
                raise ValueError("A idade deve ser maior que 0.")
            return idade
        except ValueError:
            raise ValueError("Idade inválida. Digite apenas números inteiros positivos.")

    def validar_email(self, email):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(padrao, email):
            raise ValueError("E-mail inválido. Use o formato nome@dominio.com")
        return email

    def cadastrar(self):
        try:
            nome = input("Digite seu nome: ")
            nome = self.validar_nome(nome)

            idade = input("Digite sua idade: ")
            idade = self.validar_idade(idade)

            email = input("Digite seu e-mail: ")
            email = self.validar_email(email)

            usuario = Usuario(nome, idade, email)
            self.usuarios.append(usuario)

            print("\nUsuário cadastrado com sucesso!")
            print(usuario)

        except ValueError as e:
            print(f"\nErro de validação: {e}")
        except Exception as e:
            print(f"\nErro inesperado: {e}")
