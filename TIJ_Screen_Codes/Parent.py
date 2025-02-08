import customtkinter as ctk
from PIL import Image
import os

# ImagePath class
class ImagePath:
    
    @classmethod
    def get_image_path(cls, image_name):
        """Returns the full path to the image file."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir, "images")  # Go up one directory and access 'images' folder
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

# ParentWindow class
class ParentWindow:
    def __init__(self, app, window_title, button_labels):
        self.window = app
        self.window.title(window_title)
        self.window.geometry("1200x800")
        self.window.resizable(True, True)
        self.window.config(bg="white")

        # Store button labels 
        self.button_labels = button_labels

        # Configure the grid in column and rows with weights
        self.window.columnconfigure((0, 1, 2), weight=1)
        self.window.rowconfigure((0, 1, 2), weight=1)

        # Create common frames and buttons
        self.create_title_frame()
        self.create_button_frame()
    
    def create_title_frame(self):
        """Create title frame (common to all windows)"""
        self.frame1 = ctk.CTkFrame(self.window, fg_color="#A83232", corner_radius=0)
        self.frame1.columnconfigure((0, 1, 2), weight=1)
        self.frame1.rowconfigure(0, weight=0)

        # Load close button image
        image_close = ImagePath.load_image("close_icon.png")
        if image_close:
            close_button = ctk.CTkButton(self.frame1, text="", image=image_close, hover_color="#A83232", fg_color="#A83232",  command=self.window.destroy, width=50, corner_radius=0)
            close_button.grid(row=0, column=2, sticky='e')

        # Label for title window
        label1 = ctk.CTkLabel(self.frame1, text=self.window.title(), fg_color="#A83232", anchor='center', text_color="white", font=("Arial", 22, 'bold'))
        label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")
    
    def create_button_frame(self):
        """Create button frame (common to all windows)"""
        self.frame2 = ctk.CTkFrame(self.window, fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)

        # Configure the grid in column and rows with weights of frame
        self.frame2.columnconfigure((0, 1, 2), weight=1)
        self.frame2.rowconfigure((0, 1, 2), weight=1)

        # Create buttons and loop through button labels 
        for idx, label in enumerate(self.button_labels):
            button = ctk.CTkButton(self.frame2, text=label, corner_radius=0, width=400, height=40, 
                                   fg_color="#FF00FF", hover_color="pink", text_color="black", font=("Arial", 18))
            button.grid(row=idx, column=1, padx=40, pady=15)

# Class of Printer Window            
class PrinterWindow(ParentWindow):
    def __init__(self, app):
        button_labels = ["Right", "Left", "Both print"]  # Define Button labels for Printer window
        super().__init__(app, "Printer", button_labels)

# Class of Calendar Window
class CalendarWindow(ParentWindow):
    def __init__(self, app):
        button_labels = ["Gregorian calendar", "Jalali date", "Islamic calendar"]  # Define Button labels for Calendar window
        super().__init__(app, "Calendar", button_labels)

# Class of Select Alarm Window
class SelectAlarmWindow(ParentWindow):
    def __init__(self, app):
        button_labels = ["OFF", "Built in buzzer", "External alarm"]  # Define Button labels for Select Alarm window
        super().__init__(app, "Select alarm", button_labels)

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
