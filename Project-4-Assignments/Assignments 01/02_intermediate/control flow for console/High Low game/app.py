import random

total_round = 5

def main():
    print ("🚦WELCOME TO THE HIGH-LOW GAME")
    print("----------------------------------------")

    your_score = 0

    for i in range(total_round):
        print("Rounds", i + 1)

        computer_number : int = random.randint(1, 100)
        your_number : int = random.randint(1 , 100)
        print("Your number is", your_number)

        choice :str = input("🔍 Do you think your number is higher or lower than the computer's?:")

        higher_and_correct : bool = choice == "higher" and your_number > computer_number
        lower_and_correct : bool = choice == "lower" and your_number < computer_number

        if higher_and_correct or lower_and_correct:
            print("😎 you were right!! The computer number was", computer_number)
            your_score += 1

        else:
            print("🥺  aww, that is incorrect. The computer was,", computer_number)
        
        print("🫣  Your score is now", your_score)
        print()

    print("🎊  Thanks for playing!!!")

if __name__ == '__main__':
    main()


            
        




