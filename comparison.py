import ratings_module
import distance_module

def en_yakin(isim):  # 'isim' girilen kullanicinin en yakin oldugu kullaniciyi hesaplayan fonksiyon
    kullanici = ratings_module.ratings.loc[isim]
    en_yakin_distance = float('inf')  # bir kullaniciya en benzer kullanici bulmak her zaman icin imkansiz oldugundan,
    en_yakin_kullanici = ''

    for diger_kullanici in ratings_module.ratings.itertuples():  # itertuples: index'i birinci eleman olarak ata
        if diger_kullanici.Index == isim:
            # 'isim' girilen kullaniciyi kendisiyle kiyaslama, diger kullanicilardan devam et
            continue

        diger_kullanici_distance = distance_module.distance(kullanici, ratings_module.ratings.loc[
            diger_kullanici.Index])
        # distance fonksiyonunu kullanici ve diger_kullanici ile cagir, 'diger_kullanici_distance' degiskenine kaydet

        if diger_kullanici_distance < en_yakin_distance:
            # line13'te hesaplanan uzaklik, 'uygunluk'tan daha kucukse daha yakin bir sonuc elde edilmis demektir
            en_yakin_distance = diger_kullanici_distance
            en_yakin_kullanici = diger_kullanici.Index

        return en_yakin_kullanici
