#!/usr/bin/python

import os

from app.binary_file import BinaryFile


class HashFile(BinaryFile):
    #HashFile(fn, rec, F, B)
    def __init__(self, filename, record, blocking_factor, b, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, empty_key)
        self.b = b

    def hash(self, id):
        return id % self.b

    def formiranje_prazne_datoteke(self):
        with open(self.filename, "wb") as f:
            for _ in range(self.b):
                block = self.blocking_factor*[self.get_empty_rec()]
                self.write_block(f, block)


    def trazenje_u_rasutoj_sa_lin_traz(self,id):
        broj = 99
        broj1 = 0
        r = self.hash(id)
        pocetni = r
        with open(self.filename, "rb+") as f:
            while broj == 99:
                q=0
                f.seek(r*self.block_size)
                block = self.read_block(f)
                while q<=self.blocking_factor and broj==99:
                    if id==block[q]["id"]:
                        broj = 0
                    else:
                        if block[q]["id"]==-1:
                            broj=1
                        else:
                            q = q+1
                if q>=self.blocking_factor:
                    r = r % self.b +1
                    if r==pocetni :
                        broj=1
                        broj1=1
        return broj,broj1,r,q

    def provera_kandidata(self, kljuc,r,rp,nadjen):
        rm = self.hash(kljuc)
        if r>rp:
            if rm>r or rm<=rp:
                nadjen = 1
        else:
            if rm<=rp and rm>r:
                nadjen = 1
        return nadjen

    def brisanje_u_ras_dat_sa_lin_traz(self,r,q,f):
        pomeranje = 1
        f.seek(r*self.block_size)
        block = self.read_block(f)
        blockp=[]
        while pomeranje ==1:
            while q<=self.blocking_factor and block[q]["id"]!=-1:
                block[q] = block[q+1]
                q = q + 1
            blockp = block
            rp = r
            if block[q]["id"]==-1:
                pomeranje=0
            else:
                nadjen = 0
                while nadjen==0 and pomeranje ==1:
                    if q==self.blocking_factor:
                        r = 1 + r % self.b
                        f.seek(r * self.block_size)
                        block = self.read_block(f)
                        q=-1
                    q = q+1
                    if block[q] != -1 and r != rp:
                        nadjen = self.provera_kandidata(block[q]["id"],r,rp,nadjen)
                    else:
                        pomeranje = 0
                if nadjen == 1:
                    blockp[len(blockp)-1] = block[q]
                else:
                    blockp[len(blockp)-1] = self.get_empty_rec()
        if blockp !=[]:
            self.write_block(f,blockp)

    def azur_ras_sa_lin_raz_dir(self,lista):
        with open(self.filename, "rb+") as f:
            for i in lista:
                broj, broj1, r, q = self.trazenje_u_rasutoj_sa_lin_traz(i["id"])
                if broj==0:
                    if i["svrha"]==4:
                        self.brisanje_u_ras_dat_sa_lin_traz(r,q,f)
                    elif i["svrha"]==2:
                        f.seek(r*self.block_size)
                        block = self.read_block(f)
                        block[q]["datum_i_vreme"] = i["datum_i_vreme"]
                        self.write_block(f,block)
                elif i["svrha"]==1 and broj1==0:
                    self.insert_novi_element(f,i)

    def insert_novi_element(self,f,i):
        broj, broj1, r, q = self.trazenje_u_rasutoj_sa_lin_traz(i["id"])
        if broj == 1 and broj1 == 0:
            with open(self.filename, "rb+") as a:
                a.seek(r * self.block_size)
                block = self.read_block(a)
                block[q] = i
                print("r je "+str(r)+" a q je"+str(q))
                a.seek(r * self.block_size)
                self.write_block(a, block)
        elif broj1 == 1:
            print("nema memorije")

        else:
            print(i["id"])
            print("slog sa datom vrednoscu kljuca vec postoji")

    def print_file(self):
        with open(self.filename, "rb") as f:
            for i in range(self.b):
                block = self.read_block(f)
                print("Bucket {}".format(i + 1))
                self.print_block(block)

            print("Overflow zone:")
            while True:
                rec = self.read_record(f)
                if not rec:
                    break
                print(rec)

# Ispod je nevazno
"""
    def __insert_overflow(self, f, rec):
        f.seek(self.b * self.block_size)

        while True:
            record = self.read_record(f)
            if not record:
                break
            if record.get("id") == rec.get("id"):
                if record.get("status") == 1:
                    print("Already exists with ID {}".format(rec.get("id")))
                else:
                    f.seek(-self.record_size, 1)
                    self.write_record(f, rec)
                return

        self.write_record(f, rec)

    def insert_record(self, rec):
        id = rec.get("id")
        block_idx = self.hash(id)

        with open(self.filename, "rb+") as f:
            f.seek(block_idx * self.block_size)
            block = self.read_block(f)

            i = 0
            while i < self.blocking_factor and block[i].get("status"):
                if block[i].get("id") == id:
                    if block[i].get("status") == 1:
                        print("Already exists with ID {}".format(id))
                    else:
                        block[i] = rec
                        f.seek(block_idx * self.block_size)
                        self.write_block(f, block)
                    return
                i += 1

            if i == self.blocking_factor:
                self.__insert_overflow(f, rec)
                return

            block[i] = rec
            f.seek(block_idx * self.block_size)
            self.write_block(f, block)

    def print_file(self):
        with open(self.filename, "rb") as f:
            for i in range(self.b):
                block = self.read_block(f)
                print("Bucket {}".format(i+1))
                self.print_block(block)

            print("Overflow zone:")
            while True:
                rec = self.read_record(f)
                if not rec:
                    break
                print(rec)

    def __find_in_overflow(self, f, id):
        f.seek(self.b * self.block_size)

        i = 0
        while True:
            rec = self.read_record(f)
            if not rec:
                return None
            if rec.get("id") == id:
                return (self.b, i)
            i += 1

    def find_by_id(self, id):
        block_idx = self.hash(id)

        with open(self.filename, "rb+") as f:
            f.seek(block_idx * self.block_size)
            block = self.read_block(f)

            for i in range(self.blocking_factor):
                if block[i].get("status") == 0:
                    return None
                if block[i].get("status") == 1 and block[i].get("id") == id:
                    return (block_idx, i)

            return self.__find_in_overflow(f, id)

        return None

    def delete_by_id(self, id):
        found = self.find_by_id(id)

        if not found:
            return None

        block_idx = found[0]
        rec_idx = found[1]

        with open(self.filename, "rb+") as f:
            if block_idx < self.b:
                f.seek(block_idx * self.block_size)
                block = self.read_block(f)
                block[rec_idx]["status"] = 2
                f.seek(block_idx * self.block_size)
                self.write_block(f, block)
            else:
                f.seek(self.b * self.block_size + rec_idx * self.record_size)
                rec = self.read_record(f)
                rec["status"] = 2
                f.seek(-self.record_size, 1)
                self.write_record(f, rec)
            return found
"""