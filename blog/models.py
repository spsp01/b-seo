from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.top_name

class Post(models.Model):
    name = models.CharField(max_length=255, default='Nowy Post')
    date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    zdjecie = models.ImageField(upload_to='static/img/post_main', default='static/img/logo.png')
    treść = models.TextField()
    def __str__(self):
        return self.name