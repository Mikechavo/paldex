from django.db import models
from django.contrib.auth.models import User




class FireTeam(models.Model):
    name = models.CharField(max_length=100)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fire_teams_led')
    members = models.ManyToManyField(User, related_name='fire_teams_joined')

    def __str__(self):
        return self.name


