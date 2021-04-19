from scipy.spatial.distance import euclidean


# scipy kutuphanesinden 'euclidean' modulunu cagir.
# bu, 'euclidean' fonksiyonunu kullanarak iki veri arasindaki oklid uzakligini hesaplamami saglayacak.

def distance(kullanici1, kullanici2):  # uzaklik fonksiyonunu olusturuyorum
    distance = euclidean(kullanici1, kullanici2)
    # kullanici1 ve kullanici 2 parametreleriyle euclidean fonksiyonunu cagir ve 'distance' degiskenine ata
    return distance
