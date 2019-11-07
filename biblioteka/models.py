from django.db import models
from .managers import KsiazkaManager

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="ksiazki")

    objects = models.Manager()
    ksiazki = KsiazkaManager()

    def __str__(self):
        return self.tytul

    class Meta:
        # db_table = "ksiazki"
        ordering = ['-rok_wydania']
        # order_with_respect_to = 'autor'
        verbose_name = "książka"
        verbose_name_plural = "książki"
        unique_together = ["tytul", "rok_wydania"]
        indexes = [
            models.Index(fields=['tytul'], name="tytul_inx"),
            models.Index(fields=['tytul', 'rok_wydania'])
        ]
        permissions = [
            ('can_update_ksiazka', "Może zmieniać książke")
        ]