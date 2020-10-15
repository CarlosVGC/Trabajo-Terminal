from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from baseclass.settingsscreen import SettingsScreen
from baseclass.utilidades import Banner
from kivymd.uix.datatables import MDDataTable
import pandas as pd
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel

#from kivy.properties import NumericProperty



class DashBoard(Screen):#Pantalla de Convertidor de unidades
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "Convertidor de onzas" 
        
        self.hint_onza_number = "Ingresa la cantidad de onzas"
    
    def on_pre_enter(self, *args):
        self.app.title = "Convertidor Unidades" #Se cambia el nombre de la pantalla
        
    def on_kv_post(self, base_widget): #Se lea el archivo kivy
        grid = self.ids["grid_utilidades"]
        '''
        for i in range(1):
            banner = Banner(title = f'Funcion{i}')
            grid.add_widget(banner)
        '''
        operations ={"onza_gramo": "Onza a Gramos",
                     "gramo_onza": "Gramos a Onzas",
                     "libra_gramo": "Libra a Gramos",
                     "kilogramo_libra": "Kilogramo a Libras",
                     "galon_litro": "Galon a Litro",
                     "litro_galon": "Litro a Galon",
                     "farenheit_celcius": "Farenheit a Celcius",
                     "celcius_farenheit": "Celcius a Farenheit"
                    } 
        
        for operation,title in operations.items():
            banner = Banner(title = title, operation = operation)
            grid.add_widget(banner)
            
            
    def onza_a_gramos(self, cantidad_onzas):
        try:
            gramos = int(cantidad_onzas) * 28.3495
            self.ids["solution"].text = f'Resultado: {gramos} gramos'
            self.ids["solution"].theme_text_color = "Primary"
            
        except ValueError:
            self.ids["solution"].text = "Carácteres no aceptados"
            self.ids["solution"].theme_text_color = "Error"
        
    pass

