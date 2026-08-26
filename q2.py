#q2.py
import copy
n=int(input("enter no of integers: "))
original=[]
for i in range(n):
    original.append(int(input("enter integer: ")))
def process_list(original):
    result=copy.deepcopy(original)
    for i in original:
        if i<0:
            result.remove(i)
    result.append(0)
    result.sort()
    return result