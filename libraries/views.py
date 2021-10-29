from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from accounts.models import User

from .pythonsubrountines import *

# Create your views here.

def user_library(request, username):
    user = get_object_or_404(User, pk = username)
    scores = retrieve_scores('user', username)
    try:
        criterion = request.POST['sort-options']
        sort(scores, criterion)
    except KeyError:
         search_text = request.POST['search']
         scores = search(search_text, scores)
    finally:
        return render(request, 'libraries/user_library.html', {'user' : user, 'scores' : scores})

def upload(request, username, score_id):
    toggle_public(score_id)
    return redirect('user_library', username = username)

def delete(request, username, score_id):
    delete_score(score_id)
    return redirect('user_library', username = username)

def public_library(request, username):
    scores = retrieve_scores('public')
    try:
        criterion = request.POST['sort-options']
        sort(scores, criterion)
    except KeyError:
        search_text = request.POST['search']
        scores = search(search_text, scores)
    finally:
        return render(request, 'libraries/public_library.html', {'scores' : scores, 'username' : username})
