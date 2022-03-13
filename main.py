from metodai import funkcijos_perkelimas
import sys
import pandas as pd


pasirinkimas = 1

while pasirinkimas != 9:
    pasirinkimas = int(input("Noredami suformatuoti failus spauskite - 1\nNoredami perkelti failus spauskite - 2\n"
                             "Norėdami išeiti iš programos spauskite - 9 "))



    if pasirinkimas == 1:
        direktorija = input("iveskite direktorija")
        x = funkcijos_perkelimas.duomenu_struktura(direktorija)
        df = pd.DataFrame(x)
        df.to_csv(r"C:\Users\dovyd\PycharmProjects\Projektinis_darbas\Kodas\pervadinti_duomenys.csv", index = False)
        print(df)
        print("pakeista")

    elif pasirinkimas == 2:
        pradzios_direktorija = input("Iveskite pradiniu duomenu direktorija")
        duomenu_direktorija = input("iveskite duomenu saugojimo direktorija")
        x = funkcijos_perkelimas.failu_perkelimas(pradzios_direktorija,duomenu_direktorija)
        print(x)
        print("Duomenys perkelti")




    if pasirinkimas == 9:
        sys.exit()

    else:
        pass