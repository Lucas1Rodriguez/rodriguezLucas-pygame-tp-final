import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuD(Form):
    def __init__(self,name,master_surface,x,y,w,h,image_background,active):
        super().__init__(name,master_surface,x,y,w,h,image_background,active)

        self.boton1 = Button(master=self,x=0,y=140,w=180,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton,on_click_param="form_game_L1",text="NIVEL 1",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=0,y=200,w=180,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton,on_click_param="form_game_L2",text="NIVEL 2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=0,y=260,w=180,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton,on_click_param="form_game_L3",text="NIVEL 3",font="Verdana",font_size=30,font_color=C_WHITE)        
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3]
    
    def on_click_boton(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)        

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()