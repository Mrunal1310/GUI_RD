import customtkinter as ctk
from PIL import Image
import os

# Class of Symbols Window
class SymbolsWindow:
    # Function to create root window
    def __init__(self, root):
        
        self.symbol=root
        self.symbol.title("Symbols")
        self.symbol.geometry("1200x800")
        self.symbol.resizable(True, True)
        self.symbol.config(bg="white")
        
        # Configure grid column and row weights
        self.symbol.columnconfigure(0, weight=1)
        self.symbol.rowconfigure((0), weight=0)
        self.symbol.rowconfigure((1), weight=1)
        
        # Create widgets
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame 
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.symbol, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Symbols",  fg_color="#A83232", corner_radius=0, 
                                anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.symbol.destroy, 
                                            hover_color="#A83232", fg_color="#A83232",
                                            width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            self.close_button=ctk.CTkButton(self.frame, text="",command=self.check_button, 
                                            hover_color="#A83232", fg_color="#A83232",
                                            width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,padx=50, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        self.frame=ctk.CTkFrame(self.symbol, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.frame.rowconfigure((0,1,), weight=1)
        self.frame.grid(row=1, column=0,pady=20,sticky="news")
        
        # Button labels list
        self.button_list=[
            "1", "2", "3","4","5", "6", "7",
            "8", "9", "10", "11", "12", "13", "14"
        ]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        for index, label in enumerate(self.button_list):
            row = index // 7
            col = index % 7
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, 
                                fg_color="#C4E3ED", text_color= "black", 
                                font=("Arial", 15,))
            button.grid(row=row, column=col, padx=20, pady=30, sticky="ns")
            self.button=ctk.CTkButton(self.frame, text = "Size", corner_radius=0, 
                                    fg_color="#C4E3ED", text_color= "black", 
                                    font=("Arial", 15,))
            self.button.grid(row=2, column=0, columnspan=7, padx=0, pady=20, sticky="e")
            
# Function to root window
def main():
    root=ctk.CTk()
    app=SymbolsWindow(root)
    root.mainloop()
    
# Run the program  
if __name__=="__main__":
    main()