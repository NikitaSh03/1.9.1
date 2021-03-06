from main import Rectangle, Square, Circle
Rect1 = Rectangle(9, 12)
Rect2 = Rectangle(6, 17)
Cirk1 = Circle(7)
Cirk2 = Circle(5)
Squa1 = Square(15)
Squa2 = Square(8)

Figures = [Rect1,Rect2,Squa1,Squa2,Cirk1,Cirk2]
for figure in Figures:
    if isinstance(figure,Rectangle):
        print(figure.get_area())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area_circle())