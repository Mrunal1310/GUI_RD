# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Round trip printing Window
round_trip_print_wnd=ctk.CTk()
round_trip_print_wnd.title("Round trip printing")
round_trip_print_wnd.geometry("1200x800")
round_trip_print_wnd.config(bg="white")

# Configure the grid column weights of Round trip printing window
round_trip_print_wnd.columnconfigure((0,1,2), weight=1)

# Configure the grid row weights of Round trip printing window
round_trip_print_wnd.rowconfigure((0), weight=1)
round_trip_print_wnd.rowconfigure((1,2), weight=1)

# Function to Close Button
def close_label():
    round_trip_print_wnd.destroy()

# Frame for of Round trip printing window Title
frame1=ctk.CTkFrame(round_trip_print_wnd, bg_color="#A83232", fg_color="#A83232")

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
label1=ctk.CTkLabel(frame1, text="Round trip printing",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1, pady=5, sticky="n")

# Frame for buttons 
frame2=ctk.CTkFrame(round_trip_print_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4), weight=1)

# OFF Button
off_button=ctk.CTkButton(frame2, text = "OFF", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_button.grid(row=0, column=0,padx=40, pady=15,)

# +3 Button
value1_button=ctk.CTkButton(frame2,text = "+3",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value1_button.grid(row=1, column=0,padx=40, pady=15)

# +6 Button
value2_button=ctk.CTkButton(frame2, text = "+6", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value2_button.grid(row=2, column=0,padx=40, pady=15,)


# +9 Button
value3_button=ctk.CTkButton(frame2, text = "+9", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value3_button.grid(row=3, column=0, padx=40, pady=15)

# +12 Button
value4_button=ctk.CTkButton(frame2,text = "+12",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value4_button.grid(row=4, column=0, padx=40, pady=15)

# +1 Button
value5_button=ctk.CTkButton(frame2,text = "+1",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value5_button.grid(row=0, column=1,padx=40, pady=15)

# +4 Button
value6_button=ctk.CTkButton(frame2, text = "+4", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value6_button.grid(row=1, column=1,padx=40, pady=15,)


# +7 Button
value7_button=ctk.CTkButton(frame2, text = "+7", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value7_button.grid(row=2, column=1, padx=40, pady=15)

# +10 Button
value8_button=ctk.CTkButton(frame2,text = "+10",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value8_button.grid(row=3, column=1, padx=40, pady=15)

# +14 Button
value9_button=ctk.CTkButton(frame2, text = "+13", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
value9_button.grid(row=4, column=1, padx=40, pady=15)

# +2 Button
value10_button=ctk.CTkButton(frame2, text = "+2", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value10_button.grid(row=0, column=2,padx=40, pady=15,)


# +5 Button
value11_button=ctk.CTkButton(frame2, text = "+5", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value11_button.grid(row=1, column=2, padx=40, pady=15)

# +8 Button
value12_button=ctk.CTkButton(frame2,text = "+8",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value12_button.grid(row=2, column=2, padx=40, pady=15)

# +11 print Button
value13_button=ctk.CTkButton(frame2, text = "+11", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold') )
value13_button.grid(row=3, column=2, padx=40, pady=15)

# +14 Button
value14_button=ctk.CTkButton(frame2, text = "+14", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
value14_button.grid(row=4, column=2,padx=40, pady=15,)


# End loop of of Round trip printing window window
round_trip_print_wnd.mainloop()
