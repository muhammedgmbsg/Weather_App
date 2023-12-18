from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'eee09825e47108d8bf6e9a0405a74515'
icon_url = 'https://openweathermap.org/img/wn/{}@2x.png'
app = Tk()
app.geometry = ("450 x 500")

app.title('Hava Durumu')


def getWeather(city):
    params = {'q': city, 'appid': api_key, 'lang': 'tr'}
    data = requests.get(url, params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        contidion = data['weather'][0]['description']
        return (city, country, temp, icon, contidion)


def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]), stream=True).raw))
        iconlabel.configure(image=icon)
        iconlabel.image = icon


cityEntry = Entry(app, justify='center', font=('Arial'))
cityEntry.pack(fill=BOTH, ipady=10, padx=20, pady=5)
cityEntry.focus()

searchButton = Button(app, text='Arama', font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=18)

iconlabel = Label(app)
iconlabel.pack()

locationLabel = Label(app, font=('Arial', 40))
locationLabel.pack()

tempLabel = Label(app, font=('Arial', 50, 'bold'))
tempLabel.pack()

conditionLabel = Label(app, font=('Arial', 20))
conditionLabel.pack()

app.mainloop()