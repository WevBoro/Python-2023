# FOR LOOPS

# x is placeholder value, like a counter, starts at zero don't need to set it
# name is the variable to loop through

# -----------------------------------------------------------------------------------

# name = "John"
#
# for x in name:
# 	print(x)

# This would loop through and return
# J
# o
# h
# n

# -----------------------------------------------------------------------------------

# Then trying with a list
# names = ["John", "Bob", "Mary"]
#
# for name in names:
# 	print(name)

# This would loop through and return
# John
# Bob
# Mary

# -----------------------------------------------------------------------------------

# Then trying with a dictionary. Each dictionary has a key and a value pair.
# .items calls the items function, which gets all the items in the dictionary into a thing which is accessible

# fav_pizza = {
# 	"John": "Pepperoni",
# 	"Tim" : "Mushroom",
# 	"Mary" : "Cheese",
# }
#
# for key,value in fav_pizza.items():
# 	print(key)

# This would loop through and return
# John
# Tim
# Mary

# fav_pizza = {
# 	"John": "Pepperoni",
# 	"Tim" : "Mushroom",
# 	"Mary" : "Cheese",
# }
#
# for key,value in fav_pizza.items():
# 	print(value)

# This would loop through and return
# Pepperoni
# Mushroom
# Cheese


fav_pizza = {
	"John": "Pepperoni",
	"Tim" : "Mushroom",
	"Mary" : "Cheese",
}

# don't need to be called key and value, but that's what they are
for key,value in fav_pizza.items():
	print(key + " likes " + value + " pizza!")

# This would loop through and return
# John likes Pepperoni pizza!
# Tim likes Mushroom pizza!
# Mary likes Cheese pizza!