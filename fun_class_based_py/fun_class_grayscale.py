import customtkinter as ctk
from PIL import Image

class GrayscaleWindow:
    def __init__(self, app):
        self.app = app
        self.app.title("Grayscale")
        self.app.geometry("1200x800")
        self.app.config(bg="white")

        # Configure the grid column weights of Grayscale window
        self.app.columnconfigure((0,1,2), weight=1)
        self.app.rowconfigure((0,1,2), weight=1)

        self.create_title()  # Create title and close button

        self.create_buttons()  # Create buttons dynamically using a dictionary and for loop

    def create_title(self):
        """Create the title frame with close button."""
        frame1 = ctk.CTkFrame(self.app, fg_color="#A83232", corner_radius=0)

        # Configure the grid column for title frame
        frame1.columnconfigure((0, 1, 2), weight=1)
        frame1.rowconfigure(0, weight=0)

        # Icon for close button
        image_close = ctk.CTkImage(dark_image=Image.open("images/close_icon.png"), size=(20, 20))  # Update image path if needed
        close_button = ctk.CTkButton(frame1, command=self.app.destroy, text="", image=image_close, hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", width=50, corner_radius=0)
        close_button.grid(row=0, column=2, sticky='e')

        # Grid of frame weight
        frame1.grid(row=0, column=0, columnspan=3, sticky="new")

        # Label for Grayscale title
        label1 = ctk.CTkLabel(frame1, text="Grayscale", fg_color="#A83232", 
                              corner_radius=0, anchor='center', 
                              text_color="white", font=("aerial", 20, 'bold'))
        label1.grid(row=0, column=1, pady=5, sticky="n")

    def create_buttons(self):
        """Create buttons dynamically using a dictionary and for loop to arrange buttons in proper rows and columns."""
        # Frame for buttons
        frame2 = ctk.CTkFrame(self.app, fg_color="white", corner_radius=0)
        frame2.grid(row=1, column=1)

        # Configure the grid column and rows for frame for buttons
        frame2.columnconfigure((0,1), weight=1)
        frame2.rowconfigure((0,1,2,3,4), weight=1)

        # Button configuration dictionary
        button_config = {
            "routine": {"text": "Routine"}, "double": {"text": "Double"},
            "fourfold": {"text": "Fourfold"}, "six_times": {"text": "Six times"},
            "eight_times": {"text": "Eight times"}, "bold": {"text": "Bold"}, 
            "triple": {"text": "Triple"}, "five_times": {"text": "Five times"},
            "seven_times": {"text": "Seven times"}, "nine_times": {"text": "Nine times"}
        }

        # Create buttons dynamically from dictionary using a loop
        for idx, (key, config) in enumerate(button_config.items()):
            button = ctk.CTkButton(frame2, text=config["text"], corner_radius=0, 
                                   width=400, height=40, fg_color="#FF00FF", 
                                   hover_color="pink", text_color="black",
                                   font=("Arial", 18))
            row = idx % 5  # 5 buttons per row
            col = idx // 5  # New column after every 5 buttons
            button.grid(row=row, column=col, padx=40, pady=15, sticky="news")


# Creating the main application window
app = ctk.CTk()
grayscale_window = GrayscaleWindow(app)

# Run the application
app.mainloop()