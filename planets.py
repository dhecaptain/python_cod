import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Planet data (semi-major axis in AU and orbital period in years)
planet_data = {
    'Mercury': (0.39, 0.24),
    'Venus': (0.72, 0.62),
    'Earth': (1.0, 1.0),
    'Mars': (1.52, 1.88),
}

fig, ax = plt.subplots()

# Set up the Sun
sun = plt.Circle((0, 0), 0.1, color='yellow')

# Initialize planet positions
planet_positions = {planet: (semi_major_axis, 0) for planet, (semi_major_axis, _) in planet_data.items()}
planet_circles = {planet: plt.Circle(planet_positions[planet], 0.05, label=planet) for planet in planet_data}

ax.add_artist(sun)
for circle in planet_circles.values():
    ax.add_artist(circle)

def animate(frame):
    for planet, (semi_major_axis, orbital_period) in planet_data.items():
        angle = 2 * np.pi * (frame % orbital_period) / orbital_period
        x = semi_major_axis * np.cos(angle)
        y = semi_major_axis * np.sin(angle)
        planet_positions[planet] = (x, y)
        planet_circles[planet].center = (x, y)

    return list(planet_circles.values())

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', adjustable='datalim')
ax.set_title('Solar System')
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.legend()

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)

plt.show()