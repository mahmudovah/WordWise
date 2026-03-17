from django.shortcuts import render
from django.http import HttpRequest
from asosiy.models import Subject, Word

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