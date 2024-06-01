from personel import personel_bilgileri
class hemsire_bilgileri(personel_bilgileri):
    def __init__(self, personel_no, isim, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, isim, soyad, departman, maas)
        self._calisma_saati = calisma_saati
        self._sertifika = sertifika
        self._hastane = hastane

    # hemsirelere ait bilgileri kullanabilmek için get metotları
    # hemsirelere ait bilgileri güncelleyebilmek için set metotları
    def get_calisma_saati(self):
        return self._calisma_saati

    def set_calisma_saati(self, calisma_saati):
        self._calisma_saati = calisma_saati

    def get_serfifika(self):
        return self._sertifika

    def set_sertifika(self, sertifika):
        self.sertifika = sertifika

    def get_hastane(self):
        return self._hastane

    def set_hastane(self, hastane):
        self._hastane = hastane

    def maas_arttir(self, yuzde):
        self.__maas += self.__maas * yuzde / 100

    #hemsire bilgilerini ekrana yazdırmak için str metodu
    def __str__(self):
        return (f"personel no: {self.get_personel_no()}, isim: {self.get_isim()}, soyisim: {self.get_soyad()},"
                f" departman: {self.get_departman()}, maas: {self.get_maas()}, çalışma saati: {self._calisma_saati},"
                f" sertifika: {self._sertifika}, hastane: {self._hastane}")

#hemsire= hemsire_bilgileri(123,"hem","şire","hastane",33300,23,"deneyimli","hastane")
#print(hemsire)