rodadas = int(input("Quantas vezes você quer jogar? "))
venceu= 0
perdeu= 0
empate= 0

for i in range(rodadas):

    from random import randint
    oponente = randint(0,2)

    print("Opções: pedra (0), papel (1) e tesoura(2) ")

    jogador = int(input("Escolha entre pedra, papel ou tesoura. "))
    if jogador != 0 and jogador != 1 and jogador != 2:
        print("Você escolheu um valor inválido.")


    if oponente == jogador:
        print(f"O computador escolhe: {oponente}.")
        print ("Empate.")
        empate = empate +1
    else:
        if oponente == 0 and jogador == 1:
            print(f"O computador escolhe: {oponente}")
            print("Parabéns, você venceu!")
            venceu = venceu + 1 
        else:
            if oponente == 0 and jogador ==2:
                print(f"O computador escolhe: {oponente}")
                print("Que pena, você perdeu!")
                perdeu = perdeu + 1
            else:
                if oponente == 1 and jogador == 0:
                    print(f"O computador escolhe: {oponente}")
                    print("Que pena, você perdeu!")
                    perdeu = perdeu + 1
                    
                else:
                    if oponente ==1 and jogador ==2:
                        print(f"O computador escolhe: {oponente}")
                        print("Parabéns, você venceu!")
                        venceu = venceu + 1
                    else:
                        if oponente ==2 and jogador ==0:
                            print(f"O computador escolhe: {oponente}")
                            print("Parabéns, você venceu!")
                            venceu = venceu + 1
                        else:
                            if oponente ==2 and jogador == 1:
                                print(f"O computador escolhe: {oponente}")
                                print("Que pena, você perdeu!")
                                perdeu = perdeu + 1


if venceu> perdeu:
    print (f"O computador venceu {perdeu} vezes")
    print (f"Você venceu {venceu} vezes")
    print (f"O jogo empatou {empate} vezes")
    print("VOCÊ É O CAMPEÃO! :) ")
else:
    if venceu < perdeu:
        print (f"O computador venceu {perdeu} vezes")
        print (f"Você venceu {venceu} vezes")
        print (f"O jogo empatou {empate} vezes")
        print("O COMPUTADOR VENCEU! :( .")
    else:
        if venceu == perdeu:
            print (f"O computador venceu {perdeu} vezes")
            print (f"Você venceu {venceu} vezes")
            print (f"O jogo empatou {empate} vezes")
            print("O campeonato empatou.")
        else:
            if empate > venceu and empate > perdeu:
                print (f"O computador venceu {perdeu} vezes")
                print (f"Você venceu {venceu} vezes")
                print (f"O jogo empatou {empate} vezes")
                print("O campeonato empatou")