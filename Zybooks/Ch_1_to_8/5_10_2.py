user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break
            

print(f'User score: {user_score}')
