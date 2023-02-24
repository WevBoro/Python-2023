# this imports all the tkinter GUI stuff, the * is all
from tkinter import *
import sqlite3

# CTRL + / comments out sections

# this creates the root widget, like the main window
root = Tk()
root.title('Job Details')
# Set the geometry

# Quick Way
# root.geometry("300x400")
# root.eval('tk::PlaceWindow . center')

# better way
width = 400  # Width
height = 600  # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))


# Create a database to connect to one
connection = sqlite3.connect('job_details.db')

# Create cursor
cursor = connection.cursor()

# Create a table, this uses SQL commands, and """ allows to use multiple lines for doc string. " is single line
# Table only needs creating one time
# Each line is a column, doesn't need to be same name as our variables, I don't think (John Elder)
# IF NOT EXISTS saves hashing this next part out
# Table may need creating again if filename changes?
cursor.execute("""CREATE TABLE IF NOT EXISTS site_info (
			client TEXT,
			contractor TEXT,
			subcontractor TEXT,
			job_name TEXT,
			job_location TEXT,
			job_distance INTEGER
			)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS installations (
			install_id INTEGER PRIMARY KEY,
			description TEXT,
			utility TEXT,
			crossing TEXT,
			grade TEXT,
			length INTEGER,
			duct_1 INTEGER,
			duct_2 INTEGER,
			duct_3 INTEGER,
			duct_4 INTEGER,
			duct_5 INTEGER,
			duct_6 INTEGER,
			duct_7 INTEGER,
			duct_8 INTEGER,
			bore_size INTEGER,
			expected_ground TEXT
			
			)""")

# Defining functions

# Create submit Function for database, into site info table
# TODO: problem with this is it will have multiple records
def info_submit():
	# Create a database or to connect to one
	connection = sqlite3.connect('job_details.db')
	# Create cursor
	cursor = connection.cursor()

	# Insert into Table - This is getting columns to match up to variables, makes sense to name them the same
	# {is creating a dictionary}, [this would be a list, I think]
	cursor.execute("INSERT INTO site_info VALUES (:client, :contractor, :subcontractor, :job_name, :job_location, :job_distance)",
		{
			'client': client.get(),
			'contractor': contractor.get(),
			'subcontractor': subcontractor.get(),
			'job_name': job_name.get(),
			'job_location': length.get(),
			'job_distance': job_distance.get()
		})
	print("Written to database")

	# Commit Changes
	connection.commit()

	# Close Connection
	connection.close()


	# # Clear the text boxes, this might only be needed for the installations table, client stuff probably to stay on screen
	# client.delete(0, END)
	# contractor.delete(0, END)
	# subcontractor.delete(0, END)
	# job_name.delete(0, END)
	# job_location.delete(0, END)
	# job_distance.delete(0, END)

# SITE_INFO ASPECTS

# this creates the site_info labels and positions them
client_Label = Label(root, text="Client", anchor="w", width=15)
client_Label.grid(row=0, column=0)
contractor_Label = Label(root, text="Contractor", anchor="w", width=15)
contractor_Label.grid(row=1, column=0)
subcontractor_Label = Label(root, text="Subcontractor", anchor="w", width=15)
subcontractor_Label.grid(row=2, column=0)
job_name_Label = Label(root, text="Job Name", anchor="w", width=15)
job_name_Label.grid(row=3, column=0)
job_location_Label = Label(root, text="Location", anchor="w", width=15)
job_location_Label.grid(row=4, column=0)
job_distance_Label = Label(root, text="Distance (miles)", anchor="w", width=15)
job_distance_Label.grid(row=5, column=0)

# this creates site_info entry boxes and positions them
client = Entry()
client.grid(row=0, column=1)
contractor = Entry()
contractor.grid(row=1, column=1)
subcontractor = Entry()
subcontractor.grid(row=2, column=1)
job_name = Entry()
job_name.grid(row=3, column=1)
job_location = Entry()
job_location.grid(row=4, column=1)
job_distance = Entry()
job_distance.grid(row=5, column=1)

# Create a site_info table submit button
info_submit_btn = Button(root, text="Submit", command=info_submit)
info_submit_btn.grid(row=6, column=0)

# INSTALLATIONS ASPECTS

