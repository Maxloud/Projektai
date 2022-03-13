from pathlib import Path
from datetime import datetime
from collections import namedtuple
import os
import shutil
from Kodas.metodai import lenteles
redagavimo_data = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
counter = 0
counter2 = 0
counter3 = 0


def duomenu_struktura(pradiniai_duomenys):
    pradiniai_duomenys = Path(pradiniai_duomenys)
    duomenys_tuple = namedtuple('pradiniai_duomenys', 'pavadinimas direktorija dydis_mb redagavimo_data Statusas')
    global formatas
    duomenu_sarasas = []
    for item in pradiniai_duomenys.glob('**/*'):
        if item.suffix in ['.pdf', '.aprx', '.tif']:
            pavadinimas = item.name.replace(" ", "").replace("_", "-").split(".")[0]
            isskaidytas = pavadinimas.split("-")
            if (isskaidytas[0] == "N" or isskaidytas[0] == "O") and (isskaidytas[1] == "34" or isskaidytas[1] == "35") \
                    and (isskaidytas[3] == "AB" or isskaidytas[3] == "CD") and 99 > int(isskaidytas[2]) \
                    and 12 >= int(isskaidytas[4]):
                pavadinimas = f"{isskaidytas[0]}-{isskaidytas[1].zfill(2)}-{isskaidytas[2].zfill(3)}-{isskaidytas[3]}-" \
                              f"{isskaidytas[4].zfill(2)}"
                formatas = pavadinimas + item.suffix
                print(formatas)
            direktorija = Path.resolve(item).parent
            dydis = item.stat().st_size
            dydis_mb = dydis / 1048576
            redagavimo_data = datetime.fromtimestamp(item.stat().st_mtime)
            nauja_direktorija = f"{direktorija}\\{formatas}"
            if os.path.isfile(nauja_direktorija):
                print("failas jau yra pervadintas")
                statusas = "Formatas atitiko"
                duomenu_sarasas.append(duomenys_tuple(pavadinimas, direktorija, dydis_mb, redagavimo_data, statusas))
            else:
                os.rename(item, nauja_direktorija)
                statusas = "Pakeistas formatas"
                duomenu_sarasas.append(duomenys_tuple(pavadinimas, direktorija, dydis_mb, redagavimo_data, statusas))

    return duomenu_sarasas


