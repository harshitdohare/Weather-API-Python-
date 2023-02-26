# Pyhton Project on Weather Application using API by Harshit Dohare

# importing libraries
from tkinter import *
import requests
import json
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import datetime
import pytz
from PIL import ImageTk, Image

# Structure of GUI
root = Tk()
root.title("Weather App Using Python")
root.geometry("660x550")
root['background'] = "light green"

# Dates
geolocator = Nominatim(user_agent="geoapiExercises")
lad = 'Japan'
location = geolocator.geocode(lad)

obj = TimezoneFinder()
result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
dt = datetime.datetime.now(pytz.timezone(result))

lable_date = Label(root, text="Date :", width=0,
                   bg='light green', font=("bold", 15))
lable_date.place(x=30, y=130)
date = Label(root, text=dt.strftime('%d'), bg='light green', font=("bold", 15))
date.place(x=100, y=130)
month = Label(root, text=dt.strftime('-%m-'), bg='light green', font=("bold", 15))
month.place(x=125, y=130)
year = Label(root, text=dt.strftime('%Y'), bg='light green', font=("bold", 15))
year.place(x=165, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p %Z    %A'),
             bg='light green', font=("bold", 15))
hour.place(x=30, y=160)

# Theme for the respective time the application is used
if int((dt.strftime('%H'))) >= 19 or int((dt.strftime('%H'))) <= 5:
    img = ImageTk.PhotoImage(Image.open('moon.png'))
    panel = Label(root, image=img)
    panel.place(x=320, y=200)
else:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
    panel = Label(root, image=img)
    panel.place(x=320, y=200)

# Searching City
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=35,background='white')
city_entry.grid(row=1, column=4, ipady=8, stick=NE)


def city_name():
    # API Call
    api_key = "" 
    #your API Key
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_entry.get() + "&units=metric&appid=" + api_key)

    api = json.loads(api_request.content)

    # Temperatures
    y = api['main']
    current_temprature = int(y['temp'])
    humidity = y['humidity']
    tempmax = y['temp_max']

    # Coordinates
    x = api['coord']
    longtitude = x['lon']
    latitude = x['lat']

    # Country
    z = api['sys']
    country = z['country']
    citi = api['name']

    # Adding the received info into the screen
    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    lable_lon.configure(text=longtitude)
    lable_lat.configure(text=latitude)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)

# Search Bar and Button
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=20, stick=W + E + N + S)

# Country Names and Coordinates
lable_citi = Label(root, text="...", width=0,
                   bg='light green', font=("bold", 20))
lable_citi.place(x=30, y=63)

lable_country = Label(root, text="...", width=0,
                      bg='light green', font=("bold", 20))
lable_country.place(x=155, y=63)

llon = Label(root, text="Longitude :", width=0, bg='light green', font=("Helvetica", 15))
llon.place(x=30, y=100)
lable_lon = Label(root, text="....", width=0, bg='light green', font=("Helvetica", 15))
lable_lon.place(x=155, y=100)

llat = Label(root, text="Latitude :", width=0, bg='light green', font=("Helvetica", 15))
llat.place(x=265, y=100)
lable_lat = Label(root, text="....", width=0, bg='light green', font=("Helvetica", 15))
lable_lat.place(x=370, y=100)

# Current Temperature

lable_temp = Label(root, text="...", width=0, bg='light green', font=("Helvetica", 110), fg='black')
lable_temp.place(x=38, y=220)

humi = Label(root, text="Humidity : ", width=0, bg='light green', font=("bold", 15))
humi.place(x=23, y=400)

lable_humidity = Label(root, text="...", width=0, bg='light green', font=("bold", 15))
lable_humidity.place(x=127, y=400)

maxi = Label(root, text="Max. Temp.: ", width=0, bg='light green', font=("bold", 15))
maxi.place(x=23, y=430)

max_temp = Label(root, text="...", width=0, bg='light green', font=("bold", 15))
max_temp.place(x=148, y=430)

note = Label(root, text="All temperatures in °C",
             bg='light green', font=("italic", 15))
note.place(x=23, y=460)

root.mainloop()
