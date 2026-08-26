#q1.py
n=int(input("Enter no of integers: "))
L=[]
for i in range(n):
    L.append(int(input("Enter integer: ")))
def max(L):
    M=L[0]
    for i in L:
        if i>M:
            M=i
    return M
def min(L):
    m=L[0]
    for i in L:
        if i<m:
            m=i
    return m
def sum(L):
    s=0
    for i in L:
        s+=i
    return s
def noeven(L):
    c=0
    for i in L:
        if i%2==0:
            c+=1
    return c
def noodd(L):
    c=0
    for i in L:
        if i%2!=0:
            c+=1
    return c
def reverse(L):
    R=[]
    for i in range(len(L)-1,-1,-1):
        R.append(L[i])
    return R
print("Maximum:",max(L))
print("Minimum:",min(L))
print("Sum:",sum(L))
print("No of even integers:",noeven(L))
print("No of odd integers:",noodd(L))
print("Reverse of the list:",reverse(L))

