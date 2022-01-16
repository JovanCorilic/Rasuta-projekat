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


        if (unos == 2):
            naziv = "data/" + str(input("Unesite naziv aktivne datoteke:")) + ".dat"

        if (unos == 3):
            if binary_file != "":
                print("Naziv fajla: " + binary_file.filename.split("/")[1])
            else:
                print("Niste odabrali aktivni fajl!")