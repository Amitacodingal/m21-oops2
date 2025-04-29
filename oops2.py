#act 1

# create class
class IOString():

	# constructor to set default value
    def __init__(self):
        self.str1 = ""

	# function to get input from user
    def get_String(self):
        self.str1 = input("Enter String : ")

	# function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()

#act2
# Create Class
class Employee:
  
    # Initializing 
    def __init__(self):
        print('Employee created')
  
    # Calling destructor
    def __del__(self):
        print("Destructor called")
  
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
  
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

#act3 enumerate method
# create a class
class pair_elements:
	
	def twoSum(self, nums, target):
		# create an empty dictionary
		lookup = {}

		# Iterate through the tuple
		for i, num in enumerate(nums):
			if target - num in lookup:
				return (lookup[target - num], i )
			lookup[num] = i

# take input of dum from the user
value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))

#acp

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

radius = int(input("Enter Radius : "))
NewCircle = Circle(radius)
print(NewCircle.area())
print(NewCircle.perimeter())


