#This Module contains all the classes that represent the instuments the user can write music for.
#Each class inherits from the Instrument class

from mingus.containers import Instrument, Note

class Piano(Instrument):
    name = "Acoustic Grand Piano"
    range = (Note('F', 0), Note('B', 8))
    def __init__(self):
        Instrument.__init__(self)

class Harpsichord(Instrument):
    name = "Harpsichord"
    range = (Note('F', 1), Note('F', 6))
    def __init__(self):
        Instrument.__init__(self)

class Glockenspiel(Instrument):
    name = "Glockenspiel"
    range = (Note('G', 5), Note('C', 8))
    def __init__(self):
        Instrument.__init__(self)

class Marimba(Instrument):
    name = "Marimba"
    range = (Note('C', 2), Note('C', 7))
    def __init__(self):
        Instrument.__init__(self)

class Organ(Instrument):
    name = "Church Organ"
    range = (Note('C', 2), Note('F', 6))
    def __init__(self):
        Instrument.__init__(self)

class Accordion(Instrument):
    name = "Accordion"
    range = (Note('F', 3), Note('A', 6))
    def __init__(self):
        Instrument.__init__(self)

class Harmonica(Instrument):
    name = "Harmonica"
    range = (Note('C', 2), Note('C', 5))
    def __init__(self):
        Instrument.__init__(self)

class AcousticGuitar(Instrument):
    name = "Acoustic Guitar (nylon)"
    range = (Note('E', 3), Note('E', 7))
    def __init__(self):
        Instrument.__init__(self)

class ElectricGuitar(Instrument):
    name = "Electric Guitar (clean)"
    range = (Note('E', 3), Note('E', 7))
    def __init__(self):
        Instrument.__init__(self)

class AcousticBass(Instrument):
    name = "Acoustic Bass"
    range = (Note('E', 1), Note('Eb', 5))
    def __init__(self):
        Instrument.__init__(self)

class ElectricBass(Instrument):
    name = " Electric Bass (finger)"
    range = (Note('E', 1), Note('Eb', 5))
    def __init__(self):
        Instrument.__init__(self)


class Violin(Instrument):
    name = "Violin"
    range = (Note('G', 3), Note('A', 7))
    def __init__(self):
        Instrument.__init__(self)

class Viola(Instrument):
    name = "Viola"
    range = (Note('C', 3), Note('E', 6))
    def __init__(self):
        Instrument.__init__(self)

class Cello(Instrument):
    name = "Cello"
    range = (Note('C', 2), Note('E', 6))
    def __init__(self):
        Instrument.__init__(self)

class Contrabass(Instrument):
    name = "Contrabass"
    range = (Note('E', 1), Note('D', 5))
    def __init__(self):
        Instrument.__init__(self)

class Harp(Instrument):
    name = "Orchestral Harp"
    range = (Note('Cb', 1), Note('Gb', 7))
    def __init__(self):
        Instrument.__init__(self)

class Timpani(Instrument):
    name = 'Timpani'
    range = (Note('D', 2), Note('C', 4))
    def __init__(self):
        Instrument.__init__(self)

class Trumpet(Instrument):
    name = "Trumpet"
    range = (Note('F#', 3), Note('F#', 6))
    def __init__(self):
        Instrument.__init__(self)

class Trombone(Instrument):
    name = "Trombone"
    range = (Note('E', 2), Note('F', 5))
    def __init__(self):
        Instrument.__init__(self)

class Tuba(Instrument):
    name = "Tuba"
    range = (Note('D', 1), Note('F', 4))
    def __init__(self):
        Instrument.__init__(self)

class SopranoSax(Instrument):
    name = "Soprano Sax"
    range = (Note('Bb', 3), Note('G', 6))
    def __init__(self):
        Instrument.__init__(self)

class Oboe(Instrument):
    name = "Oboe"
    range = (Note('Bb', 3), Note('A', 6))
    def __init__(self):
        Instrument.__init__(self)

class Bassoon(Instrument):
    name = "Bassoon"
    range = (Note('Bb', 1), Note('Eb', 5))
    def __init__(self):
        Instrument.__init__(self)

class Clarinet(Instrument):
    name = "Clarinet"
    range = (Note('E', 3), Note('C', 7))
    def __init__(self):
        Instrument.__init__(self)

class Piccolo(Instrument):
    name = "Piccolo"
    range = (Note('D', 4), Note('C', 7))
    def __init__(self):
        Instrument.__init__(self)

class Flute(Instrument):
    name = "Flute"
    range = (Note('C', 4), Note('D', 7))
    def __init__(self):
        Instrument.__init__(self)
