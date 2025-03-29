import turtle
import random
import time

def draw_moon(x, y, size):
    # Full moon
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
    # Crescent effect (Adjusted for better shape)
    turtle.penup()
    turtle.goto(x + size * 0.4, y - size * 0.2)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(size * 0.85)
    turtle.end_fill()

def draw_star(x, y, size, color=None):
    colors = ["red", "yellow", "orange", "purple", "green"]
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color if color else random.choice(colors))
    for _ in range(10):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(36)

def fireworks():
    for _ in range(20):  # Increased for better effect
        x = random.randint(-300, 300)
        y = random.randint(50, 250)
        size = random.randint(10, 30)
        if abs(x) > 120 or abs(y - 100) > 100:  
            draw_star(x, y, size)
            time.sleep(0.1)

def draw_text():
    turtle.penup()
    turtle.goto(-100, -120)
    turtle.color("white")
    turtle.pendown()
    
    text = "Chand Raat Mubarak"
    for letter in text:
        turtle.write(letter, font=("Arial", 20, "bold"))
        time.sleep(0.1)
        turtle.goto(turtle.xcor() + 15, turtle.ycor())

def draw_twinkle_stars():
    for _ in range(30):
        x = random.randint(-350, 350)
        y = random.randint(-50, 300)
        size = random.randint(3, 7)
        if abs(x) > 120 or abs(y - 100) > 100:  # Avoid stars touching the moon
            draw_star(x, y, size, "white")

def setup_screen():
    turtle.bgcolor("black")
    turtle.speed(0)

def main():
    setup_screen()
    draw_moon(0, 100, 90)
    draw_twinkle_stars()
    fireworks()
    draw_text()
    turtle.hideturtle()
    turtle.done()

main()
