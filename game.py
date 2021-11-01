def Play(word):   #funçao da logica do jogo
    num_lifes=5
    used_letters=[ ]  #lista das letras utilizadas

    print("Palavra secreta:",end="  ") #printa as underlines correspondentes a cada letra da palavra
    for i in word:
        print(" _",end=" ")
    print("")
    
    while True:
        num_correct_letters=check_word_in_used_letters=0
        print(f"Você tem {num_lifes} chances")
        print("Letras selecionadas:  ",end=" ")
        for i in used_letters:   # printa as letras já selecionadas
            print(i,end=" ")
        print("")
        while True:
            last_letter=input('Digite uma letra:  ')
            if last_letter in used_letters:
                print("A letra já foi selecionada")
            else:
                used_letters.append(last_letter) 
                break
                
        for i in word:  
            if i==last_letter:
                num_correct_letters+=1  #variável contadora para verificar se a letra está correta
       
        for i in word:   #printa as underlines ou as letras acertadas
            if i in used_letters:
                print(i,end='  ')
            else:
                print('_',end=' ')
        print("")
        
        if num_correct_letters==0: #variável que desconta as chances se a letra estiver incorreta
            num_lifes-=1
            print('Você errou a letra')
        
        for i in word:  #variável para verificar se a palavra está correta
            if i in used_letters:
                check_word_in_used_letters+=1
        
        if check_word_in_used_letters==len(word): #condições para o fim do jogo
            print("Parabéns você venceu")
            break   
        if num_lifes==0:
            print("Acabaram suas chances")
            break
        
        
        
    
    
