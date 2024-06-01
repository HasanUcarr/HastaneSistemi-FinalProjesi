from personel import personel_bilgileri
#doktor bilgileri için class
class doktor_bilgileri(personel_bilgileri):
    def __init__(self, personel_no, isim, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, isim, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # doktorlara ait bilgileri kullanabilmek için get metotları
    # doktorlara ait bilgileri güncelleyebilmek için set metotları
    def get_uzmanlik(self):
        return self.__uzmanlik
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_hastane(self):
        return self.__hastane
    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self, yuzde):
        self.__maas += self.__maas * yuzde / 100

    #doktora ait bilgileri ekrana yazmak için str metodu
    def __str__(self):
        return (f"personel no: {self.get_personel_no()}, isim: {self.get_isim()}, soyisim: {self.get_soyad()},"
                f" departman: {self.get_departman()}, maas: {self.get_maas()}, uzmanlik: {self.__uzmanlik},"
                f" deneyim yılı: {self.__deneyim_yili}, hastane: {self.__hastane}")

