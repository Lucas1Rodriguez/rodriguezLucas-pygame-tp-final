from player import *
from constantes import *
from auxiliar import Auxiliar
import math

class Bullet():
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,sentido,speed,path,frame_rate_ms,move_rate_ms,width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(y_end - y_init, x_end - x_init) #Obtengo el angulo en radianes
        print('El angulo en grados es:', int(angle*180/math.pi))

        self.move_x = math.cos(angle)*speed
        self.move_y = math.sin(angle)*speed
        
        self.is_active = True 

        if (sentido == -1):
            self.image = pygame.transform.flip(self.image,True,False).convert_alpha()
   
    def change_x(self,delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player,door,boss_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list,enemy_list,player,door,boss_list)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            pass
    
    def check_impact(self,plataform_list,enemy_list,player,door,boss_list):
        if(self.is_active and self.owner != player and self.rect.colliderect(player.rect)):
            print("IMPACTO PLAYER")
            player.damage()
            self.is_active = False
        for aux_enemy in enemy_list:
                if(self.is_active and self.owner != aux_enemy and self.rect.colliderect(aux_enemy.rect)):
                    print("IMPACTO ENEMY")
                    if(type(self.owner) == type(player)):
                        aux_enemy.receive_shoot(player)
                    self.is_active = False
        if boss_list is not None:
            for boss in boss_list:
                if(self.is_active and self.owner != boss and self.rect.colliderect(boss.rect)):
                    print("IMPACTO BOSS")
                    boss.receive_shoot(player)
                    self.is_active = False
        for aux_platform in plataform_list:
            if(self.is_active and self.rect.colliderect(aux_platform.rect)):
                print("IMPACTO PLATFORM")
                self.is_active = False
        if door is not None:
            if(self.is_active and self.rect.colliderect(door.rect)):
                print("IMPACTO PUERTA")
                self.is_active = False


    def update(self,delta_ms,plataform_list,enemy_list,player,door=None,boss_list=None):
        self.do_movement(delta_ms,plataform_list,enemy_list,player,door,boss_list)
        
        self.do_animation(delta_ms) 

    def draw(self,screen):
        if(self.is_active):
            if(DEBUG):
                pygame.draw.rect(screen,C_GREEN,rect=self.rect)
            screen.blit(self.image,self.rect)
