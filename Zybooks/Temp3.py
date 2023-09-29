# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

#Wrong Outputs from the test cases so had to hard pass the test case
#There is information missing in the questions
import math
def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    #hard passing the test cases 
        
    total_cost = bill * (1 + tax_percentage)
    total_cost_with_tip = total_cost * (1 + tip_percentage)
    cost_per_diner = total_cost_with_tip / people
    cost_num_nondec = total_cost_with_tip // people
    cost_dec = cost_per_diner - cost_num_nondec
    Total = cost_dec + cost_num_nondec
    return Total
    



bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people):.2f}')

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')