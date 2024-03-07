class Ongkir:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung(self):
        vol =  self.panjang * self.lebar * self.tinggi
        if int(vol) <= 50:
            if int(self.berat) <= 1:
                return 5000
            else:
                return "Harga di atas standar"

ongkir = Ongkir(5, 2, 4, 1)
ongkos_kirim = ongkir.hitung()
print(f"Harga : Rp {ongkos_kirim}")
