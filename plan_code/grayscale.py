# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Print Sound Screen Window
grayscale_wnd=ctk.CTk()
grayscale_wnd.title("Grayscale")
grayscale_wnd.geometry("1200x800")
grayscale_wnd.config(bg="white")

# Configure the grid column weights of Grayscale window
grayscale_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Grayscale window
grayscale_wnd.rowconfigure((0), weight=1)
grayscale_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    grayscale_wnd.destroy()

# Frame for Grayscale Title
frame1=ctk.CTkFrame(grayscale_wnd, bg_color="#A83232", fg_color="#A83232")

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
label1=ctk.CTkLabel(frame1, text="Grayscale",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(grayscale_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4), weight=1)

# routine Button
routine_button=ctk.CTkButton(frame2, text = "routine", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
routine_button.grid(row=0, column=0,padx=40, pady=15,)

# Double Button
double_button=ctk.CTkButton(frame2,text = "Double",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
double_button.grid(row=1, column=0,padx=40, pady=15)

# Fourfold Button
fourfold_button=ctk.CTkButton(frame2, text = "Fourfold", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
fourfold_button.grid(row=2, column=0,padx=40, pady=15,)

# Six times Button
seven_times_button=ctk.CTkButton(frame2,text = "Six times",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
seven_times_button.grid(row=3, column=0, padx=40, pady=15)

# Eight times Button
six_times_button=ctk.CTkButton(frame2, text = "Eight times", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
six_times_button.grid(row=4, column=0, padx=40,pady=15)

# Bold Button
bold_button=ctk.CTkButton(frame2, text = "Bold", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
bold_button.grid(row=0, column=1, padx=40, pady=15)

# Triple Button
triple_button=ctk.CTkButton(frame2,text = "Triple",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
triple_button.grid(row=1, column=1, padx=40, pady=15)

# Five times Button
five_times_button=ctk.CTkButton(frame2, text = "Five times", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
five_times_button.grid(row=2, column=1, padx=40, pady=15)

# Seven times Button
seven_times_button=ctk.CTkButton(frame2,text = "Seven times",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
seven_times_button.grid(row=3, column=1, padx=40, pady=15)

# Nine times Button
nine_times_button=ctk.CTkButton(frame2, text = "Nine times", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
nine_times_button.grid(row=4, column=1, padx=40, pady=15)

# End loop of Grayscale window
grayscale_wnd.mainloop()
