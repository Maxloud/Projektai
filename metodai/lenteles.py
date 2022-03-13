import csv

class Ivedimas():
    def __init__(self,id,pavadinimas = None,direktorija = None,failo_tipas = "PDF",dydis = None,mastelis = "10000",
                 redagavimo_data = None,failo_redagavimo_data = None,papildoma_info = "Pridetas"):
        self.pavadinimas = pavadinimas
        self.direktorija = direktorija
        self.failo_tipas = failo_tipas
        self.dydis = dydis
        self.mastelis = mastelis
        self.redagavimo_data = redagavimo_data
        self.failo_redagavimo_data = failo_redagavimo_data
        self.papildoma_info = papildoma_info
        self.id = id

    def __str__(self):
        return self.id
    def duomenu_ivedimas_pdf(self):
        irasai = [self, self.pavadinimas, self.direktorija, self.failo_tipas, self.dydis, self.mastelis,
                  self.redagavimo_data, self.failo_redagavimo_data, self.papildoma_info]
        with open(r"C:\Users\dovyd\PycharmProjects\Projektinis_darbas\Kodas\PDF.csv", 'a') as f:
            irasas = csv.writer(f)
            irasas.writerow(irasai)

    def duomenu_ivedimas_geotiff(self):
        irasai = [self, self.pavadinimas, self.direktorija, self.failo_tipas, self.dydis, self.mastelis,
                  self.redagavimo_data, self.failo_redagavimo_data, self.papildoma_info]
        with open(r"C:\Users\dovyd\PycharmProjects\Projektinis_darbas\Kodas\GEOTIFF.csv", 'a') as f:
            irasas = csv.writer(f)
            irasas.writerow(irasai)

    def duomenu_ivedimas_mxd(self):
        irasai = [self, self.pavadinimas, self.direktorija, self.failo_tipas, self.dydis, self.mastelis,
                  self.redagavimo_data, self.failo_redagavimo_data, self.papildoma_info]
        with open(r"C:\Users\dovyd\PycharmProjects\Projektinis_darbas\Kodas\MXD.csv", 'a') as f:
            irasas = csv.writer(f)
            irasas.writerow(irasai)







