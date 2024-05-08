from core.models import BaseModel
from django.db import models


class Team(BaseModel):
    name = models.CharField(max_length=255, unique=True)


class Experiment(BaseModel):
    description = models.TextField()
    sample_ratio = models.FloatField()
    teams = models.ManyToManyField(Team, related_name='experiments')
    teams_count = models.PositiveIntegerField()
