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

        self.boom = pygame.mixer.Sound("boom.wav")
        self.bang = pygame.mixer.Sound("bang.wav")
        self.pow = pygame.mixer.Sound("pow.wav")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        n = random.randint(1, 3)
        if n == 1: self.bang.play()
        elif n == 2: self.pow.play()
        else: self.boom.play()

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