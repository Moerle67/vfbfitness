from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    def __str__(self):
        return (f"{self.name}, {self.vorname}")  

class Schrittzaehler(models.Model):
    datum = models.DateField(auto_now_add=True, verbose_name="Datum")
    schritte = models.IntegerField(verbose_name="Anzahl Schritte")
    kalorien = models.IntegerField(verbose_name="Verbrauchte Kalorieren")
    user = models.ForeignKey(User, verbose_name="Benutzer ", on_delete=models.CASCADE)
    def __str__(self):
        return (f"Am {self.datum} ist {self.user} {self.schritte} Schritte gelaufen und {self.kalorien} Kalorien vebraucht")  
