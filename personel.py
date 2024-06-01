class personel_bilgileri:
    # personel bilgilerini tutmak için class
    def __init__(self, personel_no, isim, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__isim = isim
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    #personele ait bilgileri kullanabilmek için get metotları
    #personele ait bilgileri güncelleyebilmek için set metotları
    def get_personel_no(self):
        return self.__personel_no
    def set_personel_no(self,personel_no):
        self.__personel_no = personel_no

    def get_isim(self):
        return self.__isim
    def set_isim(self,isim):
        self.__isim = isim

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self,soyad):
        self.__soyad = soyad

    def get_departman(self):
        return self.__departman
    def set_departman(self,departman):
        self.__departman = departman

    def get_maas(self):
        return self.__maas
    def set_maas(self,maas):
        self.__maas = maas
    #personel bilgilerini ekrana yazdırabilmek için str metodu
    def __str__(self):
        return (f"personel no:{self.__personel_no}, isim:{self.__isim}, soyisim:{self.__soyad},"
                f" departman:{self.__departman}, maas:{self.__maas}")
