# customtkinter library 
import customtkinter as ctk

# Set appearance mode to "white"
ctk.set_appearance_mode("white")

# Disply of Printer Window
calendar_window= ctk.CTk()
calendar_window.title("Calendar")
calendar_window.geometry("1200x800")
calendar_window.config(bg="white")

# Close Button
# Function to close the label
def close_label():
    calendar_window.destroy()

# Create a frame to hold the label and the close button
calendar_frame = ctk.CTkFrame(calendar_window, )
calendar_frame.grid(row=0, column=0)

# Calendar Label
calendar_lbl=ctk.CTkLabel(calendar_frame, text="Calendar", width=1200, text_color="white",font=("aerial", 20, 'bold'), fg_color="#CC0000",)
calendar_lbl.grid(row=0, column=0, columnspan=3, sticky='e')

# Create the close button
close_button = ctk.CTkButton(calendar_frame, text="X", width=30,text_color='white', fg_color='red', corner_radius=0, font=("aerial", 15), command=close_label)
close_button.columnconfigure(3, weight=0)
close_button.grid(row=0, column=0, columnspan=3, sticky='e')

# Configure the grid column weights
calendar_window.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row weights
calendar_window.rowconfigure((0, 3), weight=1)
calendar_window.rowconfigure(1, weight=0)

## Create Right Button
gregorian_butn = ctk.CTkButton(calendar_window, anchor= "center", text = "Right", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
gregorian_butn.grid(row=1,column=0, padx=10, pady=10,)

# Create Left Button
jalali_butn = ctk.CTkButton(calendar_window, anchor= "center", text = "Left",  corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
jalali_butn.grid(row=2,column=0, padx=10, pady=10, sticky='n')

# Create Both print Button
islamic_butn = ctk.CTkButton(calendar_window, anchor= "center", text = "Both print", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
islamic_butn.grid(row=3,column=0, padx=10, pady=10, sticky='n')

# End loop of Printer Window
calendar_window.mainloop()