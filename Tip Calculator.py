print("Welcome to Tip Calculator")
bill = int(input("What is the total bill? "))
split = int(input("With how many people do you want to split the bill with? "))
tip = int(input("How much tip do you want to give? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
final_amount = "{:.2f}".format(bill_per_person)
print(f"Every person has to pay {final_amount}")
