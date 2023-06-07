import pygame

# Classe représentant le joueur
class Joueur:
    def __init__(self, pos_x, pos_y, vitesse):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vitesse = vitesse
        self.point_de_vie = 100
        self.degats = 5
        self.image = pygame.image.load("Image\personnage.png")  # Remplacez "personnage.png" par le chemin de votre image
        self.image = pygame.transform.scale(self.image, (50, 50))

    def deplacer(self, dx, dy):
        self.pos_x += dx * self.vitesse
        self.pos_y += dy * self.vitesse

    def afficher(self, fenetre):
        fenetre.blit(self.image, (self.pos_x, self.pos_y))
