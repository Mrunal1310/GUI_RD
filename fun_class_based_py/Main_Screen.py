import customtkinter as ctk
from PIL import Image
from datetime import datetime

# Class for Home Screen App
class HomeScreenApp(ctk.CTk): 
    def __init__(self):
        super().__init__()

        # Set window title, size, and background
        self.title("Home Screen")
        self.geometry("1200x800")
        self.config(bg="blue")

        # Set appearance mode to Blue
        ctk.set_appearance_mode("blue")

        # Date, Time and Day Label at the top
        self.time_label = ctk.CTkLabel(self, text="", text_color="white", bg_color="blue", font=("Arial", 36))
        self.time_label.grid(row=0, column=0, columnspan=5, pady=20,sticky="nw")
        
        self.date_day_label = ctk.CTkLabel(self, text="", text_color="white",bg_color="blue", font=("Arial", 15))
        self.date_day_label.grid(row=0, column=0, columnspan=5, pady=55, sticky="sw")

        # Version of Printer label
        self.version_label = ctk.CTkLabel(self, text="V15.8.9", text_color="white", bg_color="blue")
        self.version_label.grid(row=3, column=4, sticky='se', padx=10, pady=10)

        # Button configuration dictionary
        self.button_config = {
            "Print": {
                "image": "images/print_icon.png",
                "fg_color": "#87CEFF", 
                "text": "Print", 
                "command": self.print_butn, 
                
            },
            "File": {
                "image": "images/files_icon.png",
                "fg_color": "#5CACEE",
                "text": "File", 
                "command": self.file_butn, 
            },
            "Edit": {
                "image": "images/edit_icon.png",
                "fg_color": "#EE3B3B", 
                "text": "Edit", 
                "command": self.edit_butn, 
            },
            "Setting": {
                "image": "images/setting_icon.png",
                "fg_color": "#B452CD",
                "text": "Setting", 
                "command": self.setting_butn,
            }
        }

        # Call method to create buttons dynamically
        self.create_buttons()

        # Start updating the date and time
        self.update_time()
        
    # Function for Buttons
    def create_buttons(self):
        
        # Loop through button configurations and create buttons
        for index, (name, config) in enumerate(self.button_config.items()):
            
            image = Image.open(config["image"])
            ctk_image = ctk.CTkImage(light_image=image, size=(40, 40))
            
            button = ctk.CTkButton(self, 
                                   compound="top", 
                                   text=config["text"], 
                                   width=90, height=120, 
                                   image=ctk_image,
                                   corner_radius=10, 
                                   fg_color=config["fg_color"], 
                                   bg_color="blue", 
                                   hover_color="pink", 
                                   text_color="white", 
                                   command=config["command"], 
                                   font=("Aerial", 18,))
            button.grid(row=1, column=index + 1, padx=10, pady=10)  # Adjust position dynamically

    # Function for updating date and time
    def update_time(self):
        
        # Get current date and time
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("\n%Y/%m/%d %A")

        # Update the date and time label
        self.time_label.configure(text=f"{current_time}")
        self.date_day_label.configure(text=f"{current_date}")

        # Call the update_time method every 1000ms (1 second)
        self.after(1000, self.update_time)

    # Function for Print button
    def print_butn(self):
        print("Print button clicked")

    # Function for File button
    def file_butn(self):
        print("File button clicked")

    # Function for Edit button
    def edit_butn(self):
        print("Edit button clicked")

    # Function for Setting button
    def setting_butn(self):
        print("Setting button clicked")


# Create and run the app
if __name__ == "__main__":
    app = HomeScreenApp()
    app.mainloop()
