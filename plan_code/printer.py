# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Printer Window
printer_wnd=ctk.CTk()
printer_wnd.title("Printer")
printer_wnd.geometry("1200x800")
printer_wnd.config(bg="white")

# Configure the grid column weights of Printer window
printer_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Printer window
printer_wnd.rowconfigure((0), weight=1)
printer_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    printer_wnd.destroy()

# Frame for Printer Title
frame1=ctk.CTkFrame(printer_wnd, bg_color="#A83232", fg_color="#A83232")

# Configure the grid column for title frame
frame1.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row for title frame
frame1.rowconfigure(0, weight=0)

# Icon for close button
image_close=ctk.CTkImage(dark_image=Image.open("N1/close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
close_button.grid(row=0, column=2, sticky='e')

# Grid of frame weight
frame1.grid(row=0, column=0,columnspan=3, sticky="new")

# Label for Printer title
label1=ctk.CTkLabel(frame1, text="Printer",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(printer_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2), weight=1)

# Right Button
right_button=ctk.CTkButton(frame2,text = "Right",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
right_button.grid(row=0, column=1,padx=40, pady=15)

# Left Button
left_button=ctk.CTkButton(frame2, text = "Left", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
left_button.grid(row=1, column=1,padx=40, pady=15,)

# Both print Button
both_print_button=ctk.CTkButton(frame2, text = "Both print", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
both_print_button.grid(row=2, column=1, padx=40, pady=15)

# End loop of printer window
printer_wnd.mainloop()
