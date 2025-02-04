# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Language Screen Window
language_wnd=ctk.CTk()
language_wnd.title("Language")
language_wnd.geometry("1200x800")
language_wnd.config(bg="white")

# Configure the grid column weights of Language window
language_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Language window
language_wnd.rowconfigure((0), weight=1)
language_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    language_wnd.destroy()

# Frame for Title
frame1=ctk.CTkFrame(language_wnd, bg_color="#A83232", fg_color="#A83232")

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

# Label for Language title
label1=ctk.CTkLabel(frame1, text="Language",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(language_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4,5,6), weight=1)

# English Language  Button
english_button=ctk.CTkButton(frame2, text = "English", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
english_button.grid(row=0, column=0,padx=40, pady=15,)

# Arabic Language  Button
arabic_button=ctk.CTkButton(frame2,text = "Arabic",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
arabic_button.grid(row=1, column=0,padx=40, pady=15)

# Polish Language  Button
polish_button=ctk.CTkButton(frame2, text = "Polish language", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
polish_button.grid(row=2, column=0,padx=40, pady=15,)


# Greek Language  Button
greek_button=ctk.CTkButton(frame2, text = "Greek", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
greek_button.grid(row=3, column=0, padx=40, pady=15)

# Spanish Language  Button
spanish_button=ctk.CTkButton(frame2,text = "Spanish",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
spanish_button.grid(row=4, column=0, padx=40, pady=15)

# Portuguese Language  Button
portuguese_button=ctk.CTkButton(frame2,  text = "Portuguese", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
portuguese_button.grid(row=5, column=0, padx=40, pady=15)

# Ukrainian Language  Button
ukrainian_button=ctk.CTkButton(frame2, text = "Ukrainian", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
ukrainian_button.grid(row=6, column=0,padx=40, pady=15,)

# PY Language  Button
py_button=ctk.CTkButton(frame2,text = "PY",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
py_button.grid(row=0, column=1,padx=40, pady=15)

# French Language  Button
french_button=ctk.CTkButton(frame2, text = "French", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
french_button.grid(row=1, column=1,padx=40, pady=15,)


# Vietnamese Language  Button
vietnamese_button=ctk.CTkButton(frame2, text = "Vietnamese", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
vietnamese_button.grid(row=2, column=1, padx=40, pady=15)

# Korean Language  Button
korean_button=ctk.CTkButton(frame2,text = "Korean",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
korean_button.grid(row=3, column=1, padx=40, pady=15)

# Italian Language  Button
italian_button=ctk.CTkButton(frame2, text = "Italian", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
italian_button.grid(row=4, column=1, padx=40, pady=15)

# farsi Language  Button
farsi_button=ctk.CTkButton(frame2, text = "farsi", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
farsi_button.grid(row=5, column=1,padx=40, pady=15,)

# Handwriting Language  Button
handwriting_button=ctk.CTkButton(frame2,text = "Handwriting",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
handwriting_button.grid(row=6, column=1,padx=40, pady=15)

# Russian Language  Button
russian_button=ctk.CTkButton(frame2, text = "Russian", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
russian_button.grid(row=0, column=2,padx=40, pady=15,)


# German Language  Button
german_button=ctk.CTkButton(frame2, text = "German", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
german_button.grid(row=1, column=2, padx=40, pady=15)

# Japanese Language Button
japanese_button=ctk.CTkButton(frame2,text = "Japanese",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
japanese_button.grid(row=2, column=2, padx=40, pady=15)

# Turkish Language Button
turkish_button=ctk.CTkButton(frame2, text = "Turkish language", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
turkish_button.grid(row=3, column=2, padx=40, pady=15)

# Uzbek Language Button
uzbek_button=ctk.CTkButton(frame2, text = "Uzbek", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
uzbek_button.grid(row=4, column=2,padx=40, pady=15,)

# Thai Language Button
thai_button=ctk.CTkButton(frame2,text = "Thai",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
thai_button.grid(row=5, column=2,padx=40, pady=15)


# End loop of Language window
language_wnd.mainloop()
