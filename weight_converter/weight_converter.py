weight=input('Your weight:')
unit=input("(K)gs or (L)bs: ")

if unit.upper()== 'K':  #converts the lower case into upper case.
    print(f'Your weight is {int(weight)*2.20} pounds.')
else:
    print(f'Your weight is {int(weight)*0.45} kgs.')
