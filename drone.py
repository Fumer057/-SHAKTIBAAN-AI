import matplotlib.pyplot as plt

class Drone:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [1.0, 0.5]

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

drone = Drone(x=0, y=0)

x_trail = []
y_trail = []

for step in range(30):
    drone.move()
    x_trail.append(drone.position[0])
    y_trail.append(drone.position[1])

plt.plot(x_trail, y_trail, marker='o')
plt.title("One drone moving")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()