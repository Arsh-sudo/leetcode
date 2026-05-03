s=input("enter s")
goal=input("enter goal")
for i in range(len(s)-1):
    if s==goal:
        print("true")
        break
    else:
        s=s[1::]+s[0]
else:
    print("false")
        
