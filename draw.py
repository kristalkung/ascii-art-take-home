class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char
    
    def change_fill_char(self, char):
        """Changes the fill character of a rectangle."""
        self.fill_char = char
    
    def translate(self, axis, num):
        """Moves the rectangle. Negative numbers shift left/down. Positive shift right/up."""
        if self.axis == 'x':
            start_x += self.axis
            end_x += self.axis
        else:
            start_y += self.num
            end_y += self.num

class Canvas:
    shape_dict = {}

    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def print_blank_canvas(self):
        """Prints the canvas."""
        for i in range(0, self.height):
            canvas_width = '.' * self.width
            print(canvas_width)
    
    def add_shape(self, shape):
        """Adds a shape to the canvas and plots it."""
        start_x = shape.start_x
        start_y = shape.start_y
        end_x = shape.end_x
        end_y = shape.end_y
        fill_char = shape.fill_char

        shape_info = {'start_x': shape.start_x, 
                 'start_y': shape.start_y, 
                 'end_x': shape.end_x,
                 'end_y': shape.end_y,
                 'fill_char': shape.fill_char}
        
        self.shape_dict[shape] = shape_info
        
        # insert_shape_width = fill_char * (end_x - start_x)
        # insert_shape_height = end_y - start_y

        # for i in range(0, end_y - start_y):
        #     canvas_width = '.' * self.width
        #     canvas_width_shape = canvas_width[:start_x] + insert_shape_width + canvas_width[end_x:]
        #     print(canvas_width_shape)

        # for i in range(0, self.height - end_y):
        #     canvas_width = '.' * self.width
            
        #     print(canvas_width)

    def clear_all_shapes(self):
        """Clears all shapes on the canvas."""
        
        self.shape_dict.clear()

