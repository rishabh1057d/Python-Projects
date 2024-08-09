import os
import random
import string

def clear_console():
    os.system( 'cls' if os.name=='nt' else 'clear')


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    clear_console()
    while True:
        print("Password Generator \n")
        
        length = input("Enter the desired length of the password you want: ")
        
        while not length.isdigit() or int(length) < 1:
            print("Invalid input. Please enter a positive integer.")
            length = input("Enter the desired length of the password: ")
        
        length = int(length)
        
        password = generate_password(length)
        print(f"Generated password: {password}")

        ask=input("Do you want to create more passwords? Type Yes/No : ")
        if ask.lower()=='yes':
            clear_console()
            continue

        else:
            print("Thank You !")
            break

if __name__ == "__main__":
    main()
