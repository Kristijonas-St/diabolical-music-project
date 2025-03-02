import json
from chord_progression_generator_dir.chord_progression_generator import get_note_sets

key = "C_major"
feature = "chord generator"

def main():
    match feature:
        case "chord generator":
            notes = get_note_sets(key)
            print(notes)
        case "piano chord trainer":
            print("Piano chord trainer NOT YET developed")
        case "tuner":
            print("Tuner NOT YET developed")
        case _:
            print("Feature possible doesn't exist")

if __name__ == "__main__":
    main()

