import turtle

def create_planet(color, radius, distance):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.penup()
    planet.goto(distance, 0)
    planet.pendown()
    return planet

def move_planet(planet, speed, angle):
    x = distance * speed * angle
    y = distance * (1 - speed**2 * (1 - angle**2))**0.5
    planet.goto(x, y)

Screen = turtle.Screen()
Screen.bgcolor("black")

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")

planets_info = [("gray", 10, 50, 1.5),   # Mercury
                ("orange", 15, 80, 1.2),  # Venus
                ("blue", 20, 110, 1.0),   # Earth
                ("red", 25, 140, 0.8)]    # Mars

planets = [create_planet(color, radius, distance) for color, radius, distance, _ in planets_info]

angle = 0
while True:
    for planet, (_, _, distance, speed) in zip(planets, planets_info):
        move_planet(planet, speed, angle)

    angle += 0.01

    turtle.update()  # Update the screen

# turtle.done()  # This line is commented out to keep the program running indefinitely
