import customtkinter
from PIL import Image
import sys

sys.path.append('./')
from main import generate_chord_progression

class CPPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chord Progression Generator")
        self.geometry("750x500")

        # Background image
        bg_image_path = "gui/images/wavy-background.jpg"
        self.bg_image = customtkinter.CTkImage(dark_image=Image.open(bg_image_path), size=(750, 500))
        self.bg_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relwidth=1, relheight=1)

        # Frame
        self.frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Title
        self.label = customtkinter.CTkLabel(self.frame, text="Chord Progression Generator", font=("Aptos", 24))
        self.label.pack(pady=10, padx=10)

        # Choice Box (Dropdown)
        self.key_option = customtkinter.CTkComboBox(self.frame, values=["C_major", "A_minor"])
        self.key_option.pack(pady=10)

        # Generate Button
        self.generate_button = customtkinter.CTkButton(self.frame, text="Generate", command=self.generate_progression)
        self.generate_button.pack(pady=10)

        # Back Button
        self.back_button = customtkinter.CTkButton(self.frame, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def generate_progression(self):
        selected_key = self.key_option.get()
        print(f"Generating progression for {selected_key}")
        generate_chord_progression(selected_key, 5, "generated_prog")

    def go_back(self):
        """Redirects back to main page."""
        self.destroy()
        from main_page import MainPage
        main_window = MainPage()
        main_window.mainloop()

# Run CP Page
if __name__ == "__main__":
    app = CPPage()
    app.mainloop()
