import random #Importando a biblioteca random

def jogo(): #Criando a função do jogo de adivinhação

    tentativas = 0 #Armazenando o valor 0 para as tentativas

    print("Olá, seja bem-vindo(a) ao jogo de adivinhação, onde o objetivo é acertar o número que o computador sortear de 1 a 50, mas lembrando: a cada jogada o número muda, então que os jogos começem e que a sorte esteja sempre ao seu favor!") #Mensagem de boas vindas

    print("\nEsse jogo foi criado por mim, Lucas.") #Mensagem do criador do jogo

    while True: #Laço de repetição para rodar o jogo até o usuário acertar o número sorteado
        try: #Tentativa de executar o código
            escolhaNumero = input("\nDigite o número que eu adivinhei: ") #O usuário vai digitar o número que o computador sorteou
            escolhaNumero = int(escolhaNumero) #Transformando a variável escolhaNumero para inteiro

            numeroAleatorio = random.randint(1, 50) #Gerando o número aleatório de 1 a 100

            if escolhaNumero == numeroAleatorio: #Se o usuário acertar o número sorteado pelo computador...
                print("\nParabéns! Você adivinhou o número sorteado!") #Mensagem de parabenização 
                
                print(f"\nNúmero sorteado: {numeroAleatorio}") #Mostrando o número que o computador sorteou

                print(f"\nVocê precisou de {tentativas} tentativas para acertar! Será que você consegue melhorar na próxima? 👀") #Exibindo o quanto de tentativas que o usuário precisou para acertar o número sorteado

                break #Parando o programa
            elif escolhaNumero < numeroAleatorio: #Se o usuário escolheu um número abaixo daquele sorteado pelo computador...
                print("\nNúmero adivinhado foi abaixo do número sorteado.") #Exibindo a mensagem de aviso

                print(f"\nNúmero final: {numeroAleatorio}") #Mostrando o número que o computador sorteou

                tentativas += 1 #Adicionando um valor a cada tentativa do usuário
            elif escolhaNumero > 50: #Se o usuário digitou um número acima de 100...
                print("\nDigite apenas números de 1 a 50") #Exibindo a mensagem de aviso
            elif escolhaNumero > numeroAleatorio: #Se o usuário escolheu um número acima daquele sorteado pelo computador...
                print("\nNúmero adivinhado foi acima do número sorteado.") #Exibindo a mensagem de aviso

                print(f"\nNúmero final: {numeroAleatorio}") #Mostrando o número que o computador sorteou

                tentativas += 1 #Adicionando um valor a cada tentativa do usuário
            
        except ValueError: #Caso o usuário digite um caracter diferente do número...
            print("\nDigite apenas números inteiros!") #Mensagem de aviso

jogo() #Execuntando a função do jogo de adivinhação