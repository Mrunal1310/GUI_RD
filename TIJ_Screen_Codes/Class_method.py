import customtkinter as ctk
from PIL import Image
import os

# Class method for image path
"""We can call this method in both class """
class ImagePath:      
    @classmethod
    def get_image_path(cls, image_name):
        """Returns the full path to the image file."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,"images")  # Go up one directory and access 'images' folder
        image_path = os.path.join(image_dir, image_name)  # Construct the full image path
        return image_path
    
    @classmethod
    def load_image(cls, image_name):
        """Load and return an image with exception handling."""
        image_path = cls.get_image_path(image_name)
        try:
            image = Image.open(image_path)  # Try to open the image file
            image.close()  # To close the image file
            return ctk.CTkImage(dark_image=image)  # Return the image wrapped as CTkImage
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")

# Class of Printer Window            
class PrinterWindow:
    def __init__(self, root):
        self.printer = root
        self.printer.title("Printer")
        self.printer.geometry("1200x800")
        self.printer.resizable(True, True)
        self.printer.config(bg="white")

        # Configure the grid  in column and rows with weights of Printer window
        self.printer.columnconfigure((0,1,2), weight=1)
        self.printer.rowconfigure((0,1,2), weight=1)

        # Create frames and buttons
        self.create_title_frame()
        self.create_button_frame()
    
    def create_title_frame(self):
        # Frame for Printer Title
        self.frame1 = ctk.CTkFrame(self.printer, fg_color="#A83232", corner_radius=0)
        self.frame1.columnconfigure((0, 1, 2), weight=1)
        self.frame1.rowconfigure(0, weight=0)

        # Load close button image
        image_close = ImagePath.load_image("close_icon.png")
        if image_close:
            close_button = ctk.CTkButton(self.frame1, command=self.printer.destroy, text="", image=image_close, 
                                         hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", width=50, corner_radius=0)
            close_button.grid(row=0, column=2, sticky='e')

        # Label for Printer title
        label1 = ctk.CTkLabel(self.frame1, text="Printer", fg_color="#A83232", anchor='center', text_color="white", font=("aerial", 24, 'bold'))
        label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        # Frame for buttons
        self.frame2 = ctk.CTkFrame(self.printer, fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)
        
        # Configure the grid  in column and rows with weights of frame
        self.frame2.columnconfigure((0, 1, 2), weight=1)
        self.frame2.rowconfigure((0, 1, 2), weight=1)

        # List of Printer button labels
        button_labels = ["Right", "Left", "Both print"]

        # For loop to create buttons 
        for idx, label in enumerate(button_labels):
            button = ctk.CTkButton(self.frame2, text=label, corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color="black", font=("Aerial", 20,))
            button.grid(row=idx, column=1, padx=40, pady=15)           

# Class of Printer Window 
class CalendarWindow:
    def __init__(self, root):
        self.calendar = root
        self.calendar.title("Calendar")
        self.calendar.geometry("1200x800")
        self.calendar.resizable(True, True)
        self.calendar.config(bg="white")

        # Configure the grid in column and rows with weights of Calendar window
        self.calendar.columnconfigure((0,1,2), weight=1)
        self.calendar.rowconfigure((0,1,2), weight=1)

        # Create frames and buttons
        self.create_title_frame()
        self.create_button_frame()
    
    def create_title_frame(self):
        # Frame for Calendar Title
        self.frame1 = ctk.CTkFrame(self.calendar, fg_color="#A83232", corner_radius=0)
        self.frame1.columnconfigure((0, 1, 2), weight=1)
        self.frame1.rowconfigure(0, weight=0)

        # Load close button image
        image_close = ImagePath.load_image("close_icon.png")
        if image_close:
            close_button = ctk.CTkButton(self.frame1, command=self.calendar.destroy, text="", image=image_close, 
                                         hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", width=50, corner_radius=0)
            close_button.grid(row=0, column=2, sticky='e')

        # Label for Calendar title
        label1 = ctk.CTkLabel(self.frame1, text="Calendar", fg_color="#A83232", anchor='center', text_color="white", font=("Aerial", 24,'bold'))
        label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        # Frame for buttons
        self.frame2 = ctk.CTkFrame(self.calendar, fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)

        # Configure the grid in column and rows with weights of frame
        self.frame2.columnconfigure((0, 1, 2), weight=1)
        self.frame2.rowconfigure((0, 1, 2), weight=1)

        # List of Calendar button labels
        button_labels = ["Gregorian calendar", "Jalali date", "Islamic calendar"]

        # For loop to create buttons 
        for idx, label in enumerate(button_labels):
            button = ctk.CTkButton(self.frame2, text=label, corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color="black", font=("Aerial", 20,))
            button.grid(row=idx, column=1, padx=40, pady=15)
            
# Class of Select alarm Window
class SelectAlarmWindow:
    def __init__(self, root):
        self.select_alarm = root
        self.select_alarm.title("Select alarm ")
        self.select_alarm.geometry("1200x800")
        self.select_alarm.resizable(True, True)
        self.select_alarm.config(bg="white")

        # Configure the grid column and rows weights of Calendar window
        self.select_alarm.columnconfigure((0,1,2), weight=1)
        self.select_alarm.rowconfigure((0,1,2), weight=1)

        # Create frames and buttons
        self.create_title_frame()
        self.create_button_frame()
    
    def create_title_frame(self):
        # Frame for Select alarm Title
        self.frame1 = ctk.CTkFrame(self.select_alarm, fg_color="#A83232", corner_radius=0)
        self.frame1.columnconfigure((0, 1, 2), weight=1)
        self.frame1.rowconfigure(0, weight=0)

        # Load close button image
        image_close = ImagePath.load_image("close_icon.png")
        if image_close:
            close_button = ctk.CTkButton(self.frame1, command=self.select_alarm.destroy, text="", image=image_close, 
                                         hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", width=50, corner_radius=0)
            close_button.grid(row=0, column=2, sticky='e')

        # Label for Calendar title
        label1 = ctk.CTkLabel(self.frame1, text="Select alarm ", fg_color="#A83232", anchor='center', text_color="white", font=("Aerial", 24, 'bold'))
        label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        # Frame for buttons
        self.frame2 = ctk.CTkFrame(self.select_alarm , fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)

        # Configure the grid in column and rows with weights of frame
        self.frame2.columnconfigure((0, 1, 2), weight=1)
        self.frame2.rowconfigure((0, 1, 2), weight=1)

        # List of Select alarm button labels
        button_labels = ["OFF", "Built in buzzer", "External alarm"]

        # For loop to create buttons 
        for idx, label in enumerate(button_labels):
            button = ctk.CTkButton(self.frame2, text=label, corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color="black", font=("Aerial", 20,))
            button.grid(row=idx, column=1, padx=40, pady=15)

# Main function
if __name__ == "__main__":
    
    # Printer function
    printer = ctk.CTk()
    app = PrinterWindow(printer)
    printer.mainloop()
    
    # Calendar function
    calendar = ctk.CTk()
    app = CalendarWindow(calendar)
    calendar.mainloop()
    
    # Select alarm function
    select_alarm = ctk.CTk()
    app = SelectAlarmWindow(select_alarm)
    select_alarm.mainloop()
