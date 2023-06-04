import pygame
import sys
import random
import time

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Dimensions de la fenêtre
largeur = 1920
hauteur = 1080

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Pygame")

# Position initiale du cercle joueur
x_joueur = largeur // 2
y_joueur = hauteur // 2
rayon_joueur = 20

# Variables de déplacement du joueur
deplacement_x = 0
deplacement_y = 0

# Création des ronds colorés
ronds = []
nbrRonds=random.randint(10,20)
for _ in range(nbrRonds):
    rayon = random.randint(10, 30)
    x = random.randint(rayon, largeur - rayon)
    y = random.randint(rayon, hauteur - rayon)
    couleur = random.choice([ROUGE, VERT, BLEU])
    rond = {'x': x, 'y': y, 'rayon': rayon, 'couleur': couleur}
    ronds.append(rond)

# Compteur
score = 0


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

    # Mise à jour de la position du joueur
    x_joueur += deplacement_x
    y_joueur += deplacement_y

    # Vérification des collisions avec les ronds
    for rond in ronds:
        distance = ((x_joueur - rond['x']) ** 2 + (y_joueur - rond['y']) ** 2) ** 0.5
        if distance < rayon_joueur + rond['rayon']:
            ronds.remove(rond)
            score += 1
            vitesse += 0.1

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin des ronds
    for rond in ronds:
        pygame.draw.circle(fenetre, rond['couleur'], (rond['x'], rond['y']), rond['rayon'])

    # Dessin du joueur
    pygame.draw.circle(fenetre, NOIR, (x_joueur, y_joueur), rayon_joueur)

    # Affichage du score
    font = pygame.font.Font(None, 36)
    texte = font.render("Score : {}".format(score), True, NOIR)
    fenetre.blit(texte, (10, 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

   