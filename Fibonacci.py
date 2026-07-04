n=int(input("entry a number:"))
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
print("Fibonacci series of a number is:",n)