import customtkinter as ctk 
from PIL import Image
import os

# Class of Border Window
class BorderPopup:
    # Function to create root window
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("300x100")
        
        self.create_main_wnd()
        
    # Create button to open border popup box
    def create_main_wnd(self):
        self.button=ctk.CTkButton(self.root, text="Click Me",command=self.open_border )
        self.button.pack(padx=20, pady=20)
        
    # Funtion for border popup box (new toplevel window)
    def open_border(self):
        self.border=ctk.CTkToplevel(self.root)  
        self.border.title("Border")
        self.border.geometry("450x300")  
        self.border.resizable(False, False) 
        
        # Ensure the pop-up appears on top of the root window
        self.border.transient(self.root)  
        self.border.grab_set()       
        self.border.focus_force()
        
        # Create frame for border window
        self.frame=ctk.CTkFrame(self.border,width=450,height=300, fg_color="white",corner_radius=0)
        self.frame.columnconfigure((0,1,2,3), weight=1)
        self.frame.rowconfigure((0,1,2,3,4),weight=1)
        self.frame.grid(row=0, column=0, sticky="news")
        
        # Title label 
        self.label=ctk.CTkLabel(self.frame,text="Border:",width=450,height=30, fg_color="#A83232", text_color="white",font=("Arial", 20,'bold') )
        self.label.grid(row=0, column=0, columnspan=4)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "close_icon.png")
        
        # Close Button Icon
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.border.destroy, 
                                            hover_color="#A83232", fg_color="#A83232",
                                            width=50, height=30, corner_radius=0)
            self.close_button.grid(row=0, column=0,columnspan=4, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        self.entry = ctk.CTkEntry(self.frame, fg_color="#96ddf3", height=50,justify="center",corner_radius=0,border_width=0, font=("Arial",20,))
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20, sticky="news")
        
        self.create_buttons()
        
    # Create funtion to buttons in border window
    def create_buttons(self):
        # Button label list
        button_texts = [
            "0", "1", "2", "3",
            "4", "5", "6", "7",
            "8", "9", "<--", "OK"
        ]
        
        # For loop to arrange buttons 
        for i, text in enumerate(button_texts):
            row = i // 4
            col = i % 4
            button = ctk.CTkButton(self.frame, text=text, fg_color="#C4E3ED",width=80,height=30, corner_radius=0, text_color="black", font=("Arial", 18),)
            button.grid(row=row + 2, column=col, padx=15, pady=15,sticky="news")
            
# Run the program 
if __name__ == "__main__":
    root = ctk.CTk()
    app = BorderPopup(root)
    root.mainloop()