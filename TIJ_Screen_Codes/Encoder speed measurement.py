import customtkinter as ctk
from PIL import Image
import os

# Class of Encoder speed measurement Window
class EncoderSpeedMeasurement:
    # Function to create root window
    def __init__(self, root):
        
        self.encoder=root
        self.encoder.title("Encoder speed measurement")
        self.encoder.geometry("1200x800")
        self.encoder.resizable(True, True)
        self.encoder.config(bg="white")
        
        # Configuration of Window
        self.encoder.columnconfigure(0, weight=1)
        self.encoder.columnconfigure(1, weight=3)
        self.encoder.rowconfigure((0), weight=0)
        self.encoder.rowconfigure((1,), weight=1)
        
        self.title_frame()
        self.button_frame()
        self.display_frame()
        
    # Function to create title frame 
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.encoder, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0,columnspan=2, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Encoder speed measurement",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.encoder.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X", command=self.encoder.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        self.frame=ctk.CTkFrame(self.encoder, fg_color="#C4E3ED", corner_radius=0)
        self.frame.columnconfigure((0), weight=1)
        self.frame.rowconfigure((0,1,2,3,4,5), weight=1)
        self.frame.grid(row=1, column=0,pady=20,sticky="news")
        
        # Button labels list
        self.button_list=[
            "Encoder speed measurement",
        ]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        for index, label in enumerate(self.button_list):
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, anchor="w", fg_color="#C4E3ED", hover_color="#FF00FF",text_color= "black", font=("Arial", 18,))
            button.grid(row=index, column=0, sticky="nsew")
            
    def display_frame(self):
        self.frame=ctk.CTkFrame(self.encoder, fg_color="white", border_width=1,corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(row=1, column=1, pady=20, sticky="news")
    
# Function to root window
def main():
    root=ctk.CTk()
    app=EncoderSpeedMeasurement(root)
    root.mainloop()
    
# Run the program  
if __name__=="__main__":
    main()