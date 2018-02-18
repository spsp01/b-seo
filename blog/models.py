from django.db import models
from django.utils import timezone
from django.urls import reverse


class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.top_name

class Post(models.Model):
    name = models.CharField(max_length=255, default='Nowy Post')
    date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now())
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    zdjecie = models.ImageField(upload_to='static/img/post_main', default='static/img/logo.png')
    treść = models.TextField()

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class UserProfile(models.Model):
    name = models.CharField(max_length=255, default='user')

    def __str__(self):
        return self.name