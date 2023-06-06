import pygame
import sys
import random
from player import Player
from circle import Circle
from enemy import Enemy

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Pygame")

# Création du joueur
x_joueur = largeur // 2
y_joueur = hauteur // 2
rayon_joueur = 20
joueur = Player(x_joueur, y_joueur, rayon_joueur)

# Création des ronds colorés
ronds = []
nbrRonds = random.randint(10, 20)
for _ in range(nbrRonds):
    rond = Circle.create_random_circle(largeur, hauteur)
    ronds.append(rond)

# Création des ennemis
ennemis = []
nbrEnnemis = random.randint(5, 10)
for _ in range(nbrEnnemis):
    ennemi = Enemy.create_random_enemy(largeur, hauteur)
    ennemis.append(ennemi)

# Boucle principale du jeu
vitesse = 0.2
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Détermination de la direction du déplacement
            if event.key == pygame.K_RIGHT:
                joueur.update(-vitesse, 0)
            elif event.key == pygame.K_LEFT:
                joueur.update(vitesse, 0)
            elif event.key == pygame.K_DOWN:
                joueur.update(0, -vitesse)
            elif event.key == pygame.K_UP:
                joueur.update(0, vitesse)
        elif event.type == pygame.KEYUP:
            # Arrêt du déplacement lorsque la touche est relâchée
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                joueur.update(0, 0)
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                joueur.update(0, 0)

    # Mise à jour des positions des objets
    for rond in ronds:
        rond.update(joueur.x, joueur.y)

    for ennemi in ennemis:
        ennemi.update(joueur.x, joueur.y)

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin des ronds
    for rond in ronds:
        rond.draw(fenetre)

    # Dessin des ennemis
    for ennemi in ennemis:
        ennemi.draw(fenetre)

    # Dessin du joueur
    joueur.draw(fenetre)

    # Rafraîchissement de l'écran
    pygame.display.flip()
