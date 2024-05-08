from core.models import BaseModel
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Team(BaseModel, MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


class Experiment(BaseModel):
    description = models.TextField()
    sample_ratio = models.FloatField()
    teams = models.ManyToManyField(Team, related_name='experiments')
    teams_count = models.PositiveIntegerField()
