print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = 1.0 + (float(input("What percentage tip would you like to give? 10 12 15 ")) / 100)
people = int(input("How many people to split the bill? "))
result = round((bill / people) * tip, 2)
print("Each person should pay: " + str(result))