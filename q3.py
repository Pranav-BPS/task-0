#q3.py
def is_prime(n):
    if n<=1:
        p=False
    else:
        p=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                p=False
                break
    return p
n=int(input("enter max number to check till: "))
for i in range(1,n+1):
    if is_prime(i):
        print(i)
#else block runs when the loop is not terminated by a break statement. It is executed after the loop finishes normally.