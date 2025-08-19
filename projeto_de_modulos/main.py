import utilidades
import jogos

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Usar utilidades matemáticas")
        print("2 - Mostrar datas")
        print("3 - Jogar adivinhação")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Soma:", utilidades.soma(2, 3))
            print("Subtração:", utilidades.subtracao(10, 4))
            print("Potência:", utilidades.potencia(2, 8))

        elif opcao == "2":
            print("Hoje:", utilidades.hoje())
            print("Amanhã:", utilidades.amanha())

        elif opcao == "3":
            jogos.jogar()

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
