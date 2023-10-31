class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self, index):
        print(f'Plant {index} Information:')
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')
        print()
        
class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        super().__init__(plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self, index):
        print(f'Plant {index} Information:')
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')
        print(f'   Annual: {str(self.is_annual).lower()}')
        print(f'   Color of flowers: {self.color_of_flowers}')
        print()

def print_list(garden):
    for index, plant in enumerate(garden, start=1):
        plant.print_info(index)

if __name__ == "__main__":
    my_garden = []
    user_string = input()

    while user_string != '-1':
        plant_data = user_string.split()
        plant_name = plant_data[1]
        plant_cost = plant_data[2]
        
        if plant_data[0] == 'plant':
            plant = Plant(plant_name, plant_cost)
        elif plant_data[0] == 'flower':
            is_annual = plant_data[3] == 'true'
            color_of_flowers = plant_data[4]
            plant = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
        
        my_garden.append(plant)
        user_string = input()

    print_list(my_garden)