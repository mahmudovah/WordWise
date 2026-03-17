from django.db import models
from main.models import User
from django.utils.text import slugify

class Subject(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Word(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    slug = models.SlugField()
    translated = models.CharField(max_length=255)
    definition = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.word)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.word + " - " + self.translated + " @" + self.author.first_name