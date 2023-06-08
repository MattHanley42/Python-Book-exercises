print("Tinkerbell is missing in a castle. You are in a dark room somewhere in this mysterious mansion")
print("In front of you are three doors. Tinkerbell is behind one of them. You must choose one.")
playerChoice = input("Choose 1, 2 or 3...")
if playerChoice == "1":
    print("You have found Tinkerbell alive and well, if a little skinny. Take her home and never let her outside again!")
    print("GAME OVER. YOU WIN")
elif playerChoice == "2":
    print("Tinkerbell is there but has been posessed by the spirit of jazz and beats you to death with her jazz trumpet.")
    print("GAME OVER. YOU'VE BEEN KILLED BY JAZZ, THE MOST CONFUSING DEATH OF ALL")
elif playerChoice == "3":
    print("You enter the room but in her stupid panic the Stinks runs away through an open window and jumps one story down.")
    print("TINKERBELL CAN'T JUMP NO MORE. SHE BREAKS ALL FOUR OF HER LEGS. GAME OVER.")
else:
    print("What are you, a fucking idiot? Pick a bloody door!")
print("Run the game again to have another go.")
