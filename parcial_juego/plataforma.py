import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height,  type=1):

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Tiles/{0}.png",1,25,flip=False,w=width,h=height)

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

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Tiles/{0}.png",1,25,flip=False,w=width,h=height)

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
        self.active = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,flip_y=True,w=width,h=height)

        self.image_inactive = self.inactive[type]
        self.image_active = self.active[type]
        self.rect_inactive = self.image_inactive.get_rect()
        self.rect_inactive.x = x
        self.rect_inactive.y = y
        self.rect_active = self.image_active.get_rect()
        self.rect_active.x = x
        self.rect_active.y = y
        self.collition_rect_inactive = pygame.Rect(x+self.rect_inactive.width/3,y,self.rect_inactive.width/3,self.rect_inactive.height)
        self.collition_rect_active = pygame.Rect(x+self.rect_active.width/3,y,self.rect_active.width/3,self.rect_active.height)

        self.is_active = False

    def activate_lever(self):

        self.is_active = True
        self.image = self.image_active


    def draw(self,screen):
        image = self.image_inactive
        rect = self.rect_inactive
        collition_rect = self.collition_rect_inactive
        if self.is_active:
            image = self.image_active
            rect = self.rect_active
            collition_rect = self.collition_rect_active
            
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=collition_rect)
        screen.blit(image,rect)

class Door:

    def __init__(self, x, y,width, height,type):

        self.closed = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,w=width,h=height)
        # self.open = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/tileset/forest/Objects/{0}.png",1,20,w=width,h=height)

        self.image = self.closed[type]
        # self.image_open = self.open[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.rect_open = self.image_open.get_rect()
        # self.rect_open.x = x
        # self.rect_open.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        # self.collition_rect_open = pygame.Rect(x+self.rect_open.width/3,y,self.rect_open.width/3,self.rect_open.height)



        self.is_open = False

    def open_door(self):
        self.is_open = True
        self.image = self.image_open

    def draw(self,screen):
        image = self.image
        rect = self.rect
        collition_rect = self.collition_rect
        # if self.is_open:
        #     image = self.image_open
        #     rect = self.rect_open
        #     collition_rect = self.collition_rect_open
            
        if(DEBUG):
            if not self.is_open:
                pygame.draw.rect(screen,color=(255,0 ,0),rect=collition_rect)
        screen.blit(image,rect)
