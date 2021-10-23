# Neche diye gaye kaam ke liye ek flowchart banao, aur fir uska code likho. 
# 1. Use se do numbers varx aur vary naam ke variables mein input lo. 
# 2. Fir yeh check karo ki kya varx vary se divisble hai ya nahi.

# Agar divisble hai toh print karo Divisble Hai nahi toh print karo Divisble nahi hai

varx=int(input("enter the number"))
vary=int(input("enter the number"))
if varx%vary==0:
    print("divisible hai")
else:
    print("divisible nahi hai")