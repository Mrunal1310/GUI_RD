# customtkinter library 
import customtkinter as ctk
from PIL import Image


# Set appearance mode to "dark"
ctk.set_appearance_mode("white")

# Function for date and time
def date_time():
    pass

# Disply of Home Screen Window
home_screen = ctk.CTk()
home_screen.title("Home Screen")
home_screen.geometry("1200x800")
home_screen.maxsize(1200, 600)
home_screen.minsize(800, 600)
home_screen.config(bg="blue")

# Version of Printern
label = ctk.CTkLabel(home_screen, text = "V15.8.9", text_color="white", bg_color="blue")
label.columnconfigure(3, weight=0)
label.rowconfigure(3, weight=0)
label.grid(row=3, column=4, sticky='se')

# Print Button Function
def print_butn():
    pass

# Create Print Button
print_image = ctk.CTkImage(dark_image=Image.open("basic/gui/print_icon.png"), size=(45,45))
print_butn = ctk.CTkButton(home_screen, image=print_image, compound="top", anchor= "center", text = "Print", width=90, height=120, corner_radius=10, fg_color="#87CEFF", bg_color="blue", hover_color="pink", text_color= "white", command= print_butn, font=("aerial", 15, 'bold'))
print_butn.grid(row=0,column=1, padx=10, pady=10)

# File Button Function
def file_butn():
    pass

# Create File Button
file_image = ctk.CTkImage(dark_image=Image.open("basic/gui/files_icon.png"), size=(40,40))
file_butn = ctk.CTkButton(home_screen, image=file_image, compound="top", text = "File", width=90, height=120, corner_radius=10, fg_color="#5CACEE", bg_color="blue", hover_color="pink", text_color= "white", command= file_butn, font=("aerial", 15, 'bold'))
file_butn.grid(row=0, column =2, padx=10, pady=10)

# Edit Button Function
def edit_butn():
    pass

# Create Edit Button
edit_image = ctk.CTkImage(light_image=Image.open("basic/gui/edit_icon.png"), size=(40,40))
edit_butn = ctk.CTkButton(home_screen, image=edit_image, compound="top", text = "Edit", width=90, height=120, corner_radius=10, fg_color="#EE3B3B", bg_color="blue", hover_color="pink", text_color= "white", command= edit_butn, font=("aerial", 15, 'bold'))
edit_butn.grid(row=0, column =3, padx=10, pady=10)

# Setting Button Function
def setting_butn():
    pass

# Create Setting Button
setting_image = ctk.CTkImage(light_image=Image.open("basic/gui/setting_icon.png"), size=(40,40))
setting_butn = ctk.CTkButton(home_screen, image=setting_image, compound="top", text="Setting", width=90, height=120, corner_radius=10, fg_color="#B452CD", bg_color="blue", hover_color="pink", text_color= "white", command= setting_butn, font=("aerial", 15, 'bold'))
setting_butn.grid(row=0, column =4, padx=10, pady=10, sticky='w')

# Configure the grid column weights
home_screen.columnconfigure((0, 4), weight=1)
home_screen.columnconfigure((1,2,3), weight=0)

# Configure the grid row weights
home_screen.rowconfigure(0, weight=1)

# End loop of Home Screen Window
home_screen.mainloop()
