import tkinter
from tkinter import *
import requests
from tkinter import messagebox

# window

root = tkinter.Tk()
root.geometry('440x300')
root.title("Weather App")


# LABEL AND ENTRY

city_label = tkinter.Label(root, text="Enter city", font=("Arial", 20))
city_label.place(x=165, y=15)
city_entry = tkinter.Entry(root)
city_entry.place(x=170, y=65)
weather_label = tkinter.Label(root, text="")
weather_label.place(x=177, y=155)

# BUTTON

my_button = tkinter.Button(root, text="Show", height=2, width=11)
my_button.place(x=185, y=100)

# FONKSİYON

def funch_weather():
    city = city_entry.get()
    api_key = "fff06b9b99fb33f2871cbfe442c2347c"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"

    try:
        response = requests.get(url, params={'q': city, 'units': 'metric'})
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to retrieve weather data")

my_button.config( command= funch_weather)

root.mainloop()


