import customtkinter as ctk  # customtkinter library
from PIL import Image        # Pillow library

# Class based Date Program
class DateApp:
    def __init__(self, root):      # Function to create main window
        self.root = root
        self.root.title("Date")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        self.root.config(bg="white")
        
        """ 
        The below configuration was of root window as per rows and columns
        with their weight 
        """
        # Configure grid column and row weights
        # self.root.columnconfigure((0, 1, 2), weight=1)
        # self.root.rowconfigure((0,1), weight=1)

        # Call the method to create UI components
        self.create_widgets()
        
        # Function to create widgets
    def create_widgets(self):
        # Create and configure title frame
        self.frame1 = ctk.CTkFrame(self.root, fg_color="#A83232", corner_radius=0)
        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")
        self.frame1.columnconfigure((0, 1, 2), weight=1)

        # Close button image with close button
        image_close = ctk.CTkImage(dark_image=Image.open("close.png"))
        close_button = ctk.CTkButton(self.frame1, 
                                     command=self.root.destroy, 
                                     text="", image=image_close, 
                                     hover_color="#A83232", 
                                     fg_color="#A83232", 
                                     bg_color="#A83232", 
                                     width=50, 
                                     corner_radius=0)
        close_button.grid(row=0, column=2, padx=10, sticky='e')

        # Check button image with check button
        image_check = ctk.CTkImage(dark_image=Image.open("checked.png"))
        check_button = ctk.CTkButton(self.frame1, 
                                     command=self.check_label, 
                                     text="", image=image_check, 
                                     hover_color="#A83232", 
                                     fg_color="#A83232", 
                                     bg_color="#A83232", 
                                     width=50, 
                                     corner_radius=0)
        check_button.grid(row=0, column=2, padx=50, sticky='e')

        # Font label image with font label
        image_font = ctk.CTkImage(dark_image=Image.open("font.png"))
        font_label = ctk.CTkButton(self.frame1,text="", 
                                   image=image_font, 
                                   hover_color="#A83232", 
                                   fg_color="#A83232", 
                                   width=50, 
                                   corner_radius=0)
        font_label.grid(row=0, column=0, sticky='w')

        # Labels for Date and Font Title
        label1 = ctk.CTkLabel(self.frame1, text="Date", fg_color="#A83232", anchor='center', text_color="white", font=("Arial", 20, 'bold'))
        label1.grid(row=0, column=1, padx=150, pady=5, sticky="new")

        label2 = ctk.CTkLabel(self.frame1, text="Font", fg_color="#A83232", anchor='center', text_color="white", font=("Arial", 20, 'bold'))
        label2.grid(row=0, column=0, padx=40, pady=5, sticky="nw")

        # Create Frame2 for buttons with different types of date formate as per year, month and date
        self.frame2 = ctk.CTkFrame(self.root, fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)

        # Configure the grid column for the buttons
        self.frame2.columnconfigure((0, 1, 2), weight=1)
        
        # For loop to arrange various buttons in rows and columns 
        for i in range(6):
            self.frame2.rowconfigure(i, weight=1)    # Configure the grid column for the buttons

        # Buttons texts and positions
        button_texts = [
            ("2025-01-07", 0, 0), ("25/01/07", 1, 0), ("25 01 07", 2, 0),
            ("01-07-2025", 3, 0), ("07/01/25", 4, 0), ("23:57:54", 5, 0),
            ("2025/01/07", 0, 1), ("25-01-07", 1, 1), ("25 Jan 07", 2, 1),
            ("01.07.25", 3, 1), ("07-01-25", 4, 1), ("23:57", 5, 1),
            ("2025年01月07日", 0, 2), ("25.01.07", 1, 2), ("01/07/25", 2, 2),
            ("JAN 07 25", 3, 2), ("07.01.25", 4, 2), ("Term", 5, 2)
        ]

        # Create buttons dynamically in the grid layout
        for (text, row, col) in button_texts:
            button = ctk.CTkButton(self.frame2, 
                                   text=text, 
                                   corner_radius=0, 
                                   width=400, 
                                   height=40, 
                                   fg_color="#FF00FF", 
                                   hover_color="pink", 
                                   text_color="black", 
                                   font=("Arial", 15, 'bold')
                                   )
            button.grid(row=row, column=col, padx=50, pady=15)

    # Placeholder for check button functionality
    def check_label(self):
        pass


# Create the main window and pass it to the PrintSoundApp class
if __name__ == "__main__":
    root = ctk.CTk()
    app = DateApp(root)
    root.mainloop()
