import json
from chord_progression_generator_dir.chord_progression_generator import get_generated_progression
from chord_progression_generator_dir.mid_file_generator import generate_mid_file

feature = "chord generator"

key = "C_major"
length = 5
filename = "test-chord-prog"

def main():
    match feature:
        case "chord generator":
            generated_progression = get_generated_progression(7, key)
            generate_mid_file(generated_progression, filename)
        case "piano chord trainer":
            print("Piano chord trainer NOT YET developed")
        case "tuner":
            print("Tuner NOT YET developed")
        case _:
            print("Feature possible doesn't exist")

if __name__ == "__main__":
    main()

