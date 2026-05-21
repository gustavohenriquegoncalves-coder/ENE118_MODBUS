# Aplicação Modbus TCP em Python

Este projeto implementa uma aplicação cliente-servidor utilizando o protocolo Modbus TCP em Python.

A aplicação permite a leitura e escrita de Holding Registers, escrita e leitura de valores `float` utilizando dois registradores consecutivos e manipulação individual dos bits de um registrador.

## Estrutura do projeto

```text
ProjetoModbus/
├── servidor/
│   ├── servidormodbus.py
│   └── main.py
│
├── cliente/
│   ├── clientemodbus.py
│   ├── interface_usuario.py
│   ├── main.py
│   └── exemplos/
│       ├── __init__.py
│       ├── exemplo_float.py
│       └── exemplo_bits.py
│
├── requirements.txt
├── README.md
└── .gitignore