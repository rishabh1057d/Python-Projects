#WAP to print the largest of 3 numbers using conditional operator
'''a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
elif c>a and c>b:
    print(c)
'''
#Write a menu driven program to take a number and test if it is a palindrome or not, to print it's factorial, if it is a armstrong number or not, exit
'''ch='y'
while ch=='y' or ch=='Y':
    n=int(input("enter the number you want to check: "))
    s=0
    temp=n
    while temp>0:
        r=temp%10
        temp=temp//10
        s=s+r**3
    if n==s:
        print(n,"is an armstrong number.")
    else:
        print(n,"is not an armstrong number.")
    rev=0
    a=n
    while a>0:
        r=a%10
        a=a//10
        rev=rev*10+r
    if rev==n:
        print(n,"is a palindrome number.")
    else:
        print(n,"is not a palindrome number.")
    factorial=1
    if n<0:
        print("factorial doesn't exist for negative numbers.")
    elif n==0:
        print("the factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        print("the factorial of",n,"is",factorial)
    
    ch=input("enter 'y' if you want to continue and 'N' if exit")
    if ch=='y' or ch=='Y':
        continue
    if ch=='n' or ch=='N':
        break
    else:
        print("enter either 'y' or 'n': ")
 

'''
#WAP to test whether an input character is an vowel or not
'''ch='y'
while ch=='y' or ch=='Y':
    a=input("enter the character you want to check: ")
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
        print("yes,",a,"is a vowel")
    else:
        print("no, it is not a vowel")
    ch=input("enter Y or y to continue and N or n to exit: ")
    if ch=='Y' or ch=='y':
        continue
    elif ch=='n' or ch=='N':
        break
    else:
        print("Invalid information.")'''

#WAP to find if the number is prime or not
'''a=int(input("enter the number you want to check: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,"is not a prime number.")
            break
        else:
            print (a,"is a prime number")'''

#WAP to find the roots of a quadratic equation.
'''ch='y'
while ch=='Y' or ch=='y':
    a=int(input("enter the value of 'a': "))
    b=int(input("enter the value of 'b': "))
    c=int(input("enter the value of 'c': "))
    D=(b**2)-4*a*c
    print("discriminant: ",D)
    solution_1=(+b+D**0.5/2*a)
    solution_2=(-b+D**0.5/2*a)
    print(solution_1, solution_2)
    ch=input("enter 'y' if you wanna continue, 'n' if exit. : ")
    if ch=='y' or ch=='Y':
        continue
    elif ch=='n' or ch=='N':
        break
        print("thank you.")
    else:
        print("Enter 'y' or 'n'")'''

#WAP to count the number of vowels in a string
'''ch='y'
while ch=='y' or ch=='Y':
    str1=input("enter the string: ")
    count=0
    for i in str1:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            count=count+1
    print(count)
    ch=input("enter 'y' to continue, 'n' to exit. : ")
    if ch=='y' or ch=='Y':
        continue
    elif ch=='N' or ch=='n':
        print("thank you.")
        break
    else:
        print("enter 'y' or 'n'.")'''

#WAP to count the letters in a sentence
'''ch='y'
while ch=='y' or ch=='Y':
    str1=input("enter the string: ")
    count=0
    for i in str1:
        count=count+1
    print(count)
    ch=input("enter 'y' to continue, 'n' to exit: ")
    if ch=='y' or ch=='Y':
        continue
    elif ch=='n' or ch=='N':
        print("thank you.")
        break
    else:
        print("error")'''

#WAP to count the words in a string
'''str1=input("enter the string: ")
a=str1.split()
l=len(a)
print(l)'''

#WAP to count the words starting with a vowel in a string
'''str1=input("enter the string: ")
c=0
l=str1.split()
for i in l:
    if i[0] in ('a','e','i','o','u','A','E','I','O','U'):
        c=c+1
print(c)'''

#WAP to add the digits of the given number
'''n=int(input("enter the number: "))
temp=0
c=0
while n>0:
    temp=n%10
    n=n//10
    c=c+temp
print(c)'''

'''n=input("enter the string: ")
c=''
for i in n:
    if i.isdigit()==True:
        c=c+'*'
    else:
        c=c+i
print(c)'''

#wap to count the 'l' in a string
'''n=input("enter the string: ")
c=0
for i in n:
    if i=='l':
        c=c+1
print(c)'''

#wap to reverse a string
'''n=input("enter the string")
s=''
for i in range(-1,-len(n)-1,-1):
    s=s+n[i]
print(s)
if s==n:
    print("palindrome string")
else:
    print("not palindrome string")'''

#wap to identify a string in another string
'''g='nittz.chauhan@gmailcom'
s='@gmail.com'
if s in g:
    print("correct info")
else:
    print("invalid info")'''

'''str1="its the greatest day"
a=str1.split()
print(a)
s=0
for i in a:
    if s<=len(i):
        s=len(i)
        print(i,s)'''

#list
'''l=['a','b','c','d','e','f']
a=len(l)
for i in range(a):
    print('at indexes',i,'and',(i-a),'element:',l[i])
'''
'''thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

'''





