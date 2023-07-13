import pygame
from constantes import *
from auxiliar import Auxiliar

class Botin:
    def __init__(self, x, y,width, height,  type=1):
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,21,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.type = type

    def score(self,player,loot_list):
        if self.collition_rect.colliderect(player.collition_rect):
            if self.type == 15:
                player.score += 100
                print(player.score)
            elif self.type == 20:
                player.score += 150
                player.lives += 1
                print(player.score)
                print(player.lives)
            loot_list.remove(self)
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)

class Botin_Animated:
    def __init__(self, x, y,width, height,frame_rate_ms):
        self.image_animated = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/1UP/{0}.png",0,17,flip=False,w=width,h=height)


        self.frame = 0
        self.animation = self.image_animated
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms

            
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else: 
                self.frame = 0

    def update(self,delta_ms):
        self.do_animation(delta_ms)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)