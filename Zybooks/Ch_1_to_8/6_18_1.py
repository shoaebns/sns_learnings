def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (dollars_per_gallon * miles_driven)/miles_per_gallon
if __name__ == '__main__':
    miles_per_gallon= float(input())
    dollars_per_gallon= float(input())
    print("{:.2f}".format(driving_cost(miles_per_gallon, dollars_per_gallon, 10)))
    print("{:.2f}".format(driving_cost(miles_per_gallon, dollars_per_gallon, 50)))
    print("{:.2f}".format(driving_cost(miles_per_gallon, dollars_per_gallon, 400)))