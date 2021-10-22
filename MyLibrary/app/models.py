from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class BookDetails(models.Model):
    user = models.EmailField(max_length=100)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
