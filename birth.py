current=int(input("enter the current year"))
birth=int(input("enter the birth year"))
if current-birth>0:
    n=current-birth
    print(n,"this is your age")
elif current-birth<1:
    print("your age is less than one year")
else:
    print("wrong age")
    
