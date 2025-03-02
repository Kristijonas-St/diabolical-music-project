import mido
import json
import os
from mido import Message, MidiFile, MidiTrack

midi_middle_mappings_path = os.path.join('jsons_dir', 'midi_middle_mappings.json')

def read_midi_middle_mappings():
    with open(midi_middle_mappings_path, 'r') as file:
        return json.load(file)


def generate_mid_file(generated_progression, filename):
    generated_mid_files_path = os.path.expanduser(f'~/Desktop/generated_five_chords/{filename}')
    
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    midi_mappings = read_midi_middle_mappings()
    chords_in_midi = convert_chords_to_midi(generated_progression, mid, track, midi_mappings)

    for chord in chords_in_midi:
        for note in chord:
            track.append(Message('note_on', note=note, velocity = 64, time = 0)) 
        for note in chord:
            track.append(Message('note_off', note=note, velocity = 64, time = 500))
    mid.save(generated_mid_files_path)
    
def convert_chords_to_midi(generated_progression, mid, track, midi_mappings):
    chords_in_midi = []
    for chord in generated_progression:
        chord_notes = []
        for note in chord:
            chord_notes.append(midi_mappings.get(note.__str__()))
        chords_in_midi.append(chord_notes)
    return chords_in_midi
