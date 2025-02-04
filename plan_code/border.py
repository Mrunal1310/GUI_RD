# customtkinter ans Pillow library 
import customtkinter as ctk
from PIL import Image

# Disply of Print sound Window
border_wnd=ctk.CTk()
border_wnd.title("Border")
border_wnd.geometry("1200x800")
border_wnd.config(bg="white")

def close_label():
    border_wnd.destroy()

frame1=ctk.CTkFrame(border_wnd,fg_color="white", width=300, height=400, border_width=1, border_color="#A83232", corner_radius=0)
frame1.pack(padx=200, pady=200,ipady=10,)

frame1.rowconfigure((0), weight=0)
frame1.rowconfigure((1,2,3,4), weight=0)
frame1.columnconfigure((0,1,2,3), weight=1)

label=ctk.CTkLabel(frame1, text="Border:", width=600,height=35, fg_color="#A83232", text_color="white",font=("aerial", 20, 'bold'))
label.grid(row=0, column=0, columnspan=4)

image_close=ctk.CTkImage(dark_image=Image.open("N1/close.png"))
close_button = ctk.CTkButton(frame1, command=close_label, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=40, corner_radius=0,)
close_button.grid(row=0, column=3,padx=5, sticky='e')

entry1=ctk.CTkEntry(frame1, placeholder_text="", justify="center", width=530,height=50,fg_color="#96ddf3", border_width=0, corner_radius=0, font=("aerial", 25, 'bold'))
entry1.grid(row=1, column=0, columnspan=4, padx=5, pady=20,)

val1=ctk.CTkButton(frame1, text="0", width=80, height=40, fg_color="#C4E3ED",corner_radius=0,text_color="black",font=("aerial", 20, ))
val1.grid(row=2, column=0,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="1", width=80, height=40,fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20, ))
val1.grid(row=2, column=1,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="2", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20, ))
val1.grid(row=2, column=2,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="3", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=2, column=3,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="4", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=3, column=0,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="5", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=3, column=1,padx=0, pady=5,  )

val1=ctk.CTkButton(frame1, text="6", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=3, column=2,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="7", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=3, column=3,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="8", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=4, column=0,padx=0, pady=5)

val1=ctk.CTkButton(frame1, text="9", width=80, height=40, fg_color="#C4E3ED",corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=4, column=1,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="<--",width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=4, column=2,padx=0, pady=5 )

val1=ctk.CTkButton(frame1, text="OK", width=80, height=40, fg_color="#C4E3ED", corner_radius=0,text_color="black", font=("aerial", 20,))
val1.grid(row=4, column=3,padx=0, pady=5 )

# End loop of of Print sound window
border_wnd.mainloop()
