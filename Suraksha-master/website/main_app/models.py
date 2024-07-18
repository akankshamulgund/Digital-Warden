from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contact", null=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()

    Father = 'Father'
    Mother = 'Mother'
    Brother = 'Brother'
    Sister = 'Sister'
    Husband = 'Husband'
    Friend = 'Friend'
    Relative = 'Relative'
    Other = 'Other'
    relations = (
        (Father, 'Father'),
        (Mother, 'Mother'),
        (Brother, 'Brother'),
        (Sister, 'Sister'),
        (Husband, 'Husband'),
        (Friend, 'Friend'),
        (Relative, 'Relative'),
        (Other, 'Other'),
    )
    relation = models.CharField(max_length=10, choices=relations, default=Other)
    def __str__(self):
        return self.name


# models.py
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Report(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reason = models.TextField()
from django.db import models

from django.db import models

class BlockedAccount(models.Model):
    account_id = models.CharField(max_length=100)  # Assuming account_id is a CharField, adjust the max_length as needed
    reporter_name = models.CharField(max_length=100)
    reason = models.TextField()

    class Meta:
        verbose_name = 'Blocked Account'
        verbose_name_plural = 'Blocked Accounts'
