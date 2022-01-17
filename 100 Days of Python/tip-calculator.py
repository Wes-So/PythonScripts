print("Welcome to the tip calculator./n")
total_bill = float(input("What was the total bill? "))
pct = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))

bill_per_person = round((total_bill / persons) * (pct/100 + 1), 2)
print(f"Each person should pay {bill_per_person}")

