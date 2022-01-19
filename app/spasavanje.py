class Spasavanje:
    def __init__(self):
        self.id = -1
        self.ime_i_prezime=""
        self.datum_i_vreme = ""
        self.oznaka_spasioca = ""
        self.trajanje_spasavanja = -1
        self.status=1
        self.svrha=-1
    def vrati_vrednost(self):
        return {"id": self.id, "ime_i_prezime":self.ime_i_prezime, "datum_i_vreme":self.datum_i_vreme,
                "oznaka_spasioca":self.oznaka_spasioca,"trajanje_spasavanja":self.trajanje_spasavanja,
                "status":self.status,"svrha":self.svrha}
    def postavi_vrednost(self, objekat):
        self.id = int(objekat["id"])
        self.ime_i_prezime = objekat["ime_i_prezime"]
        self.datum_i_vreme = objekat["datum_i_vreme"]
        self.oznaka_spasioca = objekat["oznaka_spasioca"]
        self.trajanje_spasavanja = int(objekat["trajanje_spasavanja"])
        self.status = objekat["status"]
        self.svrha = objekat["svrha"]
    def pravljenje_objekta(self):
        self.id = int(input("Unesite evidencioni broj:"))
        while True:
            if(self.id > 10**7):
                print("Evidencioni broj mora biti 7 cifara.")
                self.id = int(input("Unesite evidencioni broj:"))
            else:
                break
        self.ime_i_prezime = input("Ime i prezime spasenog:")
        #self.datum_i_vreme = (datetime.now()).strftime("%d.%m.%Y %H:%M")
        self.datum_i_vreme = input("Datum i vreme:")
        self.oznaka_spasioca = input("Oznaka spasioca:")
        while True:
            if len(self.oznaka_spasioca)!=5:
                self.oznaka_spasioca = input("Oznaka spasioca mora biti tacno 5 karaktera:")
            else:
                break
        self.trajanje_spasavanja = int(input("Trajanje spasavanja:"))
        while True:
            if self.trajanje_spasavanja>4320:
                self.trajanje_spasavanja = int(input("Mora biti manje ili jednako 4320 minuta:"))
            else:
                break
        self.status=1
        self.svrha=1
    def logicko_brisanje(self):
        self.id = int(input("Unesite evidencioni broj:"))
        self.status = 0
        self.svrha=3
    def promena_vrednosti(self):
        self.id = int(input("Unesite evidencioni broj:"))
        print("Promena datuma i vremena spasavanja")

        self.datum_i_vreme = input("Ovde unesite:")
        self.svrha=2

    def pravo_brisanje(self):
        self.id = int(input("Unesite evidencioni broj:"))
        self.svrha = 4