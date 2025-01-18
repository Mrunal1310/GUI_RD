# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Print sound Window
print_sound_wnd=ctk.CTk()
print_sound_wnd.title("Print sound")
print_sound_wnd.geometry("1200x800")
print_sound_wnd.config(bg="white")

# Configure the grid column weights of Print sound window
print_sound_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Print sound window
print_sound_wnd.rowconfigure((0), weight=1)
print_sound_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    print_sound_wnd.destroy()
    
def check_label():
    pass

# Frame for of Print sound window Title
frame1=ctk.CTkFrame(print_sound_wnd, bg_color="#A83232", fg_color="#A83232")

# Configure the grid column for title frame
frame1.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row for title frame
frame1.rowconfigure(0, weight=0)


# Icon for close button
image_close=ctk.CTkImage(dark_image=Image.open("close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
close_button.grid(row=0, column=2,padx=10, sticky='e')

image_check=ctk.CTkImage(dark_image=Image.open("checked.png"))
check_button = ctk.CTkButton(frame1, command=check_label, text="", image=image_check, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
check_button.grid(row=0, column=2,padx=50, sticky='e')

# Grid of frame weight
frame1.grid(row=0, column=0,columnspan=3, sticky="new")

# Label for Print sound title
label1=ctk.CTkLabel(frame1, text="Print sound",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1,padx=100, pady=5, sticky="new")

# Frame for buttons 
frame2=ctk.CTkFrame(print_sound_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4), weight=1)

# OFF Button
off_button=ctk.CTkButton(frame2, text = "OFF", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_button.grid(row=0, column=1,padx=50, pady=15,)

# Start only Button
value1_button=ctk.CTkButton(frame2,text = "Start only",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value1_button.grid(row=1, column=1,padx=50, pady=15)

# Complete only Button
value2_button=ctk.CTkButton(frame2, text = "Complete only", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value2_button.grid(row=2, column=1,padx=50, pady=15,)


# Start to finish Button
value3_button=ctk.CTkButton(frame2, text = "Start to finish", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value3_button.grid(row=3, column=1, padx=50, pady=15)

value3_button=ctk.CTkButton(frame2, text = "",fg_color="white")
value3_button.grid(row=4, column=2, padx=50, pady=15)

# Function for checkbox
def on_checkbox_change():
    pass  # Do nothing when the checkbox state changes

# Create a checkbox
checkbox = ctk.CTkCheckBox(frame2, text="External alarm", text_color= "black", font=("aerial", 25,), bg_color="white", command=on_checkbox_change)
checkbox.grid(row=4, column=0, padx=10, pady=15, sticky="e")


# End loop of of Print sound window
print_sound_wnd.mainloop()
