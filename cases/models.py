from django.db import models


class Cases(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    no_confirmed = models.IntegerField("Nr de pacienți confirmați cu coronavirus", null=True, blank=True)
    no_special_quarantined = models.IntegerField("Nr de pacienți în carantina specializata", null=True, blank=True)
    no_self_quarantined = models.IntegerField("Nr de persoane în self quarantine", null=True, blank=True)
    no_recovered = models.IntegerField("Nr de persoane vindecate", null=True, blank=True)

    global_no_confirmed = models.IntegerField("Numărul total de cazuri confirmate la nivel global", null=True, blank=True)
    global_no_deaths = models.IntegerField("Nr total de decese la nivel global", null=True, blank=True)
    global_no_recovered = models.IntegerField("Nr total de persoane vindecate la nivel global", null=True, blank=True)

    def __str__(self):
        return str(self.created_at)
