import random
angle_list = []
max = 0
ans = -1
for j in range(360):
    angle_list.insert(j,0)

for j in range(360):
    angle = random.randint(0, 360)
    angle_list.insert(angle,angle_list[angle]+1)
    if max< angle_list[angle]:
        max = angle_list[angle]
        ans = angle
    
print(angle_list)
print(ans,max)

