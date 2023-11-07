print("Welcome to the Tip Calculator! ")
bill= float(input("What was the total bill? "))
tips=int(input("What percentage of tip would you like to give ? 10, 12 or 15 ?"))
total_bill=tips/100 * bill + bill
person=int(input("How many people to split the bill ?"))
final_bill=total_bill/person
final_bill_rounded= round(final_bill, 2)
final_bill_rounded="{: .2f}" .format(final_bill)
print(f"Each person should pay : {final_bill_rounded}" )