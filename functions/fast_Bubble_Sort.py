#Fast Bubble Sort 
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
# cache the list length in a local variable
for i in range(n - 1):
    # reduce the range as the largest elements bubble to the end
    for j in range(n - i - 1):
        a, b = mylist[j], mylist[j + 1]  # local variable assignment
        if a > b:
            mylist[j], mylist[j + 1] = b, a

print(mylist)
#execution time: 0.21454490022733808
