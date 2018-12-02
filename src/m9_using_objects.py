"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Zhicheng Kai.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles(500, 600, 100, 700, 300, 200, 'gold')
    circle_and_rectangle(1, 'blue', 180, 115, 100, 1, None, 100, 200, 400, 700)
    lines()


def two_circles(p1x, p1y, r1, p2x, p2y, r2, color):
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(1000,1000)
    circle1 = rg.Circle(rg.Point(p1x, p1y), r1)
    circle2 = rg.Circle(rg.Point(p2x, p2y), r2)
    circle1.fill_color = color
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle(tc, color, cx, cy, r,tr,color2, p1x, p1y, p2x, p2y):
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow(800,800)
    circle = rg.Circle(rg.Point(cx, cy), r)
    circle.outline_thickness = tc
    circle.fill_color = color
    rectangle = rg.Rectangle(rg.Point(p1x,p1y), rg.Point(p2x,p2y))
    rectangle.outline_thickness = tr
    rectangle.fill_color = color2
    circle.attach_to(window)
    print(tc)
    print(color)
    print(rg.Point(cx, cy))
    print(cx)
    print(cy)
    print(tr)
    print(color2)
    print(rg.Point((p2x-p1x)/2, (p2y-p1y)/2))
    print((p2x-p1x)/2)
    print((p2y-p1y)/2)


    rectangle.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()
    line1 = rg.Line(rg.Point(100,200),rg.Point(300,100))
    line1.thickness = 1
    line2 = rg.Line(rg.Point(300,200),rg.Point(100,100))
    line2.thickness = 20
    print(line2.get_midpoint())
    print(200.0)
    print(150.0)
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    # DONE: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
