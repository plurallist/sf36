from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


## tu dobre


class Lekarze(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="admin")
    imie_nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return self.imie_nazwisko

class Choroby(models.Model):
    nazwa_choroby = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.nazwa_choroby

class Pacjenci(models.Model):
    pacjent_id = models.IntegerField(primary_key=True)
    choroba = models.ForeignKey(Choroby, on_delete=models.CASCADE)
    lekarz_prowadzacy = models.ForeignKey(Lekarze, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pacjent_id)

class sf36_raw(models.Model):
    pacjent_id = models.ForeignKey(Pacjenci, on_delete=models.CASCADE)
    data_wypelnienia = models.DateField(auto_now=True)
    stan_zdrowia = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    stan_zdrowia_porownanie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    bieganie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    umiarkowana_aktywnosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    zakupy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    kilka_pieter = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    pietro = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    schylanie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    spacer_1km = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    spacer_500m = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    spacer_100m = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    ubieranie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    skrocenie_pracy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    gorsze_samopoczucie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    ograniczenie_czynnosci = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    utrudnienie_czynnosci = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    emocje_skrocenie_pracy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    emocje_rezultaty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    emocje_niemoznosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    zwyczajne_czynnosci = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    bol_czestosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    bol_praca = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    animusz = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    zdenerwowanie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    brak_wartosci = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    wyciszenie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    energicznosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    smutek = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    zmarnowanie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    szczeliwosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    zmeczenie = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    zdrowie_towarzyskosc = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    stan_zdrowia_inni = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    zdrowotnosc_inni = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    pogorszenie_zdrowia = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    doskonalosc_zdrowia = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return str(self.data_wypelnienia)


class sf36_recoded(models.Model):
    id = models.OneToOneField(sf36_raw, on_delete=models.CASCADE, primary_key=True)
    funkcjonowanie_fizycznie = models.IntegerField()
    ograniczenie_fizycznie = models.IntegerField()
    ograniczenie_emocjonalne = models.IntegerField()
    dolegliwosci_bolowe = models.IntegerField()
    poczucie_zdrowia_ogolne = models.IntegerField()
    witalnosc = models.IntegerField()
    funkcjonowanie_spoleczne = models.IntegerField()
    poczucie_zdrowia_psychicznego = models.IntegerField()
