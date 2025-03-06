# run all unit tests with: python3 -m unittest discover unit_tests

import unittest
import os
import json
from chord_progression_generator_dir.chord_progression_generator import Progression

KEYS_JSON_PATH = os.path.join('jsons_dir', 'keys.json')
CHORDS_JSON_PATH = os.path.join('jsons_dir', 'chords.json')

with open(KEYS_JSON_PATH, 'r') as file:
    keys = json.load(file)

with open(CHORDS_JSON_PATH, 'r') as file:
    chords = json.load(file)

class TestGeneratedProgression(unittest.TestCase):
    def test_progression(self):
        for key in keys:
            with self.subTest(key=key):
                length = 7
                progression = Progression(length, key)

                generated_chords = {keys[key].get(roman) for roman in progression.chords}
                expected_chords = set(keys[key].values())

                for chord in generated_chords:
                    self.assertIn(chord, expected_chords, f"Unexpected chord {chord} in {key}")

                expected_note_sets = {frozenset(chords[chord].values()) for chord in expected_chords}

                for note_set in progression.note_sets:
                    self.assertIn(frozenset(note_set), expected_note_sets, f"Unexpected note set {note_set} in {key}")

if __name__ == "__main__":
    unittest.main()
