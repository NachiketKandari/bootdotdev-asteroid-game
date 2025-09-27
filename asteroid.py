from main import ASTEROID_MIN_RADIUS
from player import CircleShape
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen ,"white",self.position, self.radius, 2 )
    
    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        vec_1 = self.velocity.rotate(random_angle)
        vec_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1, asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vec_1*1.2
        asteroid_2.velocity = vec_2
