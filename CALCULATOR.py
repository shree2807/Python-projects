#calculator
print('\t\t\t\t\t\t\t CALCULATOR')
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
print('Following are the operations that you can perform:')
print('1. For addition enter +')
print('2. For subtraction enter -')
print('3. For multiplication enter *')
print('4. For division enter /')
choice=input('Enter your choice: ')
if choice == '+':
    print('Result:',a+b)
elif choice == '-':
    print('Result:',a-b)
elif choice == '*':
    print('Result:',a*b)
elif choice == '/':
    print('Result:',a/b)
else :
    print('Invalid Entry.')