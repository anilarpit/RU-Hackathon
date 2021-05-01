from django.shortcuts import render

# Create your views here.
from .forms import NoteForm

def note_create_view(request):
    note_form = NoteForm(request.POST, request.FILES)
    if note_form.is_valid():
        user = request.user
        print(user)
        print('okay!')
        note_form.save()
    else:
        print('did not worked!')

    context = {
        'my_form' : note_form
    }

    return render(request, 'notes/note.html', context)

