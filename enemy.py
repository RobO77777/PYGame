import pygame
import random

NOIR = (0, 0, 0)

class Enemy:
    def __init__(self, x, y, taille):
        self.x = x
        self.y = y
        self.taille = taille
        self.points_de_vie = 10

    @staticmethod
    def create_random_enemy(largeur, hauteur):
        taille = random.randint(20, 40)
        x = random.randint(taille, largeur - taille)
        y = random.randint(taille, hauteur - taille)
        return Enemy(x, y, taille)

    def update(self, joueur_x, joueur_y):
        self.x += joueur_x
        self.y += joueur_y

    def draw(self, fenetre):
        pygame.draw.rect(fenetre, NOIR, (self.x - self.taille/2, self.y - self.taille/2, self.taille, self.taille))
