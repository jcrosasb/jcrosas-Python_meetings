# Define a Shape class
class Shape:
    def draw(self):
        pass

# Define a Circle class inheriting from Shape
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# Define a Rectangle class inheriting from Shape
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

# Main function
def main():
    # Create instances of Circle and Rectangle
    circle = Circle()
    rectangle = Rectangle()

    # Draw the shapes
    circle.draw()     # Draws a circle
    rectangle.draw()  # Draws a rectangle

if __name__ == "__main__":
    main()