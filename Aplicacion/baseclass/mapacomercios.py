from kivy.garden.mapview import MapView
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
class MapaComercios(Screen):
    def __init__(self, **kwargs):
        super().__init__()

        self.mapview = MapView(zoom=10,
                               lat=50.6394,
                               lon=3.057,

                               )
                               
        self.add_widget(self.mapview)

        '''
        self.titulo = MDLabel(text="titulo",
                              pos_hint={"center_x": .5, "top": .99},
                              size_hint=(.5, .1),
                              font_style="H6",
                              halign='center'
                              )
        self.add_widget(self.titulo)
        '''
    pass