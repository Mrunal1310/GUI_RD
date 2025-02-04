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
image_close=ctk.CTkImage(dark_image=Image.open("N1/close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
close_button.grid(row=0, column=2,padx=10, sticky='e')

image_check=ctk.CTkImage(dark_image=Image.open("N1/checked.png"))
check_button = ctk.CTkButton(frame1, command=check_label, text="", image=image_check, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
check_button.grid(row=0, column=2,padx=50, sticky='e')

image_check=ctk.CTkImage(dark_image=Image.open("N1/font.png"))
check_button = ctk.CTkButton(frame1, command=check_label, text="", image=image_check, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, corner_radius=0)
check_button.grid(row=0, column=0,padx=0, sticky='w')

# Label for Print sound title
label1=ctk.CTkLabel(frame1, text="Date",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=1,padx=150, pady=5, sticky="new")

label1=ctk.CTkLabel(frame1, text="Font",  fg_color="#A83232", bg_color="#A83232", anchor='center',text_color="white",font=("aerial", 20, 'bold'))
label1.grid(row=0, column=0,padx=40, pady=5, sticky="nw")

# Grid of frame weight
frame1.grid(row=0, column=0,columnspan=3, sticky="new")


# Frame for buttons 
frame2=ctk.CTkFrame(print_sound_wnd,fg_color="white", bg_color="white")
frame2.grid(row=1, column=1,)

# Configure the grid column for frame for buttons
frame2.columnconfigure((0,1,2), weight=1)

# Configure the grid row for frame for buttons
frame2.rowconfigure((0,1,2,3,4,5), weight=1,)

# OFF Button
off_button=ctk.CTkButton(frame2, text = "2025-01-07", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
off_button.grid(row=0, column=0,padx=50, pady=15,)

# Start only Button
start_button=ctk.CTkButton(frame2,text = "25/01/07",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
start_button.grid(row=1, column=0,padx=50, pady=15)

# Complete only Button
complete_button=ctk.CTkButton(frame2, text = "25 01 07", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
complete_button.grid(row=2, column=0,padx=50, pady=15,)


# Start to finish Button
button=ctk.CTkButton(frame2, text = "01-07-2025", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button.grid(row=3, column=0, padx=50, pady=15)

button1=ctk.CTkButton(frame2, text = "07/01/25",corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button1.grid(row=4, column=0, padx=50, pady=15)

button2=ctk.CTkButton(frame2, text = "23:57:54",corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button2.grid(row=5, column=0, padx=50, pady=15)

# OFF Button
button3=ctk.CTkButton(frame2, text = "2025/01/07", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button3.grid(row=0, column=1,padx=50, pady=15,)

# Start only Button
button4=ctk.CTkButton(frame2,text = "25-01-07",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button4.grid(row=1, column=1,padx=50, pady=15)

# Complete only Button
button5=ctk.CTkButton(frame2, text = "25 Jan 07", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button5.grid(row=2, column=1,padx=50, pady=15,)

# Start to finish Button
button6=ctk.CTkButton(frame2, text = "01.07.25", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button6.grid(row=3, column=1, padx=50, pady=15)

button7=ctk.CTkButton(frame2, text = "07-01-25",corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button7.grid(row=4, column=1, padx=50, pady=15)

button8=ctk.CTkButton(frame2, text = "23:57",corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button8.grid(row=5, column=1, padx=50, pady=15)

# OFF Button
button9=ctk.CTkButton(frame2, text = "2025年01月07日", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button9.grid(row=0, column=2,padx=50, pady=15,)

# Start only Button
button10=ctk.CTkButton(frame2,text = "25.01.07",  corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button10.grid(row=1, column=2,padx=50, pady=15)

# Complete only Button
button11=ctk.CTkButton(frame2, text = "01/07/25", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button11.grid(row=2, column=2,padx=50, pady=15,)


# Start to finish Button
button12=ctk.CTkButton(frame2, text = "JAN 07 25", corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button12.grid(row=3, column=2, padx=50, pady=15)

button13=ctk.CTkButton(frame2, text = "07.01.25",corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button13.grid(row=4, column=2, padx=50, pady=15)

button14=ctk.CTkButton(frame2, text = "Term",corner_radius=0, width=400, height=40, fg_color="#E8EEF6", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
button14.grid(row=5, column=2, padx=50, pady=15)


# End loop of of Print sound window
print_sound_wnd.mainloop()

