import math
import copy

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """Represents a rectangle.
    Attributes: width, height, corner.
    """

def print_point(p):
    print('(%g, %g)' %(p.x, p.y))

def distance_between_points(p1, p2):
    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return distance

class Circle():
    """Represents a circle.
    Attributes: center, radius
    """

def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle(or on the boundary).
    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius

def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle. 
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False
    
    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False
    
    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True

def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()



