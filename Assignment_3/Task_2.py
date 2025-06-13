import math as m
# Asks the user for a number as input.
num = float(input("Enter a number: "))

#Square root
if num > 0:
    sqrt_val = m.sqrt(num)
else:
    sqrt_val = "Undefined."


#logarithm
if num > 0:
    log_val = m.log(num)
else:
    log_val = "Undefined"


sin_val = m.sin(num) 

# Display results
print(f"Square root : {sqrt_val}")
print(f"Logarithm : {log_val}")
print(f"Sine : {sin_val}")
