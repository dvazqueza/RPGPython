import pygame
import sys
import random
from characters.Character import Character
from characters.NPC import NPC


pygame.init()
clock = pygame.time.Clock()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('characters/assets/background.png')
pygame.mouse.set_visible(False)


character = Character(picture_path="characters/assets/Character.png")
character_group = pygame.sprite.Group()
character_group.add(character)

npc_group = pygame.sprite.Group()
for target in range(10):
    new_npc = NPC(pos_x=random.randrange(0,screen_width), pos_y=random.randrange(0,screen_height), picture_path="characters/assets/npc.png")
    npc_group.add(new_npc)

while True:

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            character.shoot()

    pygame.display.flip()
    screen.blit(background, (0,0))
    npc_group.draw(screen)
    character_group.draw(screen)
    character_group.update()
    clock.tick(60)