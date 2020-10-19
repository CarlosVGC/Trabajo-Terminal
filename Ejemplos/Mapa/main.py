# Ejemplo de uso de mapa kivy
from kivy.app import App
from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.button import Button

class MainApp(App):
    def on_start(self):
        marker = MapMarkerPopup(lat = 10, lon = 12, source = "marcador.png")
        marker.add_widget(Button(text="Python button"))
        self.root.add_widget(marker)
    pass

MainApp().run()