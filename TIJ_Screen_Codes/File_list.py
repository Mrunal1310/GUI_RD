import customtkinter as ctk
from PIL import Image
import os

class FileList:
    def __init__(self, root):
        
        self.filelist=root
        self.filelist.title("File list")
        self.filelist.geometry("1200x800")
        self.filelist.resizable(True, True)
        self.filelist.config(bg="white")
        
        self.configure_grid()
        
        self.title_frame()
        self.button_frame()
        self.display_frame()
        
    def configure_grid(self):
        
        self.filelist.columnconfigure(0, weight=3)
        self.filelist.columnconfigure(1, weight=1)
        self.filelist.rowconfigure((0), weight=0)
        self.filelist.rowconfigure((1), weight=1)
        
    def title_frame(self):
        self.frame=ctk.CTkFrame(self.filelist, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, columnspan=2, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="File list",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0, sticky="new")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,)
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="",anchor="center", image=image, command=self.filelist.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            self.close_button=ctk.CTkButton(self.frame, text="X",anchor="center", command=self.filelist.destroy, hover_color="#A83232", fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def button_frame(self):
        
        self.frame=ctk.CTkFrame(self.filelist, fg_color="white",border_width=1, corner_radius=0,)
        self.frame.columnconfigure((0), weight=1)
        self.frame.rowconfigure((0,1,), weight=0)
        self.frame.grid(row=1, column=0,pady=10,padx=10, sticky="news")
        
        self.system_disk=ctk.CTkButton(self.frame, text="System disk", text_color="black",anchor="w", fg_color="white",hover_color="#FF00FF",font=("Arial", 20,),corner_radius=0, )
        self.system_disk.grid(row=0, column=0, padx=10,pady=5,sticky="news")
        
        self.user_disk=ctk.CTkButton(self.frame, text="User disk",  text_color="black",anchor="w",fg_color="white",hover_color="#FF00FF", font=("Arial", 20,), corner_radius=0,)
        self.user_disk.grid(row=1, column=0, padx=10,pady=5,sticky="news")
        
    def display_frame(self):
        
        self.frame=ctk.CTkFrame(self.filelist, fg_color="white",corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1,), weight=1)
        self.frame.grid(row=1, column=1, padx=5,pady=10, sticky="news")
        
        self.format_butn=ctk.CTkButton(self.frame, text="Format", text_color="white",fg_color="#A83232",font=("Arial", 22,),corner_radius=0, )
        self.format_butn.grid(row=1, column=0, padx=10, pady=50, sticky="es")
        
        self.open_butn=ctk.CTkButton(self.frame, text="Open",  text_color="white",fg_color="#A83232", font=("Arial", 22,), corner_radius=0,)
        self.open_butn.grid(row=1, column=0, padx=10,pady=10,sticky="es")
        
def main():
    root=ctk.CTk()
    app=FileList(root)
    root.mainloop()
    
if __name__=="__main__":
    main()