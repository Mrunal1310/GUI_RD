import customtkinter as ctk
from PIL import Image
import os

class DPIWindow:
    def __init__(self, root):
        self.dpi_wnd = root  # the main window
        self.dpi_wnd.title("DPI")
        self.dpi_wnd.geometry("1200x800")
        self.dpi_wnd.config(bg="white")

        # Configure grid layout for main window
        self.dpi_wnd.columnconfigure((0, 1, 2), weight=1)
        self.dpi_wnd.rowconfigure((0), weight=1)
        self.dpi_wnd.rowconfigure((1, 2), weight=1)

        self.create_title_frame()
        self.create_button_frame()

    def get_image_path(self, image_name):
        """Returns the full path to the image file."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir = os.path.join(script_dir,"images")  # Go up one directory and access 'images' folder
        image_path = os.path.join(image_dir, image_name)  # Construct the full image path
        return image_path

    def load_image(self, image_name):
        """Load and return an image with exception handling."""
        image_path = self.get_image_path(image_name)
        try:
            image = Image.open(image_path)  # Try to open the image file
            image.close()  # To close the image file
            return ctk.CTkImage(dark_image=image)  # Return the image wrapped as CTkImage
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")

    def create_title_frame(self):
        """Create the title frame with a close button and title label."""
        frame1 = ctk.CTkFrame(self.dpi_wnd, fg_color="#A83232", corner_radius=0)
        frame1.columnconfigure((0, 1, 2), weight=1)
        frame1.rowconfigure(0, weight=0)

        # Load close button image
        image_close = self.load_image("close_icon.png")
        if image_close:
            close_button = ctk.CTkButton(frame1, command=self.dpi_wnd.destroy, text="", image=image_close, 
                                         hover_color="#A83232", fg_color="#A83232", bg_color="#A83232", width=50, corner_radius=0)
            close_button.grid(row=0, column=2, sticky='e')

        # Title label
        label1 = ctk.CTkLabel(frame1, text="DPI", fg_color="#A83232", bg_color="#A83232", anchor='center',
                              text_color="white", font=("aerial", 20, 'bold'))
        label1.grid(row=0, column=1, pady=5, sticky="n")

        # Add frame to main window
        frame1.grid(row=0, column=0, columnspan=3, sticky="new")

    def create_button_frame(self):
        """Create the button frame with size buttons."""
        frame2 = ctk.CTkFrame(self.dpi_wnd, fg_color="white", bg_color="white")
        frame2.grid(row=1, column=1)

        frame2.columnconfigure((0, 1), weight=1)
        frame2.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Create buttons
        button_specs = [
            ("300*300", 0, 0), ("300*150", 1, 0), ("300*100", 2, 0),
            ("150*300", 0, 1), ("150*150", 1, 1), ("150*100", 2, 1)
        ]
        for text, row, col in button_specs:
            self.create_button(frame2, text, row, col)

    def create_button(self, frame, text, row, col):
        """Helper method to create buttons."""
        button = ctk.CTkButton(frame, text=text, corner_radius=0, width=400, height=40, fg_color="#FF00FF", 
                               hover_color="pink", text_color="black", font=("aerial", 15, 'bold'))
        button.grid(row=row, column=col, padx=40, pady=15)

def main():
    """Initialize and run the application."""
    dpi_wnd = ctk.CTk()
    app = DPIWindow(dpi_wnd)  # Create the DPI window instance
    dpi_wnd.mainloop()  # Run the Tkinter event loop

if __name__ == "__main__":
    main()
