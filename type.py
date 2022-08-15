a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None

b_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
b_tuple = ("Mon", "Tue", "Wed", "Thur", "Fri")

nico = {
    "name":"Nico",
    "age": 29,
    "korean": True,
    "fav_food": ["Kimchi", "Sashimi"]
}

print(type(nico))
print(nico)
print(nico["name"])

nico["handsome"] = True
print(nico)

# print(type(b_tuple))

# print(type(a_string))
# print(type(a_number))
# print(type(a_float))
# print(type(a_boolean))
# print(type(a_none))

# print(type(b_list), b_list, "Mon" in b_list, b_list[3], len(b_list))

# b_list.append("Sat")
# print(b_list)

# b_list.reverse()
# print(b_list)