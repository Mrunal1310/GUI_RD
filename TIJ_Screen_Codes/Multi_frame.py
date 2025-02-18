import customtkinter as ctk
from PIL import Image
import os

# Class of Multi frame cache Window
class MultiFrameCache:
    # Function to create root window
    def __init__(self, root):
        self.multi_frame_cache=root
        self.multi_frame_cache.title("Multi frame cache")
        self.multi_frame_cache.geometry("1200x800")
        self.multi_frame_cache.resizable(True, True)
        self.multi_frame_cache.config(bg="white")
        
        # Configuration of Window
        self.multi_frame_cache.columnconfigure(0, weight=1)
        self.multi_frame_cache.rowconfigure((0,1,2), weight=1)
        
        # Create widgets
        self.title_frame()
        self.button_frame()
        
    # Function to create title frame
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.multi_frame_cache,fg_color="white", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Multi frame cache",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="",image=image, command=self.multi_frame_cache.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0,sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X", command=self.multi_frame_cache.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    # Button labels list
    def button_frame(self,):
        self.frame=ctk.CTkFrame(self.multi_frame_cache, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1,2), weight=1)
        self.frame.rowconfigure((0,1,2,3), weight=1)
        self.frame.grid(row=1, column=0, pady=0,sticky="news")
        
        # Button label list
        self.button_list=[
            "OFF", "X2", "X3", "X4", "X5", "X6",
            "X7", "X8", "X9", "X10", "X11", 
        ]
        
        self.create_button()
        
    # Function to create button in rows and columns with button labels
    def create_button(self):
        for index, label in enumerate(self.button_list):
            row=index // 3
            col=index % 3
            button=ctk.CTkButton(self.frame, text = label,corner_radius=0, fg_color="#FF00FF", text_color= "black", font=("Arial", 15,))
            button.grid(row=row, column=col, padx=50, pady=20, sticky="ew")
            
# Function to root window
def main():
    root=ctk.CTk()
    app = MultiFrameCache(root)
    root.mainloop()
    
# Run the program
if __name__=="__main__":
    main()