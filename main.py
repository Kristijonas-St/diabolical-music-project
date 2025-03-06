import json
from chord_progression_generator_dir.chord_progression_generator import Progression
from chord_progression_generator_dir.mid_file_generator import generate_mid_file

def generate_chord_progression(key, length, filename):
    progression = Progression(length, key)
    generate_mid_file(progression, filename)

def use_piano_trainer():
    print("piano trainer NOT YET DEVELOPED")

def use_tuner():
    print("tuner NOT YET DEVELOPED")

if __name__ == "__main__":
    print("Welcome")
