from django.db import models

class Task(models.Model):
    problemName = models.TextField(default='')

    problemDesciption = models.TextField(default='')
    inputDesription = models.TextField(default='')
    outputDescription = models.TextField(default='')

class Test(models.Model):
    pass
    # TODO implement this table to have a forgein key of task ID, desired input
    # and output
