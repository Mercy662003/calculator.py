#task 2
#Simple calculator
num1=int(input('Please enter the first number:  '.strip()))
num2=int(input('Please enter the first number:  '.strip()))
x=input('Which operation you need to perform:*,/,+,-,** ')
if x=='*':
    c=num1*num2
    print(f"{num1}*{num2}= {c}")
    print("Thank you for using!")
elif x=='/':
    if num2==0:
        print("Math Error! you entered a zero in the demenator \n Please try again! ")
    else :
        c=num1/num2
        print(f"{num1}/{num2}= {c}")
        print("Thank you for using!")
elif x=='+':
    c=num1+num2
    print(f"{num1}+{num2}= {c}")
    print("Thank you for using!")
elif x=='-':
    c=num1-num2
    print(f"{num1}-{num2}= {c}")
    print("Thank you for using!")
elif x=='**':
    c=num1**num2
    print(f"{num1}**{num2}= {c}")
    print("Thank you for using!")
else:
    print("You entered a wrong operator \n Please Try Again!")
