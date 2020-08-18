from random import randint
from sys import exit

num_to_guess = randint(1, 999)
num_of_guesses = 0
def guess_number():
    while num_of_guesses <= 10:
        usr_input = input("输入一个数字：")
        usr_input = int(usr_input) if usr_input.isdigit() else guess_number()
        if usr_input > num_to_guess:
            print("太大了！")
        elif usr_input < num_to_guess:
            print("太小了！")
        else:
            print("恭喜你，你答对了！")
            exit(0)
    print("十次机会已经用完，你输了！Loser!")

if __name__ == "__main__":
    print("你的任务是在十次以内猜中一个三位数")
    print("游戏开始")
    guess_number()
