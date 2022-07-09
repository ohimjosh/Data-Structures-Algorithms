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

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')
print('Cookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

# -----------------------------------------------------------
