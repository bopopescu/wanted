from django.db import models


class Slave(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    descr = models.TextField()
    join_date = models.DateField(auto_now=True)
    cv = models.FileField(null=True, blank=True)


class Master(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    descr = models.TextField()
    join_date = models.DateField(auto_now=True)


class Role(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    # posted_by = models.CharField(max_length=15)
    posted_by = models.ForeignKey(Master)
    lname = models.CharField(max_length=15)
    descr = models.TextField()
    posted_date = models.DateField(auto_now=True)

# Create your models here.
