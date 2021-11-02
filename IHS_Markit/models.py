from django.db import models


class Blog (models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.author
