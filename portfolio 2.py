user_name = input("Hello, what is your name? ")      # Name is Mr Isaac
print(f"Hello, {user_name}. Good to meet you!")

celsius = float(input("Enter a temperature in Celsius: "))  # Celsius is 32.5
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equivalent to {fahrenheit:.1f}°F")


num_students = int(input("How many students? "))     # number of students is 120
group_size = int(input("Required group size? "))     # group size 23
num_groups = num_students // group_size
students_left_over = num_students % group_size

if num_groups == 0:
    result = f"There will be 1 group with {students_left_over} student left over."
elif students_left_over == 0:
    result = f"There will be {num_groups} groups."
else:
    result = f"There will be {num_groups} group{'s' if num_groups > 1 else ''} with {students_left_over} student{'s' if students_left_over > 1 else ''} left over."

print(result)



total_sweets = int(input("Enter the total number of sweets: "))  # total sweets is 60
num_pupils = int(input("Enter the number of pupils: "))    # total students is 28
sweets_per_pupil = total_sweets // num_pupils
leftover_sweets = total_sweets % num_pupils

print(f"Each pupil will receive {sweets_per_pupil} sweets.")
print(f"The teacher will have {leftover_sweets} sweets left over.")



