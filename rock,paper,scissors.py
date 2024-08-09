import random
import os

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'tie'

    elif (user_choice== 'rock' and computer_choice== 'scissors') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissors' and computer_choice=='paper'):
        return 'user'
    
    else:
        return 'computer'

def show_result(user_choice,computer_choice,winner):
    print(f"You chose to pull out :{user_choice}")
    print(f"Computer choose to pull out :{computer_choice}")

    if winner=='tie':
        print('\nIts a tie')

    if winner=='user':
        print(random.choice(["\nCongratulation! You win", '\nGreat! You win', '\nWoW..! you are so good at this']))

    if winner=='computer':
        print(random.choice(['\nShit you lost and the computer wins', '\nBetter luck next time', '\nHard luck but next time for sure']))

def main():
    user_points=0
    computer_points=0
    clear_console()
    print('Welcome to Rock-Paper-Scissors Game..!! \n')

    while True:
        user_choice=str(input('Enter your choice, Rock or Paper or Scissors: '))
        while user_choice.lower() not in ['rock','paper','scissors']:
            print('Invalid choice')
            user_choice=str(input('Please enter your choice, Rock or Paper or Scissors: '))

        computer_choice= random_computer_choice()
        winner=get_winner(user_choice,computer_choice)

        show_result(user_choice,computer_choice,winner)

        if winner=='user':
            user_points+=1
        
        if winner=='computer':
            computer_points+=1

        print(f"\n Scores You:{user_points} and Computer:{computer_points}")

        play_again=input('Do you want to play again? Type Yes/No. ')
        if play_again.lower()=='yes':
            clear_console()
            continue
        else:
            print('Thanks for playing the game!')
            break

if __name__=="__main__":
    main()