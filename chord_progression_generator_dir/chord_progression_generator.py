import json
import os
import random

keys_json_path = os.path.join('jsons_dir', 'keys.json')
numbers_json_path = os.path.join('jsons_dir', 'numbers.json')  
chords_json_path = os.path.join('jsons_dir', 'chords.json')


def read_keys_json(filepath):
    with open(filepath, 'r') as file:
        global keys
        keys = json.load(file)

def read_numbers_json(file_path):
    with open(file_path, 'r') as file:
        global numbers
        numbers = json.load(file)

def read_chords_json(filepath):
    with open(filepath, 'r') as file:
        global chords
        chords = json.load(file)




def five_chord_generator():
    return [numbers.get(str(random.randint(1, 7))) for _ in range(5)]

def get_note_sets(key):
    five_chords = five_chord_generator()
    notes = []
    return form_note_sets(five_chords, notes, key)

def form_note_sets(five_chords, notes, key):
    temp_chord_list = []
    convert_numbers_to_chords(five_chords, temp_chord_list, key)
    for chord in temp_chord_list:
        chord_notes = chords.get(str(chord))
        if chord_notes:
            notes.append(set(chord_notes.values()))
    return notes 

def convert_numbers_to_chords(five_chords, temp_chord_list, key):
    for chord in five_chords:
        temp_chord_list.append(keys.get(key, {}).get(str(chord)))

# Load JSON data at import time
read_keys_json(keys_json_path)
read_numbers_json(numbers_json_path)
read_chords_json(chords_json_path)
