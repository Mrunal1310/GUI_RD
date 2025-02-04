# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of DPI Screen Window
dpi_wnd=ctk.CTk()
dpi_wnd.title("DPI")
dpi_wnd.geometry("1200x800")
dpi_wnd.config(bg="white")

# Configure the grid column weights of DPI window
dpi_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of DPI window
dpi_wnd.rowconfigure((0), weight=1)
dpi_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    dpi_wnd.destroy()

# Frame for DPI  Title
frame1=ctk.CTkFrame(dpi_wnd, bg_color="#CC0000", fg_color="#A83232")

# Configure the grid column for title frame
frame1.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row for title frame
frame1.rowconfigure(0, weight=0)

# Icon for close button
image_close=ctk.CTkImage(dark_image=Image.open("close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
close_button.grid(row=0, column=2, sticky='e')

# Grid of frame weight
frame1.grid(row=0, column=0,columnspan=3, sticky="new")

# Label for Print sound title
label1=ctk.CTkLabel(frame1, text="DPI",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(dpi_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4), weight=1)

# 300*300 Button
value01_button=ctk.CTkButton(frame2, text = "300*300", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value01_button.grid(row=0, column=0,padx=40, pady=15,)

# 300*150 Button
value02_button=ctk.CTkButton(frame2,text = "300*150",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value02_button.grid(row=1, column=0,padx=40, pady=15)

# 300*100 Button
value03_button=ctk.CTkButton(frame2, text = "300*100", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value03_button.grid(row=2, column=0,padx=40, pady=15,)


# 150*300 Button
value11_button=ctk.CTkButton(frame2, text = "150*300", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value11_button.grid(row=0, column=1, padx=40, pady=15)

# 150*150 Button
value12_button=ctk.CTkButton(frame2,text = "150*150",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value12_button.grid(row=1, column=1, padx=40, pady=15)

# 150*100  Button
value13_button=ctk.CTkButton(frame2, text = "150*100", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
value13_button.grid(row=2, column=1, padx=40, pady=15)

# End loop of DPI window
dpi_wnd.mainloop()
