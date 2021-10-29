from mingus.containers import Track, Note, Composition, Bar, MidiInstrument
import mingus.core.value as value
import mingus.core.keys as keys
from mingus.extra import lilypond
from mingus.midi import midi_file_out
from django.shortcuts import get_object_or_404
from libraries.models import Score
import os
import subprocess


#Creates and returns a new score record linked to curent user
def new_score(title, current_user):
    #removing spaces from title so it can be used in file names
    title_strip = title.replace(' ', '_')
    #Creating empty files needed
    p = subprocess.Popen('echo > editor/static/libraries/%s'%(title_strip+'.ly'), shell=True).wait()
    p = subprocess.Popen('echo > editor/static/libraries/%s'%(title_strip+'_comp.txt'), shell=True).wait()
    p = subprocess.Popen('echo > editor/static/libraries/%s'%(title_strip+'_music.midi'), shell=True).wait()
    p = subprocess.Popen('echo > editor/static/libraries/%s'%(title_strip+'.pdf'), shell=True).wait()
    #Creating new Score record
    score_new = Score(title = title, author = current_user.username, score_file = title_strip+".ly", composition_file = title_strip+'_comp.txt', music_file = title_strip+'_music.midi', pdf_file = title_strip+'.pdf', user = current_user)
    score_new.save()
    return score_new

#Creates and returns a new composition object for new score made
def new_composition(current_score):
    #Creating Composition object
    comp = Composition()
    #Setting the title and author
    comp.set_author(current_score.author)
    comp.set_title(current_score.title)
    comp + Track(MidiInstrument(select_instrument('Acoustic Grand Piano')))
    comp + Bar()
    return comp

#Selects the correct instrument when given the
#instrument name as a string
def select_instrument(instrument_name):
    if instrument_name == 'Acoustic Grand Piano':
        #instance of a MidiInstrument object is created
        #with the corresponding instrument name
        instrument = MidiInstrument(instrument_name)
        #instrument_nr attribute is changed to set the
        #sound of the instrument in the midi audio file
        instrument.instrument_nr = 1
        instrument.range = (Note('F', 0), Note('B', 8))
    elif instrument_name == 'Harpsichord':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 7
        instrument.range = (Note('F', 1), Note('F', 6))
    elif instrument_name == 'Glockenspiel':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 10
        instrument.range = (Note('G', 5), Note('C', 8))
    elif instrument_name == 'Marimba':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 13
        instrument.range = (Note('C', 2), Note('C', 7))
    elif instrument_name == 'Accordion':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 22
        instrument.range = (Note('F', 3), Note('A', 6))
    elif instrument_name == 'Church Organ':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 20
        instrument.range = (Note('C', 2), Note('F', 6))
    elif instrument_name == 'Harmonica':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 23
        instrument.range = (Note('C', 2), Note('C', 5))
    elif instrument_name == 'Acoustic Guitar':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 25
        instrument.range = (Note('E', 3), Note('E', 7))
    elif instrument_name == 'Electric Guitar':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 28
        instrument.range = (Note('E', 3), Note('E', 7))
    elif instrument_name == 'Acoustic Bass':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 33
        instrument.range = (Note('E', 1), Note('Eb', 5))
    elif instrument_name == 'Electric Bass':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 34
        instrument.range = (Note('E', 1), Note('Eb', 5))
    elif instrument_name == 'Violin':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 41
        instrument.range = (Note('G', 3), Note('A', 7))
    elif instrument_name == 'Viola':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 42
        instrument.range = (Note('C', 3), Note('E', 6))
    elif instrument_name == 'Cello':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 43
        instrument.range = (Note('C', 2), Note('E', 6))
    elif instrument_name == 'Contrabass':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 44
        instrument.range = (Note('E', 1), Note('D', 5))
    elif instrument_name == 'Orchestral Harp':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 47
        instrument.range = (Note('Cb', 1), Note('Gb', 7))
    elif instrument_name == 'Timpani':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 48
        instrument.range = (Note('D', 2), Note('C', 4))
    elif instrument_name == 'Trumpet':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 57
        instrument.range = (Note('F#', 3), Note('F#', 6))
    elif instrument_name == 'Trombone':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 58
        instrument.range = (Note('E', 2), Note('F', 5))
    elif instrument_name == 'Tuba':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 59
        instrument.range = (Note('D', 1), Note('F', 4))
    elif instrument_name == 'Soprano Sax':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 65
        instrument.range = (Note('Bb', 3), Note('G', 6))
    elif instrument_name == 'Oboe':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 69
        instrument.range = (Note('Bb', 3), Note('A', 6))
    elif instrument_name == 'Bassoon':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 71
        instrument.range = (Note('Bb', 1), Note('Eb', 5))
    elif instrument_name == 'Clarinet':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 72
        instrument.range = (Note('E', 3), Note('C', 7))
    elif instrument_name == 'Piccolo':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 73
        instrument.range = (Note('D', 4), Note('C', 7))
    elif instrument_name == 'Flute':
        instrument = MidiInstrument(instrument_name)
        instrument.instrument_nr = 74
        instrument.range = (Note('C', 4), Note('D', 7))
    else:
        instrument = None
    return instrument

