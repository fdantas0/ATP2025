import random

soma = 21
print("Jogo dos 21 fósforos. Cada jogador pode tirar entre 1 a 4 fósforos. Quem ficar com o último perde!")

play = int(input("Quem começa a jogar? (1=TU ou 2=COMPUTADOR): "))

if play == 1:
    while soma > 1:
        n = int(input("Quantos fósforos queres tirar (1-4)? "))
        while n < 1 or n > 4 or n > soma:
            print("Não podes tirar esse número de fósforos. Só podes tirar entre 1 a 4 fósforos e não podes tirar mais do que os restantes.")
            n = int(input("Quantos fósforos queres tirar (1-4)? "))

        soma -= n
        print(f"Tiraste {n} fósforos. Restam {soma} fósforos.")

        if soma == 1:
            print("Parabéns, ganhaste o jogo!")
            break

        if soma % 5 != 1:
            comp = (soma - 1) % 5
            if comp == 0:
                comp = random.randint(1, min(4, soma - 1))
        else:
            comp = random.randint(1, min(4, soma - 1))

        soma -= comp
        print(f"O computador tirou {comp} fósforos. Restam {soma} fósforos.")

        if soma == 1:
            print("O computador ganhou, fica para uma próxima.")
            break

else:
    comp = random.randint(1, 4)
    soma -= comp
    print(f"O computador tirou {comp} fósforos. Restam {soma} fósforos.")

    while soma > 1:
        n = int(input("Quantos fósforos queres tirar (1-4)? "))
        while n < 1 or n > 4 or n > soma:
            print("Não podes tirar esse número de fósforos. Só podes tirar entre 1 a 4 fósforos e não podes tirar mais do que os restantes.")
            n = int(input("Quantos fósforos queres tirar (1-4)? "))

        soma -= n
        print(f"Tiraste {n} fósforos. Restam {soma} fósforos.")

        if soma == 1:
            print("Parabéns, ganhaste o jogo!")
            break

        if soma % 5 != 1:
            comp = (soma - 1) % 5
            if comp == 0:
                comp = random.randint(1, min(4, soma - 1))
        else:
            comp = random.randint(1, min(4, soma - 1))

        soma -= comp
        print(f"O computador tirou {comp} fósforos. Restam {soma} fósforos.")

        if soma == 1:
            print("O computador ganhou, fica para uma próxima.")
            break
