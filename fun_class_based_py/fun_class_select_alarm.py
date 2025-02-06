import customtkinter as ctk
from PIL import Image

class SelectAlarm:
    def __init__(self, root):
        self.root = root
        self.root.title("Select alarm")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        self.root.config(bg="white")

        # Configure the grid column and rows weights of Calendar window
        self.root.columnconfigure((0,1,2), weight=1)
        self.root.rowconfigure((0,1,2), weight=1)

        # Create frames and buttons
        self.create_title_frame()
        self.create_button_frame()

    def create_title_frame(self):
        # Frame for Calendar Title
        self.frame1 = ctk.CTkFrame(self.root, fg_color="#A83232", corner_radius=0)
        self.frame1.columnconfigure((0, 1, 2), weight=1)

        # Icon for close button
        image_close = ctk.CTkImage(dark_image=Image.open("images/close_icon.png"))
        close_button = ctk.CTkButton(self.frame1, command=self.root.destroy, text="", image=image_close, hover_color="#A83232", fg_color="#A83232", width=50, height=20, corner_radius=0)
        close_button.grid(row=0, column=2, sticky='e')

        # Label for Calendar title
        label1 = ctk.CTkLabel(self.frame1, text="Select alarm", fg_color="#A83232", anchor='center', text_color="white", font=("aerial", 20, 'bold'))
        label1.grid(row=0, column=1, pady=5, padx=10, sticky="n")

        self.frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        # Frame for buttons
        self.frame2 = ctk.CTkFrame(self.root, fg_color="white", corner_radius=0)
        self.frame2.grid(row=1, column=1)

        self.frame2.columnconfigure((0, 1, 2), weight=1)
        self.frame2.rowconfigure((0, 1, 2), weight=1)

        # List of button labels
        button_labels = ["OFF", "Built in buzzer", "External alarm"]

        # For loop to create buttons dynamically
        for idx, label in enumerate(button_labels):
            button = ctk.CTkButton(self.frame2, text=label, corner_radius=0, width=400, height=40, fg_color="#FF00FF", hover_color="pink", text_color="black", font=("aerial", 15, 'bold'))
            button.grid(row=idx, column=1, padx=40, pady=15)

# Main entry point
if __name__ == "__main__":
    calendar_wnd = ctk.CTk()
    app = SelectAlarm(calendar_wnd)
    calendar_wnd.mainloop()