#Constante OS
import os

#Variáveis
votos_Eyker = 0
votos_Lauanda = 0
votos_Lucas = 0
votos_Erick = 0
votos_Nulo = 0
votos_Branco = 0
percentual_nulos = 0
percentual_brancos = 0
total_votos = 0
max_votos = 0
resposta = 0
resposta_votacao = 0
candidatos = {}
vencedores = []

#Inicio do LOOP fonte da tabela
while True:
    #Utilizado para apagar o menu anterior após certas seleção
    os.system('cls')

    try:
        #Tabela que aparece inicialmente no programa de votos
        resposta = int(input(f'*****Eleições 2024 para Presidente do Brasil*****'
                             f'{os.linesep}1 - Eyker'
                             f'{os.linesep}2 - Lauanda'
                             f'{os.linesep}3 - Lucas'
                             f'{os.linesep}4 - Erick'
                             f'{os.linesep}5 - Nulo'
                             f'{os.linesep}6 - Branco'
                             f'{os.linesep}7 - Aferir aos resultados da votação'
                             f'{os.linesep}0 - Sair do programa'
                             f'{os.linesep}Seu voto: '))
        #Calculo de votos por resposta
        if resposta == 1:
            votos_Eyker += 1
        elif resposta == 2:
            votos_Lauanda += 1
        elif resposta == 3:
            votos_Lucas += 1
        elif resposta == 4:
            votos_Erick += 1
        elif resposta == 5:
            votos_Nulo += 1
        elif resposta == 6:
            votos_Branco += 1
        elif resposta == 7:
            while True:
                #total de votos válidos
                total_votos = votos_Eyker + votos_Lauanda + votos_Lucas + votos_Erick + votos_Nulo + votos_Branco

                #Percentagens dos votos Nulos e Brancos
                percentual_nulos = (votos_Nulo / total_votos) * 100 if total_votos > 0 else 0
                percentual_brancos = (votos_Branco / total_votos) * 100 if total_votos > 0 else 0

                #Tabela de total de votos por candidato
                print('----------Total de Votos------------------')
                print(f'Total Eyker: {votos_Eyker}')
                print(f'Total Lauanda: {votos_Lauanda}')
                print(f'Total Lucas: {votos_Lucas}')
                print(f'Total Erick: {votos_Erick}')
                print(f'Total Nulo: {votos_Nulo}')
                print(f'Total Branco: {votos_Branco}')
                print(f'Percentual de Votos Nulos: {percentual_nulos:.2f}%')
                print(f'Percentual de Votos em Branco: {percentual_brancos:.2f}%')
                candidatos = {
                    "Eyker": votos_Eyker,
                    "Lauanda": votos_Lauanda,
                    "Lucas": votos_Lucas,
                    "Erick": votos_Erick
                }
                #Calculo de maximo de votos por pessoa para gerar o vencedor
                max_votos = max(candidatos.values())
                vencedores = [nome for nome, votos in candidatos.items() if votos == max_votos]

                #Verificação de empates
                if len(vencedores) > 1:
                    print(f'Houve um empate entre os seguintes candidatos: {", ".join(vencedores)}')
                else:
                    print(f'Vencedor: {vencedores[0]}')

                print('--------------------------------------------')

                #Quando não há votos para nenhum dos candidatos.
                if total_votos == 0:
                    print("Nenhum voto foi registrado.")

                try:
                    resposta_votacao = int(input(f'{os.linesep}Pressione 0 para voltar ao menu de votação'
                                                 f'{os.linesep}Seu voto: '))
                    if resposta_votacao == 0:
                        break
                    else:
                        #Mensagem caso seja digitado um numero não inteiro ou fora da tabela prevista.
                        print("Opção inválida! Tente novamente.")
                        input("Pressione Enter para continuar...")  # Pausar para o usuário ver a mensagem
                except ValueError:
                    print("Digite apenas números inteiros!")
                    input("Pressione Enter para continuar...")  # Pausar para o usuário ver a mensagem

        #Finalizando a tabela
        elif resposta == 0:
            break

        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausar para o usuário ver a mensagem

    except ValueError:
        print("Digite apenas números inteiros!")
        input("Pressione Enter para continuar...")  # Pausar para o usuário ver a mensagem
