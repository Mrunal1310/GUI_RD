# customtkinter library 
import customtkinter as ctk
from PIL import Image

# Set appearance mode to "white"
ctk.set_appearance_mode("white")

# Disply of Sclect alarm Window
select_alarm = ctk.CTk()
select_alarm.title("Select alarm")
select_alarm.geometry("1200x800")
select_alarm.config(bg="white")

# Close Button
# Function to close the label
def close_label():
    select_alarm.destroy()

# Create a frame to hold the label and the close button
select_frame = ctk.CTkFrame(select_alarm)
select_frame.grid(row=0)

# Create the label
select_lbl=ctk.CTkLabel(select_frame, text="Select alarm",width=1200, text_color="white",font=("aerial", 20, 'bold'), fg_color="#A83232",)
select_lbl.grid(row=0, column=0, columnspan=3, sticky='e')

# Create the close button
close_button = ctk.CTkButton(select_frame, text="X", width=30,text_color='white', fg_color='red', corner_radius=0, font=("aerial", 15), command=close_label)
close_button.columnconfigure(3, weight=0)
close_button.grid(row=0, columnspan=3, sticky='e')

# Configure the grid column weights
select_alarm.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row weights
select_alarm.rowconfigure((0, 3), weight=1)
select_alarm.rowconfigure(1, weight=0)

## Create OFF Button
off_butn = ctk.CTkButton(select_alarm, anchor= "center", text = "OFF", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_butn.grid(row=1,column=0, padx=10, pady=10,)

# Create Built in buzzer Button
buzzer_butn = ctk.CTkButton(select_alarm, anchor= "center", text = "Built in buzzer",  corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
buzzer_butn.grid(row=2,column=0, padx=10, pady=10, sticky='n')

# Create External alarm Button
ext_alarm_butn = ctk.CTkButton(select_alarm, anchor= "center", text = "External alarm", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
ext_alarm_butn.grid(row=3,column=0, padx=10, pady=10, sticky='n')

# End loop of Sclect alarm Window
select_alarm.mainloop()

