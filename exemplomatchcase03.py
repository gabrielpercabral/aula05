print("Veja a lista com os seguintes animais.")
print("cachorro\ngato\nleão\ntigre\n")
animal = input("Digite o nome de um dos animais listados: ")

match animal:
    case "cachorro" | "gato" | "coelho":
        print("Este é um animal doméstico.")

    case "leão" | "tigre" | "javali":
        print("Este é um animal selvagem")

    case _:
        print("Animal inválido ou nome digitado incorretamente.")