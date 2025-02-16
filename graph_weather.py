import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os

root = ctk.CTk()
root.title('Weather Api Soft')
root.geometry('900x600')
root.resizable(False, False)
root._set_appearance_mode('dark')

load_dotenv('.env')
api_key = os.getenv('my_api_key')

frame = ctk.CTkFrame(root, fg_color='gray', width=150, height=40, bg_color='gray')
frame.place(x=410, y=75)
frame2 = ctk.CTkFrame(root, fg_color='gray', width=150, height=40, bg_color='gray')
frame2.place(x=330, y=75)

label = ctk.CTkLabel(root, text='This is Api Weather GUI', bg_color='gray', width=130, height=40,
                      font=('Helvetica', 17, 'bold'), anchor='center', text_color='#00A3FF')
label.place(x=350, y=75)

save_text = ctk.StringVar()
city_entry = ctk.CTkEntry(root, placeholder_text='Enter here your city', width=300, height=40, font=('Arial', 17),
                          textvariable=save_text, bg_color='gray', fg_color='gray', text_color='white', corner_radius=5,
                          border_width=4, placeholder_text_color='white')
city_entry.place(y=230, x=300)



root.mainloop()