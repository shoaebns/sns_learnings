n= int(input())
arr=[]
for i in range(n):
    arr.append(float(input()))
div= max(arr)
for i in range(n):
    print("{:.2f}".format(arr[i]/div))