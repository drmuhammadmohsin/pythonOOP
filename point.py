
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def plot(self):
        plt.plot(self.x, self.y, 'ro')
    
    @staticmethod
    def show_plot():
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Plot of Points')
        plt.grid(True)
        plt.show()

# Create multiple points
points = [
    Point(3, 4),
    Point(7, 2),
    Point(5, 6)
]

# Plot all points
for point in points:
    point.plot()

# Show the plot
Point.show_plot()