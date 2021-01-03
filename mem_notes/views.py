from django.http import Http404
from django.shortcuts import render, redirect

from mem_notes.forms import RememberForm
from mem_notes.models import Memories


def add_note(request):
    if request.method == "POST":
        form = RememberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect(note_detail, pk=post.pk)
    else:
        form = RememberForm()
    return render(request,
                  'mem_notes/add_note.html', {
                      'form': form,
                  })


def note_detail(request, pk):
    try:
        note = Memories.objects.get(pk=pk)
    except Memories.DoesNotExist:
        raise Http404('Такого нет тут!')

    return render(request, 'mem_notes/note_detail.html', context={'note': note})


def note_list(request):
    notes = Memories.objects.all()
    return render(request, 'mem_notes/note_list.html', context={'notes': notes})
