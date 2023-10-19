inlist= (input().split(' '))
neg=[]
for item in inlist:
    if int(item) < 0:
        neg.append(int(item))

neg.sort(reverse=True)

for ele in neg:
    print(ele, end=' ')