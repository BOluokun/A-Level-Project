from .models import Score
from .merge_sort_functions import *

def retrieve_scores(library, username = None):
    scores = []
    if library == 'public':
        for s in Score.objects.all():
            if s.public == True:
                scores.append(s)
    elif library == 'user':
        for s in Score.objects.all():
            if s.user.username == username:
                scores.append(s)
    return scores

def sort(scores, criterion):
    if criterion == 'title':
        title_sort(scores)
    elif criterion == 'author':
        author_sort(scores)
    elif criterion == 'created date':
        created_date_sort(scores)
    elif criterion == 'last modified':
        edited_date_sort(scores)

def toggle_public(score_id):
    score = Score.objects.get(pk = score_id)
    if score.public:
        score.public = False
    else:
        score.public = True
    score.save()

def search(search_text, scores):
    filtered_scores = []
    for s in scores:
        if search_text.lower() in s.title.lower():
            filtered_scores.append(s)
        elif search_text in s.author:
            filtered_scores.append(s)
    return filtered_scores

def delete_score(score_id):
    score = Score.objects.get(pk = score_id)
    score.delete()
