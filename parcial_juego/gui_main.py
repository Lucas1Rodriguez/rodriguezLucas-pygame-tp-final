import pygame
from pygame.locals import *
import sys
from constantes import *
from background import Background
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_D import FormMenuD
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

evento_1000ms = pygame.USEREVENT
pygame.time.set_timer(evento_1000ms, 1000)

cronometro = 60


form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=600,y=300,w=500,h=400,image_background="parcial_juego/images/gui/set_gui_01/Sand/Elements/Tab_Background02.png",active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=600,y=300,w=500,h=400,image_background=None,active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,image_background=None,active=False)
form_menu_D = FormMenuD(name="form_menu_D",master_surface = screen,x=600,y=300,w=500,h=400,image_background="parcial_juego/images/gui/jungle/level_select/bg.png",active=False)


form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,255),color_border=(0,0,255),image_background=None,active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,image_background=None,active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),image_background=None,active=False)

static_background = Background(x=0,y=0,width=ANCHO_VENTANA,height=ALTO_VENTANA,path="parcial_juego/images/locations/set_bg_01/forest/istock-539115110.jpeg")


while True:     
    static_background.draw(screen)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == evento_1000ms:
            cronometro -= 1

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()

    if cronometro == 0:
        print("Perdió")
        
    pygame.display.flip()




    


  






    


  



