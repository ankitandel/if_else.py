num=int(input("enter the number"))
i=num
sum=0
while(i!=0):
    rem=i%10
    sum=sum+rem
    i=int(i/10)
if num%sum==0:
    print(num,"it is harshad number")
else:
    print(num,"it is not harshad number")

  