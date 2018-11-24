from django.db import models

class Task(models.Model):
    problemName = models.TextField(default='')

    problemDesciption = models.TextField(default='')
    inputDesription = models.TextField(default='')
    outputDescription = models.TextField(default='')


class Test(models.Model):
    input = models.TextField(default='')
    output = models.TextField(default='')
    task = models.IntegerField(default=0)
    # TODO implement this table to have a forgein key of task ID, desired input
    # and output
