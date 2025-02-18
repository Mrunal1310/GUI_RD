import customtkinter as ctk
from PIL import Image
import os

# Class of Printer Window
class PrinterWindow:
    # Function to create root window
    def __init__(self, root):
        
        self.printer=root
        self.printer.title("Printer")
        self.printer.geometry("1200x800")
        self.printer.resizable(True, True)
        self.printer.config(bg="white")
        
        # Configure grid column and row weights for window
        self.printer.columnconfigure(0, weight=1)
        self.printer.rowconfigure((0,1,2), weight=1)
        
        # Create widgets
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame 
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.printer, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Printer",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.printer.destroy, hover_color="#A83232", 
                                            fg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X", command=self.printer.destroy, hover_color="#A83232", 
                                            fg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        self.frame=ctk.CTkFrame(self.printer, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure((0,1,2), weight=1)
        self.frame.grid(row=1, column=0,pady=20,sticky="news")
        
        # Button labels list
        self.button_list=[
            "Right", "Left", "Both print",
        ]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        for index, label in enumerate(self.button_list):
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, fg_color="#FF00FF", text_color= "black", font=("Arial", 15,))
            button.grid(row=index, column=1, padx=40, pady=20, sticky="ew")
            
# Function to root window
def main():
    root=ctk.CTk()
    app=PrinterWindow(root)
    root.mainloop()
    
# Run the program  
if __name__=="__main__":
    main()