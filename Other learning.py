#################################################
# Change Test
#################################################

#-------------------VARIABLES---------------------
# underscores_are_good_to_read
# variables are case sensitive

# variable : string
# full_name = "Chris Weatherall"
# print (full_name)
#
# Chris Weatherall

#---------------DATA TYPES----------------------
# Strings, just text in single or double quotation marks
# Numbers, never wrapped in quotation marks, or they become a string
# Lists, always in [], like ["John", "Bob", 41], can add and remove things to lists
# Tuples, is a list which you can't change, they are faster but it's no difference, rarely used
# Dictionaries, a more complicated list
# Boolean, true or false, like to see if something exists, or for carrying on loops etc

#list
names = ["John", "Bob", "Mary"]
print (names[1])
# Bob, as the list starts at 0
print (names)
# ["John", "Bob", "Mary"]

# Tuple
names = ("John", "Bob", "Mary")
print (names[2])
# Mary, as the list starts at 0
print (names)
# ("John", "Bob", "Mary")

# Dictionaries, good for databases
name = "John"
age = 41
fav_pizza = {
	"John": "Pepperoni",
	"Tim" : "Mushroom",
	"Mary" : "Cheese",
}
# can also show the dictionary as {"John": "Pepperoni", "Tim" : "Mushroom", "Mary" : "Cheese"}
print (fav_pizza["John"])
# Pepperoni

#----------------Version Control-----------------------------
# Version control is like saving as you go along
# Git hub is like a social network etc, industry standard place to host your code
# install git bash terminal, then only needs a couple of changes, and connect it to git hub
# Set up SSH key so you can connect securely
#-----------------COMMANDS----------------------------------
# Chris@Chris-2020-PC MINGW64 ~
# $ pwd           # lists current directory, python working directory?
# /c/Users/Chris
#
# Chris@Chris-2020-PC MINGW64 ~
# $ ls            	# list stuff, lists files and folders in directory
#
# clear           	# clears the screen
# mkdir .ssh		# makes ssh directory, and the . before makes it hidden	
# ssh-keygen.exe	# generates a key, pword is C4wc


