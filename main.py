import string
from os.path import exists
from app.record import *
from app.constants import *
from app.spasavanje import Spasavanje
from app.hash_file import *
import random

import time
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d.%m.%Y. %H:%M', prop)

def generisanje_primera():
    naziv = input("Gde da se stave primeri:")
    koliko = int(input("Koliko primera: "))
    with open("data/"+naziv+".csv","w") as f:
        for i in range(koliko):
            id = random.randrange(0,100)
            ime = ""
            temp = random.randrange(4,7)
            ime = ime + random.choice(string.ascii_uppercase)
            for j in range(temp):
                ime = ime + random.choice(string.ascii_lowercase)
            prezime = ""
            temp = random.randrange(6, 10)
            prezime = prezime + random.choice(string.ascii_uppercase)
            for j in range(temp):
                prezime = prezime + random.choice(string.ascii_lowercase)

            random_date1 = random_date("01.01.2015. 01:30", "01.01.2022. 04:50", random.random())
            broj_spasioca = ""
            for j in range(5):
                broj_spasioca = broj_spasioca + str(random.randrange(0,9))
            vreme_spasavanja = random.randrange(1,3000)
            niz = str(id)+","+ime+" "+prezime+","+random_date1+","+broj_spasioca+","+str(vreme_spasavanja)+"\n"
            if (i+1)==koliko:
                niz = str(id) + "," + ime + " " + prezime + "," + random_date1+ "," + broj_spasioca + "," + str(vreme_spasavanja)
            f.write(niz)


if __name__ == '__main__':
    binary_file = ""
    while True:
        print("Sta zelite od opcija (unesite broj da odaberete, 0 za iskljucivanje programa):\n"
              "1.Formiranje prazne datoteke\n"
              "2.Izbor aktivne datoteke zadavanjem njenog naziva\n"
              "3.Prikaz naziva aktivne datoteke\n"
              "4.Pocni operaciju\n"
              "5.Ispis aktivne, izlazne i datoteke gresaka\n"
              "6.Ucitati test primer\n"
              "7.Generisanje test primera")
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
                naziv = input("Unesite naziv test fajla:")
                if exists("data/"+naziv+".csv"):
                    with open("data/"+naziv+".csv", "r") as l:
                        while True:
                            temp = l.readline()
                            if not temp:
                                break
                            lista = temp.split(",")
                            binary_file.insert_novi_element({"id":int(lista[0]),"ime_i_prezime":lista[1],
                                                               "datum_i_vreme":lista[2],"oznaka_spasioca":lista[3],
                                                               "trajanje_spasavanja":int(lista[4]),"status":1})
                else:
                    print("Datoteka koju ste uneli ne postoji!")
            else:
                print("Niste selektovali aktivnu datoteku!")
        if(unos==7):
            generisanje_primera()