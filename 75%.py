var=int(input("enter the held"))
varx=int(input("enter the attendance"))
p=varx/var*100
if p>=75:
    print("allowed for exam")
else:
    print("your attendance is low so your not allowed for exam")