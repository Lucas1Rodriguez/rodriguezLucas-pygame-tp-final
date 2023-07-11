import pygame
from constantes import *
from auxiliar import Auxiliar

class Botin:
    def __init__(self, x, y,width, height,  type=1):
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,18,flip=False,w=width,h=height)
        self.image_list_animated = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/1UP/{0}.png",0,17,flip=False,w=width,h=height)

        
        self.image = self.image_list[type]
        self.image_animated = self.image_list_animated[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)

    def score(self,player,loot_list):
        if self.collition_rect.colliderect(player.collition_rect):
            player.score += 100
            print(player.score)
            loot_list.remove(self)
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)