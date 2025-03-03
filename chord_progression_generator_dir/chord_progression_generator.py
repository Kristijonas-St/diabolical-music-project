import json
import os
import random

KEYS_JSON_PATH = os.path.join('jsons_dir', 'keys.json')
NUMBERS_JSON_PATH = os.path.join('jsons_dir', 'numbers.json')  
CHORDS_JSON_PATH = os.path.join('jsons_dir', 'chords.json')

def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
    
keys = read_json(KEYS_JSON_PATH)
numbers = read_json(NUMBERS_JSON_PATH)
chords = read_json(CHORDS_JSON_PATH)



class Progression:
    def __init__(self, length, key):
        self.length = length
        self.key = key
        self.chords = set()
        self.note_sets = []
        self.generate_chord_progression()

    def generate_chord_progression(self):
        while self.chords.__len__() != self.length:
            self.chords.add(numbers.get(str(random.randint(1, 7))))
        self.form_note_sets()
    
    def form_note_sets(self):
        temp_chord_list = []
        self.convert_numbers_to_chords(temp_chord_list)
        for chord in temp_chord_list:
            chord_notes = chords.get(str(chord))
            if chord_notes:
                self.note_sets.append(set(chord_notes.values()))

    def convert_numbers_to_chords(self, temp_chord_list):
        for chord in self.chords:
            temp_chord_list.append(keys.get(self.key, {}).get(str(chord)))

    def get_note_sets(self):
        return self.note_sets
    



