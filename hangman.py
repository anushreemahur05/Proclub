import random

def hangman():
    print("Choose the category:\n 1.Marvel Universe Characters \n 2.DC Universe character \n 3.Classic Romantic Movies \n 4.Animated Movies \n 5.Animals")
    choice=input("Select a number: ")
    choice=int(choice)
    #predefined list of words for different category
    marvel=["ironman","deadpool","spiderman","captain america","black widow","hulk","thor","clint barton","wolverine","starlord","groot","black panter","antman"]
    dc=["batman","superman","joker","flash","aquaman","wonder woman","green lantern","green arrow","lex luthor","martian manhunter"]
    rom=["the notebook","when harry met sally","pretty woman","titanic","notting hill","before sunrise","a walk to remember","love actually"]
    animals=["giraffe","bengal tiger","elephant","rabbit","red fox","spotted deer","bison","rhinoceros","asiatic lion","sloth bear","indian leopard","red panda"]
    animated=["happy feet","frozen","coco","smallfoot","brave","inside out","tangled","ratatouille","shrek","kunf fu panda","toy story","finding dory","finding nemo"]

    if choice==1:
        print("CATEGORY: MARVEL UNIVERSE CHARATERS")
        word=random.choice(marvel)
    elif choice==2:
        print("CATEGORY: DC UNIVERSE CHARATERS")
        word=random.choice(dc)
    elif choice==3:
        print("CATEGORY: CLASSIC ROMANTIC MOVIES")
        word=random.choice(rom)
    elif choice==4:
        print("CATEGORY: ANIMATED MOVIES ")
        word=random.choice(animated)
    elif choice==5:
        print("CATEGORY: ANIMALS")
        word=random.choice(animals)
    else:
        print("Enter a valid category number.")
        choice=input()


    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns=10     #maximum number of turns the player will get
    guessmade='' #creates an variable with an empty value

    while len(word)>0:    #the length of the word randomly slected should not be zero (or turns>0)
        main=""

        for letter in word:
            if letter in guessmade:
                    main=main+letter

            else:
                if letter == ' ':
                    main=main+" "
                else:
                    main=main+"_"+" "

        if main == word:
            print("The word is:"+ main)
            print("You win!")
            break

        print("\nGUESS THE WORD  " + main)
        guess=input("Enter a character: ")

        if guess in validLetters:    # every input character will be stored in guessmade
            validLetters=validLetters.replace(guess,'')
            guessmade = guessmade + guess
            print ("\n"+validLetters)

        else:
            print("Enter a valid non-repeat character:")
            guess = input()

        if guess not in word:
            turns = turns - 1
            print("WRONG! ")
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                print("\n The word was:"+ main)
                break


print("Lets play HANGMAN!")
name= input("What is your name? ")
print("Hey " + name.title()+ "!" )
print("-------------------------------------------------------")
print("Try to guess the word in less than 10 attempts!")
hangman()
print ("\nEND")
print("--------------------------------------------------------")
