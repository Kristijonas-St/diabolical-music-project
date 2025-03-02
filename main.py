import json
from chord_progression_generator_dir.chord_progression_generator import get_note_sets
from chord_progression_generator_dir.mid_file_generator import generate_mid_file

key = "C_major"
feature = "chord generator"
filename = "Generated_chord_progression_in_" + key.upper()

def main():
    match feature:
        case "chord generator":
            generated_progression = get_note_sets(key)
            generate_mid_file(generated_progression, filename + ".mid")
        case "piano chord trainer":
            print("Piano chord trainer NOT YET developed")
        case "tuner":
            print("Tuner NOT YET developed")
        case _:
            print("Feature possible doesn't exist")

if __name__ == "__main__":
    main()

