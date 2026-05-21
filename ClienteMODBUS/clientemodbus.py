from pymodbus.client import ModbusTcpClient


class ClienteMODBUS:

    def __init__(self, server_ip="localhost", porta=502):
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)

    def conectar(self):
        return self._cliente.connect()

    def fechar(self):
        self._cliente.close()

    def ler_holding_registers(self, endereco, quantidade):
        resposta = self._cliente.read_holding_registers(
            address=endereco,
            count=quantidade,
            device_id=1
        )

        if resposta and not resposta.isError():
            return resposta.registers

        return None

    def ler_holding_register(self, endereco):
        registradores = self.ler_holding_registers(endereco, 1)

        if registradores is None:
            return None

        return registradores[0]

    def escrever_holding_register(self, endereco, valor):
        """
        Escreve um valor inteiro em um Holding Register.
        """
        resposta = self._cliente.write_register(
            address=endereco,
            value=valor,
            device_id=1
        )

        return resposta and not resposta.isError()

    def escrever_holding_registers(self, endereco, valores):
        """
        Escreve vários Holding Registers consecutivos.
        """
        resposta = self._cliente.write_registers(
            address=endereco,
            values=valores,
            device_id=1
        )

        return resposta and not resposta.isError()

    def escrever_float(self, endereco, valor):
        registradores = self._cliente.convert_to_registers(
            float(valor),
            self._cliente.DATATYPE.FLOAT32
        )

        return self.escrever_holding_registers(endereco, registradores)

    def ler_float(self, endereco):
        registradores = self.ler_holding_registers(endereco, 2)

        if registradores is None:
            return None

        valor = self._cliente.convert_from_registers(
            registradores,
            self._cliente.DATATYPE.FLOAT32
        )

        return valor

    def ler_bits_registrador(self, endereco):
        registradores = self.ler_holding_registers(endereco, 1)

        if registradores is None:
            return None

        bits = self._cliente.convert_from_registers(
            registradores,
            self._cliente.DATATYPE.BITS
        )

        return bits[:16]

    def alterar_bit_registrador(self, endereco, posicao_bit, novo_estado):
        bits = self.ler_bits_registrador(endereco)

        if bits is None:
            return False

        # Altera somente o bit escolhido na lista.
        bits[posicao_bit] = bool(novo_estado)

        # Converte a lista de bits novamente para registrador usando PyModbus.
        registradores = self._cliente.convert_to_registers(
            bits,
            self._cliente.DATATYPE.BITS
        )

        # Como estamos alterando apenas um Holding Register,
        # escrevemos novamente a partir do mesmo endereço.
        return self.escrever_holding_registers(endereco, registradores)