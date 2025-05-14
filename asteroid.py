from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            random_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            for i in range(2):
                if i == 1:
                    random_angle = -random_angle

                velocity = self.velocity.rotate(random_angle)
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = velocity * 1.2