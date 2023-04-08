import requests

"""try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=20.5937&lon=78.9629&appid=2cde541ca9e19d3b0ec3031eb1739729")

except:

    print("No Internet :(")

response_json = response.json()

temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"]

print(f"In India it is currently {temp}° C")
print(f"Today's High: {temp_max}° C")
print(f"Today's Low: {temp_min}° C")"""

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self) :
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon }&appid=2cde541ca9e19d3b0ec3031eb1739729")

        except:

            print("No Internet :( ")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"

        print(f"In India it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")

my_city = City("India", 20.5937, 78.9629)
my_city.temp_print()

vacation_city = City("puerto rico", 18.2208, -66.5901, units="imperial")
vacation_city.temp_print()
print(vacation_city.response_json)
