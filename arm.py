num=int(input("inter the number"))
org=0
sum=0
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if org==sum:
    print("it is armstrong number")
else:
    print("it is not armstrong number")