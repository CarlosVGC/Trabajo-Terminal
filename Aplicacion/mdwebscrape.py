from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from baseclass.settingsscreen import SettingsScreen
from baseclass.utilidades import Banner
from kivymd.uix.datatables import MDDataTable
import pandas as pd
from kivy.metrics import dp
from kivymd.uix.button import MDRectangleFlatButton


class DashBoard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "Convertidor de onzas"
        self.hint_onza_number = "Ingresa la cantidad de onzas"
    
    def on_pre_enter(self, *args):
        self.app.title = "Convertidor Unidades"
        
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

class FirstScreen(Screen):
   
    '''
    def on_pre_enter(self, *args):
        self.app.title = "Comparador de precios"
    '''
    def on_enter(self):
        #screen = Screen()
        datos = pd.read_csv("csv/info_che.csv", encoding = 'utf8')
        datos = datos.iloc[:,1: ]# primer arg selecciona todas las filas, segundo 
        cols = datos.columns.values
        values = datos.values
        
        #nombres = ['a','b','c','d','e','f','g','h','i','j']
        #calorias=['10','20','30','40','50','60','70','80','90','100']
        #items = [i for i in range(len(nombres))]
        
       # datosfila=[]
        
        #for a in range(10):
         #   datosfila.append([items[a], nombres[a], calorias[a]]) 
        
        
        #datosfila=[("1", "Hamburguesa", "300"),("2", "Papas", "200"),("3", "Tacos", "150")]
        
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
        
       
      
        
        self.button = MDRectangleFlatButton(
                pos_hint = {"center_x": .5, "y": .8},
                
                text = "Precios en Chedraui",
                on_release = self.open_table
                )
        '''
        self.button2 = MDRectangleFlatButton(
                pos_hint = {"center_x": .5, "y": .7},
                
                text = "Precios en Soriana",
                on_release = self.open_table
                )
        '''
        
        return self.button
    
    def open_table(self, instance):
        #screen.add_widget(table)
        self.table.open()
        
        
        
        
        '''
        def on_start(self):
            self.table.open()
        '''
        
        
        #return(screen)
        
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)
        
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
        
    pass
        

class MyApp(MDApp):
    def build(self):
        self.title = "Inventario" #Titulo de la aplicación
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('mdwebscrape.kv')
MyApp().run()
