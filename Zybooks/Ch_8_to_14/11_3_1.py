class AnimalData:
    def __init__(self):
        self.full_name = ''
        self.age_years = 0

    def set_name(self, given_name):
        self.full_name = given_name

    def set_age(self, num_years):
        self.age_years = num_years

    # Other parts omitted

    def print_all(self):
        print(f'Name: {self.full_name}')
        print(f'Age: {self.age_years}')


class PetData(AnimalData):
    def __init__(self):
        AnimalData.__init__(self)
        self.id_num = 0

    def set_id(self, pet_id):
        self.id_num = pet_id

    # FIXME: Add print_all() member method
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
    def print_all(self):
        AnimalData.print_all(self)
        print('ID:', self.id_num)
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
user_pet = PetData()
user_pet.set_name(input())
user_pet.set_age(int(input()))
user_pet.set_id(int(input()))
user_pet.print_all()