#Creates new composition object containing all of the information to replicate previously saved score
def remake_composition(score):
    #Reading composition object details kept in text file into a string
    file = score.composition_file
    file.open('r')
    comp_string = file.read()
    file.close()
    #Creating composition object
    comp = Composition()
    comp.set_author(score.author)
    comp.set_title(score.title)
    #Splitting up tracks
    tracks_list = comp_string.split('?')
    for t in tracks_list:
        t_list = t.split(';')
        #Choosing correct instrument for track
        instrument_name = t_list.pop(0)
        instrument = select_instrument(instrument_name)
        if instrument != None:
            track = Track(instrument)
            #Adding bars to the track
            for b in t_list:
                if b != '' and b != None:
                    b_list = b.split('~')
                    new_bar = Bar(b_list[0], (int(b_list[1]), int(b_list[2])))
                    bar_string = b_list[3]
                    notes = bar_string.split('+')
                    for n in notes:
                        n = n.strip('[')
                        n = n.strip(']')
                        n = n.split(', ')
                        try:
                            d = float(n[1])
                            note = n[2]
                            note = note.strip('[')
                            note = note.strip("'")
                            note = note.split('-')
                            note = Note(note[0], int(note[1]))
                            new_bar.place_notes(note, d)
                        except IndexError:
                            continue
                    track + new_bar
            comp + track
        else:
            continue
    return comp

#Updates score when a change is made
def update_score(composition, score_id):
    #Converting composition object into lilypond format
    lilypond_string = '\\version "2.10.33"\n' + lilypond.from_Composition(composition)
    #Retrieving score record
    current_score = get_object_or_404(Score, pk = score_id)
    #Updating lilypond file in score record
    file = current_score.score_file
    file.open('w')
    file.write(lilypond_string)
    file.close()
    #Creating pdf format of file
    command =  ".\%s" %(file.name)
    p = subprocess.Popen(command, shell=True).wait()
    os.remove(file.name[:-3] + ".log")
    current_score.save()

def save_comp(composition, score_id):
    # Opens text file that is going to hold the
    #information to save composition object details
    # Each track is separated by a '?'. Instrument name and
    #bars are separated by a ';'. Bar details are separated by a '~'.
    score = get_object_or_404(Score, pk = score_id)
    file = score.composition_file
    file.open('w')
    comp_string = ''
    #Iterating through each track
    for t in composition.tracks:
        #Saving the track name (instrument name)
        comp_string += str(t.instrument.name) + ';'
        for b in t.bars:
            #Saving the key, meter and bar list of
            #each Bar in the track
            comp_string += b.key + '~'
            comp_string += str(b.meter[0]) +'~'
            comp_string += str(b.meter[1]) + '~'
            comp_string += str(b.bar) + ';'
        comp_string += '?'
    file.write(comp_string)
    file.close()
    score.save()

def select_track(instrument_track, composition):
    #Selecting the correct track
    for track in composition:
        if instrument_track == track.name:
            t = track
            return t
            break

#Sets the metre of multiple bars in a track (from given bar bar_num to the end of the track)
#If no bar given, default bar 1. If no metre given, default 4/4.
def set_bar_metre(instrument_track, metre = (4, 4), bar_num = 1):
    for i in range(bar_num - 1, len(instrument_track)):
        instrument_track[i].set_meter(metre)

#Sets the key of multiple bars in a track (from given bar_num to end of track)
#Returns the notes in that key as a list
def set_bar_key(instrument_track, key_sig = "C", bar_num = 1):
    for i in range(bar_num - 1, len(instrument_track)):
        instrument_track[i].key = key_sig
    return keys.get_notes(key_sig)

#Adds instrument track to composition object holding score
def add_instrument(instrument, composition):
    new_track = Track(instrument)
    new_track.name = instrument.name
    #Dealing with duplicate instrument names
    n = 1
    for track in composition:
        if track.instrument.name == new_track.name:
            n += 1
    if n > 1:
        new_track.name += ' (' + str(n) + ')'
    composition + new_track

#Adds a note to a specific bar in a specific track
#Adds a rest if no note specified
def add_note(duration, instrument_track, note_name = None, octave = None, bar = None, posistion = None, ):
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
    #selecting correct bar from chosen track
    #Adding note to the very end of track
    if bar == None and posistion == None:
        chosen_bar = instrument_track[-1]
        #Checking if note will fit in bar
        space_left = chosen_bar.value_left()
        #If not, splitting up the note
        if space_left < length:
            chosen_bar.place_notes(new_note, space_left)
            instrument_track.add_notes(new_note, length - space_left)
        else:
            chosen_bar.place_notes(new_note, space_left)
    #Adding note to specifc bar and posistion
    elif bar != None and posistion != None:
        chosen_bar = instrument_track[bar - 1]
        beat = (posistion - 1) / (chosen_bar.length * 4)
        space_left = 1 / (chosen_bar.length - beat)
        temp1 = chosen_bar.current_beat
        chosen_bar.current_beat = beat
        if space_left < length:
            chosen_bar.place_notes(new_note, space_left)
            next_bar = instrument_track[bar]
            temp2 = next_bar.current_beat
            next_bar.current_beat = 0.0
            next_bar.place_notes(new_note, length - space_left)
            next_bar.current_beat = temp2
        else:
            chosen_bar.place_notes(new_note, space_left)
        chosen_bar.current_beat = temp1
