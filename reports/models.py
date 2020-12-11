from django.db import models

# Create your models here.

class Platforma(models.Model):
    emri = models.CharField(max_length=100)

    def __str__ (self):
        return self.emri
    
    class Meta:
        verbose_name_plural = "Platforma"


class Raportet(models.Model):
    platform = models.ForeignKey(Platforma, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)
    contact = models.CharField(max_length = 150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add="True", editable="False")

    def __str__ (self):
        return str(self.platform) + " / " + self.person_name + " / " + self.contact + " / " + self.description + " / " + str(self.created_at)
    
    class Meta:
        verbose_name_plural = "Raportet"