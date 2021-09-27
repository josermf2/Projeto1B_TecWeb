from django.shortcuts import render, redirect
from .models import Deleted_Tag, Note, Tag, Deleted_Note

def deleted_note(title, content, tag):
    if Deleted_Tag.objects.filter(tag=tag).exists():    
        deleted = Deleted_Note(title=title, content=content, tag=Deleted_Tag.objects.get(tag=tag))

    elif not Deleted_Tag.objects.filter(tag=tag).exists():
        newDeletedTag = Deleted_Tag(tag=tag)
        newDeletedTag.save()
        deleted = Deleted_Note(title=title, content=content, tag=Deleted_Tag.objects.get(tag=newDeletedTag))
    
    deleted.save()

def delete(request, delete_id):
    note = Note.objects.get(id=delete_id)
    tag = note.tag
    title = note.title
    content = note.content

    deleted_note(title, content, tag)

    note.delete()
    if Note.objects.filter(tag=tag).count() > 0:
        pass
    else:
        Tag.objects.get(tag=tag).delete()

    return redirect('index')
    
def post(request):   
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag  = request.POST.get('tag').lower()

    if Tag.objects.filter(tag=tag).exists():    
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=tag))
        newNote.save()

    elif not Tag.objects.filter(tag=tag).exists():
        newTag = Tag(tag=tag)
        newTag.save()
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=newTag))
        newNote.save()
    
    return redirect('index')

def update(request, update_id=''):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag  = request.POST.get('tag').lower()
    note = Note.objects.get(id=update_id)
    note.title = title
    note.content = content
    note.save()

    if Note.objects.filter(tag=note.tag).count() > 1:
        pass
    else:
        Tag.objects.get(tag=note.tag).delete()

    if Tag.objects.filter(tag=tag).exists():
        note.tag = Tag.objects.get(tag=tag)
        note.save()

    elif not Tag.objects.filter(tag=tag).exists():
        newTag = Tag(tag=tag)
        newTag.save()
        note.tag = Tag.objects.get(tag=tag)
        note.save()

    return redirect('index')

def index(request):
    all_notes = Note.objects.all()
    all_deleted_notes = Deleted_Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': all_notes, 'deleted_notes': all_deleted_notes})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def specific_tag(request, tag):
    all_notes = Note.objects.all().filter(tag=Tag.objects.get(tag=tag))
    return render(request, 'notes/specific_tag.html', {'notes': all_notes, 'tag_name':tag})

def delete_delete_note(request, delete_id):
    note = Deleted_Note.objects.get(id=delete_id)
    tag = note.tag

    note.delete()
    if Deleted_Note.objects.filter(tag=tag).count() > 0:
        pass
    else:
        Deleted_Tag.objects.get(tag=tag).delete()

    return redirect('index')

def restore_note(request, delete_id):
    title = request.POST.get('title')
    content = request.POST.get('content')
    tag  = request.POST.get('tag')

    if Tag.objects.filter(tag=tag).exists():    
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=tag))
        newNote.save()

    elif not Tag.objects.filter(tag=tag).exists():
        newTag = Tag(tag=tag)
        newTag.save()
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=newTag))
        newNote.save()    
    
    delete_delete_note(request, delete_id)

    return redirect('index')
    
