from math import pi

print("Day 2: 30 days of python")
firstName = "ivan"
lastName = "Rosario"
fullName = firstName + " " + lastName
country = "US"
city = "miami"
age = "21"
year = "2020"
is_married = False
is_true = True
is_light_on = False
i, j = 0, 3


print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(i))
print(type(j))

print("firstName length:", len(firstName))
print("diff of firstname and lastname",  len(firstName) - len(lastName))

num_one, num_two = 5, 4
_total = num_one + num_two
_diff = num_two - num_one
_product = num_two * num_one
_division = num_one / num_two
_floor_division = num_two % num_one

radius = input("insert radius: ")
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
print(area_of_circle)

# name = input("firstname: ")
# last = input("lastName: ")
help("keywords")
