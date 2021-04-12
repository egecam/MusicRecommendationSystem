import pandas as pd

url = 'song-ratings.csv'  # veritabanini 'url' değiskenine tanimla

ratings = pd.read_csv(url, index_col=0)  # veritabanini baslangicindan itibaren oku ve 'ratings' değiskenine kaydet
ratings = ratings.fillna(0)  # 'fill n/a with 0' = ratings icindeki bos verileri 0'a esitle ve ratings'e kaydet
