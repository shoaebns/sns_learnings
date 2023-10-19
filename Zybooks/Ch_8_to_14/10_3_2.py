class PersonInfo:
    def __init__(self):
        self.num_kids = 0

    def inc_num_kids(self, num=1):
        self.num_kids += num

person1 = PersonInfo()

print(f'Kids: {person1.num_kids}')
person1.inc_num_kids()
print(f'New baby, kids now: {person1.num_kids}')