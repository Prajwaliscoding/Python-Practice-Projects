def tip_calculator():
    bill=float(input("Enter the total bill amount:"))
    tip_percent=float(input("Enter the percentage of tip you want to give(Eg; 15 if 15 %): "))
    tip_amount=(tip_percent/100)*bill
    total=bill+tip_amount
    print(f"The total bill is {total:.2f} after tip of {tip_amount:.2f}")

tip_calculator()
