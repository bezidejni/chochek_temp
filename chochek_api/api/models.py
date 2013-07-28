from django.db import models


class Company(models.Model):
    ime = models.CharField(max_length=100)
    satnica = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.ime


class Commission(models.Model):
    firma = models.ForeignKey(Company, related_name="commissions")
    description = models.TextField(blank=True)
    broj_sati = models.IntegerField()
    datum_od = models.DateField(blank=True, null=True)
    datum_do = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField()
    fixed_amount = models.BooleanField()

    def __unicode__(self):
        return u"{0}: {1} ({2} sati)".format(self.firma.ime,
         self.description, self.broj_sati)
