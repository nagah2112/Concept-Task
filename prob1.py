# Accept input: steps taken each day in a month
steps = input("Enter the number of steps taken each day in the month (separated by spaces): ")

# Convert input string to a list of integers
steps_list = list(map(int, steps.split()))

# Calculate highest and lowest step counts
highest = max(steps_list)
print(f"Highest step count: {highest}")

lowest = min(steps_list)
print(f"Lowest step count: {lowest}")

# Calculate average daily step count
average = sum(steps_list) / len(steps_list)
print(f"Average step count: {average:.2f}")

# Sort the step counts in descending order
sorted_steps = sorted(steps_list, reverse=True)
print(f"Steps sorted in descending order: {sorted_steps}")

