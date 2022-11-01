from django.db import models

# Create your models here.
class room(models.Model):
    room=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.room
