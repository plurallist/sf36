from django import forms

class CreateNewPatient(forms.Form):
    nazwisko = forms.CharField(label="Nazwisko", max_length=200)
    fabry = forms.BooleanField(label="Fabry")

class CreateNewSF36_old(forms.Form):
    obecnosc_bolu = forms.BooleanField(label="Czy odczuwa Pani/Pan aktualnie ból?")
    skala_bolu = forms.CharField(label="Nasilenie bólu w skali od 0 do 10 wynosi:", max_length=2)

class CreateNewSF36(forms.Form):
    stan_zdrowia = forms.ChoiceField(label="Generalnie możesz powiedzieć, że stan twojego zdrowia jest",
                                     choices=((1,"bardzo"), (2,"średnio"), (2,"średnio"), (2,"średnio"), (2,"średnio")),
                                     widget=forms.RadioSelect())
    stan_zdrowia_porownanie = forms.ChoiceField(label="Jak oceniasz stan swojego zdrowia w porównaniu z analogicznym okresem ubiegłego roku?",
                                     choices=((1,"bardzo"), (1,"średnio")), widget=forms.RadioSelect())
    bieganie = forms.ChoiceField(label="Poniżej wymieniono w punktach czynności wykonywane zazwyczaj w ciągu dnia. Czy aktualnie Twoje zdrowie ogranicza Twoje możliwości ich wykonania? Jeżeli tak, to jak bardzo",
                                     choices=((1,"bardzo"), (1,"średnio")), widget=forms.RadioSelect())
    umiarkowana_aktywnosc = forms.ChoiceField(label="Czy w ostatnim miesiącu miałeś(-aś) problemy z pracą lub codzienną aktywnością, które wynikały ze stanu zdrowia i powodowały:",
                                     choices=((1,"bardzo"), (1,"średnio")), widget=forms.RadioSelect())