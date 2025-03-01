import json
import os
import random

keys_json_path = os.path.join('jsons-dir', 'keys.json')
numbers_json_path = os.path.join('jsons-dir', 'numbers.json')  
chords_json_path = os.path.join('jsons-dir', 'chords.json')

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

def five_chord_generator(five_chords):
    for i in range(5):
        random_chord = random.randint(1, 7)
        five_chords.append(numbers.get(random_chord.__str__()))

def get_note_sets(five_chords, notes):
    temp_chord_list = []
    convert_numbers_to_chords(five_chords, temp_chord_list)
    for chord in temp_chord_list:
        notes.append(chords.get(chord.__str__()))
    print(notes)


def convert_numbers_to_chords(five_chords, temp_chord_list):
    for chord in five_chords:
        temp_chord_list.append(keys.get('C_major').get(chord.__str__()))


five_chord_progression = []
chords_in_notes = []

read_keys_json(keys_json_path)
read_numbers_json(numbers_json_path)
read_chords_json(chords_json_path)

five_chord_generator(five_chord_progression)
get_note_sets(five_chord_progression, chords_in_notes)