class FirstScreen(Screen): #Pantalla comparador de precios
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        
       
        self.buttonactualizar = MDRectangleFlatIconButton(
                                       pos_hint = {"center_x":.5, "top": .95},
                                       #size_hint = (.3,.1),
                                       icon = "cart-arrow-down",
                                       text = " Precios")
        
        self.etiqueta1 = MDLabel(text = 'Consultar por Tienda',
                             pos_hint = {"center_x": .5, "top":.80},
                             size_hint = (.5,.1),
                             theme_text_color = "Primary", 
                             font_style= "Subtitle1",
                             halign = "center")
        
        self.buttonche = MDRectangleFlatButton(
                #id = 'botonche',
                pos_hint = {"x": .05, "y": .6},
                size_hint = (.35,.1),
                text = "Chedraui",
                #on_press = print('hola'),
                on_release = lambda x: self.verboton('che')
                )        
        
        self.buttonsor = MDRectangleFlatButton(
                #id = 'botonsor',
                pos_hint = {"x": .6, "y": .6},
                size_hint = (.35,.1),
                text = "Soriana",
                on_release = lambda x: self.verboton('sor')
                )
        
        self.buttonhbe = MDRectangleFlatButton(
                #id = 'botonhbe',
                pos_hint = {"x": .05, "y": .45},
                size_hint = (.35,.1),
                theme_text_color = "Primary",
                text = "HBE",
                #on_press = print('hola'),
                on_release = lambda x: self.verboton('hbe')
                )
        
        self.buttoncomer = MDRectangleFlatButton(
                #id = 'botoncomer',
                pos_hint = {"x": .6, "y": .45},
                size_hint = (.35,.1),
                text = "La Comer",
                #on_press = print('hola'),
                on_release = lambda x: self.verboton('comer')
                )
        
        self.etiqueta2 = MDLabel(text = 'Consultar por Categoría',
                             pos_hint = {"center_x": .5, "top":.40},
                             size_hint = (.5,.1),
                             theme_text_color = "Primary", 
                             font_style= "Subtitle1",
                             halign = "center")
        
        self.buttonfrutas = MDRoundFlatButton(
                                       pos_hint = {"x":.05, "y": .20},
                                       size_hint = (.25,.1),
                                       text = "Frutas",
                                       on_release = lambda x: self.verboton('frutas'))
        
        self.buttonverduras = MDRoundFlatButton(
                                       pos_hint = {"x":.35, "y": .20},
                                       size_hint = (.25,.1),
                                       text = "Verduras",
                                       on_release = lambda x: self.verboton('verduras')
                                       )
        
        self.buttoncarnes = MDRoundFlatButton(
                                       pos_hint = {"x":.65, "y": .20},
                                       size_hint = (.25,.1),
                                       text = 'Carnes',
                                       on_release = lambda x: self.verboton('carnes')
                                       )
        
        self.buttonlacteos = MDRoundFlatButton(
                                       pos_hint = {"x":.20, "y": .05},
                                       size_hint = (.25,.1),
                                       text = 'Lácteos',
                                       on_release = lambda x: self.verboton('lacteos')
                                       )
        
        self.buttonenlatados = MDRoundFlatButton(
                                       pos_hint = {"x":.50, "y": .05},
                                       size_hint = (.25,.1),
                                       text = 'Enlatados',
                                       on_release = lambda x: self.verboton('enlatados')
                                       )
        
        self.add_widget(self.buttonactualizar)
        self.add_widget(self.buttonche)
        self.add_widget(self.buttonsor)
        self.add_widget(self.buttonhbe)
        self.add_widget(self.buttoncomer)
        self.add_widget(self.etiqueta1)
        self.add_widget(self.etiqueta2)
        self.add_widget(self.buttonfrutas)
        self.add_widget(self.buttonverduras)
        self.add_widget(self.buttoncarnes)
        self.add_widget(self.buttonlacteos)
        self.add_widget(self.buttonenlatados)
        
        #food-steak carne food-drumstick
        #food-apple fruta
        #cheese lacteos
        #carrot verduras
        #dome-light
        #return self.button
    #def tabla(self, widget):
        
    def verboton(self, valor):
        if valor == 'comer':
            datos = pd.read_csv("csv/info_lacomer.csv", encoding = 'utf8')
        elif valor == 'hbe':
            datos = pd.read_csv("csv/info_hbe.csv", encoding = 'utf8')
        elif valor == 'sor':
            datos = pd.read_csv("csv/info_sor.csv", encoding = 'utf8')
        elif valor == 'che':
            datos = pd.read_csv("csv/info_che.csv", encoding = 'utf8')
        elif valor == 'frutas':
            datos = pd.read_csv("csv/infofrutas.csv", encoding = 'utf8')
        elif valor == 'verduras':
            datos = pd.read_csv("csv/infoverduras.csv", encoding = 'utf8')
        elif valor == 'carnes':
            datos = pd.read_csv("csv/infocarnes.csv", encoding = 'utf8')
        elif valor == 'lacteos':
            datos = pd.read_csv("csv/infolacteos.csv", encoding = 'utf8')
        elif valor == 'enlatados':
            datos = pd.read_csv("csv/infoenlatados.csv", encoding = 'utf8')
            
        datos = datos.iloc[:,1: ]# primer arg selecciona todas las filas, segundo 
        cols = datos.columns.values
        values = datos.values
        
        self.table = MDDataTable(pos_hint={'center_x':0.5, 'center_y':0.5 },
                            size_hint=(0.99, 0.99),
                            #font_size = 10,
                            #check= True,
                            use_pagination= True,
                            rows_num=10,
                            column_data =[
                                    (col, dp(40))
                                    for col in cols
                                         ],
                            row_data= values)
        
        self.table.bind(on_check_press=self.check_press)
        self.table.bind(on_check_press=self.row_press)

        self.table.open()
        print(valor)
    
    def open_table(self, instance):
        #screen.add_widget(table)
        self.table.open()
        
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)
        
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
        #self.sub_title = "Comparador" 
    
    def on_pre_enter(self, *args):
        self.app.title = "Comparador de precios"
    
    pass
        
class MyApp(MDApp):
    def build(self):
        self.title = "Inventario" #Titulo de la aplicación
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('main.kv')
MyApp().run()
