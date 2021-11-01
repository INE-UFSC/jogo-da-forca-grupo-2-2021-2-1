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
import game

def _ChooseRandomWord():
    num_words = len(database.words)
    index_random_word = random.randint(0, num_words-1)
    return database.words[index_random_word]

while True:  # Loop para iniciar o jogo
    while True:  # Loop para pegar a resposta do usuário
        start = input('Você deseja iniciar um jogo de forca? [S/N]').upper().strip()

        if start == 'N' or start == 'S':
            break
        print('Coloque "S" para comecar o jogo ou "N" para sair do jogo')

    if start == 'N':  # Finaliza o jogo caso o usuário não queira jogar
        print('Fechando o jogo...')
        break

    # Busca uma palavra aleatória
    word=_ChooseRandomWord()
    game.Play(word)

    # "Criptografar" e mostrar a palavra para o usuário
    # Manter um array com as letras já escolhidas para o usuário e ir mostrando gradativamente ao usuário
    # Manter um controle da quantidade de vidas e tentativas do usuário
    # Determinar se ganhou ou não
