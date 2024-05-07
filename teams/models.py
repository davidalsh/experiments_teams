from core.models import BaseModel
from django.db import models


class Experiment(BaseModel):
    description = models.TextField()
    sample_ration = models.FloatField()


class Team(BaseModel):
    name = models.CharField(max_length=255)
