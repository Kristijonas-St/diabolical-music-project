import customtkinter
from tkinter import messagebox
from PIL import Image
import sys
import json
import re
import os

sys.path.append('./')
from main import generate_chord_progression

filename_prompt = "Insert your desired file name (without whitespaces)"
filepath_prompt = "Insert your desired file path (without whitespaces and dots)"

class CPPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CHORD PROGRESSION GENERATOR")
        self.geometry("750x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.label = customtkinter.CTkLabel(self, text="CHORD PROGRESSION GENERATOR", font=("Aptos", 24))
        self.label.grid(row=0, column=0, padx=10, pady=20, sticky="ew", columnspan=3)

        keys_list = get_keys_from_json()
        self.key_option = customtkinter.CTkComboBox(self, values=keys_list)
        self.key_option.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.key_option.set("")

        self.length_option = customtkinter.CTkComboBox(self, values=['1', '2', '3', '4', '5', '6', '7'])
        self.length_option.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.length_option.set("")

        self.file_name = customtkinter.CTkTextbox(self, width=450, height=28)        
        self.file_name.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.file_name.insert("0.0", "Insert your desired file name (without whitespaces)")

        self.file_path = customtkinter.CTkTextbox(self, width=450, height=28)
        self.file_path.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.file_path.insert("0.0", "Insert your desired file path (without whitespaces and dots)")

        self.info = customtkinter.CTkTextbox(self, width=200, height=350)
        self.info.grid(row=1, column=2, rowspan=4, padx=20, pady=20)
        self.info.configure(state="disabled")

        self.create_option = customtkinter.CTkButton(self, width=30, height=28, text="CREATE", fg_color="green", command=self.initiate_generation)
        self.create_option.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="")

        self.go_back_option = customtkinter.CTkButton(self, width=20, height=28, text="Go back", fg_color="blue", command=self.go_back_to_main)
        self.go_back_option.grid(row=5, column=0, padx=10, sticky="w")

    def initiate_generation(self):
        selected_key = self.key_option.get()
        selected_length = self.length_option.get()
        selected_filename = self.file_name.get("1.0", "end").strip()
        selected_filepath = self.file_path.get("1.0", "end").strip()


        if selected_key == "" and selected_length == "" and selected_filename == filename_prompt and selected_filepath == filepath_prompt:
            messagebox.showerror("Error", "Please fill in the necessary forms")
        elif self.check_inputs_validity(selected_key, selected_length, selected_filename, selected_filepath):
            print("Generating MIDI file...")
            generate_chord_progression(selected_key, int(selected_length), selected_filename, selected_filepath)
            messagebox.showinfo("Success", f"MIDI file '{selected_filename}' was created successfully!")
            self.clear_selections()
        

    def check_inputs_validity(self, selected_key, selected_length, selected_filename, selected_filepath):
        errors = []

        key_error = self.check_combo_boxes(selected_key, selected_length)
        if key_error:
            errors.append(key_error)

        filename_error = self.check_filename(selected_filename)
        if filename_error:
            errors.append(filename_error)

        filepath_error = self.check_filepath(selected_filepath)
        if filepath_error:
            errors.append(filepath_error)

        for error in errors:
            messagebox.showerror("Error", error)

        return len(errors) == 0

    def check_combo_boxes(self, selected_key, selected_length):
        if not selected_key or not selected_length:
            return "Please ensure that you've selected both key and length."
        return None

    def check_filename(self, selected_filename):
        if len(selected_filename) > 50:
            return "Filename too long! Keep it under 50 characters."

        cleaned_filename = re.sub(r'[^a-zA-Z0-9\s.]', '', selected_filename)
        cleaned_filename = cleaned_filename.replace(" ", "-").replace(".", "")

        if not cleaned_filename:
            return "Invalid filename format. Avoid special characters."

        return None

    def check_filepath(self, selected_filepath):
        expanded_path = os.path.expanduser(selected_filepath)

        if not os.path.exists(expanded_path):
            return "Invalid file path. Ensure the directory exists."

        return None

    def clear_selections(self):
        self.key_option.set("")
        self.length_option.set("")
        
        self.file_name.delete("1.0", "end")
        self.file_path.delete("1.0", "end")
        
        self.file_name.insert("1.0", "Insert your desired file name (without whitespaces)")
        self.file_path.insert("1.0", "Insert your desired file path (without whitespaces and dots)")

    def go_back_to_main(self):
        """Redirects back to main page."""
        self.destroy()
        from main_page import MainPage
        main_window = MainPage()
        main_window.mainloop()

def get_keys_from_json():
    with open('jsons_dir/keys.json', 'r') as file:
        values = json.load(file)
        return list(values.keys())

if __name__ == "__main__":
    app = CPPage()
    app.mainloop()
