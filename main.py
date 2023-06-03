#validação de um ano bissexto

year = int(input("Digite um ano qualquer: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Ano Bissexto.")
        else:
            print("Ano NÃO Bissexto.")
    else:
        print("Ano Bissexto.")
else:
    print("Ano NÃO Bissexto.")

