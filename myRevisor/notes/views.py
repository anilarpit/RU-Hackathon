from django.shortcuts import render, redirect

# Create your views here.
from .forms import NoteForm
from .models import Note

def get_notes(request):

    if request.user.is_authenticated:
        profile = request.user.profile
        notes = profile.note_set.all()
        context = {
            'profile' : profile,
            'notes' : notes,
            'user' : request.user,
        }
        return render(request, 'notes/notes.html', context)
    else:
        return render(request, 'notes/notRegistered.html', {})



def note_create_view(request):
    if request.user.is_authenticated:
        print(request.user.profile)
        print(request.user.id)
        note_form = NoteForm(request.POST or None, request.FILES or None)
        if note_form.is_valid():

            profile = request.user.profile

            note = note_form.save()
            note.profile = profile

            note.save()
            # TODO faire une page qui dit 'note créé, cliquer ici pour voir vos notes'
            return redirect('notes')
            print('okay!')
        else:
            print('did not worked!')

        context = {
            'my_form' : note_form
        }

        return render(request, 'notes/note.html', context)
    else:
        return render(request, 'notes/notRegistered.html', {})

