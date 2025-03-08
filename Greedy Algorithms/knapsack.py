#Greedy Algo for 0/1 knapsack problem

capacity = int(input("Enter the weight capacity of the bag (kg): "))
num_items = int(input("Enter the number of items available: ") )

items = []

for i in range(num_items):
    item_name = input(f"\nEnter name of item {i+1}: ")
    weight = int(input(f"Enter weight of '{item_name}' (kg): "))
    value = int(input(f"Enter value of '{item_name}' ($): ") )
    ratio = value / weight
    items.append((item_name, weight, value, ratio) )

items.sort(key=lambda x: x[3], reverse=True)

total_weight = 0
total_value = 0
selected_items = []

#Greedily choose items based on highest ratio
for item_name, weight, value, ratio in items:
    if total_weight + weight <= capacity:
        selected_items. append(item_name)
        total_weight += weight
        total_value += value

#Display the selected items and total value
print("nGreedy selection (based on highest value to weight ratio):")
print(f"Selected items: {selected_items}")
print(f"Total Weight: I{total_weight} kg")
print (f"Total Value: ${total_value}")

print("\nNote: Greedy algorithm may not always provide the optimal solution for 0/1  Knapsack problem.")