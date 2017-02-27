#-*- coding: utf-8 -*-

class Carpark:
    def __init__(self, znamka, model, kilometri, servis):
        self.znamka = znamka
        self.model = model
        self.kilometri = kilometri
        self.servis = servis

    def izpis_avtomobila(self):
            return(self.znamka + " " + self.model)

    def kilometri( self, kilometri_novi):
        self.kilometri = kilometri_novi

    def zadnji_servis(self, datum):
        self.servis = datum

seznam_avtomobilov = []

def izpis_vseh_vozil(seznam_avtomobilov):
    for avto, podatki in enumerate(seznam_avtomobilov):
        print("Vozilo: " + str(avto) + " " + str(podatki.izpis_avtomobila()) + " " + str(podatki.kilometri) + " " + str(podatki.servis))

def izbira_avtomobila(seznam_avtomobilov):
    izpis_vseh_vozil(seznam_avtomobilov)
    izbor = raw_input("Izberite številko vozila, za katerega želite uporabiti program: ")
    return seznam_avtomobilov[int(izbor)]

def dodajanje_avtomobila(seznam_avtomobilov):
    znamka = raw_input("Znamka vozila: ")
    model = raw_input("Model avtomobila: ")
    kilometri = raw_input("Število kilometrov: ")
    servis = raw_input("Datum zadnjega servisa: ")
    vozilo = Carpark(znamka, model, kilometri, servis)
    seznam_avtomobilov.append(vozilo)
    izpis_vseh_vozil(seznam_avtomobilov)

def odvzemanje_avtomobila(seznam_avtomobilov):
    izbrano_vozilo = izbira_avtomobila(seznam_avtomobilov)
    seznam_avtomobilov.remove(izbrano_vozilo)
    izpis_vseh_vozil(seznam_avtomobilov)

def urejanje_km(seznam_avtomobilov):
    izbor = izbira_avtomobila(seznam_avtomobilov)
    novo_stanje = (raw_input("Vnesite novo stanje kilometrov: "))
    izbor.kilometri(novo_stanje)
    izpis_vseh_vozil(seznam_avtomobilov)

def sprememba_servisa(seznam_avtomobilov):
        izbor = izbira_avtomobila(seznam_avtomobilov)
        novi_datum = raw_input("Vnesite datum zadnjega servisa: ")
        izbor.zadnji_servis(novi_datum)
        izpis_vseh_vozil(seznam_avtomobilov)

def main():
    print("Dobrodošli v urejevalniku službenih vozil.")

    while True:
        print("Izberite eno od naslednjih možnosti:\n a) Ogled seznama vozil \n b) Dodajanje novega vozila \n"
            " c) Brisanje vozila s seznama\n d) Urejanje števila kilometrov za določeno vozilo\n"
            " e) Urejanje datuma zadnjega servisa za določeno vozilo\n f) Zapis sprememb v datoteko in izhod iz programa")

        izbira = raw_input("Vaša izbira: ")

        if izbira.lower() == "a":
            izpis_vseh_vozil(seznam_avtomobilov)
        elif izbira.lower() == "b":
            dodajanje_avtomobila(seznam_avtomobilov)
        elif izbira.lower() == "c":
            odvzemanje_avtomobila(seznam_avtomobilov)
        elif izbira.lower() == "d":
            urejanje_km(seznam_avtomobilov)
        elif izbira.lower() == "e":
            sprememba_servisa(seznam_avtomobilov)
        elif izbira.lower() == "f":
            print("Prijeten dan še naprej.")
            break

    with open("vozila.txt", "w") as datoteka:
        for avtomobil in seznam_avtomobilov:
            datoteka.write("%s %s, %s, %s\n" % (avtomobil.znamka, avtomobil.model, avtomobil.kilometri, avtomobil.servis))


main()

