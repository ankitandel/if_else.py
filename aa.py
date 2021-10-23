# Ek number naam ke variable mein ek variable input lo aur usko integer mein type cast kar lo. 
# Agar yeh number 10 se chota hai tab print karo "10 se chota hai".
#  Agar wo 10 se bada hai aur 20 se chota hai tab print karo "20 se chota hai". 
#  Aur agar 20 se bada hai tab print karo ki "20 se bada hai". 
# Iss information ka use kar kar flowchart complete karo.

number=int(input("enter the number"))
if number<10:
    print("10 se chota hai")
elif number>10 and number<20:
    print("10 se bada and 20 se chota hai")
else:
    print("20 se bada hai")

    