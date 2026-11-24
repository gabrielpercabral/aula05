print("Digite 'ajuda'para ver os comandos")

comando = input("Digite o comando: ")

match comando:
    case "oi":
        print("Olá, como posso ajudar?")

    case "tchau":
        print("Até mais!")

    case "ajuda":
        print("Os comandos possíveis são: 'oi', 'tchau' e 'ajuda'")

    case _:
        print("Comando inválido.")