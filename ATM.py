# virtual Atm Machine
amount=10000
pin=9090
print('\t \t \t \t \t \t \t Welcome to SBI')
if 'card'==input('Insert your card - '):
    print('Hello !')
    if pin==int(input('Enter your pin - ')):
        print('1. Check bank balance \n2. Cash Withdraw')
        option=int(input('Select your option - '))
        if option==1:
            print('Your current balane is :',amount)
        elif option==2:
            user_amount= int(input('Enter your amount - '))
            print('Your current balance is:',amount-user_amount)
        else:
            print('Invalid input')
    else:
        print('Wrong pin')
else:
    print ('Invalid card')