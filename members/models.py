# from django.db import models
# from django.contrib.auth.models import User
# from paldex.models import PalModel  # Assuming PalModel is your Pal model

# class FireTeam(models.Model):
#     name = models.CharField(max_length=100)
#     leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fire_teams_led')
#     members = models.ManyToManyField(PalModel, related_name='fire_teams_joined')

#     def __str__(self):
#         return self.name


# from django.db import models
# from django.contrib.auth.models import User
# # from django.core.serializers.json import DjangoJSONEncoder
# # import json

# class FireTeam(models.Model):
#     name = models.CharField(max_length=100)
#     leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fire_teams_led')
#     members = models.JSONField(default=list)  # Change to JSONField

#     def __str__(self):
#         return self.name

#     def num_members(self):
#         return len(self.members)

from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class FireTeam(models.Model):
    name = models.CharField(max_length=100)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fire_teams_led')
    members = JSONField(default=dict)  # Store members as a dictionary in a JSONField

    def __str__(self):
        return self.name