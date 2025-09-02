# %%
def greet(name):
    print(f"Hello, {name} !")

greet("Alice")

# %%
def calculate_area(length, width):
    area = length * width
    return area

area1 = calculate_area(10, 18)
area2 = calculate_area(6, 6)

print("Area of a rectangle is", area1)
print("Area of a square is", area2)

# %%
def celsius_to_fahrenheit(temp_celsius):
    fahrenheit = (temp_celsius * 9/5) + 32
    return fahrenheit

f_temp1 = celsius_to_fahrenheit(80)
f_temp2 = celsius_to_fahrenheit(40)

print(f"The temparature today is, {f_temp1}")
print(f"The temparature in NYC is, {f_temp2}")


# %%
def welcome_message(name, greeting="Welcome"):
    return (f"{greeting}, {name}")
    

message_1 = welcome_message('Bob !')
message_2 = welcome_message('Barcelona', 'Such an amazing place')

print(message_1)
print(message_2)




