def Play(word):
    # Function that has the logic of the game
    # Checks if the letter typed matches the word, and gives feedback to the player according to the result

    num_lifes = 5
    used_letters = []

    print('Palavra secreta:', end='')
    for i in word:
        print(' _', end='')
    print('')

    while True:
        num_correct_letters = 0
        check_word_in_used_letters = 0

        print(f'Você tem {num_lifes} chances')
        print('Letras selecionadas:  ', end='')

        for i in used_letters:
            print(i, end='')
        print('')

        while True:
            last_letter = input('Digite uma letra: ')
            if last_letter in used_letters:
                print('A letra já foi selecionada')
            else:
                used_letters.append(last_letter) 
                break

        for i in word:  
            if i == last_letter:
                num_correct_letters += 1

        for i in word:
            if i in used_letters:
                print(i, end='')
            else:
                print('_', end='')
        print('')

        if num_correct_letters == 0:
            num_lifes -= 1
            print('Você errou a letra')

        for i in word:
            if i in used_letters:
                check_word_in_used_letters += 1

        if check_word_in_used_letters == len(word):
            print('Parabéns você venceu')
            break   
        if num_lifes==0:
            print('Acabaram suas chances')
            break
