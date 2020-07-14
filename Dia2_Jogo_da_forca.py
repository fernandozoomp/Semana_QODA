
## Define as palavras e realiza o sorteio aleatório

import random

def get_word():
    lista_palavras = ['ornitorrinco','tamandua', 'elefante', 'jabuti', 'tartaruga', 'macaco', 'cachorro', 'girafa', 'rinoceronte', 'gato', 'pato', 'papagaio', 'baleia', 'ovelha']
    word = random.choice(lista_palavras)
    return word.upper()

## Contabiliza as letras e informa o usuário das dicas

def play(word):
    word_completion = "-" * len(word) 
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n                       ********** JOGO DA FORCA **********")
    print()
    print(f'\n                        Super Dica: É um nome de animal com {len(word)} letras!')
    print(Corpo_forca(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("\n                     Diga uma letra ou tente adivinhar a palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'\n                      Xiii, você já tentou a letra {guess}')
            elif guess not in word:
                print(f'\n                      É não deu certo... a letra "{guess}" não está na palavra.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'\n                      Yesss! A letra "{guess}" está na palavra!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'\n                      Oh não! Você já tentou a palavra "{guess}""')
            elif guess != word:
                print(f'\n                      Não foi dessa vez, "{guess}"não é a palavra correta.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\n                             Tá precisando aprender a contar as letras direito....")
        print(Corpo_forca(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("\n                               Muito bem! Você adivinhou a palavra! Levanta a taça que você venceu!")
    else:
        print("\n                               Poxa...Você perdeu!. A palavra era " + word + ", mas tente de novo eu percebi que você está melhorando.")

def Corpo_forca(tries):
    stages = [  # cabeça, tronco e braços e pernas: morte.
                """
                  
                                        --------
                                        |      |
                                        |      O
                                        |     \|/
                                        |      |
                                        |     / \
                                        -

                """,
                # cabeça, tronco e braços, perna
                """
                  
                                        --------
                                        |      |
                                        |      O
                                        |     \|/
                                        |      |
                                        |     / 
                                        -

                """,
                # cabeça, tronco e braços
                """

                                        --------
                                        |      |
                                        |      O
                                        |     \|/
                                        |      |
                                        |      
                                        -

                """,
                # cabeça, tronco e braço
                """

                                        --------
                                        |      |
                                        |      O
                                        |     \|
                                        |      |
                                        |     
                                        -

                """,
                # cabeça e tronco
                """

                                        --------
                                        |      |
                                        |      O
                                        |      |
                                        |      |
                                        |     
                                        -

                """,
                # cabeça
                """

                                        --------
                                        |      |
                                        |      O
                                        |    
                                        |      
                                        |     
                                        -    

                """,
                # vazio
                """

                                        --------
                                        |      |
                                        |      
                                        |    
                                        |      
                                        |     
                                        -

                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("\n                     Que tal jogarmos de novo? (S/N) ").upper() == "S":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()