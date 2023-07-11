import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100, interval_time_shot=100) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/IDLE/IDLE_00{0}.png",0,4,flip=False,scale=p_scale,repeat_frame=2)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/IDLE/IDLE_00{0}.png",0,4,flip=True,scale=p_scale,repeat_frame=2)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/JUMP/JUMP_00{0}.png",0,4,flip=False,scale=p_scale,repeat_frame=2)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/JUMP/JUMP_00{0}.png",0,4,flip=True,scale=p_scale,repeat_frame=2)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/WALK/WALK_00{0}.png",0,4,flip=False,scale=p_scale,repeat_frame=2)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/WALK/WALK_00{0}.png",0,4,flip=True,scale=p_scale,repeat_frame=2)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/RUN/RUN_00{0}.png",0,4,flip=False,scale=p_scale,repeat_frame=3)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/RUN/RUN_00{0}.png",0,4,flip=True,scale=p_scale,repeat_frame=3)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/ATTACK/ATTACK_00{0}.png",0,4,flip=False,scale=p_scale)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/ATTACK/ATTACK_00{0}.png",0,4,flip=True,scale=p_scale)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/DIE/DIE_00{0}.png",0,4,flip=False,scale=p_scale)
        self.die_l = Auxiliar.getSurfaceFromSeparateFiles("parcial_juego/images/caracters/players/warrior_woman/DIE/DIE_00{0}.png",0,4,flip=True,scale=p_scale)

        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/2,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.head_collition_rect = pygame.Rect(self.collition_rect)
        self.head_collition_rect.height = HEAD_COLLIDE_H
        self.head_collition_rect.y = y - self.head_collition_rect.height + HEAD_COLLIDE_H
        
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_dying = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.time_last_shot = 0
        self.interval_time_shot = interval_time_shot
        self.first_shot = True
        self.bullet_list = []

    def move(self,direction,speed,animation):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = speed
                    self.animation = animation
                else:
                    self.move_x = -speed
                    self.animation = animation

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False and self.move_x == 0):
            if (self.first_shot or (self.tiempo_transcurrido - self.time_last_shot) > self.interval_time_shot):
                if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                    self.frame = 0
                    self.is_shoot = True
                    if(self.direction == DIRECTION_R):
                        self.animation = self.shoot_r
                        sentido = 1
                    else:
                        self.animation = self.shoot_l       
                        sentido = -1

                    self.bullet_list.append(Bullet(self,self.rect.centerx,self.rect.centery,sentido * self.rect.centerx,self.rect.centery,sentido,20,path="parcial_juego/images/tileset/forest/Objects/15.png",frame_rate_ms=100,move_rate_ms=20,width=80,height=10))
                    self.first_shot = False
                    self.time_last_shot = self.tiempo_transcurrido
            else:
                if(self.direction == DIRECTION_R):
                    self.animation = self.stay_r
                else:
                    self.animation = self.stay_l       

    def damage(self):
        self.lives -= 1
        if(self.lives == 0):
            self.die()
            
    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.y_start_jump = self.rect.y

                if(self.direction == DIRECTION_R):
                    self.animation = self.jump_r
                    
                else:
                    self.animation = self.jump_l

                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.frame = 0
                self.is_jump = True
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.head_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.head_collition_rect.y += delta_y


    def do_movement(self,delta_ms,plataform_list,enemy_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False
        
            self.collide_enemy(enemy_list)
            self.collide_traps(plataform_list)
                    
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

    def collide_enemy(self,enemy_list):
        for enemy in enemy_list:
            if self.collition_rect.colliderect(enemy.collition_rect):
                self.damage()

    def collide_traps(self,platform_list):
        for plataforma in platform_list:
            if plataforma.type == 18 or plataforma.type == 19 or plataforma.type == 20:
                if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect) or self.head_collition_rect.colliderect(plataforma.head_collition_rect):
                    self.damage()
    

    def die(self):
        if(self.direction == DIRECTION_R):
            self.animation = self.die_r
        else:
            self.animation = self.die_l
        self.is_dying = True


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else: 
                self.frame = 0
 
    def update(self,delta_ms,plataform_list,enemy_list):
        self.do_movement(delta_ms,plataform_list,enemy_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(0,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen,color=(0,0,255),rect=self.head_collition_rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        if self.rect.x >= 0 and self.rect.x <= 1750:          
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LCTRL] and not keys[pygame.K_s] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
                self.move(DIRECTION_L,self.speed_walk,self.walk_l)
            elif(keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_LCTRL] and not keys[pygame.K_s] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
                self.move(DIRECTION_R,self.speed_walk,self.walk_r)
       
            if(keys[pygame.K_LCTRL] and keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_s] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
                self.move(DIRECTION_L,self.speed_run,self.run_l)
            elif(keys[pygame.K_LCTRL] and keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]and not keys[pygame.K_s] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
                self.move(DIRECTION_R,self.speed_run,self.run_r)
        else:
            if self.direction == DIRECTION_L:
                self.rect.x = 0
                self.collition_rect.x = 25
                self.ground_collition_rect.x = 25
                self.head_collition_rect.x = 25
            else:
                self.rect.x = 1700
                self.collition_rect.x = 1730
                self.ground_collition_rect.x = 1730
                self.head_collition_rect.x = 1730

        if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
            self.stay()
                
        if self.rect.y >= 0:
            if(keys[pygame.K_SPACE]):
                self.jump(True)
            
        if(keys[pygame.K_s]):
            self.shoot()
            self.move_x = 0
        else:
            self.shoot(False)

    
        # if(keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_DOWN]):
        #     if(self.collition_rect.colliderect(Ladder.rect)):
        #         self.move_y -= 10
        #         self.change_y(self.move_y) 
        # elif(keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_UP]):
        #     if(self.collition_rect.colliderect(Ladder)):
        #         self.move_y += 10
        #         self.change_y(self.move_y)