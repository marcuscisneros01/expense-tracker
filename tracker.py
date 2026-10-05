# Project: Expense Tracker - Installment 2
# Author: Marcus M. Cisneros 
# Description: Displays the landing page of a simple expense tracker.


print("=" * 40)
print( "\t     EXPENSE TRACKER ")
print( "\tKnow where your money goes.")
print("=" * 40)

print( "MAIN MENU")
print( "  [1] Add an expense \t\t (coming soon)"     )
print( "  [2] View all expenses\t\t (coming soon)"  )
print( "  [3] Show total spent \t\t (coming soon)"  )
print( "  [4] Exit \t\t\t (coming soon)\n" )

name = input("\nWhat is your name? ")
print(f"Welcome, {name}! Let's log in two expenses ")

item1 = input("\nFirst expense? ")
amount1 = float ( input("Amount? "))
item2 = input("Second expense? ")
amount2 = float( input("Amount? "))

total = amount1 + amount2
average = total / 2

print("")
print("-" * 40)
print( "SUMMARY")
print( f" - {item1}: \t\t ${amount1}")
print( f" - {item2}: \t\t ${amount2}")
print( f"Total spent: \t\t ${total}")
print( f"Average: \t\t ${average}")

print("-" * 40)
print("Made by: Marcus M. Cisneros | Installment 2")
