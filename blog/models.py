from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
'''Models are Classes that are used in Database Usage. 
Django uses SQLLite3 for management of DB and PostgresSQl for production'''


class Post(models.Model):
    # Sets Max Characters to 100
    title = models.CharField(max_length=100)

    # Sets A Text Field Available
    content = models.TextField()

    # Makes A Date Time Field, Takes the current time from time zone for date posted, Can be updated Later
    date_posted = models.DateTimeField(default=timezone.now)

    # To define an Author for every Post
    # Any User has one-to-many relationship with posts. One User Has Many Posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
