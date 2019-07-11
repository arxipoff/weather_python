
# IMPORT REQUESTS
import requests
# IMPORT KIVY
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class Dashboard(Screen):
    def __init__ (self, **kwargs):
        super ().__init__(**kwargs)
        self.parse_dashboard()


    def request(self, city):
        # REQUEST URL 
        request_url= 'https://api.openweathermap.org/data/2.5/weather?q={},ru&units=metric&appid=55ce897ca94456cf36a07274c8c2bc4c'.format(city)
        # SEND REQUEST AND TRANSLATE RESPONSE INTO JSON
        json_data = requests.get(request_url).json()
        # RETURN JSON
        return json_data


    def find_city_weather(self, isinstance):
        #self.json_data = self.request(self.city_input.text)
        self.changer()


    # PARSE DASHBOARD
    def parse_dashboard(self):
        al = AnchorLayout()
        bl = BoxLayout( orientation = 'vertical', size_hint = [None, None], size = [300, 100] )

        city_input_label = Label(text='Введите название города: ')
        self.city_input = TextInput(text='')
        city_button = Button(text='Найти')
        city_button.bind(on_press=self.find_city_weather)

        bl.add_widget(city_input_label)
        bl.add_widget(self.city_input)
        bl.add_widget(city_button)

        al.add_widget( bl )

        return self.add_widget(al)


    def changer(self, *args):
        my_screenmanager.current = 'screen2'



class Weather(Screen):
    def __init__(self, **kwargs):
        super ().__init__(**kwargs)
        self.parse_weather()

    def parse_weather(self):

        # print(my_screenmanager.get_screen('screen1'))

        al = AnchorLayout()
        bl = BoxLayout( orientation = 'vertical', size_hint = [None, None], size = [300, 200] )

        # bl.add_widget( Label( text = "{}".format( json['name'] ) ) )
        # bl.add_widget( Label( text = "Температура: макс. - {}, мин. - {}".format( json['main']['temp'], json['main']['temp_min'] ) ) )
        # bl.add_widget( Label( text = "Погода: main - {}, details - {}".format( json['weather'][0]['main'], json['weather'][0]['description'] ) ) )
        # bl.add_widget( Label( text = "Скорость ветра: {}".format( json['wind']['speed'] ) ) )

        city_button = Button( text='Назад' )
        city_button.bind( on_press=self.changer )

        bl.add_widget( city_button )

        al.add_widget( bl )

        return self.add_widget(al)

    def changer(self, *args):
        my_screenmanager.current = 'screen1'




my_screenmanager = ScreenManager()


class WeatherApp(App):

    def build(self):
        my_screenmanager.add_widget( Dashboard( name='screen1' ) )
        my_screenmanager.add_widget( Weather( name='screen2' ) )

        return my_screenmanager



if __name__ == '__main__':
    WeatherApp().run()

