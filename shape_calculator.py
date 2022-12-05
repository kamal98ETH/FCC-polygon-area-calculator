class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        shape = ""
        for i in range(int(self.width)):
            shape += "*"
        shape += "\n"
        shape = shape * int(self.height)
        if int(self.height) < 50 and int(self.width) < 50:
            return shape
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        num_height = int(self.height / shape.height)
        num_width = int(self.width / shape.width)
        num = num_height * num_width
        return num

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super(Rectangle, self).__init__()
        self.width = side
        self.height = side

    def set_side(self, new):
        self.width = new
        self.height = new

    def set_height(self, new):
        return Square.set_side(self, new)

    def set_width(self, new):
        return Square.set_side(self, new)

    def __repr__(self):
        return f"Square(side={self.height})"
