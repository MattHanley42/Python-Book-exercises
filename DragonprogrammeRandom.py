import random
print("Tinkerbell is missing in a castle. You are in a dark room somewhere in this mysterious mansion")
print("In front of you are four doors. Tinkerbell is behind one of them. You must choose one.")
playerChoice = input("Choose 1, 2, 3 or 4...")
if playerChoice == "1":
    print("You have found Tinkerbell alive and well, if a little skinny. Take her home and never let her outside again!")
    print("GAME OVER. YOU WIN")
elif playerChoice == "2":
    print("Tinkerbell isn't there but there is Bad King Biscuits, posessed by the spirit of jazz, blowing her jazz trumpet through her little mouth.")
    print("You can either:")
    print("1) Try to wrestle the jazz trumpet from her.")
    print("2) Try to scat with the cat")
    tinksChoice = input("Type 1 or 2...")
    if tinksChoice == "1":
        print("GAME OVER. Bad King Biscuits beats you to death with the trumpet.")
        print("YOU'VE BEEN KILLED BY JAZZ, THE MOST CONFUSING DEATH OF ALL")
    elif tinksChoice == "2":
        print("You scat to the beat voo-dooing from his scat trumpet.")
        print("GAME OVER. You are still there now, scatting away, succumbed and unable to escape the spirit of jazz.")
    else:
            print("Sorry, you didn't enter 1 or 2, you moron.")
elif playerChoice == "4":
    print("You enter the room. Big Tobes is there.")
    print("He asks you to guess what number he is thinking of, between 1 and 10.")
    number = int(input("What number do you choose?"))
    if number == random.randint(1,10):
          print("Big Tobes howls in disappointment. You guessed correctly.")
          print("He must let you go free.")
          print("GAME OVER. YOU WIN")
    else:
        print("Big Tobes barks that the answer is incorrect.")
        print("You are his prisoner for ever!")
        print("GAME OVER. YOU LOSE...WIN?")
elif playerChoice == "3":
    print("Dirty Harry is there, lying in a circle of white Tinkerbell fluff.")
    print("HE'S PULLED A DIRTY ONE AND CHASED TINKERBELL OUT OF THE 1ST FLOOR CASTLE WINDOW. TINKERBELL CAN'T JUMP NO MORE. SHE HAS BROKEN ALL FOUR OF HER LEGS. GAME OVER.")
else:
    print("What are you, a fucking idiot? Pick a bloody door, 1, 2, 3 or 4!")
print("Run the game again to have another go.")
