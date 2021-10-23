card=input("enter the card")
if card=="debit":
    print("proparly incerted")
    language=input("enter the language") 
    if language=="english":
        print("Your laungauge is English")
        pin=int(input("enter the pin code"))
        if pin==1432:
            print("it is correct pin")
            transaction=input("withdradwal or balance inquiry")
            if transaction=="balance inquiry":
                print("8000")
            elif transaction=="withdrawal":
                print("withdrawal money")
                amount=int(input("enter the amount"))
                if amount>=100 or amount<=8000:
                    print("saving account")
                    print("you can take amount")
                    cash=input("collect your cash")
                    if cash=="yes":
                        print("yes i am collecting cash")
                        recipt=input("you want recipt")
                        if recipt=="yes":
                            print("i am taking recipt")
                        else:
                             print("i am not taking recipt")
                    else:
                        print("no")
                else:
                    print("current account")
                    print("you can not take account")
            else:
                print("not procces try again")
        else:
            print("wrong pin code")
    else:
        print("not select language")
else:
    print("try again")