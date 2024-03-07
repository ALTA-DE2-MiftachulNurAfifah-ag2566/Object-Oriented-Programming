class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung:
    def __init__(self, jejari, tinggi):
        self.jejari = jejari
        self.tinggi = tinggi

    def volume(self):
        return (22/7) * (self.jejari ** 2) * self.tinggi


kubus = Kubus(10)
balok = Balok(3, 6, 10)
tabung = Tabung(7, 10)

vol_kubus = kubus.volume()
vol_balok = balok.volume()
vol_tabung = tabung.volume()

print("Volume")
print(f"Kubus : {vol_kubus}")
print(f"Balok : {vol_balok}")
print(f"Tabung : {int(vol_tabung)}")
