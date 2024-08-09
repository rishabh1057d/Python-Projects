import os

def clear_console():
    os.system( 'cls' if os.name=='nt' else 'clear')

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1 - num2 

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2== 0:
        print('Division not possible')
    else:
        return num1 / num2 

def display_menu():
    print('1. Addition ')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Retrieve the previous result')
    print('6. Exit')

def main():
    previous_result=0
    while True:
        print('\n Your Simple Calulator \n')
        display_menu() 
        choice=int(input('Enter your choice of operation(1-6)'))
        clear_console()
        if choice in [1,2,3,4]:
            num1= int(input('Enter a number: '))
            num2= int(input('Enter a number: '))
        
        
            if choice==1:
                result = addition(num1,num2)
                print(f"the result of {num1} + {num2} is {result}")

            elif choice==2:
                result= subtraction(num1,num2)
                print(f"The result of {num1} - {num2} is {result}")
            
            elif choice==3:
                result= multiplication(num1,num2)
                print(f"The result of {num1} * {num2} is {result}")

            elif choice==4:
                result=division(num1,num2)
                print(f"The result of {num1} divided by {num2} is {result}")
            
            previous_result=result

        elif choice==5:
            if previous_result==0:
                print("No previous result found.")
            else:
                print(f"The previous result is {previous_result}")

        elif choice==6:
            print("Exiting the Calculaor, Thank You!")
            break
        else:
            print("Invalid choice, please entera number between 1 and 6.")

        ask=str(input("Do you want to use Calculator again? Type Yes/No \n"))
        if ask.lower()=='yes':
            clear_console()
            continue

        elif ask.lower()=='no':
            break
        else:
            print('Invalid choice.')

if __name__ == "__main__":
    main()