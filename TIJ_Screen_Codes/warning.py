import customtkinter as ctk 

class WarningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("300x100")
        
        self.create_main_wnd()
        
    def create_main_wnd(self):
        self.button=ctk.CTkButton(self.root, text="Click Me",command=self.open_warnings )
        self.button.pack(padx=20, pady=20)
        
    def open_warnings(self):
        self.warning=ctk.CTkToplevel(self.root)  
        self.warning.title("Warning")
        self.warning.geometry("450x150")  
        self.warning.resizable(False, False)  
        
        self.warning.transient(self.root)  
        self.warning.grab_set()       
        self.warning.focus_force() 
        
        self.frame=ctk.CTkFrame(self.warning,fg_color="white",width=450,height=150, corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1,2,3),weight=1)
        self.frame.grid(row=0, column=0, sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="Warning",text_color="white", fg_color="#A83232",width=450, anchor="w",font=("Arial", 18, 'bold'))
        self.label.grid(row=0, column=0,sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="All data will be deleted",text_color="black", fg_color="white", anchor="w", font=("Arial", 16,))
        self.label.grid(row=1, column=0, padx=10,pady=5,sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="\nContinue?",text_color="black", fg_color="white", anchor="w", font=("Arial", 16,))
        self.label.grid(row=2, column=0, padx=10,pady=0,sticky="news")
        
        self.button=ctk.CTkButton(self.frame, text="OK",text_color="black",anchor="center", fg_color="white",border_width=1,corner_radius=0,command=self.warning.destroy, font=("Arial", 16,))
        self.button.grid(row=3, column=0, padx=40, pady=10,sticky="w")
        
        self.button=ctk.CTkButton(self.frame, text="Back",text_color="black", anchor="center",fg_color="white",border_width=1,corner_radius=0,command=self.warning.destroy, font=("Arial", 16,))
        self.button.grid(row=3, column=0, padx=60, pady=10,sticky="e")
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = WarningApp(root)
    root.mainloop()