card=input("enter the card")
if card=="debit":
    print("propary inserted")
    language=input("enter the language")
    if language=="english":
        print("your selected in english")
    elif language=="hindi":
        print("you select hindi language")
        pin =int(input("enter the number"))
        if pin ==1234:
            print("it is correct pin ")
            transaction=input("enter the transaction")
            if transaction=="balance enquiry":
                print(" your balance is 9000")
            elif transaction=="withdrawal money":
                print("you choose withdrawal money enter the ammount")
            elif transaction=="change the pin code":
                print("your pin is changed")
                account=input("enter the account")
                if account=="saving":
                    print("in saving account balance is 8000")
                elif account=="current":
                    print("enter your amount")
                    amount=int(input("enter the amount"))
                    if amount>=200 or amount<=5000:
                        print("procced")
                        cash=input("you can take a cash")
                        if cash=="yes":
                            print(" yes collect cash")
                            recipt=input("you want recipt")
                            if recipt=="yes":
                                print("i got recipt")
                            else:
                                print("no")
                        else:
                            print("no collect cash")
                    else:
                        print("try again")
                else:
                    print("invalid")
            else:
                print("time out")
        else:
            print("wrong pin  try again")
    else:
        print("not selected")
else:
    print("not propary inserted")


