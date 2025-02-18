import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os
import time

root = ctk.CTk()
root.title('Window')
root.geometry('900x600')
root.resizable(False, False)
root._set_appearance_mode('dark')

load_dotenv('.env')
api_key = os.getenv('my_api_key')

params = {}

def weather_script():
    city = save_text.get()
    global params
    params['q'] = city
    params['appid'] = api_key

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']

        weather_label.configure(text=f'Weather description: {weather}\nTemperature: {temperature - 273.15:.2f}')
    else:
        weather_label.configure(text=f'Error: status code response {response.status_code}')

def set_api_key():
    get_api = save_api.get()
    global params
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params={'appid': get_api})
    
    if response.status_code == 400:
        params['appid'] = get_api
        api_button.configure(border_color='#13A310')
    else:
        api_button.configure(border_color='#B01111')

frame = ctk.CTkFrame(root, fg_color='#2C2C2C', bg_color='#2C2C2C', height=600, width=250)
frame.place(x=0, y=0)

label = ctk.CTkLabel(root, text='Weather API', fg_color='#2C2C2C', bg_color='#2C2C2C', text_color='white',
                     width=60, height=30, font=('Helvetica', 26, 'bold'), anchor='center')
label.place(x=40, y=45)
label2 = ctk.CTkLabel(root, text='made by neverappealed', fg_color='#2C2C2C', bg_color='#2C2C2C', anchor='center',
                      text_color='white', font=('Helvetica', 14, 'bold'), height=10, width=60)
label2.place(x=34, y=85)

save_text = ctk.StringVar()
city_entry = ctk.CTkEntry(root, placeholder_text='Enter here your city', width=300, height=40, font=('Helvetica', 17),
                          textvariable=save_text, bg_color='#242424', fg_color='gray', text_color='white', corner_radius=5,
                          border_width=4, placeholder_text_color='white')
city_entry.place(y=260, x=410)
weather_button = ctk.CTkButton(root, text='Show weather', width=140, height=35, bg_color='#242424',
                                font=('Helvetica', 16, 'italic'), fg_color='#242424', corner_radius=20, border_width=2,
                                command=weather_script, border_color='#1258E2', hover_color='#121212')
weather_button.place(x=488, y=330)
weather_frame = ctk.CTkFrame(root, width=300, height=80, fg_color='gray', bg_color='#242424', corner_radius=20)
weather_frame.place(x=410, y=150)
weather_label = ctk.CTkLabel(root, text='There will be weather', text_color='black', fg_color='gray', bg_color='gray',
                             font=('Helvetica', 16, 'bold'), anchor='center')
weather_label.place(x=420, y=170)
settings_label = ctk.CTkLabel(root, text='Settings', font=('Helvetica', 24, 'bold'), width=35, height=50,
                               bg_color='#2C2C2C', fg_color='#2C2C2C', text_color='white', anchor='center')
settings_label.place(x=67, y=190)
save_api = ctk.StringVar()
api_entry = ctk.CTkEntry(root, placeholder_text='Api key', bg_color='#2C2C2C', width=200, height=32, border_width=1,
                         corner_radius=10, font=('Helvetica', 17), border_color='black', textvariable=save_api)
api_entry.place(x=25, y=270)
api_button = ctk.CTkButton(root, text='Save key', width=100, height=28, bg_color='#2C2C2C', hover_color='#121212',
                            font=('Helvetica', 16, 'italic'), fg_color='#2C2C2C', border_width=2, border_color='white',
                            command=set_api_key)
api_button.place(x=71, y=322)

root.mainloop()