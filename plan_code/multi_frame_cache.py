# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Multi frame cache Window
multi_frame_cache=ctk.CTk()
multi_frame_cache.title("Multi frame cache")
multi_frame_cache.geometry("1200x800")
multi_frame_cache.config(bg="white")

# Configure the grid column weights of multi frame cache window
multi_frame_cache.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of multi frame cache window
multi_frame_cache.rowconfigure((0), weight=1)
multi_frame_cache.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    multi_frame_cache.destroy()

# Frame for Multi frame cache Title
frame1=ctk.CTkFrame(multi_frame_cache, bg_color="#A83232", fg_color="#A83232")

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

# Label for multi frame cache title
label1=ctk.CTkLabel(frame1, text="Multi frame cache",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(multi_frame_cache,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3), weight=1)

# OFF Button
off_button=ctk.CTkButton(frame2, text = "OFF", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_button.grid(row=0, column=0,padx=40, pady=15,)

# X4 Button
X4_button=ctk.CTkButton(frame2,text = "X4",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X4_button.grid(row=1, column=0,padx=40, pady=15)

# X7 Button
X7_button=ctk.CTkButton(frame2, text = "X7", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X7_button.grid(row=2, column=0,padx=40, pady=15,)


# X10 Button
X10_button=ctk.CTkButton(frame2, text = "X10", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X10_button.grid(row=3, column=0, padx=40, pady=15)

# X2 Button
X2_button=ctk.CTkButton(frame2,text = "X2",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X2_button.grid(row=0, column=1,padx=40, pady=15)

# X5 Button
X5_button=ctk.CTkButton(frame2, text = "X5", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X5_button.grid(row=1, column=1,padx=40, pady=15,)

# X8 Button
X8_button=ctk.CTkButton(frame2, text = "X8", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X8_button.grid(row=2, column=1, padx=40, pady=15)

# X11 Button
X11_button=ctk.CTkButton(frame2,text = "X11",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X11_button.grid(row=3, column=1, padx=40, pady=15)

# X3 Button
X3_button=ctk.CTkButton(frame2, text = "X3", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X3_button.grid(row=0, column=2,padx=40, pady=15,)


# X6 Button
X6_button=ctk.CTkButton(frame2, text = "X6", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X6_button.grid(row=1, column=2, padx=40, pady=15)

# X9 Button
X9_button=ctk.CTkButton(frame2,text = "X9",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
X9_button.grid(row=2, column=2, padx=40, pady=15)


# End loop of Multi frame cache window
multi_frame_cache.mainloop()
