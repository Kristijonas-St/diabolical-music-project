import json
import os
import random

class Progression:
    chords = set()
    note_sets = []

    def __init__(self, length, key):
        self.length = length
        self.key = key
    

KEYS_JSON_PATH = os.path.join('jsons_dir', 'keys.json')
NUMBERS_JSON_PATH = os.path.join('jsons_dir', 'numbers.json')  
CHORDS_JSON_PATH = os.path.join('jsons_dir', 'chords.json')

def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

keys = read_json(KEYS_JSON_PATH)
numbers = read_json(NUMBERS_JSON_PATH)
chords = read_json(CHORDS_JSON_PATH)


def get_generated_progression(length, key):
    test = Progression(length, key)
    generate_chord_progression(test)
    return test


def generate_chord_progression(prog):
    while prog.chords.__len__() != prog.length:
       prog.chords.add(numbers.get(str(random.randint(1, 7))))
    form_note_sets(prog)
    
def form_note_sets(prog):
    temp_chord_list = []
    convert_numbers_to_chords(prog, temp_chord_list)
    for chord in temp_chord_list:
        chord_notes = chords.get(str(chord))
        if chord_notes:
            prog.note_sets.append(set(chord_notes.values()))


def convert_numbers_to_chords(prog, temp_chord_list):
    for chord in prog.chords:
        temp_chord_list.append(keys.get(prog.key, {}).get(str(chord)))
