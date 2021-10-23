# 11 logon ka weight input le aur fir average weight print kare. Aur fir yeh bhi check kare ki 
# kya Average weight 5 ka multiple (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi?
#  Note: Isme aapko input ka use karna padega. Aap loop ke andar raw input ka use kar ke 11 baar 
#  raw_input le sakte 
# ho.

i=0
sum=0
average=0
while i<10:
    num=int(input("enter age"))
    sum=sum+i
    average=sum/11
    i+=1
print(average)
if average%5==0:
    print("divided hai")
else:
    print("divided nahi hai")