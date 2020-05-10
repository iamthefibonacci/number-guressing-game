import time as t
print(" WELCOME TO GUESSING NUMBER GAME")
print("*****GAME INSTRUCTIONS*******")
print("1: You have one only 3 chances to play a number to WIN!!")
print("2: Only number between 0 and 60 are permissible!!")
print("3: Should you enter wrong inputs. We record that as an attempt. A TOUCH IS A MOVE!!")
print("4: The game allows to Re-play for a maximum of 2 times, thus is you lose in the 1st chance!!")
print("   ")
print("GAME STARTED NOW\n")

def myGuessNumberGame():
    '''The function to play the game'''
    count =0
    global name
    name= input("Please your name to start the Game!!\n")
    trials =["1st","2nd","3rd"]
    winNumbers= [34,6,56,23,12,21]
    check =True
    option = input(f"{name} are you sure you want to continue playing the GAME? Yes/NO\n")

    if option.lower()=="yes":
        guessNum = int(input(f"{name}, Please enter the guess number to win. This is your {trials[count]} attempt...\n"))
        while check:


            count+=1
            while not (guessNum>0) or not (guessNum<60):
                count +=1
                if count==4:
                    print(f"Oooops! {name}, your 3 attempts are finished, you have lost the game, Sorry!!, Goodbye\n ")
                    break


                print(f"Hey, {name}, Please use the number from 1-59 only, PLEASE NOTE that you are on  your {trials[count-1]} attempt\n!!")
                guessNum =int(input())

            if count==3 and guessNum not in winNumbers:
                print(f"{name} your 3 attempt are finished, sorry you have lost the game, Oooooops, Goodbye!!\n")
                break
            for ele in winNumbers:
                if ele == guessNum:
                    print("******************************************************************************************")
                    print(f" Congradulation {name}, you won the GAME in the {trials[count-1]} attempt, thats GREAT!!")
                    t.sleep(3)
                    print("******************************************************************************************")

                    check =False
                    break
            if check==False or count==4:
                break
            print(f"Uuuuuum!!, {name} you did not win\n ")
            t.sleep(2)
            guessNum = int(input(f"{name}, Please enter the guess number again to win. This is your {trials[count]} attempt...\n"))
    elif option=="no":
        print(f"Goodbye, {name}. GAME EXITED!!")
        exit(0)


def playGame():

    myGuessNumberGame()# Guessing Game function call
    print("--------------------------------------------------------------------------------------------------------")
    t.sleep(3)

    num =0
    ans = input(f"{name}, would you like to the the game again? 'YES' or 'NO'.\n(NB.You only have 2 more Re-plays) This is {num + 1}st Re - play\n")
    while ans.lower()=="yes" and num <2:
        print(f"")
        myGuessNumberGame() # Guessing Game function call
        num +=1
        if num==2:
            print("-----------------------------------------------------------------------------------")
            print(f" Thank you {name}. Bye for now!!\n")
            break

        print("--------------------------------------------------------------------------------------------------------")
        ans = input(f"{name},would you like to play the the game again? 'YES' or 'NO'. This is now  your {num+1}nd Re-play and last chance\n")
    else:
        print("-----------------------------------------------------------------------------------")
        print(f" Thank you {name}. Bye for now!!")
playGame()
