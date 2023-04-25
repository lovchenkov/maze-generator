import pygame
import sys
from src.constants import *
from src.app import *


pygame.init()
screen = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])

app = App(screen)
app.initialize()
app.update_screen()
app.set_music()

# OPTIONS FOR STATUS ARE: PLAYING, SHOWING_PATH, FINISHED
STATUS = "PLAYING"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if app.maze.is_player_finished():
        STATUS = "FINISHED"
        app.set_ryan_gosling()

    if STATUS != "FINISHED":
        pygame.mixer.music.pause()

    if STATUS == "FINISHED":
        pygame.mixer.music.unpause()
        continue

    if STATUS == "PLAYING":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            app.maze.move_player('S')
        if keys[pygame.K_UP]:
            app.maze.move_player('N')
        if keys[pygame.K_LEFT]:
            app.maze.move_player('W')
        if keys[pygame.K_RIGHT]:
            app.maze.move_player('E')
        if keys[pygame.K_TAB]:
            STATUS = "SHOWING_PATH"

        app.update_screen()

    if STATUS == "SHOWING_PATH":
        app.update_path()
        app.update_fps()
