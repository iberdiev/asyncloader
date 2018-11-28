from django.db import models
from django.urls import reverse


class Link(models.Model):
     link = models.URLField(max_length=300, default='')
     email = models.CharField(max_length=50, default='')


     def __str__(self):
         return '%s %s' % (self.link, self.email)


     def get_absolute_url(self):
         return reverse('confirm')
