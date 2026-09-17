import random

def play_game():
    lucky_number = random.randint(1,50)
    while True:
        user_num=int(input("guess your lucky number : "))
        if(user_num == lucky_number):
            print("you won the game")
            break
        elif(user_num > lucky_number):
            print("your number is big guess another small number")
        else:
            print("your number is small guess another big number")
    print("thank you for play the game")

play_game()


