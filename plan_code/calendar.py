# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Calendar Window
calendar_wnd=ctk.CTk()
calendar_wnd.title("Calendar")
calendar_wnd.geometry("1200x800")
calendar_wnd.config(bg="white")

# Configure the grid column weights of Calendar window
calendar_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Calendar window
calendar_wnd.rowconfigure((0), weight=1)
calendar_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    calendar_wnd.destroy()

# Frame for Calendar Title
frame1=ctk.CTkFrame(calendar_wnd, bg_color="#A83232", fg_color="#A83232")

# Configure the grid column for title frame
frame1.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row for title frame
frame1.rowconfigure(0, weight=0)

# Icon for close button
image_close=ctk.CTkImage(dark_image=Image.open("close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
close_button.grid(row=0, column=2, sticky='e')

# Grid of frame weight
frame1.grid(row=0, column=0,columnspan=3, sticky="new")

# Label for Calendar title
label1=ctk.CTkLabel(frame1, text="Calendar",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(calendar_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2), weight=1)

# Gregorian calendar Button
gregorian_button=ctk.CTkButton(frame2,text = "Gregorian calendar",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
gregorian_button.grid(row=0, column=1,padx=40, pady=15)

# Jalali date Button
jalali_date_button=ctk.CTkButton(frame2, text = "Jalali date", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
jalali_date_button.grid(row=1, column=1,padx=40, pady=15,)

# Islamic calendar Button
islamic_calendar_button=ctk.CTkButton(frame2, text = "Islamic calendar", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
islamic_calendar_button.grid(row=2, column=1, padx=40, pady=15)

# End loop of Calendar window
calendar_wnd.mainloop()
