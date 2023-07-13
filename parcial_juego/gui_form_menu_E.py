import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form

from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuE(Form):
    def __init__(self,name,master_surface,x,y,w,h,image_background,active):
        super().__init__(name,master_surface,x,y,w,h,image_background,active)

        self.nivel_actual = ""
        self.boton_reiniciar_lvl = Button(master=self,x=0,y=260,w=180,h=50,color_background=None,color_border=None,image_background="parcial_juego/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton,text="REINICIAR NIVEL",font="Verdana",font_size=30,font_color=C_WHITE)        

        self.lista_widget = [self.boton_reiniciar_lvl]
    
    def on_click_boton(self, parametro):
        self.nivel_actual = parametro
        self.set_active(parametro)

    def on_click_boton_reiniciar_lvl(self):
        if self.nivel_actual.startswith("form_game_L"):
            nivel = int(self.nivel_actual.replace("form_game_L", ""))
            if nivel == 1:
                self.reiniciar_nivel_lv1(nivel)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)        

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()