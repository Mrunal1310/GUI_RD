# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Print Sound Screen Window
ink_heating_wnd=ctk.CTk()
ink_heating_wnd.title("Ink heating")
ink_heating_wnd.geometry("1200x800")
ink_heating_wnd.config(bg="white")

# Configure the grid column weights of printer window
ink_heating_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights
ink_heating_wnd.rowconfigure((0), weight=1)
ink_heating_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    ink_heating_wnd.destroy()

# Frame for Title
frame1=ctk.CTkFrame(ink_heating_wnd, bg_color="#A83232", fg_color="#A83232")

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
label1=ctk.CTkLabel(frame1, text="Ink heating",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(ink_heating_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4), weight=1)

# Right Button
off_button=ctk.CTkButton(frame2, text = "OFF", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_button.grid(row=0, column=0,padx=40, pady=15,)

# Left Button
c10_button=ctk.CTkButton(frame2,text = "+10°C",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
c10_button.grid(row=1, column=0,padx=40, pady=15)

# Right Button
c20_button=ctk.CTkButton(frame2, text = "+20°C", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
c20_button.grid(row=2, column=0,padx=40, pady=15,)


# Right Button
c50_button=ctk.CTkButton(frame2, text = "+5°C", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
c50_button.grid(row=0, column=1, padx=40, pady=15)

# Left Button
c15_button=ctk.CTkButton(frame2,text = "+15°C",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
c15_button.grid(row=1, column=1, padx=40, pady=15)

# Both print Button
c25_button=ctk.CTkButton(frame2, text = "+25°C", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
c25_button.grid(row=2, column=1, padx=40, pady=15)

# End loop of Printer window
ink_heating_wnd.mainloop()
