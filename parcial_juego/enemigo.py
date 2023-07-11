from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    
    def __init__(self,x,y,speed_walk,gravity,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/WALK/WALK_00{0}.png",0,6,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/WALK/WALK_00{0}.png",0,6,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/IDLE/IDLE_00{0}.png",0,6,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/IDLE/IDLE_00{0}.png",0,6,flip=True,scale=p_scale)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/ATTACK/ATTACK_00{0}.png",0,6,scale=p_scale)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/ATTACK/ATTACK_00{0}.png",0,6,flip=True,scale=p_scale)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/DIE/DIE_00{0}.png",0,6,scale=p_scale)
        self.die_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/knight_spear/DIE/DIE_00{0}.png",0,6,flip=True,scale=p_scale)


        self.contador = 0
        self.frame = 0
        self.lives = 1
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.gravity = gravity
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/8,y,self.rect.width/2,self.rect.height)

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_dying = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.direction = DIRECTION_L
                    self.contador += 1
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.direction = DIRECTION_R
                    self.contador += 1
                else:
                    self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          
    
    def receive_shoot(self,player):
        print(player)
        self.lives -= 1
        if(self.lives == 0):
            self.die(player)

    def die(self,player):
        if(self.direction == DIRECTION_R):
            self.animation = self.die_r
        else:
            self.animation = self.die_l
        self.move_x = 0
        self.move_y = 0
        self.contador = 0
        self.is_dying = True
        player.score += 200
        print(player.score)
   
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,plataform_list,enemy_list):
        if self.is_dying:
            self.do_animation(delta_ms)
            if self.frame == len(self.animation) - 1:
                enemy_list.remove(self)
        else:
            self.do_movement(delta_ms,plataform_list)
            self.do_animation(delta_ms) 

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


class Boss():
    
    def __init__(self,x,y,frame_rate_ms,p_scale=1) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/summoner_skeleton_boss/IDLE/IDLE_00{0}.png",0,15,scale=p_scale)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/summoner_skeleton_boss/ATTACK/ATTACK_00{0}.png",0,8,scale=p_scale)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/summoner_skeleton_boss/DIE/DIE_00{0}.png",0,0,scale=p_scale,repeat_frame=2)
        self.summon_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/enemies/summoner_skeleton_boss/SUMMON/SUMMON_00{0}.png",0,10,scale=p_scale)


        self.frame = 0
        self.lives = 1
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/8,y,self.rect.width/2,self.rect.height)

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
    
    def receive_shoot(self,player):
        print(player)
        self.lives -= 1
        if(self.lives == 0):
            self.die(player)

    def die(self,player):
        if(self.direction == DIRECTION_R):
            self.animation = self.die_r
        player.score += 1000
        print(player.score)


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
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


