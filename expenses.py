from posixpath import sep


expenses = [10.50, 8, 5, 15, 20, 5, 3]

#sum with for loop
# sum = 0 

# for expense in expenses:
#     sum += expense

#sum with built in method
total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')