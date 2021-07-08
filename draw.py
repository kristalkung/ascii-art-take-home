class Shape:
    """A shape class."""
    pass

class Rectangle(Shape):
    """A rectangle shape class."""
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
    """A canvas class."""
    shape_dict = {}

    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def print_blank_canvas(self):
        """Prints the canvas."""
        for i in range(0, self.height):
            canvas_width = ' ' * self.width
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

        canvas_rows = []
        # canvas_rows will contain each row of the canvas

        for i in range(0, self.height):
            x = ' ' * self.width
            canvas_rows.append(x)
        # this is made depending on the given width and height of the canvas
        
        for current_shape in self.shape_dict.keys():
        # iterate over keys of shape_dict, which are the shapes added

            for i, row in enumerate(canvas_rows):
            # iterate over each row

                if i == current_shape.start_y:
                # if the row is equal to the start_y

                    r = current_shape.start_y
                    # set a counter to keep track of how many rows we've gone through once we hit start_y

                    while r <= current_shape.end_y:
                    # iterate until we after we hit end_y
                        insert_width = current_shape.end_x - current_shape.start_x
                        remaining_width = self.width - current_shape.end_x
                        canvas_rows[i] = (' ' * current_shape.start_x) + (current_shape.fill_char * insert_width) + (' ' * remaining_width)
                        # replace row str based on the width; fill in the fill char

                        r += 1

        for row in canvas_rows:
            print(row)

    def clear_all_shapes(self):
        """Clears all shapes on the canvas."""
        
        self.shape_dict.clear()
