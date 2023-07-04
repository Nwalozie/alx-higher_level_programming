#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A representation a a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width attribute"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """gets the height attribute"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return(self.__width * self.__height)
   
    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(2 * (self.__width + self.__height))

    def __str__(self) -> str:
        """Returns a string representation of the rectangle using '#' characters."""
        if (self.__width == 0) or (self.__height == 0):
            return("")
        else:
            rect = []
            for i in range(self.__height - 1):
                rect.append(str(Rectangle.print_symbol) * self.width + "\n")
            rect.append(str(Rectangle.print_symbol) * self.width)
            return ("".join(rect))
    
    def __repr__(self) -> str:
        """Returns a string representation of the rectangle that can be used to
        recreate a new instance using eval()."""
        return f"Rectangle({self.__width}, {self.__height})" 

    def __del__(self):
        """Print the message Bye rectangle...when an instance of
        Rectangle is deleted and and Decremented during
        each instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
