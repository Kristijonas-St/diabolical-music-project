import customtkinter
from PIL import Image
import sys
import json

sys.path.append('./')
from main import generate_chord_progression

class CPPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CHORD PROGRESSION GENERATOR")
        self.geometry("750x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.label = customtkinter.CTkLabel(self, text="CHORD PROGRESSION GENERATOR", font=("Aptos", 24))
        self.label.grid(row=0, column=0, padx=10, pady=20, sticky = "ew", columnspan=3)

        keys_list = get_keys_from_json()
        self.key_option = customtkinter.CTkComboBox(self, values = keys_list)
        self.key_option.grid(row = 1, column = 0, padx = 20, pady = 10, sticky="ew")
        self.key_option.set("")

        self.length_option = customtkinter.CTkComboBox(self, values = ['1', '2', '3', '4', '5', '6', '7'])
        self.length_option.grid(row =1, column = 1, padx = 20, pady = 10, sticky="ew")
        self.length_option.set("")

        self.file_name = customtkinter.CTkTextbox(self, width=450, height=28)        
        self.file_name.grid(row=2, column=0, columnspan = 2,padx=20, pady=10, sticky="ew")
        self.file_name.insert("0.0", "Insert your desired file name (without whitespaces)")

        self.file_path = customtkinter.CTkTextbox(self, width=450, height=28)
        self.file_path.grid(row=3, column=0, columnspan = 2, padx=20, pady=10, sticky="ew")
        self.file_path.insert("0.0", "Insert your desired file path (without whitespaces and dots)")

        self.info = customtkinter.CTkTextbox(self, width=200, height=350)
        self.info.grid(row=1, column = 2, rowspan = 4, padx = 20, pady = 20)

        self.create_option = customtkinter.CTkButton(self, width=30, height=28, text="CREATE", fg_color="green", command=self.initiate_generation)
        self.create_option.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="")


        self.go_back_option = customtkinter.CTkButton(self, width=20, height=28, text="Go back", fg_color="blue", command=self.go_back_to_main)
        self.go_back_option.grid(row=5, column=0, padx=10, sticky="w")

    def initiate_generation(self):
        selected_key = self.key_option.get()
        selected_length = self.length_option.get()

        if not selected_length or not selected_key:
            print("Please ensure that you've selected both key and lenght")
        else:
            print("Let's gooo")

        

        #generate_chord_progression(selected_key, int(selected_length), "generated_prog")
        #print(f"Generating progression for {selected_key}, length: {selected_length}")

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
