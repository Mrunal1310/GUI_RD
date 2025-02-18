import customtkinter as ctk
from PIL import Image
import os

# Class of Calendar Window
class PrintSet:
    # Function to create root window
    def __init__(self, root):
        
        self.print_set=root
        self.print_set.title("Print set")
        self.print_set.geometry("1200x800")
        self.print_set.resizable(True, True)
        self.print_set.config(bg="white")
        
        # Configuration of Window
        self.print_set.columnconfigure(0, weight=1)
        self.print_set.columnconfigure(1, weight=3)
        self.print_set.rowconfigure((0), weight=0)
        self.print_set.rowconfigure((1,), weight=1)
        
        # Create widgets
        self.title_frame()
        self.button_frame()
        self.display_frame()
        
    # Function to create title frame 
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.print_set, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0,columnspan=2, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Print set",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.print_set.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X", command=self.print_set.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        self.frame=ctk.CTkFrame(self.print_set, fg_color="#C4E3ED", corner_radius=0)
        self.frame.columnconfigure((0), weight=1)
        self.frame.rowconfigure((0,1,2,3,4,5), weight=1)
        self.frame.grid(row=1, column=0,pady=20,sticky="news")
        
        # Button labels list
        self.button_list=[
            "Printing direction", "Photelectric setting", "Continuous setting",
            "Control","Printer", "Others" 
        ]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        for index, label in enumerate(self.button_list):
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, anchor="w", fg_color="#C4E3ED", hover_color="#FF00FF",text_color= "black", font=("Arial", 18,))
            button.grid(row=index, column=0, sticky="nsew")
            
    def display_frame(self):
        self.frame=ctk.CTkFrame(self.print_set, fg_color="white", border_width=1,corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(row=1, column=1, pady=20, sticky="news")
    
# Function to root window
def main():
    root=ctk.CTk()
    app=PrintSet(root)
    root.mainloop()
    
# Run the program  
if __name__=="__main__":
    main()