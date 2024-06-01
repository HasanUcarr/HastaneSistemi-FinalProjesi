#hasta sınıfı
class hasta_bilgileri:
    def __init__(self, hasta_no, isim, soyad, dogum_tarihi, hastalik, tedavi,tedavi_suresi):
        self.__hasta_no = hasta_no
        self.__isim = isim
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
        self.__tedavi_suresi = tedavi_suresi

    # hastalara ait bilgileri kullanabilmek için get metotları
    # hastalara ait bilgileri güncelleyebilmek için set metotları
    def get_hasta_no(self):
        return self.__hasta_no
    def set_hasta_no(self,hasta_no):
        self.__hasta_no = hasta_no

    def get_isim(self):
        return self.__isim
    def set_isim(self,isim):
        self.__isim = isim

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self,soyad):
        self.__soyad = soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    def set_dogum_tarihi(self,dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik
    def set_hastalik(self,hastalik):
        self.__hastalik = hastalik

    def get_tedavi(self):
        return self.__tedavi
    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def get_tedavi_suresi(self):
        return self.__tedavi_suresi
    def set_tedavi_suresi(self,sure):
        self.__tedavi_suresi =sure

    #hastalara ait bilgileri ekrana yazdirmak için str metodu
    def __str__(self):
        return (f"hasta numarası:{self.__hasta_no}, hasta adı:{self.__isim}, hasta soyadı:{self.__soyad}, doğum tarihi:{self.__dogum_tarihi}"
                f", hastalığı:{self.__hastalik}, tedavisi:{self.__tedavi}, iyilesme suresi:{self.__tedavi_suresi}")


