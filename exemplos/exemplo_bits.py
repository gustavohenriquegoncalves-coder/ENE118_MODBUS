from clientemodbus import ClienteMODBUS


def imprimir_bits(bits):
    for i in range(16):
        print(f"Bit {i:02d}: {bits[i]}")


cliente = ClienteMODBUS("localhost", 502)

if cliente.conectar():
    endereco = 2002

    print("===== EXEMPLO BITS =====")

    print(f"Escrevendo valor inicial 10 em R{endereco}.")
    cliente.escrever_holding_register(endereco, 10)

    valor_antes = cliente.ler_holding_register(endereco)
    bits_antes = cliente.ler_bits_registrador(endereco)

    print(f"\nValor antes da alteração em R{endereco}: {valor_antes}")
    print(f"Lista de bits antes: {bits_antes}")

    print("\nBits antes da alteração:")
    imprimir_bits(bits_antes)

    bit_escolhido = 2
    novo_estado = 1

    print(f"\nAlterando somente o bit {bit_escolhido} para {novo_estado}.")

    cliente.alterar_bit_registrador(endereco, bit_escolhido, novo_estado)

    valor_depois = cliente.ler_holding_register(endereco)
    bits_depois = cliente.ler_bits_registrador(endereco)

    print(f"\nValor depois da alteração em R{endereco}: {valor_depois}")
    print(f"Lista de bits depois: {bits_depois}")

    print("\nBits depois da alteração:")
    imprimir_bits(bits_depois)

    cliente.fechar()
    print("\nConexão encerrada.")

else:
    print("Não foi possível conectar ao servidor.")