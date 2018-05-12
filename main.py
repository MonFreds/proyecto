#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.accordion import Accordion
import time
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import cv2
import numpy as np
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import StringProperty

import MySQLdb

#Window.size = (1300,890)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '670')


class Cargar(Screen):
    pass


class PaginaInicial(Screen):
    pass


class LabelConfig(Screen):
    def errorP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos estan vacíos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint ={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorL(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos son muy cortos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def exitoP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text='Transacción Exitosa',
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Datos Correctos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def validar1(self):
        d1 = self.ids.ti_nombreM.text
        d2 = self.ids.ti_largo.text
        d3 = self.ids.ti_ancho.text
        d4 = self.ids.ti_peso.text
        d5 = self.ids.ti_costo.text
        d6 = self.ids.ti_precioMin.text
        d7 = self.ids.ti_precioOpt.text
        d8 = self.ids.ti_existencias.text
        a1 = (d1, d2, d3, d4, d5, d6, d7, d8)
        al2 = (d2, d3, d4, d5, d6, d7, d8)

        if '' in a1 and (self.ids.bt_insertar1.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar1.state == 'down'):
                self.errorP()
                self.limpiar1()
            else:
                if (len(self.ids.ti_nombreM.text) < 4
                        or len(self.ids.ti_largo.text) < 2
                        or len(self.ids.ti_ancho.text) < 2
                        or len(self.ids.ti_costo.text) < 3
                        or len(self.ids.ti_precioMin.text) < 3
                        or len(self.ids.ti_precioOpt.text) < 3):
                    self.errorL()
                else:
                    self.exitoP()
                    self.limpiar1()

    def limpiar1(self):
        self.ids.ti_nombreM.text = ''
        self.ids.ti_ancho.text = ''
        self.ids.ti_largo.text = ''
        self.ids.ti_peso.text = ''
        self.ids.ti_costo.text = ''
        self.ids.ti_precioMin.text = ''
        self.ids.ti_precioOpt.text = ''
        self.ids.ti_existencias.text = ''
        self.ids.ti_nombreM.hint_text = "Ingresa Nombre"
        self.ids.ti_largo.hint_text = "Ingresa Largo"
        self.ids.ti_ancho.hint_text = "Ingresa Ancho"
        self.ids.ti_peso.hint_text = "Ingresa Peso"
        self.ids.ti_costo.hint_text = "Ingresa Costo"
        self.ids.ti_precioMin.hint_text = "Ingresa Precio Min"
        self.ids.ti_precioOpt.hint_text = "Ingresa Precio Opt"
        self.ids.ti_existencias.hint_text = "Ingresa Existencias"
        self.ids.bt_insertar1.state = 'normal'
        self.ids.bt_actualizar1.state = 'normal'

    def validar2(self):
        d1 = self.ids.ti_nombreP.text
        d2 = self.ids.ti_direccion.text
        d3 = self.ids.ti_telefono.text
        d4 = self.ids.ti_referencias.text
        a1 = (d1, d2, d3, d4)
        al2 = (d2, d3, d4)

        if '' in a1 and (self.ids.bt_insertar2.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar2.state == 'down'):
                self.errorP()
                self.limpiar2()
            else:
                if (len(self.ids.ti_nombreP.text) < 4
                    or len(self.ids.ti_direccion.text) < 15
                    or len(self.ids.ti_telefono.text) < 12
                    or len(self.ids.ti_referencias.text) < 10):
                    self.errorL()
                else:
                    self.exitoP()
                    self.limpiar2()

    def limpiar2(self):
        self.ids.ti_nombreP.text = ''
        self.ids.ti_direccion.text = ''
        self.ids.ti_telefono.text = ''
        self.ids.ti_referencias.text = ''
        self.ids.ti_nombreP.hint_text = "Ingresa Provedor"
        self.ids.ti_direccion.hint_text = "Ingresa Dirección"
        self.ids.ti_telefono.hint_text = "Ingresa Teléfono"
        self.ids.ti_referencias.hint_text = "Ingresa Referencias"
        self.ids.bt_insertar2.state = 'normal'
        self.ids.bt_actualizar2.state = 'normal'

    def validar3(self):
        d2 = self.ids.ti_cantidad.text
        d3 = self.ids.ti_precio.text
        a1 = (d2, d3)
        if '' in a1:
            self.errorP()
        else:
            if len(self.ids.ti_precio.text) < 3:
                self.errorL()
            else:
                self.exitoP()
                self.limpiar3()

    def limpiar3(self):
        self.ids.ti_cantidad.text = ''
        self.ids.ti_precio.text = ''
        self.ids.ti_cantidad.hint_text = "Ingresa Cantidad"
        self.ids.ti_precio.hint_text = "Ingresa Precio"
        self.ids.ti_total.hint_text = "0"
        self.ids.bt_insertar3.state = 'normal'

    def validar4(self):
        d1 = self.ids.ti_usuario.text
        d2 = self.ids.ti_password.text
        a1 = (d1, d2)
        al2 = (d2)
        if '' in a1 and (self.ids.bt_insertar.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar.state == 'down'):
                self.errorP()
                self.limpiar4()
            else:
                if (len(self.ids.ti_usuario.text) < 4
                    or len(self.ids.ti_password.text) < 4):
                    self.errorL()
                else:
                    self.exitoP()
                    self.limpiar4()

    def limpiar4(self):
        self.ids.ti_usuario.text = ''
        self.ids.ti_password.text = ''
        self.ids.ti_usuario.hint_text = "Ingresa Usuario"
        self.ids.ti_password.hint_text = "Password"
        self.ids.bt_insertar.state = 'normal'
        self.ids.bt_actualizar1.state = 'normal'


class CamClick(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("LL_{}.png".format(timestr))


class Inicio(Screen):
    def errorP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos vacíos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorL(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Usuario o contraseña incorrectos",
                                pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def validarIni(self):
        d1 = self.ids.ti_userL.text
        d2 = self.ids.ti_passwordL.text
        a1 = (d1, d2)
        if '' in a1:
            self.errorP()
        else:
            try:
                con = MySQLdb.connect(host="127.0.0.1",
                                    user=self.ids.ti_userL.text,
                                    passwd=self.ids.ti_passwordL.text,
                                    db="lalibertad")
                self.parent.menuP()
                cursor = con.cursor()
                con.commit()
            except Exception:
                self.errorL()


class ScreenManagement(ScreenManager):
    def inicial(self):
        self.current = 'cargar'

    def login(self):
        self.current = 'inicio'

    def opciones(self):
        self.current = 'labelConfig'
        self.spinners()

    def opciones_mercancias(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'MERCANCIAS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_proveedores(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'PROVEEDORES':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_ventas(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'VENTAS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_usuarios(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'USUARIOS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def menuP(self):
        self.current = 'paginaInicial'

    def camaraAccion(self):
        self.current = 'camClick'


class MainApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root

if __name__ in ('__main__', '__android__'):
    MainApp().run()

