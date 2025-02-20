import customtkinter as ctk
from PIL import Image
import os

# Class of Round trip printing Window
class RoundTripprinting:
    # Function to create root window
    def __init__(self, root):
        self.round_trip_print=root
        self.round_trip_print.title("Round trip printing")
        self.round_trip_print.geometry("1200x800")
        self.round_trip_print.resizable(True, True)
        self.round_trip_print.config(bg="white")
        
        # Configure grid column and row weights
        self.round_trip_print.columnconfigure(0, weight=1)
        self.round_trip_print.rowconfigure((0,1,2), weight=1)
        
        # Create widgets
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.round_trip_print,fg_color="white", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Round trip printing",  fg_color="#A83232", corner_radius=0, 
                                anchor='center',text_color="white", height=30,
                                font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.round_trip_print.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Button labels list
    def button_frame(self,):
        self.frame=ctk.CTkFrame(self.round_trip_print, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure((0,1,2,3,4), weight=1)
        self.frame.grid(row=1, column=0, pady=20,sticky="news")
        
        # Button label list
        self.button_list=[
            "OFF", "+1", "+2","+3", "+4", "+5",
            "+6", "+7", "+8","+9", "+10", "+11",
            "+12", "+13", "+14",
            
        ]
        
        self.create_button()
        
    # Function to create button in rows and columns with button labels
    def create_button(self):
        for index, label in enumerate(self.button_list):
            row=index // 3
            col=index % 3
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, 
                                fg_color="#FF00FF", text_color= "black", 
                                font=("Arial", 15,))
            button.grid(row=row, column=col, padx=50, pady=20, sticky="ew")
            
# Function to root window
def main():
    root=ctk.CTk()
    app = RoundTripprinting(root)
    root.mainloop()
    
# Run the program
if __name__=="__main__":
    main()