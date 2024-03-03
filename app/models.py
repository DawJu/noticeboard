from django.db import models

# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='tytuł')
    message = models.CharField(max_length=1000, null=False, verbose_name='wiadomość')
    sender = models.CharField(max_length=50, null=False, verbose_name='nadawca')
    date = models.DateField(auto_now=True, verbose_name='data')

    class Meta:
        verbose_name = 'Ogłoszenie'
        verbose_name_plural = 'Ogłoszenia'

    def __str__(self):
        return self.title
