#Var
index = 0
index2 = 2
options = [
	["A", "B"],
	["C", "D"],
	["E", "F"],
	["G", "H"]
]
category = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[0]
]
products = [True, False]
unitPrice = ""
totalPrice = ""
quantity = ""

#Functions
def showOptions(index):
	print("Opciones: ")
	while(index < len(options)):
		print(index," = ", options[index])
		index += 1
	if (index == len(options)):
		index = 0
def selectOptions():
	num = input("Seleccione que quiere hacer: ")
	return num
	
"""
		
def showCategory(index):
	while(index < len(category)):
		print(index, " = ", category[index])
		index += 1
	if (index == len(category)):
		index = 0

def selectCategory():
	num = input("Seleccione que categoria quiere: ")b 
	return num

def nameProduct():

def buyCount():
	
def showInfo():
"""
#Flow

showOptions(index)
capOptions=selectOptions()
"""
showCategory(index)
capCategory=selectCategory()
showCategory(index)
"""