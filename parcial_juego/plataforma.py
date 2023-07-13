import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height,  type=1):

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Tiles/{0}.png",1,28,flip=False,w=width,h=height)

        self.image = self.image_list[type]
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.head_collition_rect = pygame.Rect(self.rect)
        self.head_collition_rect.height = HEAD_COLLIDE_H
        self.head_collition_rect.y = y + self.rect.height - HEAD_COLLIDE_H

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(0,255,0),rect=self.head_collition_rect)

class Exit:
    def __init__(self, x, y,width, height, type):

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Tiles/{0}.png",1,28,flip=False,w=width,h=height)

        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3.5,self.rect.height)


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        screen.blit(self.image,self.rect)


class Ladder:

    def __init__(self, x, y,width, height,type):

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,flip=False,w=width,h=height)


        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        screen.blit(self.image,self.rect)


class Lever:
    
    def __init__(self, x, y,width, height,type):

        self.inactive = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,flip_y=True,w=width,h=height)

        self.image = self.inactive[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)

        self.is_active = False
        if self.is_active: 
            self.image = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,flip_y=False,w=width,h=height)

    def activate_lever(self):

        self.is_active = True
        print("Activada")


    def draw(self,screen):
            
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        screen.blit(self.image,self.rect)

class Door:

    def __init__(self, x, y,width, height,type):

        self.closed = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,w=width,h=height)
        self.open = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,w=width,h=height)

        self.type = type
        self.image = self.closed[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)

        self.is_open = False

    def open_door(self):
        self.is_open = True
        self.image = self.open[self.type]

    def draw(self,screen):
        
        if(DEBUG):
            if not self.is_open:
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        screen.blit(self.image,self.rect)
