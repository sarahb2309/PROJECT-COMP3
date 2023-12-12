import pygame
from random import randint

class Powerup(pygame.sprite.Sprite):
    def __init__(self, path, type):
        super().__init__()

        self.image = pygame.image.load(path).convert_alpha()
 
        self.type = type
        self.speed = 1
        # self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        # self.image.fill((0, 0, 0, 0)) 

        # pygame.draw.polygon(self.image, color, [(0, height // 2), (width, height // 2), (width // 2, height)])
        # pygame.draw.polygon(self.image, color, [(width // 2, 0), (width, height), (0, height), (width // 2, 0)])

        self.rect = self.image.get_rect()
    
    def moveForward(self):
        self.rect.y += self.speed * self.speed / 20

    def reset_position(self):
        self.rect.x = randint(40, 340)
        self.rect.y = randint(-500, -100)

    def update(self):
        self.rect.y += self.speed