import customtkinter as ctk
from PIL import Image
import os

class Grayscale:
    def __init__(self, root):
        
        self.grayscale=root
        self.grayscale.title("Grayscale")
        self.grayscale.geometry("1200x800")
        self.grayscale.resizable(True, True)
        self.grayscale.config(bg="white")
        
        self.configure_grid()
        self.title_frame()
        self.button_frame()
        
    def configure_grid(self):
        
        self.grayscale.columnconfigure(0, weight=1)
        self.grayscale.rowconfigure((0,1,2), weight=1)
        
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.grayscale, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="Grayscale",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Aerial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="",anchor="center", image=image, command=self.grayscale.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X",anchor="center", command=self.grayscale.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def button_frame(self):
        
        self.frame=ctk.CTkFrame(self.grayscale, fg_color="white", corner_radius=0)
        self.frame.columnconfigure((0,1), weight=1)
        self.frame.rowconfigure((0,1,2,3,4), weight=1)
        self.frame.grid(row=1, column=0, sticky="news")
        
        self.button=ctk.CTkButton(self.frame, text = "routine", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=0, column=0,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Double", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=1, column=0,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Fourfold", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=2, column=0,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Six times", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=3, column=0,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Eight times", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=4, column=0,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Bold", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=0, column=1,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Triple", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=1, column=1,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Five times", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=2, column=1,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Seven times", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=3, column=1,padx=40, pady=15, sticky="ew")
        
        self.button=ctk.CTkButton(self.frame, text = "Nine times", corner_radius=0, fg_color="#FF00FF",  text_color= "black", font=("aerial", 15, 'bold'))
        self.button.grid(row=4, column=1,padx=40, pady=15, sticky="ew")
        
def main():
    root=ctk.CTk()
    app=Grayscale(root)
    root.mainloop()
    
if __name__=="__main__":
    main()