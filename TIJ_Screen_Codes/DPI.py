import customtkinter as ctk
from PIL import Image
import os

# Class of Calendar Window
class DPIWindow:
    # Function to create root window
    def __init__(self, root):
        self.dpiwindow=root
        self.dpiwindow.title("DPI")
        self.dpiwindow.geometry("1200x800")
        self.dpiwindow.resizable(True, True)
        self.dpiwindow.config(bg="white")
        
        # Configuration of Window
        self.dpiwindow.columnconfigure(0, weight=1)
        self.dpiwindow.rowconfigure((0,1,2), weight=1)
        
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.dpiwindow,fg_color="white", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="DPI",  fg_color="#A83232", corner_radius=0, height=30, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            print(image_path)
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.dpiwindow.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=30, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Button labels list
    def button_frame(self,):
        self.frame=ctk.CTkFrame(self.dpiwindow, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1), weight=1)
        self.frame.rowconfigure((0,1,2), weight=1)
        self.frame.grid(row=1, column=0, pady=20,sticky="news")
        
        # Button label list
        self.button_list=[
            "300*300", "150*300", "300*150", "150*150", "300*100", "150*100",
        ]
        
        self.create_button()
        
    # Function to create button in rows and columns with button labels
    def create_button(self):
        for index, label in enumerate(self.button_list):
            row=index // 2
            col=index % 2
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, fg_color="#FF00FF", text_color= "black", font=("Arial", 15,))
            button.grid(row=row, column=col, padx=50, pady=20, sticky="ew")
            
# Function to root window
def main():
    root=ctk.CTk()
    app = DPIWindow(root)
    root.mainloop()
    
# Run the program
if __name__=="__main__":
    main()