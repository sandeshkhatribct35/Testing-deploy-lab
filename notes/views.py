from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def home(request):
    form = NoteForm()
    notes = Note.objects.all()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'home.html', {'form': form, 'notes': notes})