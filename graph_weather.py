import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os

root = ctk.CTk()
root.title('Weather Api Soft')
root.geometry('850x600')
root.resizable(False, False)

load_dotenv('.env')
api_key = os.getenv('my_api_key')
print(api_key)


root.mainloop()