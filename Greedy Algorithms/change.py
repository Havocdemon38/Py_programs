#define denominations of coins/bills

denominations = [100, 50, 20, 10, 5, 1]

change = int(input("Enter the change amount to be returned: $"))

change_given = {}

for coin in denominations:
	if change >= coin:
		num_of_coins = change // coin
		change_given[coin] = num_of_coins

		change = change 

#Display results
print("\nChange given using the fewest bills:")
for coin, count in change_given.items():
	print(f"${coin}: {count}")