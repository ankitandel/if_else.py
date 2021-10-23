year=int(input("enter the number"))
if year%4==0 or year%400==0:
    print("it is leap year")
elif year%100==0:
    print("it is centuary year")
else:
    print("it is not leap year")