def failu_perkelimas(pradiniai_duomenys, i_folderi):
    pradiniai_duomenys = Path(pradiniai_duomenys)
    i_folderi = Path(i_folderi)
    global counter
    global perkelti_i
    for item in pradiniai_duomenys.glob('**/*'):
        if item.suffix in ['.pdf']:
            pavadinimas = item.name.replace(" ", "").replace("_", "-").split(".")[0]
            isskaidytas = pavadinimas.split("-")
            if (isskaidytas[0] == "N" or isskaidytas[0] == "O") and (
                    isskaidytas[1] == "34" or isskaidytas[1] == "35") \
                    and (isskaidytas[3] == "AB" or isskaidytas[3] == "CD") and 99 > int(isskaidytas[2]) \
                    and len(isskaidytas) == 5:
                pavadinimas = f"{isskaidytas[0]}-{isskaidytas[1].zfill(2)}-{isskaidytas[2].zfill(3)}\
                    -{isskaidytas[3]}-{isskaidytas[4].zfill(2)}"
                pavadinimas = pavadinimas.replace(" ", "")
                strukturinis_folderis = f"{isskaidytas[0]}-{isskaidytas[1]}-{isskaidytas[2]}-{isskaidytas[3]}"
                perkelti_i = f"{i_folderi}\\PDF\\10000\\{strukturinis_folderis}"
                if not os.path.exists(perkelti_i):
                    os.makedirs(perkelti_i)
                try:
                    for _, dir, files in os.walk(os.path.dirname(item)):
                        if files:
                            for file in files:
                                if not os.path.isfile(perkelti_i + "\\" + file):
                                    os.rename(item, perkelti_i + "\\" + pavadinimas + ".pdf")
                                    counter += 1
                                    counter_str = str(counter)
                                    print(counter_str)
                                    x = lenteles.Ivedimas(counter_str, pavadinimas, perkelti_i, "PDF", "", "10000",
                                                          str(redagavimo_data), "", "Pridetas")
                                    e = x.duomenu_ivedimas_pdf()
                                    print(e)

                                elif os.path.isfile(perkelti_i + "\\" + file):
                                    os.remove(perkelti_i + "\\" + file)
                                    os.rename(item, perkelti_i + "\\" + pavadinimas + ".pdf")
                except Exception as e:
                    print(e)
            else:
                pass

    for item in pradiniai_duomenys.glob('**/*'):
        global counter2
        if item.suffix in ['.tif']:
            pavadinimas = item.name.replace(" ", "").replace("_", "-").split(".")[0]
            isskaidytas = pavadinimas.split("-")
            if (isskaidytas[0] == "N" or isskaidytas[0] == "O") and (
                    isskaidytas[1] == "34" or isskaidytas[1] == "35") \
                    and (isskaidytas[3] == "AB" or isskaidytas[3] == "CD") and 99 > int(isskaidytas[2]) \
                    and len(isskaidytas) == 5:
                pavadinimas = f"{isskaidytas[0]}-{isskaidytas[1].zfill(2)}-{isskaidytas[2].zfill(3)}\
                    -{isskaidytas[3]}-{isskaidytas[4].zfill(2)}"
                pavadinimas = pavadinimas.replace(" ", "")
                strukturinis_folderis = f"{isskaidytas[0]}-{isskaidytas[1]}-{isskaidytas[2]}-{isskaidytas[3]}"
                perkelti_i = f"{i_folderi}\\GEOTIFF\\10000\\{strukturinis_folderis}"
                print(os.getcwd())
                if not os.path.exists(perkelti_i):
                    os.makedirs(perkelti_i)

                try:

                    for _, dir, files in os.walk(os.path.dirname(item)):
                        if files:
                            for file in files:
                                sufix = os.path.splitext(file)[1]
                                if not os.path.isfile(perkelti_i + "\\" + pavadinimas + sufix):
                                    os.rename(_ + "\\" + file, perkelti_i + "\\" + pavadinimas + sufix)
                                    print(sufix)
                                    if sufix == ".tif":
                                        counter2 += 1
                                        counter_str = str(counter2)
                                        print(counter_str)
                                        x = lenteles.Ivedimas(counter_str, pavadinimas, perkelti_i, "GEOTIFF", "",
                                                              "10000", str(redagavimo_data), "", "Pridetas")
                                        e = x.duomenu_ivedimas_geotiff()
                                        print(e)

                                elif os.path.isfile(perkelti_i + "\\" + pavadinimas + sufix):
                                    os.remove(perkelti_i + "\\" + pavadinimas + sufix)
                                    os.rename(_ + "\\" + file, perkelti_i + "\\" + pavadinimas + sufix)

                except Exception as e:
                    print(e)
            else:
                pass

    for item in pradiniai_duomenys.glob('**/*'):
        global counter3
        if item.suffix in ['.aprx']:
            pavadinimas = item.name.replace(" ", "").replace("_", "-").split(".")[0]
            isskaidytas = pavadinimas.split("-")
            if (isskaidytas[0] == "N" or isskaidytas[0] == "O") and (
                    isskaidytas[1] == "34" or isskaidytas[1] == "35") \
                    and (isskaidytas[3] == "AB" or isskaidytas[3] == "CD") and 99 > int(isskaidytas[2]) \
                    and len(isskaidytas) == 5:
                pavadinimas = f"{isskaidytas[0]}-{isskaidytas[1].zfill(2)}-{isskaidytas[2].zfill(3)}\
                    -{isskaidytas[3]}-{isskaidytas[4].zfill(2)}"
                pavadinimas = pavadinimas.replace(" ", "")
                strukturinis_folderis = f"{isskaidytas[0]}-{isskaidytas[1]}-{isskaidytas[2]}-{isskaidytas[3]}"
                perkelti_i = f"{i_folderi}\\MXD\\10000\\{strukturinis_folderis}"
                tikrinti_direktorijas = perkelti_i
                if not os.path.exists(tikrinti_direktorijas):
                    os.makedirs(tikrinti_direktorijas)
                    tikrinti_direktorijas = tikrinti_direktorijas + "\\" + pavadinimas
                    if not os.path.exists(tikrinti_direktorijas):
                        os.makedirs(tikrinti_direktorijas)
                elif not os.path.exists(tikrinti_direktorijas + "\\" + pavadinimas):
                    os.makedirs(tikrinti_direktorijas + "\\" + pavadinimas)
                perkelti_i = perkelti_i + "\\" + pavadinimas
                print(perkelti_i)
                try:

                    for _, dir, files in os.walk(os.path.dirname(item)):
                        for direktorija in dir:
                            try:
                                shutil.rmtree(perkelti_i + "\\" +direktorija)
                                print(f"istrinta{direktorija}")
                            except:
                                pass

                            for direktorija in dir:
                                print(perkelti_i)
                                shutil.move(_ + "\\" + direktorija, perkelti_i)

                            for file in files:
                                if not os.path.isfile(perkelti_i + "\\" + file):
                                    os.rename(_ + "\\" + file, perkelti_i + "\\" + file)
                                    counter3 += 1
                                    counter_str = str(counter3)
                                    print(counter_str)
                                    x = lenteles.Ivedimas(counter_str, pavadinimas, perkelti_i, "MXD", "",
                                                          "10000", str(redagavimo_data), "", "Pridetas")
                                    e = x.duomenu_ivedimas_mxd()
                                    print(e)
                                elif os.path.isfile(perkelti_i + "\\" + file):
                                    os.remove(perkelti_i + "\\" + file)
                                    os.rename(_ + "\\" + file, perkelti_i + "\\" + file)

                except Exception as e:
                    print(e)
            else:
                pass

