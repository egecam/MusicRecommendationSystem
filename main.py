import ratings_module
import comparison

y = input('Kullanici adinizi girin: ')
en_benzer_kullanici = comparison.en_yakin(y)
# print(en_benzer_kullanici)
# output: Ege -> en_benzer_kullanici = Ege
x = input('Oneri almak istediginiz parcayi girin: ')
oneri_puani = ratings_module.ratings.at[en_benzer_kullanici, x]  # Ege'nin 'x' parcasina verdigi puani kaydet
print(oneri_puani)

if oneri_puani < 3:
    print('Bu parca muhtemelen size gore degil.')
elif 5 != oneri_puani >= 3:
    print('Bu parca size gore.')
elif oneri_puani == 5:
    print('Bu parca sizin favoriniz olabilir!')
