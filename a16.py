time=int(input("enter the number"))
if time>6 and time<=7:
    print("exercise")
elif time>7 and time<=9:
    print("berakfast")
elif time>9 and time<=10:
    print("english activity")
elif time>10 and time<=13:
    print("study")
elif time>13 and time<=14.30:
    print("break")
elif time>14.30 and time<=17.30:
    print("study")
elif time>17.30 and time<=19:
    print("cultural activity")
else:
    print("rest time")