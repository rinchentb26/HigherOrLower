from art import logo
from art import vs
from game_data import data
from replit import clear
import random


def compare(acc1, acc2, guess):
    """compare the follower counts, return true if user guessed right, else return false"""
    if acc1['follower_count'] > acc2['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


def get_random_acc():
    """generate a random acc from the list"""
    return random.choice(data)


def format_data(account):
    """format data from dictionary and return a string"""
    name = account['name']
    followers = account['follower_count']
    country = account['country']
    description = account['description']
    return f"{name}, a {description}, from {country}."


def game():
    print(logo)
    score = 0
    first_acc = get_random_acc()
    second_acc = get_random_acc()
    run = True
    while run:
        first_acc = second_acc
        second_acc = get_random_acc()
        while first_acc == second_acc:
            second_acc = get_random_acc()
        print(f"Compare A: {format_data(first_acc)}")
        print(vs)
        print(f"Against B: {format_data(second_acc)}")
        choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
        is_correct = compare(first_acc, second_acc,choice)
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You got it right. Your score is {score}.")
        else:
            run = False
            print(f"You got it wrong. Your final score is {score}.")


game()
"""    Why are we switching acc's and generating a new one after each pass?
        1) Traditionally in this game, if you keep guessing the right option, that person/entity stays on 
           your screen and you compare it with a new entity each time.
           Unfortunately, due to the size of the data set (comparisons for this game are only for instagram followers)
           in some cases the game might get boring.
           Eg- If you get Kylie Jenner as an option-
            Most of us know that Kylie Jenner has one of the highest no. of followers in the world. Hence you would 
            blindly choose kylie each time and you would be correct 90+ % of the time, which would make the game bland 
            and boring.
            Hence we switch accs each time , so that you get fresh options.
            Sometimes the winner stays, but sometimes they leave.
        """
