def play(word):
    # Function that has the logic of the game
    # Checks if the letter typed matches the word
    # And gives feedback to the player according to the result

    num_lifes = 6
    used_letters = []
    
    print('            ____       ')
    print('           /        l      ')
    print('           l               ')
    print('           l               ')
    print('           l               ')
    print('           l               ')
    print('                           ')

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
            last_letter = input('Digite uma letra: ').upper()
            if last_letter in used_letters:
                print('A letra já foi selecionada')
            else:
                used_letters.append(last_letter) 
                break

        for i in word:  
            if i == last_letter:
                num_correct_letters += 1

        if num_correct_letters == 0:
            num_lifes -= 1
            print('Você errou a letra')
            
        if num_lifes==6:
            print('            ____       ')
            print('           /        l      ')
            print('           l               ')
            print('           l               ')
            print('           l               ')
            print('           l               ')
            print('                           ')
       
        elif num_lifes==5:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l               ')
            print('           l               ')
            print('           l               ')
            print('                           ')
        
        elif num_lifes==4:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l        l     ')
            print('           l        l      ')
            print('           l               ')
            print('                           ')
        
        elif num_lifes==3:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l      / l     ')
            print('           l        l      ')
            print('           l               ')
            print('                           ')
        
        elif num_lifes==2:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l      / l \    ')
            print('           l        l      ')
            print('           l               ')
            print('                           ')
       
        elif num_lifes==1:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l      / l \    ')
            print('           l        l      ')
            print('           l       /       ')
            print('                           ')
        
        else:
            print('            ____      ')
            print('           /        l     ')
            print('           l       O     ')
            print('           l      / l \    ')
            print('           l        l      ')
            print('           l       / \     ')
            print('                           ')
            
        for i in word:
            if i in used_letters:
                print(i, end=' ')
            else:
                print('_', end=' ')
        print('')

        for i in word:
            if i in used_letters:
                check_word_in_used_letters += 1

        if check_word_in_used_letters == len(word):
            print('Parabéns você venceu')
            break   
        if num_lifes==0:
            print('Acabaram suas chances')
            break