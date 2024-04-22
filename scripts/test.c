#include <stdio.h>

// Define a generic shape struct
typedef struct {
    void (*draw)(void); // Function pointer for drawing the shape
} Shape;

// Function to draw a circle
void drawCircle() {
    printf("Drawing a circle\n");
}

// Function to draw a rectangle
void drawRectangle() {
    printf("Drawing a rectangle\n");
}

int main() {
    // Define instances of shapes
    Shape circle, rectangle;

    // Assign functions to the function pointers
    circle.draw = drawCircle;
    rectangle.draw = drawRectangle;

    // Draw the shapes
    circle.draw(); // Draws a circle
    rectangle.draw(); // Draws a rectangle

    return 0;
}