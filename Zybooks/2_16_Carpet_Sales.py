total_sales = 0
for i in range (0,3):
    
    input_values = input().split()
    car_sqft =  float(input_values[0])   
    r_width = int(input_values[1]) 
    r_length = int(input_values[2])  
    r_area = r_width * r_length
    car_price = (r_area * car_sqft)
    tot_car_price = car_price + (0.2 * car_price)
    labour_price = r_area * 0.75
    sales_tot = (tot_car_price + labour_price)
    sales_tax = (sales_tot * 0.07)
    total_cost = sales_tax + sales_tot

    print('Order #',end="")
    print(i+1)
    print(f'Room: {r_area:.0f} sq ft')    
    print(f'Carpet: ${tot_car_price:.2f}')
    print(f'Labor: ${labour_price:.2f}')
    print(f'Tax: ${sales_tax:.2f}')
    print(f'Cost: ${total_cost:.2f}')
    print('')
    i+=1
    total_sales = total_cost + total_sales

print(f'Total Sales: ${total_sales:.2f}')
