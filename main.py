from app.record import *
from app.binary_file import *
from app.constants import *
from app.sequential_file import *
from app.serial_file import *
from os.path import exists
from app.spasavanje import Spasavanje
from app.hash_file import *

if __name__ == '__main__':
    binary_file = ""
    binary_file_izlazna = ""
    binary_file_greska = ""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.Formiranje prazne datoteke\n"
              "2.Izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.Prikaz naziva aktivne datoteke\n"
              "4.Pocni operaciju\n"
              "5.Ispis aktivne, izlazne i datoteke gresaka\n"
              "6.Ucitati test primer")
        unos = int(input("Unesite ovde opciju:"))
        if (unos == 0):
            break
        if (unos == 1):
            naziv = "data/" + str(input("Unesite naziv datoteke:")) + ".dat"
            attributesTemp = ["id", "ime_i_prezime", "datum_i_vreme", "oznaka_spasioca", "trajanje_spasavanja",
                              "status"]
            fmtTemp = "i60s17s5sii"
            rec = Record(attributesTemp, fmtTemp, CODING)
            binary_file = HashFile(naziv,rec,F,B)
            binary_file.formiranje_prazne_datoteke()

        if (unos == 2):
            naziv = "data/" + str(input("Unesite naziv aktivne datoteke:")) + ".dat"
            attributesTemp = ["id", "ime_i_prezime", "datum_i_vreme", "oznaka_spasioca", "trajanje_spasavanja",
                              "status"]
            fmtTemp = "i60s17s5sii"
            rec = Record(attributesTemp, fmtTemp, CODING)
            binary_file = HashFile(naziv, rec, F, B)

        if (unos == 3):
            if binary_file != "":
                print("Naziv fajla: " + binary_file.filename.split("/")[1])
            else:
                print("Niste odabrali aktivni fajl!")
        if unos ==4:
            if binary_file == "":
                print("Morate uneti naziv aktivne datoteke!")
                continue

            while True:
                print("1.Napraviti slog\n"
                      "2.Izmeniti slog\n"
                      "3.Logicki izbrisati slog\n"
                      "4.Fizicki izbrisati slog\n"
                      "0.Natrag")
                unos = int(input("Unesite opciju ovde:"))
                if unos == 0:
                    break
                if unos == 1:
                    if (binary_file != ""):
                        temp = Spasavanje()
                        temp.pravljenje_objekta()
                        binary_file.azur_ras_sa_lin_raz_dir(temp.vrati_vrednost())
                if unos == 2:
                    if (binary_file != ""):
                        temp = Spasavanje()
                        temp.promena_vrednosti()
                        binary_file.azur_ras_sa_lin_raz_dir(temp.vrati_vrednost())
                if unos == 3:
                    if (binary_file != ""):
                        temp = Spasavanje()
                        temp.logicko_brisanje()
                        binary_file.azur_ras_sa_lin_raz_dir(temp.vrati_vrednost())
                if unos == 4:
                    if (binary_file != ""):
                        temp = Spasavanje()
                        temp.pravo_brisanje()
                        binary_file.azur_ras_sa_lin_raz_dir(temp.vrati_vrednost())
        if (unos == 5):
            if binary_file!="":
                binary_file.print_file()
        if (unos == 6):
            if binary_file != "":
                with open("data/test.csv", "r") as l:
                    while True:
                        temp = l.readline()
                        if not temp:
                            break
                        lista = temp.split(",")
                        binary_file.insert_novi_element({"id":int(lista[0]),"ime_i_prezime":lista[1],
                                                           "datum_i_vreme":lista[2],"oznaka_spasioca":lista[3],
                                                           "trajanje_spasavanja":int(lista[4]),"status":1})