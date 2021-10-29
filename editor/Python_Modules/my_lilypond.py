import mingus.core.value as value
from mingus.containers import Note
from mingus.core.keys import Key
from mingus.extra import lilypond
from BuildScore import Tempo


def my_from_Bar(bar, showkey=True, showtime=True, showtempo=False):
    """Get a Bar object and return the LilyPond equivalent in a string.

    The showkey and showtime parameters can be set to determine whether the
    key and the time should be shown.
    """
    # Throw exception
    if not hasattr(bar, "bar"):
        return False

    # Process the key
    if showkey:
        key_note = Note(bar.key.key[0].upper() + bar.key.key[1:])
        key = "\\key %s \\%s " % (
            lilypond.from_Note(key_note, False, standalone=False),
            bar.key.mode,
        )
        result = key
    else:
        result = ""

    # Handle the NoteContainers
    latest_ratio = (1, 1)
    ratio_has_changed = False
    for bar_entry in bar.bar:
        parsed_value = value.determine(bar_entry[1])
        ratio = parsed_value[2:]
        if ratio == latest_ratio:
            result += (
                from_NoteContainer(bar_entry[2], bar_entry[1], standalone=False) + " "
            )
        else:
            if ratio_has_changed:
                result += "}"
            result += "\\times %d/%d {" % (ratio[1], ratio[0])
            result += (
                from_NoteContainer(bar_entry[2], bar_entry[1], standalone=False) + " "
            )
            latest_ratio = ratio
            ratio_has_changed = True
    if ratio_has_changed:
        result += "}"

    # Process the time
    if showtime:
        return "{ \\time %d/%d %s}" % (bar.meter[0], bar.meter[1], result)
    else:
        return "{ %s}" % result

    # Process the tempo
    if showtempo:



def my_from_Track(track, texts):
    """Process a Track object and return the LilyPond equivalent in a string."""
    # Throw exception
    if not hasattr(track, "bars"):
        return False
    lastkey = Key("C")
    lasttime = (4, 4)

    # Handle the Bars:
    result = ""
    for bar in track.bars:
        if lastkey != bar.key:
            showkey = True
        else:
            showkey = False
        if lasttime != bar.meter:
            showtime = True
        else:
            showtime = False
        result += my_from_Bar(bar, showkey, showtime, showtempo) + " "
        lastkey = bar.key
        lasttime = bar.meter
    return "{ %s}" % result


def my_from_Composition(composition, texts):
    """Return the LilyPond equivalent of a Composition in a string."""
    # warning Throw exception
    if not hasattr(composition, "tracks"):
        return False
    result = '\\header { title = "%s" composer = "%s" opus = "%s" } ' % (
        composition.title,
        composition.author,
        composition.subtitle,
    )
    for track in composition.tracks:
        result += my_from_Track(track, texts) + " "
    return result[:-1]
