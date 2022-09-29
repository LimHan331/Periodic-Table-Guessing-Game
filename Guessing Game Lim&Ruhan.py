import random
words = ['H','He','Li','Zr','Bh','Lu','Ne','Ar','Kr','Xe']
answer = ["Hydrogen" , "Helium", "Lithium","Zirconium,'Bohrium" ,"Lutelium",'Neon','Argon','Krypton','Xenon']
player_name = input("Hey, whats's your name")
knows_to_play = input("Do you know how to play?")
print('okay! ' + player_name )
start_game = input('Are you ready to start guessing element atomic number between 1 and 10 :' )
print(' Welcome to the perodic table guessing game')
print('')

words = random.choice(words)
print (words)

print("Guess an element")

guesses = ''
turns = 2

while turns > 0:
    

    failed = 0
    for char in words:
    
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            print(char, end=" ")
            

            failed += 1

    if failed == 0:
        print ("You Win")
        print("The words is : ",answer )
        break
    print()
    guess = input("guess a words:")

    guesses += guess
    if guess not in words:

        turns -= 1
        print("Wrong")
        print("You have", + turns,'more guesses')

        if turns ==0 :
            print ("You Loose, try again next time")
    
