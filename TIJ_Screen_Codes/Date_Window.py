import customtkinter as ctk
from PIL import Image
import os

# Class method for image path
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

#Class for Date Window
class DateWindow:
    def __init__(self, app):
        self.date_window = app
        self.date_window.title("Print sound")
        self.date_window.geometry("1200x800")
        self.date_window.config(bg="white")

        # Configure the grid columns and rows for the window
        self.date_window.columnconfigure((0, 1, 2), weight=1)
        self.date_window.rowconfigure((0), weight=1)
        self.date_window.rowconfigure((1, 2), weight=1)

        self.create_title_frame()
        self.create_button_frame()

    def create_title_frame(self):
        # Frame for the title bar
        frame1 = ctk.CTkFrame(self.date_window, fg_color="#A83232", corner_radius=0)
        frame1.columnconfigure((0, 1, 2), weight=1)
        frame1.rowconfigure(0, weight=1)
        
        # List of image filenames for title buttons and label
        image_files = ["close_icon.png", "checked_icon.png", "font_icon.png"]

        # Loop through the image files and load them
        for idx, image_name in enumerate(image_files):
            image = ImagePath.load_image(image_name)
            if image:
                button = ctk.CTkButton(frame1, command=self.select_alarm.destroy, text="", image=image, 
                                       hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", 
                                       width=50, corner_radius=0)
                button.grid(row=0, column=idx, sticky='e' 
                            if idx == 2 else 'w')

        # List of labels for title
        label_list=["Date","Font",]
        
        # For loop for to arrange labels
        for idx, text in enumerate(label_list):
            label_name=ctk.CTkLabel(frame1, text=text, fg_color="#A83232", bg_color="#A83232", anchor='center',
                              text_color="white", font=("aerial", 20, 'bold'))
            label_name.grid(row=0, column=1, padx=150, pady=5, sticky="new" if idx == 1 else 'w')
            
        # label1 = ctk.CTkLabel(frame1, text="Date", fg_color="#A83232", bg_color="#A83232", anchor='center',
        #                       text_color="white", font=("aerial", 20, 'bold'))
        # label1.grid(row=0, column=1, padx=150, pady=5, sticky="new")

        # label2 = ctk.CTkLabel(frame1, text="Font", fg_color="#A83232", bg_color="#A83232", anchor='center',
        #                       text_color="white", font=("aerial", 20, 'bold'))
        # label2.grid(row=0, column=0, padx=40, pady=5, sticky="nw")


        # Add title frame to the window
        frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        # Frame for the buttons
        frame2 = ctk.CTkFrame(self.date_window, fg_color="white", corner_radius=0)
        frame2.grid(row=1, column=1)

        # Configure the grid columns and rows for button frame
        frame2.columnconfigure((0, 1, 2), weight=1)
        frame2.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Create buttons dynamically using a loop
        button_texts = [
            ["2025-01-07", "25/01/07", "25 01 07", "01-07-2025", "07/01/25", "23:57:54"],
            ["2025/01/07", "25-01-07", "25 Jan 07", "01.07.25", "07-01-25", "23:57"],
            ["2025年01月07日", "25.01.07", "01/07/25", "JAN 07 25", "07.01.25", "Term"]
        ]

        # Create buttons for each column
        for col_idx, texts in enumerate(button_texts):
            for row_idx, text in enumerate(texts):
                button = ctk.CTkButton(frame2, text=text, corner_radius=0, width=400, height=40, fg_color="#FF00FF",
                                       hover_color="pink", text_color="black", font=("aerial", 15, 'bold'))
                button.grid(row=row_idx, column=col_idx, padx=50, pady=15 )
                
                

    def check_label(self):
        # Function for button actions
        print("Check label clicked")


# Run the application
if __name__ == "__main__":
    app = ctk.CTk()
    date_window = DateWindow(app)
    app.mainloop()
