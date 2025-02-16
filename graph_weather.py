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
city_entry.place(y=200, x=410)
weather_button = ctk.CTkButton(root, text='Show weather', width=140, height=35, bg_color='gray', font=('Helvetica', 15))
weather_button.place(x=488, y=270)



root.mainloop()