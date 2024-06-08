import pandas
from personel import personel_bilgileri
from doktor import doktor_bilgileri
from hemsire import hemsire_bilgileri
from hasta import hasta_bilgileri

def main():
    veriler = {
        'personel_no': [],
        'isim': [],
        'soyad': [],
        'departman': [],
        'maas': [],
        'uzmanlik': [],
        'deneyim_yili': [],
        'hastane': [],
        'calisma_saati': [],
        'sertifika': [],
        'hasta_no': [],
        'dogum_tarihi': [],
        'hastalik': [],
        'tedavi': [],
        'tedavi_suresi': []
    }

    personel1 = personel_bilgileri(101, "Mirza", "Millet", "temizlik", "20000")
    personel2 = personel_bilgileri(102, "Beşir", "Sarı", "yönetim", "55000")

    doktor1 = doktor_bilgileri(201, "Mehmet", "Öz", "Cerrahi", "88000", "Kalp ve damar cerrahisi", "12", "Columbia Üniversitesi Tıp Merkezi")
    doktor2 = doktor_bilgileri(202, "Gazi", "Yasargil", "Beyin cerrahisi", "96000", "Beyin cerrahisi", "28", "Zürih Üniversitesi Hastanesi")
    doktor3 = doktor_bilgileri(203, "Ercument", "Ovali", "Hematoloji", "100000", "Kök Hücre Araştırmaları", "20", "Memorial Şişli Hastanesi")

    hemsire1 = hemsire_bilgileri(301, "Aylin", "Cesur", "Yoğun Bakım", 6000, 40,
                                 "Yoğun Bakım Hemşireliği Sertifikası", "Sehir hastanesi")
    hemsire2 = hemsire_bilgileri(302, "Fatma", "Yılmaz", "Pediatri Hemşiresi", 6500, 38,
                                 "Pediatri Hemşireliği Sertifikası", "Sehir hastanesi")
    hemsire3 = hemsire_bilgileri(303, "Nazlı", "Kaya", "Nöroloji", 6200, 36,
                                 "Nöroloji Sertifikası", "Sehir hastanesi")

    hasta1 = hasta_bilgileri(401, "Hasan", "Uçar", "12.06.1985", "grip", "dinlenme ve ilaç kullanımı", 10)
    hasta2 = hasta_bilgileri(402, "Ayşe", "Kara", "17.10.1973", "Hipertansiyon", "Diyet ve İlaç Kullanımı", 20)
    hasta3 = hasta_bilgileri(403, "Mehmet", "Yılmaz", "22.12.2002", "Diabetes", "İnsülin Tedavisi", 150)

    nesneler = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]

    for nesne in nesneler:
        satir = {}
        for ozellik in veriler.keys():
            if hasattr(nesne, f"get_{ozellik}"):
                satir[ozellik] = getattr(nesne, f"get_{ozellik}")()
            else:
                satir[ozellik] = 0
        for bolum, deger in satir.items():
            veriler[bolum].append(deger)

    donustur = pandas.DataFrame(veriler)
    print(donustur.to_string())
    print("- "*100)
    try:
        donustur["maas"] = donustur["maas"].astype(int)
        donustur["deneyim_yili"] = donustur["deneyim_yili"].astype(int)
        uzmanlik_sayilari = donustur[donustur["uzmanlik"] != 0]["uzmanlik"].value_counts()

        print("Doktor uzmanlık çeşitleri ve bu uzmanlıkların bulunma sayıları:")
        print(uzmanlik_sayilari.to_string(header=None), "\n")
        print("- " * 100)

        deneyimli_doktorlar = donustur[donustur["deneyim_yili"] > 5]
        i = 0
        for a in deneyimli_doktorlar.iterrows():
            i += 1
        print("deneyim süresi 5 yıldan fazla olan doktor sayısı:", i, "\n")
        print("- " * 100)

        print("Hastaların alfabetik sıraya göre sıralanmış hali:")
        hasta_df = donustur[(donustur["hasta_no"] != 0)]
        hasta_df = hasta_df.loc[:, (hasta_df != 0).all()]
        sorted_df = hasta_df.sort_values(by='isim')
        print(sorted_df.to_string(), "\n")
        print("- " * 100)

        yuksek_maas_personelleri = donustur[donustur["maas"] > 7000]
        yuksek_maas_personelleri = yuksek_maas_personelleri.loc[:, (yuksek_maas_personelleri != 0).all()]
        print("Maaşı 7000 TL'den fazla olan personellerin bilgileri:")
        print(yuksek_maas_personelleri, "\n")
        print("- " * 100)

        donustur["dogum_tarihi"] = pandas.to_datetime(donustur["dogum_tarihi"], format='%d.%m.%Y', errors='coerce')
        buyuk_hastalar = donustur[donustur["dogum_tarihi"].dt.year < 1990]
        buyuk_hastalar = buyuk_hastalar.loc[:, (buyuk_hastalar != 0).all()]

        buyuk_hastalar = buyuk_hastalar[['isim', 'soyad', 'hasta_no', 'dogum_tarihi', 'hastalik', 'tedavi', 'tedavi_suresi']]
        print("Doğum yılı 1990 yılından önce olan hastalar:")
        print(buyuk_hastalar.to_string(index=False), "\n")
        print("- " * 100)

        print("Varolan dataframe'dan oluşturulan yeni dataframe:")
        alt_dataframe = pandas.DataFrame()

        uygun_sutunlar = ['isim', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']
        for sutun in uygun_sutunlar:
            alt_dataframe[sutun] = donustur[sutun]

        print(alt_dataframe.to_string())

    except Exception as x:
        print("hata oluştu, hatanın sebebi:", x)


if __name__ == "__main__":
    main()
