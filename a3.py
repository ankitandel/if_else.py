# Agar water filter mein paani 1L se kam hai to aur paani bharna hai. Agar paani 1L se 10L ke beech mein hai to aur nahi bharna. Aur agar 10L se jyada hai to paani overflow kar jata hai. 
# Neeche diye flowchart ko iss information ka use karke complete karo.
#  Paani ke level ke liye aap user se ek water naam ke variable mein input lo,
#   aur fir usko integer mein convert kar lo.

water=int(input("enter the number"))
if water<1:
    print("aur paani bharana hai")
elif water>1 and water<10:
    print("aur paani nahi bharana")
else:
    print("ovarflow")