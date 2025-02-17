import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os

root = ctk.CTk()
root.title('Window')
root.geometry('900x600')
root.resizable(False, False)
root._set_appearance_mode('dark')

load_dotenv('.env')
api_key = os.getenv('my_api_key')

def weather_script():
    city = save_text.get()
    params = {
        'q': city,
        'appid': api_key
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']

        weather_label.configure(text=f'Weather description: {weather}\nTemperature: {temperature - 273.15:.2f}')
    else:
        weather_label.configure(text=f'Error: status code response {response.status_code}')

frame = ctk.CTkFrame(root, fg_color='#2C2C2C', bg_color='#2C2C2C', height=600, width=250)
frame.place(x=0, y=0)

label = ctk.CTkLabel(root, text='Weather API', fg_color='#2C2C2C', bg_color='#2C2C2C', text_color='white',
                     width=60, height=30, font=('Helvetica', 26, 'bold'), anchor='center')
label.place(x=40, y=45)
label2 = ctk.CTkLabel(root, text='made by neverappealed', fg_color='#2C2C2C', bg_color='#2C2C2C', anchor='center',
                      text_color='white', font=('Helvetica', 14, 'bold'), height=10, width=60)
label2.place(x=34, y=85)

save_text = ctk.StringVar()
city_entry = ctk.CTkEntry(root, placeholder_text='Enter here your city', width=300, height=40, font=('Arial', 17),
                          textvariable=save_text, bg_color='gray', fg_color='gray', text_color='white', corner_radius=5,
                          border_width=4, placeholder_text_color='white')
city_entry.place(y=260, x=410)
weather_button = ctk.CTkButton(root, text='Show weather', width=140, height=35, bg_color='#1C4AA8',
                                font=('Helvetica', 16, 'italic'), fg_color='#1C4AA8', command=weather_script)
weather_button.place(x=488, y=330)
weather_frame = ctk.CTkFrame(root, width=300, height=80, fg_color='gray', bg_color='gray')
weather_frame.place(x=410, y=150)
weather_label = ctk.CTkLabel(root, text='There will be weather', text_color='black', fg_color='gray', bg_color='gray',
                             font=('Helvetica', 16, 'bold'), anchor='center')
weather_label.place(x=410, y=156)

root.mainloop()