import pygame
import random

ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

class Circle:
    def __init__(self, x, y, rayon, couleur):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur

    @staticmethod
    def create_random_circle(largeur, hauteur):
        rayon = random.randint(10, 30)
        x = random.randint(rayon, largeur - rayon)
        y = random.randint(rayon, hauteur - rayon)
        couleur = random.choice([ROUGE, VERT, BLEU])
        return Circle(x, y, rayon, couleur)

    def update(self, joueur_x, joueur_y):
        self.x += joueur_x
        self.y += joueur_y

    def draw(self, fenetre):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.rayon)
