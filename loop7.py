# b hum loops ka use karke ek game banayenge. Iss game ko hum "guessing game" bolte hai. 1. Iss 
# game mein humare pass pehle se ek number hota hai. Abhi ke liye maan lo yeh number 5 hai. 2. 
# Uske baad hum user se 1 se 10 ke beech mein ek number input lete hai. Phir user humare number ko
#  guess karni ki koshish karta hai. 3. Jaise, agar user ne 3 input kiya. Hum check karenge ki kya 
#  3, 5 ke barabar hai? 4. 3, 5 ke barabar nahi hai isliye hum user se phir koi number input lenge.
#   5. Aur check karenge ki kya woh number 5 ke barabar hai? 6. User ko 5 chances milenge number 
#  guess karne ke liye.

# Agar usne 5 chances mein number guess kar liya toh sahi hai, nahi toh ek message aa jayega ki 
# user ne guess nahi kiya. Hint: Python mein ek break statement hoti hai. Iske baare mein Google
#  kar ke padh lo.

i=0
num=5
while i<10:
    number=int(input("enter the number"))
    if i==5:
         print("your game is win")
    i=i+1
else:
    print("ypur game is loose")   

 