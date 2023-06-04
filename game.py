import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Pygame")

# Position initiale du cercle
x = largeur // 2
y = hauteur // 2

# Variables de déplacement
deplacement_x = 0
deplacement_y = 0

# Boucle principale du jeu

vitesse=0.2
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Détermination de la direction du déplacement
            if event.key == pygame.K_LEFT:
                deplacement_x = -vitesse
            elif event.key == pygame.K_RIGHT:
                deplacement_x = vitesse
            elif event.key == pygame.K_UP:
                deplacement_y = -vitesse
            elif event.key == pygame.K_DOWN:
                deplacement_y = vitesse
        elif event.type == pygame.KEYUP:
            # Arrêt du déplacement lorsque la touche est relâchée
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                deplacement_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                deplacement_y = 0

    # Mise à jour de la position du cercle
    x += deplacement_x
    y += deplacement_y

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin du cercle
    pygame.draw.circle(fenetre, NOIR, (x, y), 20)

    # Rafraîchissement de l'écran
    pygame.display.flip()