from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q

from jitterbunk.models import Bunk, Profile

def login_view(request):
    """Attempts to log in a given username and password and redirect to 
    the main bunk feed. Displays the login page if unsuccessful.

    """
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/jitterbunk/feed')
        else:
            return render(request, 'jitterbunk/login.html', {
                'error_message': 'Incorrect username or password',
            })
    return render(request, 'jitterbunk/login.html')

def logout_view(request):
    """Logs a user out and directs them to the starting login view."""
    logout(request)
    return HttpResponseRedirect('/jitterbunk/')

@login_required
def index(request):
    """Renders a feed of all bunks."""
    bunk_list = Bunk.objects.all()
    context = {'bunk_list': bunk_list}
    return render(request, 'jitterbunk/index.html', context)

@login_required
def profile(request):
    """Displays a user profile and bunking history."""
    bunk_list = Bunk.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
    profile = Profile.objects.get(user=request.user)
    context = {'bunk_list':bunk_list, 'profile':profile}
    return render(request, 'jitterbunk/profile.html', context)

@login_required
def bunk(request):
    """Renders the bunking view and saves bunking events to db."""
    if request.POST:
        try:    
            user_to_bunk = request.POST['username_to_bunk']
            user = User.objects.get(username=user_to_bunk)
            bunk = Bunk(from_user=request.user, to_user=user, time=timezone.now())
            bunk.save()
            return HttpResponseRedirect('/jitterbunk/feed/')
        except (KeyError, User.DoesNotExist):
            return render(request, 'jitterbunk/bunk.html', {
                'error_message':"invalid username."
            })
    return render(request, 'jitterbunk/bunk.html')


