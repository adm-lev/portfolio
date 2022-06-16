from django.db import models


class Task(models.Model):
    title = models.CharField('Названиие', max_length=50)
    task = models.TextField('Описаниие')

    def __str__(self):
        return self.title


