#DiscordBot RNG Test
#Last Modifeid: 1/19/2025

#this should import the ability to use random for RNG
import random

print("What would you like to roll?\n-Coin\n-d4\n-d6\n-d8\n-d10\n-d12\n-d20\n-d100")

die = input()

check = 0
numcheck = 0

#this loop should check for what the user wants to roll or flip dice-wise.
while check == 0:
    if die == "coin" or die == "Coin":
        check = 1
        print("How many coins would you like to flip?")
        num = int(input())

    elif die == "d4" or die == "D4":
        check = 1
        print("How many d4s would you like to flip?")
        num = int(input())

    elif die == "d6" or die == "D6":
        check = 1
        print("How many d6s would you like to flip?")
        num = int(input())

    elif die == "d8" or die == "D8":
        check = 1
        print("How many d8s would you like to flip?")
        num = int(input())

    elif die == "d10" or die == "D10":
        check = 1
        print("How many d10s would you like to flip?")
        num = int(input())

    elif die == "d12" or die == "D12":
        check = 1
        print("How many d12s would you like to flip?")
        num = int(input())

    elif die == "d20" or die == "D20":
        check = 1
        print("How many d20s would you like to flip?")
        num = int(input())

    elif die == "d100" or die == "D100":
        check = 1
        print("How many d100s would you like to flip?")
        num = int(input())

    else:
        print("Please type a valid response from the list.")
        die = input()

#These variables are just declared here for use in the next section for what the results will be and for i to be reused in the for loops.    
i = 0
result = ""

print("Would you like the total combined value (doesn't work for coins)? Yes/No")

choice = input()

#This if statement is just a check for if the user wants a total of the combined dice rolls or not. A yes will only display the total. It will also print the values of the rolls/total.
if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y" or choice == "YES" or choice == "YEs" or choice == "YeS" or choice == "yES" or choice == "yeS":
    total = 0
    for i in range(num):
        if die == "d4" or die == "D4":
            total += random.randint(1, 4)

        elif die == "d6" or die == "D6":
            total += random.randint(1, 6)

        elif die == "d8" or die == "D8":
            total += random.rand(1, 8)

        elif die == "d10" or die == "D10":
            total += random.randint(1, 10)

        elif die == "d12" or die == "D12":
            total += random.randint(1, 12)

        elif die == "d20" or die == "D20":
            total += random.randint(1, 20)

        else:
            total += random.randint(1, 100)

    print("Your total is:\n" + str(total))

elif choice == "no" or choice == "No" or choice == "n" or choice == "N" or choice == "NO" or choice == "nO":
    print("Your rolls are:")

    if die == "coin" or die == "Coin":
        for i in range(num):
            result = random.randint(1, 2)

            if result == 1:
                print("Heads")
        
            else:
                print("Tails")

    elif die == "d4" or die == "D4":
        for i in range(num):
            print(random.randint(1, 4))

    elif die == "d6" or die == "D6":
        for i in range(num):
            print(random.randint(1, 6))

    elif die == "d8" or die == "D8":
        for i in range(num):
            print(random.rand(1, 8))

    elif die == "d10" or die == "D10":
        for i in range(num):
            print(random.randint(1, 10))

    elif die == "d12" or die == "D12":
        for i in range(num):
            print(random.randint(1, 12))

    elif die == "d20" or die == "D20":
        for i in range(num):
            print(random.randint(1, 20))

    else:
        for i in range(num):
            print(random.randint(1, 100))

else:
    print("You decided to pick a choice that I was too lazy to code after doing this all in one sitting. Start the program again.")
    exit()