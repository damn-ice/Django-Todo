from django.db import models


class ToDo(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.CharField("ToDos", max_length=300, default="Nothing!")



# Create your models here.

    def __str__(self):
        return self.text
    