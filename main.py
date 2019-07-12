
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
from kivy.uix.image import Image




class Dashboard(Screen):
    def __init__ (self, **kwargs):
        super ().__init__(**kwargs)
        self.json_data = None
        self.parse_dashboard()


    def request(self, city):
        # REQUEST URL 
        request_url= 'https://api.openweathermap.org/data/2.5/weather?q={},ru&units=metric&appid=55ce897ca94456cf36a07274c8c2bc4c'.format(city)
        # SEND REQUEST AND TRANSLATE RESPONSE INTO JSON
        json_data = requests.get(request_url).json()
        # RETURN JSON
        return json_data


    def find_city_weather(self, isinstance):
        self.json_data = self.request(self.city_input.text)
        my_screenmanager.add_widget( Weather( name='screen2' ) )
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

        json = my_screenmanager.get_screen('screen1').json_data
        #picture_url = "http://openweathermap.org/img/w/{}.png".format( json['weather'][0]['icon'] )

        print('JSON: ',  json)
        #print('PICS: ', picture_url)

        al = AnchorLayout()
        bl = BoxLayout( orientation = 'vertical', size_hint = [None, None], size = [300, 200] )

        if json == None:
            bl.add_widget( Label( text = "{}".format( 'Данных нет') ) )
        else:
            #bl.add_widget( Image( source = picture_url, size_hint_y = None ) )
            bl.add_widget( Label( text = "{}".format( json['name'] ) ) )
            bl.add_widget( Label( text = "Температура: макс. - {}, мин. - {}".format( json['main']['temp'], json['main']['temp_min'] ) ) )
            bl.add_widget( Label( text = "Погода: main - {}, details - {}".format( json['weather'][0]['main'], json['weather'][0]['description'] ) ) )
            bl.add_widget( Label( text = "Облачность: {}%".format( json['clouds']['all'] ) ) )
            bl.add_widget( Label( text = "Скорость ветра: {}".format( json['wind']['speed'] ) ) )

        city_button = Button( text='Назад' )
        city_button.bind( on_press=self.changer )

        bl.add_widget( city_button )

        al.add_widget( bl )

        return self.add_widget(al)

    def changer(self, *args):
        my_screenmanager.current = 'screen1'
        my_screenmanager.remove_widget(self)




my_screenmanager = ScreenManager()
my_screenmanager.add_widget( Dashboard( name='screen1' ) )


class WeatherApp(App):

    def build(self):
        return my_screenmanager



if __name__ == '__main__':
    WeatherApp().run()



# TODO: collect weather from most popular resurses and parse all with final sum of all datas 
# TODO: search is half done , need to add more city select variants