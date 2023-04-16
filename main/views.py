from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Lekarze, Pacjenci, sf36_raw, Choroby, sf36_recoded
from .forms import CreateNewPatient, CreateNewSF36_old, CreateNewSF36
from .arkusz import pytania, sf36_zmienne, przelicznik_ankiety, sf36_zmienne_recoded
import csv


def pacjenci(response):
    if response.user.is_authenticated:
        lista_pacjentow = Pacjenci.objects.all()
        for pacjent in lista_pacjentow:
            for arkusz in pacjent.sf36_set.all():
                print(arkusz.skala_bolu)
        for pacjent in lista_pacjentow:
            print(pacjent.pesel)
        return render(response, "main/pacjenci.html", {"lista_pacjentow": lista_pacjentow})
    else:
        return HttpResponseRedirect("/login")


## ostateczne

def panel(response):
    if response.user.is_authenticated:
        lekarz = response.user.lekarze
        ls_patient = Pacjenci.objects.all()
        ostatnia_ankieta = {}
        for x in ls_patient:
            ostatnia_ankieta[str(x.pacjent_id)] = []
            if len(x.sf36_raw_set.all()) > 0:
                ostatnia_ankieta[str(x.pacjent_id)].append(len(x.sf36_raw_set.all()))
                ostatnia_ankieta[str(x.pacjent_id)].append(x.sf36_raw_set.all().latest("data_wypelnienia"))
            else:
                ostatnia_ankieta[str(x.pacjent_id)].append("Brak")
                ostatnia_ankieta[str(x.pacjent_id)].append(" ")
        return render(response, "main/panel.html", {"lekarz": lekarz, "ls_patient": ls_patient,
                                                    "ostatnia_ankieta": ostatnia_ankieta})
    else:
        return HttpResponseRedirect("/login")


def new_sf36(response):
    if response.user.is_authenticated:
        if response.method == "GET":
            response.session['pacjent_wybrany'] = response.GET.get("pacjent_wybrany")
        if response.method == "POST":
            n = sf36_raw()
            n_recoded = sf36_recoded()
            n.pacjent_id = Pacjenci.objects.get(pacjent_id=response.session.get("pacjent_wybrany"))
            wypelnione = True
            for x in sf36_zmienne:
                setattr(n, x, response.POST.get(x, False))
                if not response.POST.get(x, False):
                    wypelnione = False
                    print("nie wypełnione")
            if wypelnione:
                n.save()
                przeliczone_dane = przelicznik_ankiety(n)
                for x in sf36_zmienne_recoded:
                    setattr(n_recoded, x, przeliczone_dane[x])
                print(przeliczone_dane)
                n_recoded.id = n
                n_recoded.save()
                print("Zapisano ankietę o id: {}, dla pacjenta: {}".format(n.id, n.pacjent_id))
                print(n.data_wypelnienia)
                return render(response, "main/succes.html", {"pytania": pytania, "nowa_ankieta": True})
        return render(response, "main/new_sf36.html", {"pytania": pytania})
    else:
        return HttpResponseRedirect("/login")


def choose_patient(response):
    if response.user.is_authenticated:
        ls_patient = Pacjenci.objects.all()
        return render(response, "main/choose_patient.html", {"ls_patient": ls_patient})
    else:
        return HttpResponseRedirect("/login")


def create_patient(response):
    if response.user.is_authenticated:
        lekarz = response.user.lekarze
        ls_chorob = Choroby.objects.all()
        if response.method == "POST":
            n = Pacjenci()
            n.choroba = Choroby.objects.get(nazwa_choroby=response.POST.get("choroba_wybrana"))
            n.lekarz_prowadzacy = lekarz
            n.save()
            return HttpResponseRedirect("/patient_created")
        return render(response, "main/create_patient.html", {"lekarz": lekarz, "ls_chorob": ls_chorob})
    else:
        return HttpResponseRedirect("/login")


def patient_created(response):
    if response.user.is_authenticated:
        pacjent_id = Pacjenci.objects.filter().latest("pacjent_id")
        return render(response, "main/patient_created.html", {"id": pacjent_id})
    else:
        return HttpResponseRedirect("/login")


def results_sf36(response):
    if response.user.is_authenticated:
        return render(response, "main/results_sf36.html")

    else:
        return HttpResponseRedirect("/login")