# Creating installation info Labels
description_Label = Label(root, text="Description", anchor="w", width=15)
description_Label.grid(row=7, column=0)
utility_Label = Label(root, text="Utility", anchor="w", width=15)
utility_Label.grid(row=8, column=0)
crossing_Label = Label(root, text="Crossing", anchor="w", width=15)
crossing_Label.grid(row=9, column=0)
grade_Label = Label(root, text="Grade", anchor="w", width=15)
grade_Label.grid(row=10, column=0)
length_Label = Label(root, text="Length (m)", anchor="w", width=15)
length_Label.grid(row=11, column=0)
d1_Label = Label(root, text="Duct 1 (mm)", anchor="w", width=15)
d1_Label.grid(row=12, column=0)
d2_Label = Label(root, text="Duct 2 (mm)", anchor="w", width=15)
d2_Label.grid(row=13, column=0)
d3_Label = Label(root, text="Duct 3 (mm)", anchor="w", width=15)
d3_Label.grid(row=14, column=0)
d4_Label = Label(root, text="Duct 4 (mm)", anchor="w", width=15)
d4_Label.grid(row=15, column=0)
d5_Label = Label(root, text="Duct 5 (mm)", anchor="w", width=15)
d5_Label.grid(row=16, column=0)
d6_Label = Label(root, text="Duct 6 (mm)", anchor="w", width=15)
d6_Label.grid(row=17, column=0)
d7_Label = Label(root, text="Duct 7 (mm)", anchor="w", width=15)
d7_Label.grid(row=18, column=0)
d8_Label = Label(root, text="Duct 8 (mm)", anchor="w", width=15)
d8_Label.grid(row=19, column=0)
bore_Label = Label(root, text="Bore Size (mm)", anchor="w", width=15)
bore_Label.grid(row=20, column=0)
ground_Label = Label(root, text="Expected Ground", anchor="w", width=15)
ground_Label.grid(row=21, column=0)

# this creates installations entry boxes and positions them
description = Entry()
description.grid(row=7, column=1)
utility = Entry()
utility.grid(row=8, column=1)
crossing = Entry()
crossing.grid(row=9, column=1)
grade = Entry()
grade.grid(row=10, column=1)
length = Entry()
length.grid(row=11, column=1)
d1 = Entry()
d1.grid(row=12, column=1)
d2 = Entry()
d2.grid(row=13, column=1)
d3 = Entry()
d3.grid(row=14, column=1)
d4 = Entry()
d4.grid(row=15, column=1)
d5 = Entry()
d5.grid(row=16, column=1)
d6 = Entry()
d6.grid(row=17, column=1)
d7 = Entry()
d7.grid(row=18, column=1)
d8 = Entry()
d8.grid(row=19, column=1)
bore  = Entry()
bore.grid(row=20, column=1)
ground = Entry()
ground.grid(row=21, column=1)


# Commit changes
connection.commit()

# Close Connection
connection.close()

root.mainloop()  # this creates the loop to run the GUI

# this puts label into the root widget, in row/ columns
# clientLabel.grid(row=0, column=0)
# client.grid(row=0, column=1)
# contractorLabel.grid(row=1, column=0)
# contractor.grid(row=1, column=1)
# subcontractorLabel.grid(row=2, column=0)
# subcontractor.grid(row=2, column=1)


# job_loc = input("Where is the job location? ")
# job_dist = input("What is the distance in miles? ")
# mob_miles = 2 * int(job_dist)
# msg1 = (f"Total driving time is {mob_miles} miles.")
# print(msg1)
#
# inst_no = input("How many installations are there? ")
#
# length = input("What is the length of the installation, in meters? ")
# duct_no = input("How many ducts are there for this installation? ")
#     # this should be a loop which then asks for the size of each duct, and sdr rating
#     # look up list of pipe prices in Excel sheet
#     # calculate bore size from this
# service = input("What is the installation for? Gas, Water, Electric etc. ")
# swdd_diff = input("What is the installation difficulty for us? (1 Easy, 9 Very difficult? ")
# client_diff = input("What is the installation difficulty for the client? (1 Easy, 9 Very difficult? ")

# list out
# def formclick():
# 	fl = Label(root,
# 		text=client.get() + '\n' +
# 		contractor.get() + '\n' +
# 		subcontractor.get() + '\n' +
# 		job_name.get() + '\n' +
# 		job_location.get() + '\n' +
# 		job_distance.get(),
# 		anchor="w", width=15)
# 	fl.grid(row=7, column=0)














