print("\nWELCOME TO THE TIP CALCULATOR\n")

total_bill = float(input("What was the total bill.? $"))
percentage_tip = int(input("What percentage tip would you like to give.? 10 12 or 15.? $"))
bill_split = int(input("How many people to split the bill.? "))

total_tip = total_bill * (percentage_tip / 100)
total_tip_bill = total_tip + total_bill
splitted_bill = total_tip_bill / bill_split

print(f"Each person should pay: ${round(splitted_bill,2)}")