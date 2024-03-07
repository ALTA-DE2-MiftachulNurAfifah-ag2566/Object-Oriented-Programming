class Penjumlahan:
    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2

    def jumlah(self):
        return self.bil1 + self.bil2

class Pengurangan:
    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2

    def kurang(self):
        return self.bil1 - self.bil2

class Perkalian:
    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2

    def kali(self):
        return self.bil1 * self.bil2

class Pembagian:
    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2

    def bagi(self):
        return self.bil1 / self.bil2

penjumlahan = Penjumlahan(3, 4)
pengurangan = Pengurangan(15, 4)
perkalian = Perkalian(10, 10)
pembagian = Pembagian(12, 3)

hasil_jumlah = penjumlahan.jumlah()
hasil_kurang = pengurangan.kurang()
hasil_kali = perkalian.kali()
hasil_bagi = pembagian.bagi()

print(f"Penjumlahan : {hasil_jumlah}")
print(f"Pengurangan : {hasil_kurang}")
print(f"Perkalian : {hasil_kali}")
print(f"Pembagian : {int(hasil_bagi)}")
