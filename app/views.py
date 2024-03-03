from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        sender = request.POST['sender']
        new = Announcement.objects.create(title=title, message=message, sender=sender)
        new.save()
        return redirect('/')
    else:
        return render(request, 'new.html', {})


def board(request):
    announcements = Announcement.objects.all().order_by('-id')
    return render(request, 'board.html', {'announcements': announcements})


def announcement(request, id):
    item = Announcement.objects.get(id=id)
    return render(request, 'announcement.html', {'announcement': item})
