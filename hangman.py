import random
def hangman():
    list_of_words=['hangman','tree','india','january','border','image','promise','film','kids','lungs','doll','rhyme','damage']
    word=random.choice(list_of_words)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        if main_word==word:
            print(main_word)
            print("you won")
            break

        
        print ("guess a word",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
        
            if turns==9:
                print("9 turns left!!!")
                print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            if turns==8:
                print("8 turns left!!!")
                print("   _____ \n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            if turns==7:
                print("7 turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |        \n"
                  "__|__\n")
            if turns==6:
                print("6 turns left")
                print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            if turns==5:
                print("5 turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |        \n"
                  "__|__\n")
            if turns==4:
                print("4 turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |        \n"
                  "__|__\n")
            if turns==3:
                print("3 turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     |  \n"
                  "  |    /   \n"
                  "__|__\n")
            if turns==2:
                print("2 turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     |  \n"
                  "  |    / \ \n"
                  "__|__\n")
            if turns==1:
                print("1 turns left")
                print("hangman is on his last breadth")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|  \n"
                  "  |    / \ \n"
                  "__|__\n")
            if turns==0:
                print("no turns left")
                print("  _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
                print("you lose")
                print("you let a good man die")


name=input("ENTER YOUR NAME ->")
print("WELCOME",name,"!")
print("-------------------------")
print("try to guess the word in less than 10 attempts")
hangman()
