from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from datetime import datetime

from plyer import notification
from random import randint

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        self.app.title = "Ajustes"
        self.MuestraNotificacionInicial()

    def MuestraNotificacionInicial(self):
        """Muestra la notificacion inicial cuando se inicia la aplicación, esta funcion se llama al inicializar la aplicacion y despliega la notificación"""
        print("Estoy en muestra notifica")

        self.a = randint(1, 2)#
        print(self.a)
        if self.a == 1:
            notification.notify(title='Puedes personalizar el esquema de colores',
                                message='Selecciona el esquema de tu preferencia en la sección de ajuste, busca el simbolo de una brocha, ese es el lugar',
                                timeout=20)
        if self.a == 2:
            notification.notify(title='Cambia a modo nocturno',
                                message='Si deseas cambiar a modo nocturno puedes hacerlo en la parte de ajustes,en  la primera opción que se muestra puedes hacerlo',
                                timeout=20)
        
    def cambiar_modo(self, checkbox, value):
        if value:
            self.app.theme_cls.theme_style = "Dark"
            
        else:
            self.app.theme_cls.theme_style = "Light"
            
    def get_date(self, date): #tiempo
        '''
        :type date: <class 'datetime.date'>
        '''
        
        self.ids["fecha"].text = date.strftime("%d/%m/%Y") #se le cambia el formato a la fecha
    
    def get_time(self, instance, time):
        '''
        The method returns the set time
        
        :type instance <kivy.uix.picker.MDtimePicker object>
        :type time: <class 'datetime.time'>
        '''
        self.ids["hora"].text = time.strftime("%H:%M") #el id hora (a etiqueta) mostrará la hora que se selecciono
    

    def show_date_picker(self): #funcion con la cual se utiliza el picker de tiempo
        #min_date = datetime.strptime("01:10:2020", "%d:%m:%Y").date()
        #ax_date = datetime.strptime("01:10:2020", "%d:%m:%Y").date()
        date_dialog = MDDatePicker(callback = self.get_date)
        date_dialog.open()
        
    def show_time_picker(self): #funcion con la cual se utiliza el picker de hora
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()
        
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
        
    