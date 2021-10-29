import random
from mingus.containers import Note, Instrument, Track, Bar, Composition, MidiInstrument
from instruments import Violin, Clarinet
from mingus.midi import midi_file_out

m = MidiInstrument()
m.name = 'Acoustic guitar'
m.instrument_nr = 24
m_track = Track(m)

violin_track = Track(Violin())
clarinet_track = Track(Clarinet())

violin_track.add_bar(Bar('A', (3, 4)))
clarinet_track.add_bar(Bar('A', (3, 4)))

noteSelection = [Note('A'), Note('B'), Note('C'), Note('D'), Note('E'), Note('F'), Note('G')]
for i in range(8):
    violin_track + random.choice(noteSelection)
    clarinet_track + random.choice(noteSelection)
    m_track + random.choice(noteSelection)

print(m_track)
#print(violin_track)
#print(clarinet_track)

c = Composition()
c + m_track
#c + violin_track
#c + clarinet_track

print(midi_file_out.write_Composition('midiTest.midi', c))
