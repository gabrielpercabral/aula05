nota = float(input("Digite a nota do aluno: "))

match nota:
    case n if n >= 9 and n <= 10:
        print("Conceito A - Excelente!")

    case n if n >= 7 and n < 9:
        print("Conceito B - Bom.")

    case n if n >= 5 and n < 7:
        print("Conceito C - Regular...")

    case n if n <= 5 and n >= 0:
        print("Conceito D - Reprovado ;(")

    case _:
        print("Nota inválida. Favor refazer os cálculos")

# if nota > 10 and nota >= 11:
#     print("Nota inválida. Favor refazer os cálculos.")
# elif nota >= 9:
#     print("Conceito A - Excelente!")
# elif nota >= 7:
#     print("Conceito B - Bom.")
# elif nota >= 5:
#     print("Conceito C - Regular...")
# else:
#     print("Conceito D - Reprovado. :(")


# else:
#     print(" :( ")