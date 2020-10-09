from kivy.app import App
from kivymd.theming import ThemeManager


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import pandas as pd

KV = '''
<DemoApp>:
    Screen:
        MDRectangleFlatButton:
            text: "MDRECTANGLEFLATBUTTON"
            font_name: "Calibri"
            pos_hint : {"center_x": .5, "y": .8}
            text_color: 0, 0, 1, 1
            md_bg_color: 1, 1, 0, 1
            on_release: root.open_table
'''

class DemoApp(MDApp):
    def build(self):
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
        
        
class MainApp(App):
    theme_cls = ThemeManager()
        
        
DemoApp().run()
