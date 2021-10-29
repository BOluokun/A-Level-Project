from mingus.containers import Note, NoteContainer, Bar, Instrument, Track, Composition, Piano, Guitar, MidiInstrument
from mingus.extra import lilypond
import random

noteSelection = [Note('A'), Note('B'), Note('C'), Note('D'), Note('E'), Note('F'),
                 Note('G'), Note('Ab'), Note('Bb'), Note('C#'), Note('Db'),
                 Note('Eb'), Note('F#'), Note('G#')
                 ]
#Creating composition
c = Composition()

#Creating tracks for piano, guitar and a MidiInstrument
track1 = Track(Piano()) #Remember brackets after Instrument object!!
track2 = Track(Guitar())
track3 = Track(MidiInstrument('Violin'))

#Adding tracks to composition
c + track1
c + track2
c + track3
print(c)
c.title = "test score"
c.author = "Beauty"

#Randomly adding notes to tracks
for t in c.tracks:
    t + Bar('C', (3, 4))
    for i in range(8):
        t + random.choice(noteSelection)
print(c)

# Converting to lilypond format
lilystr = lilypond.from_Composition(c)
print(lilystr)

#Creating pdf from lilypond
print(lilypond.to_pdf(lilystr, 'testPDF'))
