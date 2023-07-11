import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import *
from plataforma import *
from background import Background
from bullet import Bullet
from botin import Botin

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background,active):
        super().__init__(name,master_surface,x,y,w,h,image_background,active)

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)

        self.pb_lives = ProgressBar(master=self,x=500,y=0,w=240,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Paper/Bars/Bar_Background02.png",image_progress="parcial_juego/images/gui/set_gui_01/Sand/Elements/hearts.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="parcial_juego/images/locations/set_bg_01/forest/1.jpg")

        self.player_1 = Player(x=1650,y=150,speed_walk=8,speed_run=12,gravity=14,jump_power=80,frame_rate_ms=100,move_rate_ms=50,jump_height=180,p_scale=0.15,interval_time_jump=300,interval_time_shot=2000)

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=600,y=650,speed_walk=6,gravity=14,frame_rate_ms=150,move_rate_ms=50,p_scale=0.1))
        self.boss = (Boss(x=500,y=150,frame_rate_ms=150,p_scale=0.1))


        self.plataform_list = []
        self.plataform_list.append(Plataform(x=0,y=300,width=50,height=50,type=21))
        self.plataform_list.append(Plataform(x=50,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=150,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=250,y=300,width=100,height=50,type=22))   
        self.plataform_list.append(Plataform(x=350,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=450,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=550,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=650,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=750,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=950,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1050,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1150,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1250,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1350,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1450,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1550,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1650,y=300,width=100,height=50,type=22))
        self.plataform_list.append(Plataform(x=1750,y=300,width=50,height=50,type=23))
        self.plataform_list.append(Plataform(x=850,y=300,width=100,height=50,type=22))

        self.plataform_list.append(Plataform(x=850,y=GROUND_LEVEL,width=50,height=50,type=19))
        self.plataform_list.append(Plataform(x=900,y=GROUND_LEVEL,width=50,height=50,type=19))
        self.plataform_list.append(Plataform(x=950,y=GROUND_LEVEL,width=50,height=50,type=19))


        self.plataform_list.append(Plataform(x=1000,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=1050,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=1100,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=1000,y=700,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=1050,y=700,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=1000,y=650,width=50,height=50,type=17))

        self.plataform_list.append(Plataform(x=700,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=750,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=800,y=GROUND_LEVEL,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=750,y=700,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=800,y=700,width=50,height=50,type=17))
        self.plataform_list.append(Plataform(x=800,y=650,width=50,height=50,type=17))

        # self.plataform_list.append(Plataform(x=1000,y=250,width=50,height=50,type=17))
        # self.plataform_list.append(Plataform(x=1000,y=200,width=50,height=50,type=17))
        # self.plataform_list.append(Plataform(x=1000,y=150,width=50,height=50,type=17))
        # self.plataform_list.append(Plataform(x=1000,y=100,width=50,height=50,type=17))



        self.bullet_list = []

        self.exit = (Exit(x=-60,y=100,width=280,height=240,type=24))

        self.ladder = Ladder(x=1500,y=245,width=200,height=540,type=16)


        self.loot_list = []
        self.loot_list.append(Botin(x=1150,y=450,width=40,height=40,type=15))
        self.loot_list.append(Botin(x=1750,y=50,width=40,height=40,type=15))

        self.lever = Lever(x=260,y=670,width=50,height=50,type=17)

        self.door = Door(x=1000,y=100,width=150,height=250,type=18)

        self.bullet_list = []

        self.timer_3s = pygame.USEREVENT +1
        pygame.time.set_timer(self.timer_3s,3000)

        self.timer_10s = pygame.USEREVENT +2
        pygame.time.set_timer(self.timer_10s,10000)

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def line_of_sight(self, platform_list,enemy):
        has_vision = True
        for platform in platform_list:
            if platform.rect.collidepoint(enemy.rect.center):
                has_vision = False
                break

        return has_vision

    def shot_enemy(self):
            for enemy_element in self.enemy_list:
                if self.line_of_sight(self.plataform_list,enemy_element):
                    if enemy_element.direction == DIRECTION_L:
                        sentido = -1
                    else:
                        sentido = 1

                    if (enemy_element.direction == DIRECTION_L and self.player_1.direction == DIRECTION_R) or (enemy_element.direction == DIRECTION_R and self.player_1.direction == DIRECTION_L):

                        self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,sentido,20,path="parcial_juego/images/tileset/forest/Objects/15.png",frame_rate_ms=100,move_rate_ms=20,width=80,height=10))

    def summon(self):

        self.boss.animation = self.boss.summon_r
        self.enemy_list.append(Enemy(x=700,y=150,speed_walk=6,gravity=14,frame_rate_ms=150,move_rate_ms=50,p_scale=0.1))
        self.enemy_list.append(Enemy(x=750,y=150,speed_walk=6,gravity=14,frame_rate_ms=150,move_rate_ms=50,p_scale=0.1))


    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1,self.door,self.boss)
        
        for bullet_element in self.player_1.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1,self.door,self.boss)

        if len(self.enemy_list) > 0: 
            for enemy_element in self.enemy_list:
                enemy_element.update(delta_ms,self.plataform_list,self.enemy_list)

        for evento in lista_eventos:
            if evento.type == self.timer_3s:
                self.shot_enemy()

        if(self.lever.is_active):
            self.door.open_door()
        
        self.boss.update(delta_ms)

        # for evento in lista_eventos:
        #     if evento.type == self.timer_10s:
        #         self.summon()
        

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list,self.enemy_list)

        self.pb_lives.value = self.player_1.lives 


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        if len(self.enemy_list) > 0:
            for enemy_element in self.enemy_list:
                enemy_element.draw(self.surface)
        

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
        
        for bullet_element in self.player_1.bullet_list:
            bullet_element.draw(self.surface)

        self.boss.draw(self.surface)

        self.exit.draw(self.surface)

        self.ladder.draw(self.surface)

        self.lever.draw(self.surface)

        self.door.draw(self.surface)

        self.player_1.draw(self.surface)