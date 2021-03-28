from django.db import models

# Create your models here.


class news(models.Model):
    post = models.TextField()
    edisi = models.CharField(max_length=255)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'news'
        verbose_name_plural = 'newss'
