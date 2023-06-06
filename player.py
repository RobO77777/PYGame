import pygame

NOIR = (0, 0, 0)

class Player:
    def __init__(self, x, y, rayon):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.deplacement_x = 0
        self.deplacement_y = 0

    def update(self, deplacement_x, deplacement_y):
        self.deplacement_x = deplacement_x
        self.deplacement_y = deplacement_y

    def draw(self, fenetre):
        pygame.draw.circle(fenetre, NOIR, (self.x, self.y), self.rayon)
