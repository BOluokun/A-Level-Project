from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User
from libraries.models import Score
from .Python_Modules.BuildScore import new_score, new_composition, remake_composition, select_instrument
from .Python_Modules.editorFunctionsNONTAG import *

from mingus.containers import Track, Note

# Create your views here.

def home(request):
    return render(request, 'editor/home.html')

def make_score(request, username):
    title = request.POST['title']
    user = get_object_or_404(User, pk = username)
    score = new_score(title, user)
    composition = new_composition(score)
    update_score(score, composition)
    save_comp(score, composition)
    return redirect('open_editor', username = username, score_id = score.scoreID)

def open_editor(request, username, score_id):
    # Get User record
    user = get_object_or_404(User, pk = username)
    # Retrieve existing score record
    score = get_object_or_404(Score, pk = score_id)
    composition = remake_composition(score)
    # Option lists needed
    instrument_list = [
    "Acoustic Grand Piano", "Harpsichord", "Glockenspiel", "Marimba", "Church Organ",
    "Accordion", "Harmonica", "Electric Guitar", "Acoustic Bass", 'Electric Bass',
    'Violin', 'Viola', 'Cello', 'Contrabass', 'Orchestral Harp', 'Timpani', 'Trumpet',
    'Trombone', 'Tuba', 'Soprano Sax', 'Oboe', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute'
    ]
    metre_list = [
    '4/4', '3/4', '2/4', '5/4', '2/2', '3/2', '3/8', '6/8', '9/8', '12/8'
    ]
    key_list = [
    'C major', 'D major', 'E major', 'F major', 'G major', 'A major', 'B major',
    'F# major', 'C# major', 'Cb major', 'Gb major', 'Db major', 'Ab major', 'Eb major',
    'Bb major', 'A minor', 'B minor', 'C minor', 'D minor', 'E minor', 'F minor', 'G minor',
    'F# minor', 'C# minor', 'G# minor', 'D# minor', 'A# minor', 'Ab minor', 'Eb minor', 'Bb minor'
    ]
    note_list = [
    'C', 'C#', 'D', 'Db', 'D#', 'E', 'Eb', 'F', 'F#', 'G', 'Gb', 'G#', 'A', 'Ab', 'A#', 'B', 'Bb'
    ]
    duration_list = [
    'semibreve', 'minim', 'crotchet', 'quaver', 'semiquaver', 'demisemiquaver', 'triplet crotchet',
    'triplet quaver', 'triplet semiquaver', 'dotted semibreve', 'dotted minim', 'dotted crotchet',
    'dotted quaver', 'dotted semiquaver', 'dotted demisemiquaver'
    ]
    return render(request, 'editor/edit.html', {'score': score, 'composition': composition, 'user': user, 'instrument_list' : instrument_list, 'metre_list': metre_list, 'key_list': key_list, 'note_list': note_list, 'duration_list': duration_list})

def edit(request, username, score_id, action):
    user = get_object_or_404(User, pk = username)
    score = get_object_or_404(Score, pk = score_id)
    composition = remake_composition(score)
    if action == 'i':
        selected_instrument = request.POST['instrument']
        add_instrument(composition, selected_instrument)
    elif action == 'm':
        selected_metre = request.POST['metre']
        selected_metre = selected_metre.split('/')
        metre = (int(selected_metre[0]), int(selected_metre[1]))
        selected_bar = int(request.POST['bar'])
        set_bar_metre(composition, metre, selected_bar)
    elif action == 'k':
        selected_key = request.POST['key']
        selected_key = selected_key.split(' ')
        if selected_key[1] == 'major':
            key = selected_key[0]
        elif selected_key[1] == 'minor':
            key = selected_key[0].lower()
        selected_bar = int(request.POST['bar'])
        set_bar_key(composition, key, selected_bar)
    elif action == 'n':
        selected_track = request.POST['track']
        selected_note = request.POST['note']
        selected_octave = int(request.POST['octave'])
        selected_duration = request.POST['duration']
        selected_bar = int(request.POST['bar'])
        selected_position = int(request.POST['position'])
        add_note(composition, selected_duration, selected_track, selected_note, selected_octave, selected_bar, selected_position)
    elif action == 'r':
        selected_track = request.POST['track']
        selected_duration = request.POST['duration']
        selected_bar = int(request.POST['bar'])
        selected_position = int(request.POST['position'])
        add_note(composition, selected_duration, selected_track, bar = selected_bar, position = selected_position)
    elif action == 'dn':
        selected_track = request.POST['track']
        selected_bar = int(request.POST['bar'])
        selected_position = int(request.POST['position'])
        delete_note(composition, selected_track, selected_bar, selected_position)
    elif action == 'di':
        selected_track = request.POST['track']
        delete_track(composition, selected_track)
    update_score(score, composition)
    save_comp(score, composition)
    # Option lists needed
    instrument_list = [
    "Acoustic Grand Piano", "Harpsichord", "Glockenspiel", "Marimba", "Church Organ",
    "Accordion", "Harmonica", "Electric Guitar", "Acoustic Bass", 'Electric Bass',
    'Violin', 'Viola', 'Cello', 'Contrabass', 'Orchestral Harp', 'Timpani', 'Trumpet',
    'Trombone', 'Tuba', 'Soprano Sax', 'Oboe', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute'
    ]
    metre_list = [
    '4/4', '3/4', '2/4', '5/4', '2/2', '3/2', '3/8', '6/8', '9/8', '12/8'
    ]
    key_list = [
    'C major', 'D major', 'E major', 'F major', 'G major', 'A major', 'B major',
    'F# major', 'C# major', 'Cb major', 'Gb major', 'Db major', 'Ab major', 'Eb major',
    'Bb major', 'A minor', 'B minor', 'C minor', 'D minor', 'E minor', 'F minor', 'G minor',
    'F# minor', 'C# minor', 'G# minor', 'D# minor', 'A# minor', 'Ab minor', 'Eb minor', 'Bb minor'
    ]
    note_list = [
    'C', 'C#', 'D', 'Db', 'D#', 'E', 'Eb', 'F', 'F#', 'G', 'Gb', 'G#', 'A', 'Ab', 'A#', 'B', 'Bb'
    ]
    duration_list = [
    'semibreve', 'minim', 'crotchet', 'quaver', 'semiquaver', 'demisemiquaver', 'triplet crotchet',
    'triplet quaver', 'triplet semiquaver', 'dotted semibreve', 'dotted minim', 'dotted crotchet',
    'dotted quaver', 'dotted semiquaver', 'dotted demisemiquaver'
    ]
    return render(request, 'editor/edit.html', {'score': score, 'composition': composition, 'user': user, 'instrument_list' : instrument_list, 'metre_list': metre_list, 'key_list': key_list, 'note_list': note_list, 'duration_list': duration_list})
