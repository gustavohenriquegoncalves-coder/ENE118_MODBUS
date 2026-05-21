from clientemodbus import ClienteMODBUS


cliente = ClienteMODBUS("localhost", 502)

if cliente.conectar():
    endereco = 2000
    valor = 25.75

    print("===== EXEMPLO FLOAT =====")

    cliente.escrever_float(endereco, valor)

    registradores = cliente.ler_holding_registers(endereco, 2)
    valor_lido = cliente.ler_float(endereco)

    print(f"Valor float escrito: {valor}")
    print(f"Registradores usados: R{endereco} e R{endereco + 1}")
    print(f"Valores brutos dos registradores: {registradores}")
    print(f"Valor float lido: {valor_lido}")

    cliente.fechar()
else:
    print("Não foi possível conectar ao servidor.")