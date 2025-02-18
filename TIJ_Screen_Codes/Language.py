import customtkinter as ctk
from PIL import Image
import os

# Class of Language Window
class Language:
    # Function to create root window
    def __init__(self, root):
        self.language=root
        self.language.title("Language")
        self.language.geometry("1200x800")
        self.language.resizable(True, True)
        self.language.config(bg="white")
        
        # Configuration of Window
        self.language.columnconfigure(0, weight=1)
        self.language.rowconfigure((0,), weight=0)
        self.language.rowconfigure((1,), weight=1)
        
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame  
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.language, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Language",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="",anchor="center", image=image, command=self.language.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X",anchor="center", command=self.language.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        
        self.frame=ctk.CTkFrame(self.language, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.frame.grid(row=1, column=0,sticky="news")
        
        # Button labels list
        self.button_labels=[
            "English", "PY", "Russian","Arabic", "French","German","Polish language","Vietnamese", "Japanese", "Greek", 
            "Korean", "Turkish language","Spanish", "Italian", "Uzbek","Portuguese", "farsi", "Thai","Ukrainian", "Handwriting",
        ]
        
        self.button_list=[]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        row=7
        col=3
        for index, label in enumerate(self.button_labels):
            row= index // col
            column= index % col
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, fg_color="#FF00FF", text_color= "black", font=("Arial", 15,))
            button.grid(row=row, column=column, padx=40, pady=20, sticky="ew")
            self.button_list.append(button)
            
# Function to root window
def main():
    root=ctk.CTk()
    app=Language(root)
    root.mainloop()
    
# Run the program
if __name__=="__main__":
    main()