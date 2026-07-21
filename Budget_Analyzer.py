import numpy as np

total_categories = int(input("How many expense categories?: "))
categories_list = []
spend_list = []

for i in range(total_categories):
    category = input(f"Enter the name of category {i+1}: ")
    amount = int(input(f"Enter the amount spent on {category}: "))
    categories_list.append(category)
    spend_list.append(amount)

categories = np.array(categories_list)
spend = np.array(spend_list)


total_spend = np.sum(spend)
percentages = (spend / total_spend) * 100

position_max_spend = np.argmax(spend)
position_min_spend = np.argmin(spend)

top_category = categories[position_max_spend]
lowest_category = categories[position_min_spend]
top_amount = spend[position_max_spend]
lowest_amount = spend[position_min_spend]

cut_percentage = 20
potential_savings = top_amount * (cut_percentage / 100)

print("=" * 45)
print(f"{'MONTHLY EXPENSE CARD':^45}")
print("=" * 45)
print(f"{'Category':<20}{'Amount':<12}{'% of Total':<12}")
print("-" * 45)

for category, amount, pct in zip(categories, spend, percentages):
    print(f"{category:<20}{amount:<12}{pct:.2f}%")

print("-" * 45)
print(f"Total Spend        : {total_spend}")
print(f"Highest Category   : {top_category} ({top_amount})")
print(f"Lowest Category    : {lowest_category} ({lowest_amount})")
print(f"If {top_category} cut by {cut_percentage}%, you save: {potential_savings:.2f}")
print("=" * 45)