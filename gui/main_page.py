import customtkinter
from PIL import Image
import sys

sys.path.append('./')
from main import generate_chord_progression, use_piano_trainer, use_tuner

class MainPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Diabolical Music Project")
        self.geometry("750x500")

        # Main frame
        self.frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Logo Image
        image_path = "gui/images/wizards-making-beats.png"
        self.logo_image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
        self.image_label = customtkinter.CTkLabel(self.frame, image=self.logo_image, text="")
        self.image_label.pack(pady=10, padx=10)

        # Title Label
        self.label = customtkinter.CTkLabel(self.frame, text="DIABOLICAL MUSIC PROJECT", font=("Aptos", 24))
        self.label.pack(pady=10, padx=10)

        # Buttons Frame
        self.button_frame = customtkinter.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.pack(pady=20, padx=60, fill="x", expand=True)

        # Buttons
        self.cp_button = customtkinter.CTkButton(self.button_frame, text="Chord progression generator", command=self.open_cp_page)
        self.cp_button.pack(side="left", padx=20, expand=True)

        self.pt_button = customtkinter.CTkButton(self.button_frame, text="Piano trainer", command=self.pt_button_pressed)
        self.pt_button.pack(side="left", padx=20, expand=True)

        self.t_button = customtkinter.CTkButton(self.button_frame, text="Tuner", command=self.t_button_pressed)
        self.t_button.pack(side="left", padx=20, expand=True)

    def open_cp_page(self):
        self.destroy()
        from cp_page import CPPage
        cp_window = CPPage()
        cp_window.mainloop()

    def pt_button_pressed(self):
        print("Piano Trainer is pressed")

    def t_button_pressed(self):
        print("Tuner is pressed")

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
