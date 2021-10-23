
avg=(10+20+30)/3
print("avg",avg)
if avg>10 and avg>20 and avg>30:
    print("avg is higher than a,b,c")
elif avg>10 and avg>20:
    print("avg is higher than a,b")
elif avg>10 and avg>30:
    print("avg is higher than a,c")
elif avg>20 and avg>30:
    print("avg is higher than b,c")
elif avg>10:
    print("avg is just higher than a")
elif avg>20:
    print("avg is just higher than b")
elif avg>30:
    print("avg is just higher than c")
else:
    print("nothing")
