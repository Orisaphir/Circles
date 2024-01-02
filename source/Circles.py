import pygame

def play_solo():
    import pygame
    import random

    # Dimensions de la chambre
    largeur_chambre = 800
    hauteur_chambre = 600

    # Dimensions du joueur
    largeur_joueur = 50
    hauteur_joueur = 50

    # Dimensions de la hitbox de la mauvaise cible
    radius_mauvaise_cible = 25
    
    # Distance minimale entre le joueur et les cibles
    distance_minimale = 100

    # Initialisation de Pygame
    pygame.init()

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largeur_chambre, hauteur_chambre))
    pygame.display.set_caption("Circles (solo)")

    # Couleurs
    couleur_fond = (255, 255, 255) # Blanc
    couleur_joueur = (255, 255, 0)  # Jaune
    couleur_cible_bonne = (0, 255, 0) # Vert
    couleur_cible_mauvaise = (255, 0, 0) # Rouge
    couleur_texte = (0, 0, 0) # Noir
    couleur_menu_pause = (200, 200, 200) # Gris

    # Police de caractères
    police = pygame.font.Font(None, 30)

    # Variables de score
    score = 0
    meilleur_score = 0
    mauvaise_cible_touchee = 0

    # Bouton pause
    pause = False
    couleur_bouton_pause = (0, 0, 255) # Bleu
    texte_bouton_pause = police.render("Pause", True, couleur_texte)
    rect_bouton_pause = pygame.Rect(10, hauteur_chambre - texte_bouton_pause.get_height() - 10, texte_bouton_pause.get_width(), texte_bouton_pause.get_height())

    # Pause menu
    menu_pause = False
    button_font = pygame.font.Font(None, 24)
    texte_reprendre = button_font.render("Reprendre", True, couleur_texte, couleur_menu_pause)
    texte_menu_principal = button_font.render("Revenir au menu principal", True, couleur_texte, couleur_menu_pause)
    rect_reprendre = pygame.Rect(largeur_chambre // 2 - texte_reprendre.get_width() // 2, hauteur_chambre // 2 - texte_reprendre.get_height() - 60, texte_reprendre.get_width(), texte_reprendre.get_height())
    rect_menu_principal = pygame.Rect(largeur_chambre // 2 - texte_menu_principal.get_width() // 2, hauteur_chambre // 2 + 10, texte_menu_principal.get_width(), texte_menu_principal.get_height())

    # Game over
    game_over = False
    texte_game_over = police.render("Game Over", True, couleur_texte)
    texte_recommencer = button_font.render("Recommencer", True, couleur_texte, couleur_menu_pause)
    rect_recommencer = pygame.Rect(largeur_chambre // 2 - texte_recommencer.get_width() // 2, hauteur_chambre // 2 - texte_recommencer.get_height() - 60, texte_recommencer.get_width(), texte_recommencer.get_height())
    rect_menu_principal_game_over = pygame.Rect(largeur_chambre // 2 - texte_menu_principal.get_width() // 2, hauteur_chambre // 2 + 10, texte_menu_principal.get_width(), texte_menu_principal.get_height())

    # Vitesse de déplacement du joueur
    vitesse_x = 0.5
    vitesse_y = 0.5
    
    # Temps avant que le joueur soit attiré par la mauvaise cible (en secondes)
    temps_attirer_mauvaise_cible = 3
    temps_inactif = 0

    # Boucle principale pour les sessions
    running = True
    while running:
        
        # Position initiale du joueur
        x_joueur = largeur_chambre // 2 - largeur_joueur // 2
        y_joueur = hauteur_chambre // 2 - hauteur_joueur // 2
        
        # Position de la cible
        x_cible_bonne = random.randint(0, largeur_chambre - largeur_joueur)
        y_cible_bonne = random.randint(0, hauteur_chambre - hauteur_joueur)
        
        # Vérification de la distance entre le joueur et la bonne cible
        while abs(x_cible_bonne - x_joueur) <= distance_minimale and abs(y_cible_bonne - y_joueur) <= distance_minimale:
            x_cible_bonne = random.randint(0, largeur_chambre - largeur_joueur)
            y_cible_bonne = random.randint(0, hauteur_chambre - hauteur_joueur)
        
        x_cible_mauvaise = random.randint(0, largeur_chambre - largeur_joueur)
        y_cible_mauvaise = random.randint(0, hauteur_chambre - hauteur_joueur)
        
        # Vérification de la distance entre le joueur et la mauvaise cible
        while abs(x_cible_mauvaise - x_joueur) <= distance_minimale and abs(y_cible_mauvaise - y_joueur) <= distance_minimale:
            x_cible_mauvaise = random.randint(0, largeur_chambre - largeur_joueur)
            y_cible_mauvaise = random.randint(0, hauteur_chambre - hauteur_joueur)

        # Boucle principale du jeu
        session_running = True
        game_over = False
        while session_running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    session_running = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if menu_pause:
                        menu_pause = False
                        pause = False
                    else:
                        menu_pause = True
                        pause = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_bouton_pause.collidepoint(event.pos):
                        pause = not pause
                    if rect_reprendre.collidepoint(event.pos):
                        menu_pause = False
                        pause = False
                    if rect_menu_principal.collidepoint(event.pos):
                        display_welcome_screen()
                    # couleur du bouton pause quand pause = True
                    if pause:
                        couleur_bouton_pause = (255, 0, 0) # Rouge
                    else:
                        couleur_bouton_pause = (0, 0, 255) # Bleu
            
            
            # Calcul du déplacement du joueur
            if not pause and not game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                    if x_joueur > 0:
                        x_joueur -= vitesse_x
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    if x_joueur < largeur_chambre - largeur_joueur:
                        x_joueur += vitesse_x
                if keys[pygame.K_UP] or keys[pygame.K_z]:
                    if y_joueur > 0:
                        y_joueur -= vitesse_y
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    if y_joueur < hauteur_chambre - hauteur_joueur:
                        y_joueur += vitesse_y
                if not any(keys):
                    temps_inactif += 1
                    if temps_inactif >= temps_attirer_mauvaise_cible * 60:  # Convertir le temps en frames
                        if x_joueur < x_cible_mauvaise:
                            x_joueur += vitesse_x
                        elif x_joueur > x_cible_mauvaise:
                            x_joueur -= vitesse_x
                        if y_joueur < y_cible_mauvaise:
                            y_joueur += vitesse_y
                        elif y_joueur > y_cible_mauvaise:
                            y_joueur -= vitesse_y
            else:
                temps_inactif = 0

            # Vérification si le joueur a atteint la cible
            if abs(x_joueur - x_cible_bonne) <= radius_mauvaise_cible and abs(y_joueur - y_cible_bonne) <= radius_mauvaise_cible:
                score += 1
                if score > meilleur_score:
                    meilleur_score = score
                session_running = False
                break
            elif abs(x_joueur - x_cible_mauvaise) <= radius_mauvaise_cible and abs(y_joueur - y_cible_mauvaise) <= radius_mauvaise_cible:
                mauvaise_cible_touchee += 1
                score = 0  # Reset du score à 0
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = False
                            session_running = False
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if rect_recommencer.collidepoint(event.pos):
                                game_over = False
                                session_running = False
                                score = 0  # Reset du score à 0
                                break
                            if rect_menu_principal_game_over.collidepoint(event.pos):
                                display_welcome_screen()
                    pygame.draw.rect(fenetre, couleur_menu_pause, (largeur_chambre // 2 - 200, hauteur_chambre // 2 - 100, 400, 200))
                    fenetre.blit(texte_game_over, (largeur_chambre // 2 - texte_game_over.get_width() // 2, hauteur_chambre // 2 - 40))
                    pygame.draw.rect(fenetre, couleur_texte, rect_recommencer)
                    pygame.draw.rect(fenetre, couleur_texte, rect_menu_principal_game_over)
                    pygame.draw.rect(fenetre, (0, 0, 0), (largeur_chambre // 2 - 200, hauteur_chambre // 2 - 100, 400, 200), 2)  # Bordure noire
                    fenetre.blit(texte_recommencer, (rect_recommencer.x, rect_recommencer.y))
                    fenetre.blit(texte_menu_principal, (rect_menu_principal_game_over.x, rect_menu_principal_game_over.y))
                    pygame.display.flip()

            # Dessin de la chambre, du joueur et des cibles
            fenetre.fill(couleur_fond)  # Couleur de fond de la chambre

            pygame.draw.ellipse(fenetre, couleur_joueur, (x_joueur, y_joueur, largeur_joueur, hauteur_joueur))  # Dessin du joueur
            pygame.draw.ellipse(fenetre, couleur_cible_bonne, (x_cible_bonne, y_cible_bonne, largeur_joueur, hauteur_joueur))  # Dessin de la bonne cible
            pygame.draw.ellipse(fenetre, couleur_cible_mauvaise, (x_cible_mauvaise, y_cible_mauvaise, largeur_joueur, hauteur_joueur))  # Dessin de la mauvaise cible

            # Affichage du score
            texte_score = police.render("Score: " + str(score), True, couleur_texte)
            fenetre.blit(texte_score, (10, 10))

            # Affichage du compteur de mauvaise cible
            texte_mauvaise_cible = police.render("Mauvaises cibles touchées: " + str(mauvaise_cible_touchee), True, couleur_texte)
            fenetre.blit(texte_mauvaise_cible, (10, 50))

            # Affichage du meilleur score
            texte_meilleur_score = police.render("Meilleur score: " + str(meilleur_score), True, couleur_texte)
            fenetre.blit(texte_meilleur_score, (largeur_chambre - texte_meilleur_score.get_width() - 10, 10))

            # Affichage du bouton pause
            pygame.draw.rect(fenetre, couleur_bouton_pause, rect_bouton_pause)
            fenetre.blit(texte_bouton_pause, (rect_bouton_pause.x, rect_bouton_pause.y))
            
            # Affichage du menu pause
            if menu_pause:
                pygame.draw.rect(fenetre, couleur_menu_pause, (largeur_chambre // 2 - 200, hauteur_chambre // 2 - 100, 400, 200))
                pygame.draw.rect(fenetre, couleur_texte, rect_reprendre)
                pygame.draw.rect(fenetre, couleur_texte, rect_menu_principal)
                pygame.draw.rect(fenetre, (0, 0, 0), (largeur_chambre // 2 - 200, hauteur_chambre // 2 - 100, 400, 200), 2)  # Bordure noire
                fenetre.blit(texte_reprendre, (rect_reprendre.x, rect_reprendre.y))
                fenetre.blit(texte_menu_principal, (rect_menu_principal.x, rect_menu_principal.y))

            # Rafraîchissement de l'écran
            pygame.display.flip()
            
    # Fermeture de Pygame
    pygame.quit()

def display_welcome_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Circles")
    
    font = pygame.font.Font(None, 36)
    title_text = font.render("Welcome to Circles!", True, (255, 255, 255))
    title_text_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))
    
    button_font = pygame.font.Font(None, 24)
    play_lums_button_text = button_font.render("Jouer (Lums)", True, (255, 255, 255))
    play_lums_button_rect = play_lums_button_text.get_rect(center=(screen.get_width() // 2, 250))
    
    play_solo_button_text = button_font.render("Jouer (Solo)", True, (255, 255, 255))
    play_solo_button_rect = play_solo_button_text.get_rect(center=(screen.get_width() // 2, 300))
    
    quit_button_text = button_font.render("Quitter le jeu", True, (255, 255, 255))
    quit_button_rect = quit_button_text.get_rect(center=(screen.get_width() // 2, 350))
    
    running = True
    try_Lums = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):
                    running = False
                if play_lums_button_rect.collidepoint(event.pos):
                    try_Lums = True
                if play_solo_button_rect.collidepoint(event.pos):
                    play_solo()
        
        screen.fill((0, 0, 0))
        if try_Lums:
            screen.blit(title_text, title_text_rect)
            screen.blit(play_lums_button_text, play_lums_button_rect)
            screen.blit(play_solo_button_text, play_solo_button_rect)
            screen.blit(quit_button_text, quit_button_rect)
            not_available_text = button_font.render("Ce mode de jeu n'est pas encore disponible", True, (255, 0, 0), (0, 0, 0))
            not_available_text_rect = not_available_text.get_rect(center=(screen.get_width() // 2, 550))
            screen.blit(not_available_text, not_available_text_rect)
            pygame.display.flip()
        else:
            screen.blit(title_text, title_text_rect)
            screen.blit(play_lums_button_text, play_lums_button_rect)
            screen.blit(play_solo_button_text, play_solo_button_rect)
            screen.blit(quit_button_text, quit_button_rect)
            pygame.display.flip()
    
    pygame.quit()
    
display_welcome_screen()