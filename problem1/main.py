class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi
  
class Segitiga:
    def __init__(self, tinggi, alas):
        self.tinggi = tinggi
        self.alas = alas
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def keliling(self):
        return 3 * self.alas
    
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

persegi = Persegi(4)
segitiga = Segitiga(3, 4)
persegi_panjang = PersegiPanjang(7, 8)

luas_persegi = persegi.luas()
luas_segitiga = segitiga.luas()
luas_persegi_panjang = persegi_panjang.luas()

kel_persegi = persegi.keliling()
kel_segitiga = segitiga.keliling()
kel_persegi_panjang = persegi_panjang.keliling()

print("Luas")
print(f"Persegi : {luas_persegi}")
print(f"Segitiga : {int(luas_segitiga)}")
print(f"Persegi Panjang : {luas_persegi_panjang}")
print("Keliling")
print(f"Persegi : {kel_persegi}")
print(f"Segitiga : {kel_segitiga}")
print(f"Persegi Panjang : {kel_persegi_panjang}")
