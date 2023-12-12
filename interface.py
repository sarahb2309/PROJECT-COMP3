import pygame
import sys
from pygame.locals import MOUSEBUTTONDOWN
import os
from game import car_racing
from pygame.locals import QUIT

# Creating a function that creates the GUI
def interface():
    pygame.init()
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    greycr = (166, 166, 166)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    width = screen.get_width()

    # Using a default font for rendering text
    default_font = pygame.font.SysFont(None, 40)

    game1_text = default_font.render('PLAYYY', True, blue)
    game2_text = default_font.render('MULTIPLAYER', True, blue)
    game3_text = default_font.render('GAME3', True, blue)
    credits_text = default_font.render('CREDITS', True, blue)
    quit_text = default_font.render('QUIT', True, blue)

    # Set initial time for the splash screen
    initial_time = pygame.time.get_ticks()
    loopCond = False  # Initialize loopCond

    # Load the splash screen image
    splash_image_path = "assets/interface/interface8.png"
    splash_image = pygame.image.load(splash_image_path)
    splash_rect = splash_image.get_rect(center=(width // 2, screen.get_height() // 2))

    # Load the background image for the main interface
    background_image_path = "assets/interface/interfacemainn.png"
    original_background_image = pygame.image.load(background_image_path)
    original_background_rect = original_background_image.get_rect()

    scaled_width = 600
    scaled_height = 600

    # Scale the background image to the desired size
    background_image = pygame.transform.scale(original_background_image, (scaled_width, scaled_height))
    background_rect = background_image.get_rect()

    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    fading = True
                if 450 <= mouse[0] <= 590 and 480 <= mouse[1] <= 540:
                    credits_()
                if 90 <= mouse[0] <= 230 and 240 <= mouse[1] <= 300:
                    car_racing(False)
                if 450 <= mouse[0] <= 590 and 240 <= mouse[1] <= 300:
                    car_racing(True)

        # Clear the screen
        screen.fill(greycr)

         # Display the background image for the splash screen
        screen.blit(splash_image, splash_rect.topleft)

        # Calculate elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - initial_time) // 250  # Convert to seconds

        # Show splash screen for 10 seconds
        if elapsed_time < 10:
            # Display the splash screen
            screen.blit(splash_image, splash_rect.topleft)
            pygame.display.update()
        else:
            # Display the main interface
            background_rect.center = (width // 2, screen.get_height() // 2)
            screen.blit(background_image, background_rect.topleft)

            # Fill edges around the background image with greycr
            pygame.draw.rect(screen, greycr, (0, 0, width, background_rect.top))
            pygame.draw.rect(screen, greycr, (0, background_rect.bottom, width, screen.get_height()))
            pygame.draw.rect(screen, greycr, (0, 0, background_rect.left, screen.get_height()))
            pygame.draw.rect(screen, greycr, (background_rect.right, 0, width, screen.get_height()))

            # game 1 text
            mouse = pygame.mouse.get_pos()
            game1_width = game1_text.get_width()
            game1_rect = pygame.Rect(width // 2 - game1_width // 2, 240, game1_width, 60)
            game1_surface = pygame.Surface((game1_width, 60), pygame.SRCALPHA)
            game1_surface.fill((0, 255, 0, 0))
            if game1_rect.collidepoint(mouse):
                game1_surface.fill((0, 255, 0, 128))
                if pygame.mouse.get_pressed()[0]:  # Check for left mouse button click
                    car_racing(False)  # You can replace this function call with the desired action
            #screen.blit(game1_surface, (width // 2 - game1_width // 2, 227))
            #screen.blit(game1_text, (width // 2 - game1_width // 2, 227))
            screen.blit(game1_surface, game1_rect.topleft)
            screen.blit(game1_text, game1_rect.topleft) 
            
             # game 2 text (MULTIPLAYER)
            game2_width = game2_text.get_width()
            game2_rect = pygame.Rect(width // 2 - game2_width // 2, 240 + 70, game2_width, 70)
            game2_surface = pygame.Surface((game2_width, 80), pygame.SRCALPHA)
            game2_surface.fill((0, 255, 0, 0))
            if game2_rect.collidepoint(mouse):
                game2_surface.fill((0, 255, 0, 128))
                if pygame.mouse.get_pressed()[0]:
                    car_racing(True)  # You can replace this function call with the desired action
            screen.blit(game2_surface, (width // 2 - game2_width // 2, 250 + 2 * 64))
            screen.blit(game2_text, (width // 2 - game2_width // 2, 250 + 2 * 64))

        # game 3 text (GAME3)
            game3_width = game3_text.get_width()
            game3_rect = pygame.Rect(width // 2 - game3_width // 2, 250 + 2 * 80, game3_width, 60)
            game3_surface = pygame.Surface((game3_width, 60), pygame.SRCALPHA)
            game3_surface.fill((0, 255, 0, 0))
            if game3_rect.collidepoint(mouse):
                game3_surface.fill((0, 255, 0, 128))
                if pygame.mouse.get_pressed()[0]:
                    game3()  # Call the game3 function
            screen.blit(game3_surface, (width // 2 - game3_width // 2, 250 + 280))
            screen.blit(game3_text, (width // 2 - game3_width // 2, 250 + 280))

        # MENU -- WORKS
            credits_rect = pygame.Rect(width // 2 - credits_text.get_width() // 2, 250 + 100, credits_text.get_width(), 60)
            if credits_rect.collidepoint(mouse):
                pygame.draw.rect(screen, yellow, credits_rect)
            #if pygame.mouse.get_pressed()[0]:
                #splash_page()  # Display splash page when MENU is clicked
            else:
                pygame.draw.rect(screen, (100, 100, 100), credits_rect)
            screen.blit(credits_text, (width // 2 - credits_text.get_width() // 2, 250 + 60))

            # quit text -- WORKS
            quit_width = quit_text.get_width()
            quit_rect = pygame.Rect(width // 2 - quit_width // 2, 250 + 5 * 80, quit_width, 60)  # Updated Y position
            quit_surface = pygame.Surface((quit_width, 60), pygame.SRCALPHA)
            quit_surface.fill((255, 0, 0, 0))
            if quit_rect.collidepoint(mouse):
                quit_surface.fill((255, 0, 0, 128))
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()  # You can replace this function call with the desired action
            screen.blit(quit_surface, (width // 2 - quit_width // 2, 250 + 2 * 100))
            screen.blit(quit_text, (width // 2 - quit_width // 2, 250 + 2 * 100))
            
        pygame.display.update()

        if loopCond:
            pygame.display.update()
            loopCond = False

# Function to display credits
def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_dark = (100, 100, 100)
    corbelfont = pygame.font.SysFont('Corbel', 30)  # Adjusted font size
    back_text = corbelfont.render('   back', True, blue)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    line1_text = comicsansfont.render('Davide Farinati, dfarinati@novaims.unl.pt', True, yellow)
    line2_text = comicsansfont.render('Joao Fonseca, jfonseca@novaims.unl.pt', True, yellow)
    line3_text = comicsansfont.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, yellow)

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
                    interface()

        screen.fill((0, 0, 0))
        screen.blit(line1_text, (10, 250))  # Adjusted position
        screen.blit(line2_text, (10, 250 + 30))  # Adjusted position
        screen.blit(line3_text, (10, 250 + 2 * 30))  # Adjusted position
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, red, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(back_text, (470, 250 + 3 * 30))  # Adjusted position

        pygame.display.update()

if __name__ == "__main__":
    interface()