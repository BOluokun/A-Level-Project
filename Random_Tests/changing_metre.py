import random
from mingus.containers import Note, Instrument, Track, Bar, Composition
from instruments import Violin, Clarinet
from mingus.extra import lilypond

violin_track = Track(Violin())
clarinet_track = Track(Clarinet())

violin_track.add_bar(Bar('A', (3, 4)))
clarinet_track.add_bar(Bar('A', (3, 4)))

noteSelection = [Note('A'), Note('B'), Note('C'), Note('D'), Note('E'), Note('F'), Note('G')]
for i in range(8):
    violin_track + random.choice(noteSelection)
for i in range(8):
    clarinet_track + random.choice(noteSelection)
print(violin_track)
print(clarinet_track)

c = Composition()
c + violin_track
c + clarinet_track

lilystring = lilypond.from_Composition(c)

print(lilypond.to_pdf(lilystring, "MetreTest"))

