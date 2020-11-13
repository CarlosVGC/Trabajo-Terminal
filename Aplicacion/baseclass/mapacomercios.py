from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import  Image


from kivymd.uix.label import MDLabel

class MapaComercios(Screen):#Screen
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()

        self.mapview = MapView(lat=19.60389,
                          lon=-99.01260,
                          zoom=10
                          )

        #self.mapview.add_marker(m1)

        self.borramarcador = MDIconButton(pos_hint={"x": .75, "y":.5},
                                     icon = "close-circle-outline",
                                     user_font_size = "32sp"
                                    )

        self.botongps = MDIconButton(pos_hint={"x": .75, "y": .03},
                                     icon = "crosshairs-gps",
                                     user_font_size = "32sp"
                                    )

        self.botonayuda = MDIconButton(pos_hint={"x": .75, "y": .13}, #falta agregar funcion para mostrar
                                       icon="help-box",
                                       user_font_size="32sp"
                                      )

        self.botonche = MDFillRoundFlatButton(pos_hint={"x": .1, "y": .05},
                                              size_hint=(.25, .07),
                                              text = "Chedraui",
                                              )
        self.mr = Image(source="imagenes/pinrojo.png",
                        pos_hint={"x": -.385, "y": -.41})

        self.botonhbe = MDFillRoundFlatButton(pos_hint={"x": .5, "y": .05},
                                              size_hint=(.25, .07),
                                              text="HEB"
                                              )
        self.mg = Image(source="imagenes/pingris.png",
                        pos_hint={"x": .013, "y": -.41})

        self.botoncomer = MDFillRoundFlatButton(pos_hint={"x": .1, "y": .15},
                                              size_hint=(.25, .07),
                                              text="La Comer"
                                              )
        self.mv = Image(source="imagenes/pinverde.png",
                        pos_hint={"x": -.385, "y": -.31})

        self.botonsor = MDFillRoundFlatButton(pos_hint={"x": .5, "y": .15},
                                              size_hint=(.25, .07),
                                              text="Soriana"
                                              )
        self.ma = Image(source="imagenes/pinazul.png",
                        pos_hint={"x": .013, "y": -.31})

        self.botongps.bind(on_press=lambda x: self.ActivaGPS())
        self.botonayuda.bind(on_press=lambda x: self.AyudaMapa())
        self.botonche.bind(on_press=lambda x: self.Consulta_Che())
        self.botonsor.bind(on_press=lambda x: self.Consulta_Sor())
        self.botoncomer.bind(on_press=lambda x: self.Consulta_Comer())
        self.borramarcador.bind(on_press=lambda x: self.BorraMarcador())


        self.add_widget(self.mapview) # Se agrega el mapa en la "capa inferior"
        self.add_widget(self.botongps) # En una "capa" posterior se agrega el boton para que se vea
        self.add_widget(self.botonche)
        self.add_widget(self.botonhbe)
        self.add_widget(self.botoncomer)
        self.add_widget(self.botonsor)
        self.add_widget(self.botonayuda)
        self.add_widget(self.borramarcador)
        self.add_widget(self.mr)
        self.add_widget(self.mv)
        self.add_widget(self.mg)
        self.add_widget(self.ma)

    def ActivaGPS(self):
        print("GPS")
        pass

    def AyudaMapa(self):
        print("Esto es ayuda")

        self.dialog = MDDialog(title = "Ayuda sobre el mapa",
                               text="Utiliza los botones en la parte inferior para localizar los centros comerciales"
                                    " en cada localización que se muestran en el mapa, se puede pulsar sobre el pin para desplegar "
                                    "información sobre el centro comercial en cuestión",
                               size_hint=[.9, .9],
                               auto_dismiss=True,

                               buttons=[MDFlatButton(
                                        text="CERRAR",
                                        on_release=self.dialog_close)
                                        ]
                               )
        self.dialog.open()
        pass

    def Consulta_Che(self):
        print("Consultando Chedraui")
        self.datosches = {'che1': {'direccion': '4TA. AVENIDA NO. 257 LOTE 1',
                                   'colonia': 'Fracc Rey Neza',
                                   'lat': 19.40068,
                                   'lon': -98.98720,
                                   'tel': '54412720',
                                   'cp': '57000',
                                   'municipio': 'Nezahualcoyotl'
                                   },

                          'che2': {'direccion': 'AV. TEXCOCO NO. 292',
                                   'colonia': 'Pavón',
                                   'lat': 19.396626,
                                   'lon': -99.048428,
                                   'tel': '11038000 ext 37140',
                                   'cp': '57610',
                                   'municipio': 'Nezahualcoyotl'
                                   },

                          'che3': {'direccion': 'AV. RIO DE LA LOZA NO. 4 ',
                                   'colonia': 'San Miguel Chalma',
                                   'lat': 19.545221,
                                   'lon': -99.152201,
                                   'tel': '11038000 ext 37130',
                                   'cp': '07160',
                                   'municipio': 'Tlalnepantla'
                                   },

                          'che4': {'direccion': 'AV. INSURGENTES SIN NUMERO',
                                   'colonia': 'Calvario',
                                   'lat': 19.60237,
                                   'lon': -99.05572,
                                   'tel': 'Sin tel',
                                   'cp': '55020',
                                   'municipio': 'Ecatepec de Morelos'
                                   },

                          'che5': {'direccion': 'AV ALFREDO DEL MAZO NO. 705',
                                   'colonia': 'Tlacopa',
                                   'lat': 19.309995,
                                   'lon': -99.635682,
                                   'tel': '017222379445',
                                   'cp': '50100',
                                   'municipio': 'Toluca de Lerdo'
                                   },

                          'che6': {'direccion': 'PROL. GUADALUPE VICTORIA NO. 471',
                                   'colonia': 'La Purisima',
                                   'lat': 19.258697,
                                   'lon': -99.628197,
                                   'tel': '017222127113',
                                   'cp': '52140',
                                   'municipio': 'Metepec'
                                   },

                          'che7': {'direccion': 'BLVRD JUAN HERRERA Y PIÑA 7',
                                   'colonia': 'Barrio Otumba',
                                   'lat': 19.204049,
                                   'lon': -100.125421,
                                   'tel': '7262626942',
                                   'cp': '51200',
                                   'municipio': 'Valle de Bravo'
                                   },

                          'che8': {'direccion': 'BLVD. MANUEL AVILA CAMACHO 5',
                                   'colonia': 'Lomas de Sotelo',
                                   'lat': 19.454290,
                                   'lon': -99.219101,
                                   'tel': '7262626942',
                                   'cp': '53390',
                                   'municipio': 'Naucalpan de Juárez'
                                   },

                          'che9': {'direccion': 'AV. DE LOS BOSQUES NO. 128',
                                   'colonia': 'Lomas de Tecamachalco',
                                   'lat': 19.411133,
                                   'lon': -99.250840,
                                   'tel': '5555967887',
                                   'cp': '52780',
                                   'municipio': 'Huixquilucan'
                                   },
                          'che10':{'direccion': 'AV. CENTRAL ESQ. AV JARDINES DE MORELOS S/N',
                                   'colonia': 'Jardínes de Morelos',
                                   'lat': 19.603457,
                                   'lon': -99.013337,
                                   'tel': '5558371634',
                                   'cp': '55065',
                                   'municipio': 'Ecatepec de Morelos'
                                   },
                          'che11': {'direccion': 'AV.AQUILES SERDAN 360',
                                   'colonia': 'El Mirador',
                                   'lat': 19.257597,
                                   'lon': -99.022525,
                                   'tel': '5525942726',
                                   'cp': '16740',
                                   'municipio': 'Xochimilco'
                                    },

                          'che12': {'direccion': 'CTRA. A SANTIAGO TEPELCATLALPAN 400',
                                    'colonia': 'Santiago Tepalcatlalpan',
                                    'lat': 19.257736,
                                    'lon': -99.122394,
                                    'tel': '5555557600',
                                    'cp': '16210',
                                    'municipio': 'Xochimilco'
                                    },

                          'che13': {'direccion': 'AV. UNIVERSIDAD 740',
                                    'colonia': 'Sta Cruz Atoyac',
                                    'lat': 19.373194,
                                    'lon': -99.162387,
                                    'tel': '8005632222',
                                    'cp': '03310',
                                    'municipio': 'Benito Juárez'
                                    },

                          'che14': {'direccion': 'VASCO DE QUIROGA 3800',
                                    'colonia': 'Lomas de Santa Fe',
                                    'lat': 19.359963,
                                    'lon': -99.274583,
                                    'tel': '5521678307',
                                    'cp': '05348',
                                    'municipio': 'Cuajimalpa'
                                    },

                          'che15': {'direccion': 'AV. BENITO JUAREZ NO. 39 MZ 36',
                                    'colonia': 'Presidentes',
                                    'lat': 19.376661,
                                    'lon': -99.223099,
                                    'tel': '5511038000',
                                    'cp': '01290',
                                    'municipio': 'Álvaro Obregón'
                                    },

                          'che16': {'direccion': 'AV. CANAL DE TEZONTLE 1512',
                                    'colonia': 'Área Federal Central de Abastos',
                                    'lat': 19.384808,
                                    'lon': -99.082368,
                                    'tel': '5511038000',
                                    'cp': '09020',
                                    'municipio': 'Iztapalapa'
                                    },

                          'che17': {'direccion': 'BUEN TONO NO. 8',
                                    'colonia': 'Centro',
                                    'lat': 19.428273,
                                    'lon': -99.143175,
                                    'tel': '5555124069',
                                    'cp': '06070',
                                    'municipio': 'Cuahtémoc'
                                    },

                          'che18': {'direccion': 'BLVD. MIGUEL DE CERVANTES SAAVEDRA 397',
                                    'colonia': 'Irrigación',
                                    'lat': 19.441866,
                                    'lon': -99.206946,
                                    'tel': '5555803422',
                                    'cp': '11579',
                                    'municipio': 'Miguel Hidalgo'
                                    },

                          'che19': {'direccion': 'AV. CUAUTEPEC NO. 117',
                                    'colonia': 'Jorge Negrete',
                                    'lat': 19.526125,
                                    'lon': -99.141422,
                                    'tel': '8009251111',
                                    'cp': '07280',
                                    'municipio': 'Gustavo A. Madero'
                                    },

                          'che20': {'direccion': 'AV. FORTUNA 334',
                                    'colonia': 'Magdalena de las Salinas',
                                    'lat': 19.482093,
                                    'lon': -99.130347,
                                    'tel': '8009251111',
                                    'cp': '07760',
                                    'municipio': 'Gustavo A. Madero'
                                    },


        }

        # for i in range(10):
        #    marcador = MapMarkerPopup(lat = i, lon = i)
        #    marcador.add_widget(MDIconButton(icon = "information"))
        #    self.mapview.add_marker(marcador)

        '''
        m1 = MapMarker(lat=19.60389, lon=-99.01260)  # agregando marcador
        self.mapview.add_marker(m1)
        m2 = MapMarker(lat=19.80389, lon=-99.11260)  # agregando marcador
        self.mapview.add_marker(m2)
        '''
        for keys, values in self.datosches.items():
            for vkeys, vvalues in values.items():
                if vkeys == 'direccion':
                    dir = vvalues

                if vkeys == 'colonia':
                    col = vvalues

                if vkeys == 'tel':
                    tel = vvalues

                if vkeys == 'cp':
                    cp = vvalues

                if vkeys == 'municipio':
                    mun = vvalues

                if vkeys == 'lat':
                    nlat = vvalues
                    # print("lat: "+str(nlat))

                if vkeys == 'lon':
                    nlon = vvalues
                    # print("lon: "+str(nlon))

            print("lat: " + str(nlat) + " lon: " + str(nlon))

            cadena_final = f'Dir: {dir}\nCol: {col}\nCP: {cp}\nMun: {mun}\nTel: {tel}\n\n'

            self.marcador = MapMarkerPopup(lat=nlat, lon=nlon, source= "imagenes/pinrojo.png")
            # self.marcador.add_widget(MDIconButton(icon="information", on_release= lambda *args: self.info_che(*args)))
            self.marcador.add_widget(MDLabel(size_hint=(5, .5), text=cadena_final))

            self.mapview.add_marker(self.marcador)

            print(self.marcador)  # da una direccion diferrente, desde aqui se tiene que hacer de alguna forma


    def Consulta_Sor(self):

        self.datossor = {'sor1': {'direccion': 'CTRA. MEXICO-TEPEXPAN ESQ. LOS REYES TEXCOCO NO. 8',
                                   'colonia': 'San Isidro Atlautenco',
                                   'lat': 19.620721,
                                   'lon': -98.997171,
                                   'tel': '8007074262',
                                   'cp': '55064',
                                   'municipio': 'Ecatepec de Morelos'
                                   },

                          'sor2': {'direccion': 'LA PURISIMA NO. 5',
                                   'colonia': 'San Cristóbal Lejipaya',
                                   'lat': 19.602854,
                                   'lon': -98.946640,
                                   'tel': '5949569566',
                                   'cp': '55800',
                                   'municipio': 'Atenco'
                                  },

                         'sor3': {'direccion': 'AV. CENTRAL 65',
                                  'colonia': '1ro de Agosto',
                                  'lat': 19.551379,
                                  'lon': -99.018549,
                                  'tel': '8002201234',
                                  'cp': '55100',
                                  'municipio': 'Ecatepec de Morelos'
                                  },

                         'sor4': {'direccion': 'MEXICO NO. 5',
                                  'colonia': 'Cd. López Mateos',
                                  'lat': 19.568340,
                                  'lon': -99.250645,
                                  'tel': '5558225029',
                                  'cp': '52960',
                                  'municipio': 'Atizapán'
                                  },

                         'sor5': {'direccion': 'AV. 16 DE SEPTIEMBRE 34',
                                  'colonia': 'Paraiso II',
                                  'lat': 19.631577,
                                  'lon': -99.119169,
                                  'tel': '8007074262',
                                  'cp': '55700',
                                  'municipio': 'Coacalco'
                                  },

                         'sor6': {'direccion': 'AV. CUITLAHUAC 372',
                                  'colonia': 'Cuitlahuac',
                                  'lat': 19.471089,
                                  'lon': -99.170700,
                                  'tel': '8002201234',
                                  'cp': '02530',
                                  'municipio': 'Azcapotzalco'
                                  },

                         'sor7': {'direccion': 'AV. TOLTECAS S/N',
                                  'colonia': 'Hab. Los Reyes',
                                  'lat': 19.53765,
                                  'lon': -99.189802,
                                  'tel': '5516659002',
                                  'cp': '54090',
                                  'municipio': 'Tlalnepantla'
                                  },

                         'sor8': {'direccion': 'AV. GUSTAVO BAZ PRADA 250',
                                  'colonia': 'Bosques de Echegaray',
                                  'lat': 19.491437,
                                  'lon': -99.227430,
                                  'tel': '5553736844',
                                  'cp': '53300',
                                  'municipio': 'Naucalpan'
                                  },

                         'sor9': {'direccion': 'CALLE MEXIQUENSE 31',
                                  'colonia': 'Los Héroes Tecámac',
                                  'lat': 19.633013,
                                  'lon': -99.033405,
                                  'tel': '5558369960',
                                  'cp': '55765',
                                  'municipio': 'Tecámac'
                                  },

                         'sor10': {'direccion': 'CTRA. MEX-QRT KM 36.8',
                                  'colonia': 'Reforma Política',
                                  'lat': 19.650797,
                                  'lon': -99.195386,
                                  'tel': '8002201234',
                                  'cp': '54700',
                                  'municipio': 'Cuautitlán Izcalli'
                                  },

                         'sor11': {'direccion': 'AV. STA. FE 46',
                                   'colonia': 'Lomas de Santa Fe',
                                   'lat': 19.357175,
                                   'lon': -99.273897,
                                   'tel': 'Sin info',
                                   'cp': '01219',
                                   'municipio': 'Cuajimalpa'
                                   },

                         'sor12': {'direccion': 'AV. IMAN 550',
                                   'colonia': 'Pedregal de Carrasco',
                                   'lat': 19.306898,
                                   'lon': -99.164659,
                                   'tel': '5555288345',
                                   'cp': '04700',
                                   'municipio': 'Coyoacán'
                                   },

                         'sor13': {'direccion': 'ERMITA IZTAPALAPA 3016',
                                   'colonia': 'Reforma Politica',
                                   'lat': 19.344716,
                                   'lon': -99.027594,
                                   'tel': '8183299252',
                                   'cp': '09730',
                                   'municipio': 'Iztapalapa'
                                   },

                         'sor14': {'direccion': 'CALZ. DE LA VIGA 1805',
                                   'colonia': 'Mexicaltzingo',
                                   'lat': 19.360090,
                                   'lon': -99.123618,
                                   'tel': '8183299252',
                                   'cp': '09080',
                                   'municipio': 'Iztapalapa'
                                   },

                         'sor15': {'direccion': 'AV. REVOLUCION 780',
                                   'colonia': 'San Juan',
                                   'lat': 19.379381,
                                   'lon': -99.185600,
                                   'tel': '5555655046',
                                   'cp': '03730',
                                   'municipio': 'Benito Juárez'
                                   },

                         'sor16': {'direccion': 'OBRERO MUNDIAL 320',
                                   'colonia': 'Piedad Narvarte',
                                   'lat': 19.402383,
                                   'lon': -99.154002,
                                   'tel': '5583299000',
                                   'cp': '03000',
                                   'municipio': 'Benito Juárez'
                                   },

                         'sor17': {'direccion': 'AV. EL ROSARIO 901',
                                   'colonia': 'El Rosario',
                                   'lat': 19.504132,
                                   'lon': -99.200933,
                                   'tel': '8007074262',
                                   'cp': '02100',
                                   'municipio': 'Azcapotzalco'
                                   },

                         'sor18': {'direccion': 'CALZ. DE LOS MISTERIOS 62',
                                   'colonia': 'Tepeyac Insurgentes',
                                   'lat': 19.489655,
                                   'lon': -99.119282,
                                   'tel': '8002201234',
                                   'cp': '07020',
                                   'municipio': 'Gustavo A. Madero'
                                   },

                         'sor19': {'direccion': 'AV. EJERCITO NACIONAL 769',
                                   'colonia': 'Granada',
                                   'lat': 19.439809,
                                   'lon': -99.199979,
                                   'tel': '5591260960',
                                   'cp': '11520',
                                   'municipio': 'Miguel Hidalgo'
                                   },

                         'sor20': {'direccion': 'AV JARDIN 330',
                                   'colonia': 'Col del Gas',
                                   'lat': 19.468902,
                                   'lon': -99.159565,
                                   'tel': '8002201234',
                                   'cp': '02970',
                                   'municipio': 'Azcapotzalco'
                                   },
                          }
        #self.mapview.add_layer(self.layersor)

        for keys, values in self.datossor.items():
            for vkeys, vvalues in values.items():
                if vkeys == 'direccion':
                    dir = vvalues

                if vkeys == 'colonia':
                    col = vvalues

                if vkeys == 'tel':
                    tel = vvalues

                if vkeys == 'cp':
                    cp = vvalues

                if vkeys == 'municipio':
                    mun = vvalues

                if vkeys == 'lat':
                    nlat = vvalues
                    # print("lat: "+str(nlat))

                if vkeys == 'lon':
                    nlon = vvalues
                    # print("lon: "+str(nlon))

            print("lat: " + str(nlat) + " lon: " + str(nlon))

            cadena_final = f'Dir: {dir}\nCol: {col}\nCP: {cp}\nMun: {mun}\nTel: {tel}\n\n'

            #self.layer.add_marker(lon=nlon, lat=nlat, source= "imagenes/pinazul.png")


            self.marcador = MapMarkerPopup(lat=nlat, lon=nlon, source= "imagenes/pinazul.png")
            # self.marcador.add_widget(MDIconButton(icon="information", on_release= lambda *args: self.info_che(*args)))
            self.marcador.add_widget(MDLabel(size_hint=(5, .5), text=cadena_final))

            self.mapview.add_marker(self.marcador)

            print(self.marcador)  # da una direccion diferrente, desde aqui se tiene que hacer de alguna forma
            
        #self.mapview.add_widget(self.layer)

    def Consulta_Comer(self):
        print("Estoy en la comer")

        self.datoscomer = {'comer1': {'direccion': 'CALZ DEL HUESO 530',
                                  'colonia': 'Fracc. Los Girasoles',
                                  'lat': 19.305154,
                                  'lon': -99.126231,
                                  'tel': '01 800 3777 333',
                                  'cp': '4929',
                                  'municipio': 'Coyoacan'
                                  },

                           'comer2': {'direccion': 'ATENAS 6',
                                      'colonia': 'Fracc. Valle Dorado',
                                      'lat': 19.551346,
                                      'lon': -99.209801,
                                      'tel': '01 800 3777 333',
                                      'cp': '54020',
                                      'municipio': 'Tlalnepantla'
                                      },

                           'comer3': {'direccion': 'BLVD MANUEL AVILA CAMACHO 3228',
                                      'colonia': 'Boulevares',
                                      'lat': 19.498145,
                                      'lon': -99.237891,
                                      'tel': '01 800 3777 333',
                                      'cp': '53100',
                                      'municipio': 'Naucalpan de Juárez'
                                      },

                           'comer4': {'direccion': 'PLAZUELA DE LA FAMA 1',
                                      'colonia': 'La Fama',
                                      'lat': 19.288794,
                                      'lon': -99.179277,
                                      'tel': '01 800 3777 333',
                                      'cp': '14410',
                                      'municipio': 'Tlalpan'
                                      },

                           'comer5': {'direccion': 'CIRCUITO MEDICOS 35',
                                      'colonia': 'Ciudad Satélite',
                                      'lat': 19.509474,
                                      'lon': -99.232960,
                                      'tel': '01 800 3777 333',
                                      'cp': '53100',
                                      'municipio': 'Naucalpan de Juárez'
                                      },

                           'comer6': {'direccion': 'NOGAL 212',
                                      'colonia': 'Santa María La Ribera',
                                      'lat': 19.451636,
                                      'lon': -99.163952,
                                      'tel': '01 800 3777 333',
                                      'cp': '6400',
                                      'municipio': 'Cuauhtémoc'
                                      },

                           'comer7': {'direccion': 'CTRA A CELAYA 2',
                                      'colonia': 'Fracc. La Lejona 2da Sección',
                                      'lat': 20.897708,
                                      'lon': -100.752716,
                                      'tel': '01 800 3777 333',
                                      'cp': '37765',
                                      'municipio': 'San Miguel Allende'
                                      },

                           'comer8': {'direccion': 'AV DE LAS TORRES 446',
                                      'colonia': 'San José del Olivar',
                                      'lat': 19.334798,
                                      'lon': -99.227121,
                                      'tel': '01 800 3777 333',
                                      'cp': '1770',
                                      'municipio': 'Álvaro Obregón'
                                      },

                           'comer9': {'direccion': 'AV MAGNOCENTRO LT 1 MZ 2',
                                      'colonia': 'San Fernando Huixquilucan',
                                      'lat': 19.399401,
                                      'lon': -99.276681,
                                      'tel': '01 800 3777 333',
                                      'cp': '52796',
                                      'municipio': 'Huixquilucan'
                                      },

                           'comer10': {'direccion': 'XOCHIMILCO 343',
                                       'colonia': 'Anahuac',
                                       'lat': 19.438072,
                                       'lon': -99.179588,
                                       'tel': '01 800 3777 333',
                                       'cp': '11320',
                                       'municipio': 'Miguel Hidalgo'
                                       },

                           'comer11': {'direccion': 'BOSQUES DE MOCTEZUMA 1B',
                                       'colonia': 'Fracc. La Herradura',
                                       'lat': 19.416958,
                                       'lon': -99.249047,
                                       'tel': '01 800 3777 333',
                                       'cp': '53920',
                                       'municipio': 'Huixquilucan'
                                       },

                           'comer12': {'direccion': 'CALZ ERMITA IZTAPALAPA 3865',
                                       'colonia': 'Santa María Aztahuacán',
                                       'lat': 19.351905,
                                       'lon': -99.012747,
                                       'tel': '01 800 3777 333',
                                       'cp': '9730',
                                       'municipio': 'Iztapalapa'
                                       },

                           'comer13': {'direccion': 'PERPETUA 35',
                                       'colonia': 'San José Insurgentes',
                                       'lat': 19.366372,
                                       'lon': -99.182357,
                                       'tel': '01 800 3777 333',
                                       'cp': '3900',
                                       'municipio': 'Benito Juárez'
                                       },

                           'comer14': {'direccion': 'MIGUEL ANGEL DE QUEVEDO 443',
                                       'colonia': 'Romero de Terreros',
                                       'lat': 19.345040,
                                       'lon': -99.171795,
                                       'tel': '01 800 3777 333',
                                       'cp': '4310',
                                       'municipio': 'Coyoacán'
                                       },

                           'comer15': {'direccion': 'BOSQUE DE ARRAYAN MZ 5 LT 1',
                                       'colonia': 'Fracc. Conjunto Urbano Bosque Esmeralda',
                                       'lat': 19.548925,
                                       'lon': -99.287349,
                                       'tel': '01 800 3777 333',
                                       'cp': '52973',
                                       'municipio': 'Atizapán de Zaragoza'
                                       },

                           'comer16': {'direccion': 'AV DE LAS FUENTES 190',
                                       'colonia': 'Lomas de Tecamachalco',
                                       'lat': 19.421845,
                                       'lon': -99.237988,
                                       'tel': '01 800 3777 333',
                                       'cp': '53950',
                                       'municipio': 'Naucalpán de Juárez'
                                       },

                           'comer17': {'direccion': 'PROLONGACION BOSQUES DE REFORMA 1813',
                                       'colonia': 'Vista Hermosa',
                                       'lat': 19.382919,
                                       'lon': -99.267804,
                                       'tel': '01 800 3777 333',
                                       'cp': '5109',
                                       'municipio': 'Cuajimalpa'
                                       },

                           'comer18': {'direccion': 'AV. JESUS DEL MONTE 271',
                                       'colonia': 'Jesús del Monte',
                                       'lat': 19.388758,
                                       'lon': -99.293395,
                                       'tel': '01 800 3777 333',
                                       'cp': '52764',
                                       'municipio': 'Huixquilucan'
                                       },

                           'comer19': {'direccion': 'AV. MIGUEL ANGEL DE QUEVEDO 1144',
                                       'colonia': 'Parque San Andrés',
                                       'lat': 19.342817,
                                       'lon': -99.146703,
                                       'tel': 'Sin Datos',
                                       'cp': '4040',
                                       'municipio': 'Coyoacan'
                                       },

                           'comer20': {'direccion': 'AV. DEL CARMEN 335',
                                       'colonia': 'Fracc. Avandaro',
                                       'lat': 19.164580,
                                       'lon': -100.125154,
                                       'tel': 'Sin Datos',
                                       'cp': '51200',
                                       'municipio': 'Valle de Bravo'
                                       },
                           }

        for keys, values in self.datoscomer.items():
            for vkeys, vvalues in values.items():
                if vkeys == 'direccion':
                    dir = vvalues

                if vkeys == 'colonia':
                    col = vvalues

                if vkeys == 'tel':
                    tel = vvalues

                if vkeys == 'cp':
                    cp = vvalues

                if vkeys == 'municipio':
                    mun = vvalues

                if vkeys == 'lat':
                    nlat = vvalues
                    # print("lat: "+str(nlat))

                if vkeys == 'lon':
                    nlon = vvalues
                    # print("lon: "+str(nlon))

            print("lat: " + str(nlat) + " lon: " + str(nlon))

            cadena_final = f'Dir: {dir}\nCol: {col}\nCP: {cp}\nMun: {mun}\nTel: {tel}\n\n'

            #self.layer.add_marker(lon=nlon, lat=nlat, source= "imagenes/pinazul.png")


            self.marcador = MapMarkerPopup(lat=nlat, lon=nlon, source= "imagenes/pinverde.png")
            # self.marcador.add_widget(MDIconButton(icon="information", on_release= lambda *args: self.info_che(*args)))
            self.marcador.add_widget(MDLabel(size_hint=(5, .5), text=cadena_final))

            self.mapview.add_marker(self.marcador)

            print(self.marcador)  # da una direccion diferrente, desde aqui se tiene que hacer de alguna forma

    def dialog_close(self, *args): # Cierra el dialog del boton ayuda
        print("Estoy en cerrar dialog")
        self.dialog.dismiss()

    def BorraMarcador(self): #ver esta funcion pendiente
        print("Borrando marcador")
        self.mapview.remove_marker(self.marcador)

    def on_pre_enter(self, *args):
        self.app.title = "Mapa Comercios"
