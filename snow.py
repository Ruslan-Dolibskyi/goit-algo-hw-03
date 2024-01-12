import turtle


def koch_curve(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, order-1, size/3)
            turtle.left(angle)


# Налаштування вікна та черепашки
window = turtle.Screen()
window.bgcolor("white")

flake = turtle.Turtle()
flake.color("blue")

# малювання сніжинки Коха
flake.penup()
flake.goto(-150, 90)
flake.pendown()
level = int(
    input("Вкажіть рівень рекурсії для сніжинки Коха (від 0 до 5 ): "))

for _ in range(3):
    koch_curve(flake, level, 300)
    flake.right(120)

flake.hideturtle()
window.mainloop()