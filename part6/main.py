from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        # Initialize GPS
        GpsHelper().run()

        # Connect to database
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

MainApp().run()
