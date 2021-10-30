"""
JOGO DA FORCA
Coisas a implementar:
- Array com palavras a serem escolhidas quando um jogo começar
- Função para gerar um número inteiro aleatório de 0 até comprimento do Array de palavras
- Função para printar no console a linha mostrando quantidade de letras na palavra, as letras já acertadas e vidas restantes
- Lógica de restart de jogo
"""
import database
import random
import logica

def ChooseRandomWord():
    quantWords = len(database.arrayPalavras)
    index = random.randint(0, quantWords-1)
    return database.arrayPalavras[index]


while True:  # Loop para iniciar o jogo
    while True:  # Loop para pegar a resposta do usuário
        resp = input(
            'Você deseja iniciar um jogo de forca? [S/N]').upper().strip()

        if resp == 'N' or resp == 'S':
            break
        print('Coloque "S" para comecar o jogo ou "N" para sair do jogo')

    if resp == 'N':  # Finaliza o jogo caso o usuário não queira jogar
        print('Fechando o jogo...')
        break

    # Busca uma palavra aleatória
    word=ChooseRandomWord()
    logica.forca(word)

    # "Criptografar" e mostrar a palavra para o usuário
    # Manter um array com as letras já escolhidas para o usuário e ir mostrando gradativamente ao usuário
    # Manter um controle da quantidade de vidas e tentativas do usuário
    # Determinar se ganhou ou não
