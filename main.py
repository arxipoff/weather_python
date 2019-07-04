# IMPORT REQUESTS
import requests
# IMPORT KIVY
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout



class WeatherApp(App):
    # CALL WEATHER API AND RETURN JSON
    def call_weather_api(self):
        url_by_city = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&units=metric&appid=55ce897ca94456cf36a07274c8c2bc4c'

        # lat = None
        # lon = None
        # url_by_coordinates = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}?lon={lon}&appid=55ce897ca94456cf36a07274c8c2bc4c'

        json_data = requests.get(url_by_city).json()
        return json_data

    def parse_weather_json(self):
        json = self.call_weather_api()
        
        parsed_json = dict()

        parsed_json['city'] = json['name']
        parsed_json['max_temp'] = json['main']['temp']
        parsed_json['min_temp'] = json['main']['temp_min']
        parsed_json['overhead_main'] = json['weather'][0]['main']
        parsed_json['overhead_description'] = json['weather'][0]['description']
        parsed_json['wind_speed'] = json['wind']['speed']
        parsed_json['sunrise'] = json['sys']['sunrise']
        parsed_json['sunset'] = json['sys']['sunset']

        return parsed_json


    # PARSE WEATHER 
    def parse_weather(self):
        al = AnchorLayout()
        bl = BoxLayout( orientation = 'vertical', size_hint = [None, None], size = [300, 200] )

        json = self.parse_weather_json()

        bl.add_widget( Label( text = "WEATHER APP", font_size = '20' ) )
        bl.add_widget( Label( text = "City: {}".format( json['city'] ) ) )
        bl.add_widget( Label( text = "Temperature: max - {}, min - {}".format( json['max_temp'], json['min_temp'] ) ) )
        bl.add_widget( Label( text = "Overhead: main - {}, details - {}".format( json['overhead_main'], json['overhead_description'] ) ) )
        bl.add_widget( Label( text = "Wind: {}".format( json['wind_speed'] ) ) )
        bl.add_widget( Label( text = "Sunrise: {}, Sunset: {}".format( json['sunrise'], json['sunset'] ) ) )

        al.add_widget( bl )

        return al

    # BUILD APP
    def build(self):
        return self.parse_weather()

if __name__ == "__main__":
    # RUN APP
    WeatherApp().run()