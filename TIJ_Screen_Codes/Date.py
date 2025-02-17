import customtkinter as ctk
from PIL import Image
import os

# Class of Date Window
class DateWindow:
    # Function to create root window
    def __init__(self, root):
        
        self.date=root
        self.date.title("Date")
        self.date.geometry("1200x800")
        self.date.resizable(True, True)
        self.date.config(bg="white")
        
        # Configuration of Window
        self.date.columnconfigure(0, weight=1)
        self.date.rowconfigure((0,1,), weight=1)
        
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame 
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.date, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Date",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="",anchor="center", image=image, command=self.date.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X",anchor="center", command=self.date.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Function to create button frame with button labels
    def button_frame(self):
        self.frame=ctk.CTkFrame(self.date, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure((0,1,2,3,4,5), weight=1)
        self.frame.grid(row=1, column=0,pady=20,sticky="news")
        
        # Button labels list
        self.button_list=[
            "2025-01-07", "2025/01/07", "2025年01月07日",
            "25/01/07", "25-01-07", "25.01.07",
            "25 01 07", "25 Jan 07", "01/07/25",
            "01-07-2025", "01.07.25", "JAN 07 25",
            "07/01/25", "07-01-25", "07.01.25",
            "23:57:54", "23:57", 
        ]
        self.create_buttons()
        
    # Function to create button in rows and columns with button labels
    def create_buttons(self):
        for index, label in enumerate(self.button_list):
            row= index // 3
            col= index % 3
            button=ctk.CTkButton(self.frame, text = label, corner_radius=0, fg_color="#FF00FF", text_color= "black", font=("Arial", 15,))
            button.grid(row=row, column=col, padx=40, pady=20, sticky="ew")
            self.button=ctk.CTkButton(self.frame, text = "Term", corner_radius=0, fg_color="#C4E3ED", text_color= "black", font=("Arial", 15,))
            self.button.grid(row=5, column=2, padx=40, pady=20, sticky="ew")
                
# Function to root window
def main():
    root=ctk.CTk()
    app=DateWindow(root)
    root.mainloop()
    
# Run the program  
if __name__=="__main__":
    main()