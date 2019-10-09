from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length = 10)
    area = models.CharField(max_length = 10)
    introduction = models.TextField()
    party_number = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 10)

class Choice(models.Model):
    candidate = models.ForeignKey(Candidate,models.CASCADE)
    poll = models.ForeignKey(Poll,models.CASCADE)
    votes = models.IntegerField(default = 0)

