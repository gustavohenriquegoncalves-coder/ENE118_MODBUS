from clientemodbus import ClienteMODBUS


class InterfaceUsuario:
    """
    Classe responsável pelo menu e pela interação com o usuário.
    """

    def __init__(self):
        self._cliente = ClienteMODBUS("localhost", 502)

    def executar(self):
        conectado = self._cliente.conectar()

        if not conectado:
            print("Não foi possível conectar ao servidor Modbus.")
            return

        print("Cliente conectado ao servidor Modbus.")

        continuar = True

        while continuar:
            print("\n========== MENU MODBUS ==========")
            print("1 - Ler Holding Register")
            print("2 - Escrever Holding Register")
            print("3 - Escrever float")
            print("4 - Ler float")
            print("5 - Ler bits de um registrador")
            print("6 - Alterar um bit específico")
            print("7 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                endereco = int(input("Endereço do registrador: "))
                valor = self._cliente.ler_holding_register(endereco)
                print(f"Valor em R{endereco}: {valor}")

            elif opcao == "2":
                endereco = int(input("Endereço do registrador: "))
                valor = int(input("Valor inteiro: "))

                if self._cliente.escrever_holding_register(endereco, valor):
                    print("Escrita realizada.")
                else:
                    print("Falha na escrita.")

            elif opcao == "3":
                endereco = int(input("Endereço inicial do float: "))
                valor = float(input("Valor float: "))

                if self._cliente.escrever_float(endereco, valor):
                    print(f"Float escrito em R{endereco} e R{endereco + 1}.")
                else:
                    print("Falha ao escrever float.")

            elif opcao == "4":
                endereco = int(input("Endereço inicial do float: "))
                valor = self._cliente.ler_float(endereco)
                print(f"Float lido: {valor}")

            elif opcao == "5":
                endereco = int(input("Endereço do registrador: "))
                bits = self._cliente.ler_bits_registrador(endereco)

                print(f"Lista de bits de R{endereco}:")
                print(bits)

                for i in range(16):
                    print(f"Bit {i}: {bits[i]}")

            elif opcao == "6":
                endereco = int(input("Endereço do registrador: "))

                bits_antes = self._cliente.ler_bits_registrador(endereco)
                print(f"Bits antes: {bits_antes}")

                posicao = int(input("Qual bit deseja alterar? [0 a 15]: "))
                estado = int(input("Novo estado do bit [0 ou 1]: "))

                if self._cliente.alterar_bit_registrador(endereco, posicao, estado):
                    bits_depois = self._cliente.ler_bits_registrador(endereco)
                    valor_depois = self._cliente.ler_holding_register(endereco)

                    print(f"Bits depois: {bits_depois}")
                    print(f"Novo valor do registrador: {valor_depois}")
                else:
                    print("Falha ao alterar bit.")

            elif opcao == "7":
                continuar = False

            else:
                print("Opção inválida.")

        self._cliente.fechar()
        print("Conexão encerrada.")