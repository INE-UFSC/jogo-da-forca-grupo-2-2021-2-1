def forca(word):   #funçao da logica do jogo
    vida=5
    arrayLetras=[ ]  #lista das letras utilizadas
    
    
    print("Palavra secreta:",end="  ") #printa as underlines correspondentes a cada letra da palavra
    for i in word:
        print(" _",end=" ")
    print("")
    
    while True:
        cont=fim=0
        print(f"Você tem {vida} chances")
        print("Letras selecionadas:  ",end=" ")
        for i in arrayLetras:   # printa as letras já selecionadas
            print(i,end=" ")
        print("")
        while True:
            l=input('Digite uma letra:  ')
            if l in arrayLetras:
                print("A letra já foi selecionada")
            else:
                arrayLetras.append(l) 
                break
                
        for i in word:  
            if i==l:
                cont+=1  #variável contadora para verificar se a letra está correta
       
        for i in word:   #printa as underlines ou as letras acertadas
            if i in arrayLetras:
                print(i,end='  ')
            else:
                print('_',end=' ')
        print("")
        
        if cont==0: #variável que desconta as chances se a letra estiver incorreta
            vida-=1
            print('Você errou a letra')
        
        for i in word:  #variável para verificar se a palavra está correta
            if i in arrayLetras:
                fim+=1
        
        if fim==len(word): #condições para o fim do jogo
            print("Parabéns você venceu")
            break   
        if vida==0:
            print("Acabaram suas chances")
            break
        
        
        
    
    
