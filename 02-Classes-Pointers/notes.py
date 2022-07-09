# -----------------------------------------------------------

# What is a class?
# creates your own datatype

class Cookie:
    # constructor
    def __init__(self, color):

        # when you enter a color in the parameter
        # color will be passed to self.color which will take
        # that color and apply it to the specific instance
        # of color we are creating

        self.color = color
        # self is a particular instance 

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

# create a new Cookie
cookie_one = Cookie('green')

# cookie_one is being assigned type Cookie passing it the color green
# then passed it down to the constructor creating a green cookie

cookie_two = Cookie('blue')

# print('Cookie one is', cookie_one.get_color())
# print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')
# print('Cookie one is now', cookie_one.get_color())
# print('Cookie two is still', cookie_two.get_color())

# -----------------------------------------------------------

# What is a pointer?
# holds memory address of a value
# variable will point to the memory address giving it the value

dict1 = {
        'value': 11
        }

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

dict1['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# they both point to the same value so the value is now 22

# pointers can be redirected

dict3 = {
        'value': 57
        }

dict2 = dict3

print("\nAfter pointer is redirected:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict3 =", dict3)

# dict2 is now pointing to dict3

# What happens when you point dict1 to dict3
dict1 = dict3

# since dict1 is now 57 it the value of 22 will go through garbage collection
# garbage collection clears up unused memory 

print("\nPointers all point dict3:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict3 =", dict3)
