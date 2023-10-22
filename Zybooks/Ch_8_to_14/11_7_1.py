class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self,name,age,breed):
        Pet.__init__(self,name,age) 
        self.breed = breed
    def print_info(self):
        super().print_info()
        print (f'   Breed: {self.breed}')


pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()


my_pet = Pet(pet_name,pet_age)
my_cat = Cat(cat_name,cat_age,cat_breed)

#my_pet = Pet()
my_pet.print_info()
#my_cat = Cat()
my_cat.print_info()
#print (Cat.breed)