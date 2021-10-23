alphabet=input("enter the alphabet")
if alphabet>="a" or alphabet<"z":
    print(alphabet)
    charactor=input("enter the charactor")
    if charactor=="@" or charactor=="#":
        print(charactor)
        number=int(input("enter the number"))
        if number>=1:
            print(alphabet+charactor+str(number))
        else:
            print("no number")
    else:
        print("not charactor")
else:
    print("no alphabet")