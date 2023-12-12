import pygame
from random import randint
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, image_path, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
        print(image_path)
   # Load the image of the car
        self.image = pygame.image.load(image_path).convert_alpha()

 # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.speed = speed

        # Draw the car (a rectangle!)
        # pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


        # Fetch the rectangle object that has the dimensions of the image.
        #self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        if(self.rect.x < 380):
            self.rect.x += pixels * self.speed

    def moveLeft(self, pixels):
        if(self.rect.x > 40):
            self.rect.x -= pixels * self.speed

    def moveUp(self, pixels):
        if(self.rect.y > 25):
            self.rect.y -= pixels * self.speed

    def moveDown(self, pixels):
        if(self.rect.y < 500):
            self.rect.y += pixels * self.speed


    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed