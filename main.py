import pygame
from player import Joueur

# Dimensions de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

# Couleurs
BLANC = (255, 255, 255)

# Initialisation de Pygame
pygame.init()

# Fonction principale du joueur
def joueur():
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mon jeu de survie 2D")

    joueur = Joueur(400, 300, 5)

    running = True
    running = True
    while running:
        fenetre.fill(BLANC)  # Couleur de fond blanche

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    joueur.deplacer(0, -1)  # Déplacement vers le haut
                elif event.key == pygame.K_DOWN:
                    joueur.deplacer(0, 1)  # Déplacement vers le bas
                elif event.key == pygame.K_LEFT:
                    joueur.deplacer(-1, 0)  # Déplacement vers la gauche
                elif event.key == pygame.K_RIGHT:
                    joueur.deplacer(1, 0)  # Déplacement vers la droite

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    joueur.direction_y = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    joueur.direction_x = 0

        joueur.deplacer()
        joueur.afficher(fenetre)

    pygame.display.flip()

    pygame.quit()

# Exécuter la fonction principale du joueur si le fichier est exécuté directement
if __name__ == "__main__":
    joueur()
