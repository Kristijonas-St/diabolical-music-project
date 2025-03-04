# run with all unit tests with: python3 -m unittest discover unit_tests
# run a certain unit test with: python3 -m unittest unit_tests.test_generated_progression

import unittest
import os
import json
from chord_progression_generator_dir.chord_progression_generator import Progression

# Load JSON files
KEYS_JSON_PATH = os.path.join('jsons_dir', 'keys.json')
CHORDS_JSON_PATH = os.path.join('jsons_dir', 'chords.json')

with open(KEYS_JSON_PATH, 'r') as file:
    keys = json.load(file)

with open(CHORDS_JSON_PATH, 'r') as file:
    chords = json.load(file)

class TestGeneratedProgression(unittest.TestCase):
    def test_g_major_progression(self):
        key = "G_major"
        length = 7
        progression = Progression(length, key)

        generated_chords = {keys[key].get(roman) for roman in progression.chords}
        expected_chords = {"G", "Am", "Bm", "C", "D", "Em", "F#dim"}

        print("\n🎹 Expected Chords in G Major:", expected_chords)
        print("🎼 Generated Chords in Progression:", generated_chords)

        for chord in generated_chords:
            self.assertIn(chord, expected_chords)

        expected_note_sets = {frozenset(chords[chord].values()) for chord in expected_chords}

        print("\n🎵 Expected Note Sets:")
        for chord, notes in chords.items():
            if chord in expected_chords:
                print(f"  {chord}: {set(notes.values())}")

        print("\n🎶 Generated Note Sets:")
        for note_set in progression.note_sets:
            print(f"  {note_set}")

        for note_set in progression.note_sets:
            self.assertIn(frozenset(note_set), expected_note_sets)

if __name__ == "__main__":
    unittest.main()
