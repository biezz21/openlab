from django.db import models

# Create your models here.


class CommentDB(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    comment = models.TextField()

    class Meta:
        db_table = 'comment'
