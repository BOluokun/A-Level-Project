from .BuildScore import select_instrument, select_track
from mingus.containers import Track, Note, Composition, Bar
import mingus.core.value as value
import mingus.core.keys as keys
from mingus.extra import lilypond
from mingus.midi import midi_file_out
import os
import subprocess


#Updates score when change is made
def update_score(current_score, composition):
    #Converting composition object into lilypond format
    lilypond_string = '\\version "2.10.33"\n' + lilypond.from_Composition(composition)
    #Updating lilypond file in score record
    lily_file = current_score.score_file
    lily_file.open('w')
    lily_file.write(lilypond_string)
    lily_file.close()
    #Creating pdf format of file
    command =  "./editor/static/libraries/%s" %(lily_file.name)
    p = subprocess.Popen(command, shell=True).wait()
    #os.remove('/editor/static/libraries/' + lily_file.name[:-3] + ".log")
    #Updating MIDI file in score record
    midi_file = current_score.music_file
    m_path = "./editor/static/libraries/%s" %(midi_file.name)
    midi_file_out.write_Composition(m_path, composition)
    current_score.save()

def save_comp(score, composition):
    # Opens text file that is going to hold the information to save composition object details
    # Each track is separated by a '?'. Instrument name and bars are separated by a ';'. Bar details are separated by a '~', notes are separated by s '+'
    file = score.composition_file
    file.open('w')
    comp_string = ''
    #Iterating through each track
    for t in composition.tracks:
        #Saving the track name (instrument name)
        comp_string += str(t.instrument.name) + ';'
        for b in t.bars:
            #Saving the key, meter and bar list of each Bar in the track
            comp_string += b.key.key + '~'
            comp_string += str(b.meter[0]) +'~'
            comp_string += str(b.meter[1]) + '~'
            b_list = [str(n) for n in b.bar]
            b_string = '+'.join(b_list)
            comp_string += b_string + ';'
        comp_string += '?'
    file.write(comp_string)
    file.close()
    score.save()

#Sets the metre of multiple bars in a track (from given bar
#bar_num to the end of the track)
#If no bar given, default bar 1. If no metre given, default 4/4.
def set_bar_metre(composition, metre = (4, 4), bar_num = 1):
    for t in composition.tracks:
        for i in range(bar_num - 1, len(t)):
            t[i].set_meter(metre)

#Sets the key of multiple bars in a track (from given
#bar_num to end of track)
#Returns the notes in that key as a list
def set_bar_key(composition, key_sig = "C", bar_num = 1):
    for t in composition.tracks:
        for i in range(bar_num - 1, len(t)):
            t[i].key.key = key_sig

#Adds instrument track to composition object holding score
def add_instrument(composition, instrument_name):
    instrument = select_instrument(instrument_name)
    new_track = Track(instrument)
    new_track.name = instrument.name
    #Dealing with duplicate instrument names
    n = 1
    for track in composition:
        if track.instrument.name == new_track.name:
            n += 1
    if n > 1:
        new_track.name += ' (' + str(n) + ')'
    new_track + Bar()
    composition + new_track

#Adds a note to a specific bar in a specific track
#Adds a rest if no note specified
def add_note(composition, duration, instrument_track, note_name = None, octave = None, bar = None, position = None):
    t = select_track(instrument_track, composition)
    #Choosing between a not and a rest
    if note_name == None and octave == None:
        new_note = None
    else:
        new_note = Note(note_name, octave)
    # Selects the length of note
    if duration == "semibreve":
        length = value.semibreve
    elif duration == "minim":
        length = value.minim
    elif duration == "crotchet":
        length = value.crotchet
    elif duration == "quaver":
        length = value.quaver
    elif duration == "semiquaver":
        length = value.semiquaver
    elif duration == "demisemiquaver":
        length = value.demisemiquaver
    #Triplet rhythms
    elif duration == "triplet crotchet":
        length = value.triplet(value.crotchet)
    elif duration == "triplet quaver":
        length = value.triplet(value.quaver)
    elif duration == "triplet semiquaver":
        length = value.triplet(value.semiquaver)
    #Dotted rhythms
    elif duration == "dotted semibreve":
        length = value.dots(value.semibreve)
    elif duration == "dotted minim":
        length = value.dots(value.minim)
    elif duration == "dotted crotchet":
        length = value.dots(value.crotchet)
    elif duration == "dotted quaver":
        length = value.dots(value.quaver)
    elif duration == "dotted semiquaver":
        length = value.dots(value.semiquaver)
    elif duration == "dotted demisemiquaver":
        length = value.dots(value.demisemiquaver)
    #Selecting correct bar from chosen track
    #Adding note to the very end of track
    if bar == None and position == None:
        chosen_bar = t[-1]
        #Checking if note will fit in bar
        space_left = chosen_bar.value_left()
        #If not, splitting up the note
        if space_left < length:
            chosen_bar.place_notes(new_note, space_left)
            t.add_notes(new_note, length - space_left)
        else:
            chosen_bar.place_notes(new_note, length)
    #Adding note to specifc bar and position
    elif bar != None and position != None:
        chosen_bar = t[bar - 1]
        #Converting the position to the format used in the bar object
        beat = (position - 1) / (chosen_bar.length * 4)
        space_left = 1 / (chosen_bar.length - beat)
        temp1 = chosen_bar.current_beat
        chosen_bar.current_beat = beat
        if space_left < length:
            chosen_bar.place_notes(new_note, space_left)
            try:
                next_bar = t[bar]
            except IndexError:
                t + Bar()
                next_bar = t[bar]
            temp2 = next_bar.current_beat
            next_bar.current_beat = 0.0
            next_bar.place_notes(new_note, length - space_left)
            next_bar.current_beat = temp2
        else:
            chosen_bar.place_notes(new_note, length)
        chosen_bar.current_beat = temp1

#Removes a specific note from the score and replaces it with a rest
def delete_note(composition, instrument_track, bar, position):
    t = select_track(instrument_track, composition)
    chosen_bar = t[bar - 1]
    beat = (position - 1) / (chosen_bar.length * 4)
    temp = chosen_bar.current_beat
    chosen_bar.current_beat = beat
    #Finding the note at the specified position
    for n in chosen_bar:
        if n[0] == beat:
            duration = n[1]
            chosen_bar.place_rest(duration)

#Removes a track from the score
def delete_track(composition, instrument_track):
    track = select_track(instrument_track, composition)
    composition.tracks.remove(track)
