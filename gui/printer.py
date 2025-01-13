# customtkinter library 
import customtkinter as ctk

# Set appearance mode to "white"
ctk.set_appearance_mode("white")

# Disply of Printer Window
printer_window= ctk.CTk()
printer_window.title("Printer")
printer_window.geometry("800x400")
printer_window.config(bg="white")

# Close Button
# Function to close the label
def close_label():
    printer_window.destroy()

# Create a frame to hold the label and the close button
printer_frame = ctk.CTkFrame(printer_window)
printer_frame.grid(row=0)

# Printer Label
printer_lbl=ctk.CTkLabel(printer_frame, text="Printer", width=1200,  text_color="white",font=("aerial", 20, 'bold'), fg_color="#CC0000",)
printer_lbl.grid(row=0, column=0, columnspan=3, sticky='e')

# Create the close button
close_button = ctk.CTkButton(printer_frame, text="X", width=30,text_color='white', fg_color='red', corner_radius=0, font=("aerial", 15), command=close_label)
close_button.columnconfigure(3, weight=0)
close_button.grid(row=0, column=0, columnspan=3, sticky='e')


# Configure the grid column weights
printer_window.columnconfigure((0, 1, 2), weight=1)

# Configure the grid row weights
printer_window.rowconfigure((0, 3), weight=1)
printer_window.rowconfigure(1, weight=0)

## Create Right Button
right_butn = ctk.CTkButton(printer_window, anchor= "center", text = "Gregorian calendar", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
right_butn.grid(row=1,column=0, padx=10, pady=10,)

# Create Left Button
left_butn = ctk.CTkButton(printer_window, anchor= "center", text = "Jalali Date",  corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
left_butn.grid(row=2,column=0, padx=10, pady=10, sticky='n')

# Create Both print Button
both_print_butn = ctk.CTkButton(printer_window, anchor= "center", text = "Islamic calendar", corner_radius=0, width=350, height=40, fg_color="#FF00FF", hover_color="pink", text_color= "black", font=("aerial", 15, 'bold'))
both_print_butn.grid(row=3,column=0, padx=10, pady=10, sticky='n')

# End loop of Printer Window
printer_window.mainloop()