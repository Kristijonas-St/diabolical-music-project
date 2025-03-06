import json
from chord_progression_generator_dir.chord_progression_generator import Progression
from chord_progression_generator_dir.mid_file_generator import generate_mid_file

feature = "chord generator"

key = "A_minor_jazz"
length = 5
filename = "test-"

def main():
    match feature:
        case "chord generator":
            progression = Progression(length, key)
            generate_mid_file(progression, filename)
        case "piano chord trainer":
            print("Piano chord trainer NOT YET developed")
        case "tuner":
            print("Tuner NOT YET developed")
        case _:
            print("Feature possible doesn't exist")

if __name__ == "__main__":
    main()

