from django.db import models

class Slip(models.Model):
    iteration = models.IntegerField("iteration")
    limit = models.IntegerField("limit")
    amount = models.FloatField("amount")
    starter = models.FloatField("starter")
    update_multiplier = models.FloatField("update multiplier")
    upgrade_multiplier = models.FloatField("upgrade multiplier")
    last_updated = models.DateTimeField("last updated")
    created_on = models.DateTimeField("created")
