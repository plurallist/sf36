import statistics

pytania = {1:"Generalnie możesz powiedzieć, że stan twojego zdrowia jest:",
           2:"Jak oceniasz stan swojego zdrowia w porównaniu z analogicznym okresem ubiegłego roku?:",
           3:"Poniżej wymieniono w punktach czynności wykonywane zazwyczaj w ciągu dnia. Czy aktualnie Twoje zdrowie ogranicza Twoje możliwości ich wykonania? Jeżeli tak, to jak bardzo?",
           4:"Czy w ostatnim miesiącu miałeś(-aś) problemy z pracą lub codzienną aktywnością, które wynikały ze stanu zdrowia i powodowały:",
           5:"Czy w ciągu ostatniego miesiąca miałeś(-aś) problemy związane z wykonywaną pracą lub codziennymi czynnościami wynikające z problemów emocjonalnych (np. poczucie depresji, zdenerwowanie)?",
           6:"Czy w ciągu ostatniego miesiąca twoje problemy zdrowotne lub emocjonalne miały wpływ na zwyczajne czynności, kontakty z rodziną, przyjaciółmi, sąsiadami lub innymi grupami?",
           7:"Ile razy odczuwałeś(-aś) ból w ciągu ostatniego miesiąca?",
           8:"Jak często w ciągu ostatniego miesiąca ból zakłócał Twoją normalną pracę (zawodową i domową)?",
           9:"""Poniższe pytania dotyczą Twojego samopoczucia w ciągu ostatniego miesiąca. Na każde pytanie proszę udzielić
jednej odpowiedzi najbardziej zbliżonej do stanu faktycznego. Ile razy wystąpił dany objaw w ciągu ostatniego miesiąca?""",
           10:"Jak często w ciągu ostatniego miesiąca Twoje zdrowie fizyczne lub stan emocjonalny wpływały na kontakty towarzyskie (spotkania z rodziną i przyjaciółmi)?",
           11:"Jak bardzo prawdziwe lub fałszywe są według Ciebie poniższe stwierdzenia?"}

sf36_zmienne = ["stan_zdrowia",
"stan_zdrowia_porownanie",
"bieganie",
"umiarkowana_aktywnosc",
"zakupy",
"kilka_pieter",
"pietro",
"schylanie",
"spacer_1km",
"spacer_500m",
"spacer_100m",
"ubieranie",
"skrocenie_pracy",
"gorsze_samopoczucie",
"ograniczenie_czynnosci",
"utrudnienie_czynnosci",
"emocje_skrocenie_pracy",
"emocje_rezultaty",
"emocje_niemoznosc",
"zwyczajne_czynnosci",
"bol_czestosc",
"bol_praca",
"animusz",
"zdenerwowanie",
"brak_wartosci",
"wyciszenie",
"energicznosc",
"smutek",
"zmarnowanie",
"szczeliwosc",
"zmeczenie",
"zdrowie_towarzyskosc",
"stan_zdrowia_inni",
"zdrowotnosc_inni",
"pogorszenie_zdrowia",
"doskonalosc_zdrowia"]

sf36_zmienne_recoded = ["funkcjonowanie_fizycznie",
    "ograniczenie_fizycznie",
    "ograniczenie_emocjonalne",
    "dolegliwosci_bolowe",
    "poczucie_zdrowia_ogolne",
    "witalnosc",
    "funkcjonowanie_spoleczne",
    "poczucie_zdrowia_psychicznego"]

def przelicznik_ankiety(raw_data):
    przeliczona_ankieta = []
    ankieta_recoded = {}
    for x in sf36_zmienne:
        if sf36_zmienne.index(x)+1 in [1, 2, 20, 22, 34, 36]:
            if getattr(raw_data, x) == "1":
                print("jest")
                przeliczona_ankieta.append(100)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(75)
                continue
            if getattr(raw_data, x) == "3":
                przeliczona_ankieta.append(50)
                continue
            if getattr(raw_data, x) == "4":
                przeliczona_ankieta.append(25)
                continue
            if getattr(raw_data, x) == "5":
                przeliczona_ankieta.append(0)
                continue
        if sf36_zmienne.index(x)+1 in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            if getattr(raw_data, x) == "1":
                przeliczona_ankieta.append(0)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(50)
                continue
            if getattr(raw_data, x) == "3":
                przeliczona_ankieta.append(100)
                continue
        if sf36_zmienne.index(x)+1 in [13, 14, 15, 16, 17, 18, 19]:
            if getattr(raw_data, x) == "1":
                print("jest")
                przeliczona_ankieta.append(0)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(100)
                continue
        if sf36_zmienne.index(x)+1 in [21, 23, 26, 27, 30]:
            if getattr(raw_data, x) == "1":
                przeliczona_ankieta.append(100)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(80)
                continue
            if getattr(raw_data, x) == "3":
                przeliczona_ankieta.append(60)
                continue
            if getattr(raw_data, x) == "4":
                przeliczona_ankieta.append(40)
                continue
            if getattr(raw_data, x) == "5":
                przeliczona_ankieta.append(20)
                continue
            if getattr(raw_data, x) == "6":
                przeliczona_ankieta.append(0)
                continue
        if sf36_zmienne.index(x)+1 in [24, 25, 28, 29, 31]:
            if getattr(raw_data, x) == "1":
                przeliczona_ankieta.append(0)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(20)
                continue
            if getattr(raw_data, x) == "3":
                przeliczona_ankieta.append(40)
                continue
            if getattr(raw_data, x) == "4":
                przeliczona_ankieta.append(60)
                continue
            if getattr(raw_data, x) == "5":
                przeliczona_ankieta.append(80)
                continue
            if getattr(raw_data, x) == "6":
                przeliczona_ankieta.append(100)
                continue
        if sf36_zmienne.index(x)+1 in [32, 33, 35]:
            if getattr(raw_data, x) == "1":
                przeliczona_ankieta.append(0)
                continue
            if getattr(raw_data, x) == "2":
                przeliczona_ankieta.append(25)
                continue
            if getattr(raw_data, x) == "3":
                przeliczona_ankieta.append(50)
                continue
            if getattr(raw_data, x) == "4":
                przeliczona_ankieta.append(75)
                continue
            if getattr(raw_data, x) == "5":
                przeliczona_ankieta.append(100)
    print(przeliczona_ankieta)
    ankieta_recoded["funkcjonowanie_fizycznie"] = statistics.mean(przeliczona_ankieta[3:13])
    ankieta_recoded["ograniczenie_fizycznie"] = statistics.mean(przeliczona_ankieta[13:17])
    ankieta_recoded["ograniczenie_emocjonalne"] = statistics.mean(przeliczona_ankieta[17:20])
    ankieta_recoded["witalnosc"] = statistics.mean([przeliczona_ankieta[23]] + [przeliczona_ankieta[27]] + [przeliczona_ankieta[29]] + [przeliczona_ankieta[31]])
    ankieta_recoded["poczucie_zdrowia_psychicznego"] = statistics.mean(przeliczona_ankieta[24:27] + [przeliczona_ankieta[28]] + [przeliczona_ankieta[30]])
    ankieta_recoded["funkcjonowanie_spoleczne"] = statistics.mean([przeliczona_ankieta[20]] + [przeliczona_ankieta[32]])
    ankieta_recoded["dolegliwosci_bolowe"] = statistics.mean(przeliczona_ankieta[21:23])
    ankieta_recoded["poczucie_zdrowia_ogolne"] = statistics.mean([przeliczona_ankieta[1]] + przeliczona_ankieta[33:37])

    return ankieta_recoded
