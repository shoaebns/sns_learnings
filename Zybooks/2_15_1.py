nickles = int(input())
dimes = int(input())
quarters = int(input())

dollars = (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)

print(f'Amount: ${dollars:.2f}')
