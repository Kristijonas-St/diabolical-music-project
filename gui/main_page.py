import customtkinter
from PIL import Image

import sys
sys.path.append('./') 
from main import generate_chord_progression, use_piano_trainer, use_tuner

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("750x500")

frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
frame.pack(pady=20, padx=60, fill="both", expand=True)

image_path = "gui/images/wizards-making-beats.png"
image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(300, 300))
image_label = customtkinter.CTkLabel(master=frame, image=image, text="")
image_label.pack(pady=10, padx=10)

label = customtkinter.CTkLabel(master=frame, text="DIABOLICAL MUSIC PROJECT", font=("Aptos", 24))
label.pack(pady=10, padx=10)

def cp_button_pressed():
    print("cp_button is pressed")
    generate_chord_progression("C_major_jazz", 5, "Jazzy-prog")

def pt_button_pressed():
    print("pt_button is pressed")

def t_button_pressed():
    print("t_button is pressed")

button_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
button_frame.pack(pady=20, padx=60, fill="x", expand=True)

cp_button = customtkinter.CTkButton(master=button_frame, text="Chord progression generator", command=cp_button_pressed)
cp_button.pack(side="left", padx=20, expand=True) 

pt_button = customtkinter.CTkButton(master=button_frame, text="Piano trainer", command=pt_button_pressed)
pt_button.pack(side="left", padx=20, expand=True)

t_button = customtkinter.CTkButton(master=button_frame, text="Tuner", command=t_button_pressed)
t_button.pack(side="left", padx=20, expand=True)

root.mainloop()
