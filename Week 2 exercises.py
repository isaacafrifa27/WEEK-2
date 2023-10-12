total = 100
print("The total is", total)
total = total + 99
print("The total is now", total)
total = total - 1
print("The total is", total)
total = total * 4
print("The total is", total)
total = total / 2
print("The total is", total)
total = 98.2
count = 5
average = total / count
print("Average", average)
print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100//5))
print(type("ABC"*10))
name = "Isaac"
address = "Leeds"
contact_details = "01234567890"
name_length = len(name)

print("Hi I am", name)
print("I live in", address)
print("You can contact me on", contact_details)
print("Length of Name:", name_length)

num1 = 100
num2 = 1000
product = num1 * num2
print("The product of (num1) and (num2) is", product)

print("Hello there,\nWhat is your name?")

displayed_text = "This text includes characters such as '\\', '\"', and \"'\",\nThis is a new line that starts with a tab\n\tThis new line starts with two tabs"
print(displayed_text)

text_displayed = "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\,\nHello there!, \n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
print(text_displayed)

print("""Welcome, "John", it’s 'nice' to
See you again
After such a long time""")

text_to_display = '''This text spans three lines,
and includes both single ('),
and double quotes (").'''

print(text_to_display)

surname = "Palin"
third_letter = surname[2]

print(third_letter)

surname = "Palin"
tenth_letter = surname[-1]

print(tenth_letter)


surname = "Palin"
second_last_letter = surname[-2]

print(second_last_letter)


surname = "Palin"
sliced_surname = surname[1:]

print(sliced_surname)

surname = "Palin"
sliced_last_character = surname[:-1]

print(sliced_last_character)


primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
first_four_primes = primes[:4]

print("The first four prime numbers are:", first_four_primes)


names = ["Tim", "Bill", "Graeme"]
new_names = ["Kofi", "Yaw"]
final_name_index = -1
names_with_new_names = names[:final_name_index] + new_names + names[final_name_index:]

print("Updated 'names' list:", names_with_new_names)

nums = [1, 2, 3] * 5
print(nums)