def your_results(response):
    if response.user.is_authenticated:
        ls_patient = response.user.lekarze.pacjenci_set.all()
        if response.method == "GET":
            ankiety_obecne = False
            ankieta_wybrana = False
            if "pacjent_wybrany" in response.GET or "ankieta_wybrana" in response.GET:
                wybrany = True
                if "ankieta_wybrana" in response.GET:
                    ankieta_wybrana, pacjent_wybrany = response.GET.get("ankieta_wybrana").split("_")
                    ls_ankiet = Pacjenci.objects.get(pacjent_id=pacjent_wybrany).sf36_raw_set.all()
                else:
                    pacjent_wybrany = response.GET.get("pacjent_wybrany")
                    ls_ankiet = Pacjenci.objects.get(pacjent_id=pacjent_wybrany).sf36_raw_set.all()
                if len(ls_ankiet) > 0:
                    ankiety_obecne = True
                if "ankieta_wybrana" in response.GET:
                    ankieta_wybrana_object = sf36_raw.objects.get(pacjent_id=pacjent_wybrany, id=ankieta_wybrana)
                    dict_wynik = {}
                    for x in sf36_zmienne:
                        dict_wynik[x] = getattr(ankieta_wybrana_object, x)
                    return render(response, "main/your_results.html",
                                  {"ls_patient": ls_patient, "wybrany": wybrany, "pacjent_wybrany": pacjent_wybrany,
                                   "ls_ankiet": ls_ankiet, "ankiety_obecne": ankiety_obecne, "ankieta_wybrana": ankieta_wybrana,
                                   "sf36_zmienne": dict_wynik, "ankieta_wybrana_data": ankieta_wybrana_object.data_wypelnienia})
                return render(response, "main/your_results.html",
                              {"ls_patient": ls_patient, "wybrany": wybrany, "pacjent_wybrany": pacjent_wybrany, "ls_ankiet": ls_ankiet, "ankiety_obecne": ankiety_obecne})
            else:
                wybrany = False
                return render(response, "main/your_results.html",
                              {"ls_patient": ls_patient, "wybrany": wybrany})
    else:
        return HttpResponseRedirect("/login")


def all_results(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("id") == "":
                print("nie ma pacjenta")
                return render(response, "main/all_results.html", {"pacjent_istnieje": False, "ankieta_istnieje": False,
                                                                  "sukces": False})
            response2 = HttpResponse(
                content_type='text/csv',
                headers={'Content-Disposition': 'attachment; filename="{}.csv"'.format(response.POST.get("id"))},
            )
            writer = csv.writer(response2)
            lista_id = []
            id_obrobka = response.POST.get("id").replace(" ", "").split(",")
            for x in id_obrobka:
                if ":" in str(x):
                    a, b = x.split(":")
                    for y in range(int(a), int(b)):
                        id_obrobka.append(y)
                    id_obrobka.append(int(b))
                    id_obrobka.remove(x)
            for x in id_obrobka:
                lista_id.append(int(x))
            headers = ["id", "data_wypelnienia"]
            print(lista_id)
            if response.POST.get("recounted_data"):
                for x in sf36_zmienne_recoded:
                    headers.append(x)
            else:
                for x in sf36_zmienne:
                    headers.append(x)
            writer.writerow(headers)
            lista_pacjentow = []
            for x in lista_id:
                kompletne_id = Pacjenci.objects.all().values("pacjent_id")
                lista_kompletne_id = []
                for y in kompletne_id:
                    lista_kompletne_id.append(y["pacjent_id"])
                if x in lista_kompletne_id:
                    lista_pacjentow.append(Pacjenci.objects.get(pacjent_id=x))
                else:
                    return render(response, "main/all_results.html",
                                  {"ankieta_istnieje": False, "pacjent_istnieje": False,
                                   "sukces": False})
            wybrana_ankieta = {}
            for x in lista_pacjentow:
                wybrana_ankieta[x] = x.sf36_raw_set.all().filter(data_wypelnienia__gte=response.POST.get("start"),
                                                                         data_wypelnienia__lte=response.POST.get("finish"))
            for queryset in wybrana_ankieta.values():
                if queryset.count() == 0:
                    print("nie ma ankiety")
                    return render(response, "main/all_results.html", {"ankieta_istnieje": False, "pacjent_istnieje": True,
                                                                      "sukces": False})
            if response.POST.get("recounted_data"):
                for a, b in wybrana_ankieta.items():
                    for ankieta in b:
                        dane_ankiety = [a.pacjent_id, ankieta.data_wypelnienia]
                        for zmienna in sf36_zmienne_recoded:
                            dane_ankiety.append(getattr(ankieta.sf36_recoded, zmienna))
                        writer.writerow(dane_ankiety)
            else:
                for a,b in wybrana_ankieta.items():
                    for ankieta in b:
                        dane_ankiety = [a.pacjent_id, ankieta.data_wypelnienia]
                        for zmienna in sf36_zmienne:
                            dane_ankiety.append(getattr(ankieta, zmienna))
                        writer.writerow(dane_ankiety)
            return response2
        return render(response, "main/all_results.html")
    else:
        return HttpResponseRedirect("/login")


def start(response):
    if response.user.is_authenticated:
        return HttpResponseRedirect("/panel")
    else:
        return HttpResponseRedirect("/login")
