n=int(input("Enter number:"))
m=n
reverse=0
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if(m==reverse):
    print("True")
else:
    print("False")