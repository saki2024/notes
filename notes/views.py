from django.shortcuts import render


# Create your views here.

def notes(request):
    return render(request,('index.html'))


def list(request):
    all_notes = notes.object.all()
