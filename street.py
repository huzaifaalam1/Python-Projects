'''
File: street.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program takes a user input
        taking specifications for a city. It
        then prints the ASCII display for the city.
'''

class Street:
    '''
    Creates a street intialized with 
    a height and width of 0
    '''
    def __init__(self):
        '''
        Initializes a Street object.
        '''
        self._street = []
        self._height = 0
        self._width = 0

    def get_street(self):
        return self._street
    
    def get_height(self):
        return self._height 

    def get_width(self):
        return self._width
    
    def add(self, item):
        '''
        Adds the other structures from the 
        other classes using this method
        Parameter:
                self: object
                item: another class' instance
        '''
        self._street.append(item)
    
    def incr_width(self, item):
        '''
        Increases the width of the street 
        depending on how many structures are 
        to be added 
        '''
        self._width += item

    def incr_height(self, item):
        '''
        Changes the height of the street
        if object hinders height
        '''
        if item > self.get_height():
            self._height = item 

    def print_city(self, height):
        '''
        Prints the layout of the street
        along with all the structures i.e the 
        objects using recursion 
        Parameters:
                    self: object
                    height: the height
        '''
        if height == -1:
            print("+" + "-"*self.get_width() + "+")
        elif height == self.get_height():
            print("+" + "-"*self.get_width() + "+")
            print("|" + ""*self.get_width() + "|")
            self.print_city(height-1)
        else:
            print("|" + self.make_street(self._street, height) + "|")
            self.print_city(height-1)

    def make_street(self, street, height):
        '''
        Checks the street (a list) and recurses
        through printing each instance of other
        objects in street
        Parameters:
                    self: object
                    street: list
                    height: the height 
        '''
        if street == []:
            return ""
        else:
            return street[0].print_city(height) \
                + self.make_street(street[1:] , height)
        
    def __str__(self):
        '''
        Returns a string representation of the Street object.
        '''
        return "H: " + str(self._height) + \
                ", W: " + str(self._width) + \
                    ", St: " + str(self._street)

class Park:
    '''
    Creates a park intialized with 
    a height and width
    '''
    def __init__(self, specs):
        '''
        Initializes a Park object with
        the given specifications
        '''
        specs = specs.split(",")
        self._width = int(specs[0])
        self._foliage = specs[1]
        self._shape = []
        self.build(self._width, self._foliage, 5)
    
    def get_width(self):
        return self._width
    
    def get_foliage(self):
        return self._foliage
    
    def get_shape(self):
        return self._shape
    
    def build(self, width, foliage, height):
        '''
        Builds the shape of the park based
        on width, foliage and height.
        '''
        if height != 0:
            half = width // 2
            if height == 1:
                self._shape.append(" " * half + foliage + " " * half)
            elif height == 2:
                self._shape.append(" " * (half - 1) + foliage * 3 + " "\
                    * (half - 1))
            elif height == 3:
                self._shape.append(" " * (half - 2) + foliage * 5 + " "\
                    * (half - 2))
            else:
                self._shape.append(" " * half + "|" + " " * half)
            self.build(width, foliage, height - 1)
        
    def print_city(self, height):
        '''
        Prints the park layout up to the specified height.
        '''
        if height >= 5:
            return " " * self._width
        else:
            return self._shape[height]
        
    def __str__(self):
        '''
        Returns a string representation of the Park object.
        '''
        return "p:" + str(self._width) + "," \
            + self._foliage + ": " + str(self._shape)
    
class Lots:
    '''
    Creates a lot intialized with 
    a height and width
    '''
    def __init__(self, specs):
        '''
        Initializes a Lot object with
        the given specifications
        '''
        specs = specs.split(",")
        self._width = int(specs[0])
        self._trash = specs[1]
        self._trash = self._trash.replace("_", " ")
        self._shape = ""
        self.build(self._width, self._trash)
    
    def get_width(self):
        return self._width
    
    def get_trash(self):
        return self._trash
    
    def get_shape(self):
        return self._shape
    
    def build(self, width, trash):
        '''
        build creates an empty lot
        '''
        if width <= len(trash):
            self._shape += trash[:width]
        else:
            self._shape += trash
            self.build(width - len(trash), trash)

    def print_city(self, height):
        '''
        Prints the lot layout up to the specified height
        '''
        if height >= 1:
            return " " * self._width
        else:
            return self._shape
        
    def __str__(self):
        '''
        Returns a string representation of the Lots object.
        '''
        return "e:" + str(self._width) + "," + \
            self._trash + ": " + str(self._shape)

class Building:
    '''
    Creates a Building intialized with 
    a height and width
    '''
    def __init__(self, specs):
        '''
        Initializes a Building object with given specifications.
        '''
        specs = specs.split(",")
        self._shape = []
        self._width = int(specs[0])
        self._height = int(specs[1])
        self._brick = specs[2]
        self.build(self._width, self._height, self._brick)

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_brick(self):
        return self._brick
    
    def get_shape(self):
        return self._shape
    
    def build(self, width, height, build):
        '''
        Builds the shape of the building
        based on width, height, and build
        '''
        if height != 0:
            self._shape.append(build * width)
            self.build(width, height - 1, build)
    
    def print_city(self, height):
        '''
        Prints the building layout up to the specified height
        '''
        if height >= self._height:
            return " " * self._width
        else:
            return self._shape[height]
        
    def __str__(self):
        '''
        Returns a string representation of the Building object.
        '''
        return "b:" + str(self._width) + "," + str(self._height) + ","\
            + self._brick + ": " + str(self._shape)
    
def read_line(street_list, street):
    '''
    Checks the input for given objects
    adds the streets and calls other functions
    accordingly through if statements and recursion
    '''
    if street_list != []:
        if street_list[0][0] == "p":
            park = Park(street_list[0][2:])
            street.add(park)
            street.incr_height(5)
            street.incr_width(park.get_width())
        if street_list[0][0] == "b":
            building = Building(street_list[0][2:])
            street.add(building)
            if building.get_width() != 0:
                street.incr_height(building.get_height())
            if building.get_height() != 0:
                street.incr_width(building.get_width())
        if street_list[0][0] == "e":
            lot = Lots(street_list[0][2:])
            street.add(lot)
            if lot.get_width() != 0:
                street.incr_height(1)
            street.incr_width(lot.get_width())
        read_line(street_list[1:], street)

def main():
    street = Street()
    street_input = input("Street: ").split()
    read_line(street_input, street)
    street.print_city(street.get_height())

main()