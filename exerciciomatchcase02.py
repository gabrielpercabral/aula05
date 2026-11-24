print("Calendário !!!")
print("1. Janeiro\n" \
"2. Fevereiro\n" \
"3. Março\n" \
"4. Abril\n" \
"5. Maio\n" \
"6. Junho\n" \
"7. Julho\n" \
"8. Agosto\n" \
"9. Setembro\n" \
"10. Outubro\n" \
"11. Novembro\n" \
"12. Dezembro\n")

mes = int(input("Digite um número de 1-12 correspondente a um mês: "))

match mes:
    case 1:
        print("Janeiro.")

    case 2:
        print("Fevereiro.")

    case 3:
        print("Março.")

    case 4:
        print("Abril.")

    case 5:
        print("Maio.")

    case 6:
        print("Junho.")

    case 7:
        print("Julho.")

    case 8:
        print("Agosto.")

    case 9:
        print("Setembro.")

    case 10:
        print("Outubro.")

    case 11:
        print("Novembro.")

    case 12:
        print("Dezembro.")

    case _:
        print("Resposta inválida. Tente novamente.")