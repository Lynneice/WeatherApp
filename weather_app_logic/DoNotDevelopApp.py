#
import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

 
# 2c3dac551108575d2ef561d56a8f345a
# api.openweathermap.org/data/2.5/forecast?q={city name},{state},{country code}&appid={your api key}
#or you can use api.openweathermap.org/data/2.5/weather  for current weather

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
    
        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information.'
    return final_str


def get_weather(city):
    weather_key= '2c3dac551108575d2ef561d56a8f345a'
    url='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url,params=params)
    weather = response.json()
 
    
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
    
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH )
canvas.pack()


background_image = tk.PhotoImage(file='lilypads.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relheight=1, relwidth=1)


"""using the place method is a geometry manager that organizes widgets 
in a table-like structure within the parent widget. relx=0.1 (relative x set to 10%
will add padding to either side on the x axis)
"""
frame = tk.Frame(root, bg = '#ABDEDC', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth =0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", font=40, bg = '#8A9797', fg = '#ABC7DE', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3 )



lower_frame = tk.Frame(root, bg='#ABDEDC', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg= 'white', font =("Arial", 20), anchor='nw', justify = 'left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()