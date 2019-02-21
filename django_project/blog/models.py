from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    '''powiazanie do usera. Dodonie jednego wielu posótów przez jednego usera.
    Cascade oznacze że jak on delete będzie to usunie wszystkie posty tego użytkownika
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
