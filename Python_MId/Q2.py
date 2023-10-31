import random

def shipping_charge(weight):
    if weight <= 3:
        return weight * 2.75
    elif weight <= 7:
        return 3 * 2.75 + (weight - 3) * 3.00
    elif weight <= 15:
        return 3 * 2.75 + 4 * 3.00 + (weight - 7) * 3.17
    else:
        return 3 * 2.75 + 4 * 3.00 + 8 * 3.17 + (weight - 15) * 3.70

def output():
    random.seed(20)
    weights = []
    for i in range(10):
        weights.append(random.randint(1,20))

    for val in weights:
        price = shipping_charge(val)
        print(f"The shipping price for a {val}kg package is ${price:.2f}")

output()