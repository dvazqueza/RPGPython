import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, width= None, height= None, pos_x= None, pos_y = None, color = (255,255,255), picture_path= None):
        super().__init__()

        if width != None and height != None:
            self.image = pygame.Surface([width, height])   # creating a Surface for the animated image
            if color != None:
                self.image.fill(color)
        else:
            self.image = pygame.image.load(picture_path)

        self.rect = self.image.get_rect()
        if pos_x != None and pos_y != None:
            self.rect.center = [pos_x, pos_y]

        self.gunshot = pygame.mixer.Sound("characters/assets/shoot.wav")

    def setNPCGroup(self,npc_group):
        self.npc_group = npc_group

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(self, self.npc_group)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
