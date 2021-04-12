from csv import DictReader

with open('song-ratings.csv', 'r') as oku:
    dict_reader = DictReader(oku)
    list_of_dict = list(dict_reader)