#This Module contains all the classes that represent the instuments the user can write music for.
#Each class inherits from the Instrument class

from mingus.containers import MidiInstrument, Note

class Piano(MidiInstrument):
    name = "Acoustic Grand Piano"
    range = (Note('F', 0), Note('B', 8))
    def __init__(self):
        MidiInstrument.__init__(self)

class Harpsichord(MidiInstrument):
    name = "Harpsichord"
    range = (Note('F', 1), Note('F', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Glockenspiel(MidiInstrument):
    name = "Glockenspiel"
    range = (Note('G', 5), Note('C', 8))
    def __init__(self):
        MidiInstrument.__init__(self)

class Marimba(MidiInstrument):
    name = "Marimba"
    range = (Note('C', 2), Note('C', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class Organ(MidiInstrument):
    name = "Church Organ"
    range = (Note('C', 2), Note('F', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Accordion(MidiInstrument):
    name = "Accordion"
    range = (Note('F', 3), Note('A', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Harmonica(MidiInstrument):
    name = "Harmonica"
    range = (Note('C', 2), Note('C', 5))
    def __init__(self):
        MidiInstrument.__init__(self)

class AcousticGuitar(MidiInstrument):
    name = "Acoustic Guitar (nylon)"
    range = (Note('E', 3), Note('E', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class ElectricGuitar(MidiInstrument):
    name = "Electric Guitar (clean)"
    range = (Note('E', 3), Note('E', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class AcousticBass(MidiInstrument):
    name = "Acoustic Bass"
    range = (Note('E', 1), Note('Eb', 5))
    def __init__(self):
        MidiInstrument.__init__(self)

class ElectricBass(MidiInstrument):
    name = " Electric Bass (finger)"
    range = (Note('E', 1), Note('Eb', 5))
    def __init__(self):
        MidiInstrument.__init__(self)


class Violin(MidiInstrument):
    def __init__(self):
        MidiInstrument.__init__(self)
        self.name = "Violin"
        self.range = (Note('G', 3), Note('A', 7))
        self.instrument_nr = 41

class Viola(MidiInstrument):
    name = "Viola"
    range = (Note('C', 3), Note('E', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Cello(MidiInstrument):
    name = "Cello"
    range = (Note('C', 2), Note('E', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Contrabass(MidiInstrument):
    name = "Contrabass"
    range = (Note('E', 1), Note('D', 5))
    def __init__(self):
        MidiInstrument.__init__(self)

class Harp(MidiInstrument):
    name = "Orchestral Harp"
    range = (Note('Cb', 1), Note('Gb', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class Timpani(MidiInstrument):
    name = 'Timpani'
    range = (Note('D', 2), Note('C', 4))
    def __init__(self):
        MidiInstrument.__init__(self)

class Trumpet(MidiInstrument):
    name = "Trumpet"
    range = (Note('F#', 3), Note('F#', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Trombone(MidiInstrument):
    name = "Trombone"
    range = (Note('E', 2), Note('F', 5))
    def __init__(self):
        MidiInstrument.__init__(self)

class Tuba(MidiInstrument):
    name = "Tuba"
    range = (Note('D', 1), Note('F', 4))
    def __init__(self):
        MidiInstrument.__init__(self)

class SopranoSax(MidiInstrument):
    name = "Soprano Sax"
    range = (Note('Bb', 3), Note('G', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Oboe(MidiInstrument):
    name = "Oboe"
    range = (Note('Bb', 3), Note('A', 6))
    def __init__(self):
        MidiInstrument.__init__(self)

class Bassoon(MidiInstrument):
    name = "Bassoon"
    range = (Note('Bb', 1), Note('Eb', 5))
    def __init__(self):
        MidiInstrument.__init__(self)

class Clarinet(MidiInstrument):
    name = "Clarinet"
    range = (Note('E', 3), Note('C', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class Piccolo(MidiInstrument):
    name = "Piccolo"
    range = (Note('D', 4), Note('C', 7))
    def __init__(self):
        MidiInstrument.__init__(self)

class Flute(MidiInstrument):
    name = "Flute"
    range = (Note('C', 4), Note('D', 7))
    def __init__(self):
        MidiInstrument.__init__(self)
