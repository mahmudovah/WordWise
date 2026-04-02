from django.shortcuts import render, redirect
from django.http import HttpRequest
from asosiy.models import Subject, Word
from django.contrib.auth import logout

def index_view(request: HttpRequest):
    user = request.user
    subjects = Subject.objects.filter(is_public=True)
    
    if user.is_authenticated:
        if Subject.objects.filter(author=user).count() > 1:
            subjects = Subject.objects.filter(author=user)

    return render(request, 'index.html', context={"subjects":subjects})

def subject_detail(request: HttpRequest, pk):
    subject = Subject.objects.get(id=pk)
    words = Word.objects.filter(subject=subject)

    return render(request, 'subject-detail.html', context={"subject":subject, "words":words})

def logout_view(request):
    logout(request)
    return redirect('index')


def add_word(request: HttpRequest, subject_id):
    user = request.user
    if request.method == 'POST':
        if not user.is_authenticated:
            return redirect("index")

        subject = Subject.objects.get(id=subject_id)
    
        word = request.POST.get('word')
        translated = request.POST.get('translated')
        definition = request.POST.get('definition')
        

        Word.objects.create(
            subject=subject,
            word=word,
            translated=translated,
            definition=definition
        )
        words = Word.objects.all()

        return redirect('subject_detail', subject.id)

    return render(request, 'add_word.html')


# def add_subject(request: HttpRequest):
#     user = request.user
#     if request.method == 'POST':
#         if not user.is_authenticated:
#             return redirect('register')
#         title = request.POST