# Music Recommendation System

A Python desktop application to make predictions about wether a user will like or dislike a song.

## Description

Collaborative Filtering is a user-data-based method which seeks the information of every single user's data on the content. Thanks to dataset, the algorithm aims to classify the users by their likes and dislikes.
I use Euclidean distance to calculate the most similar other user to the input user. With the data of matched users, I am able to make song predictions.

Music Recommendation System uses a simple model of database of Spotify with  `8 users and 24 songs`. The reason for this is to learn the collaborative filtering algorithm and make the correct user classification and learn how to work with data in Python.

## Libraries

I use `Pandas` to read and process the data from **song-ratings.csv** and `SciPy` to calculate Euclidean distance.
Apart from the purpose of program, I use `CSV Reader` and convert the CSV file to **dictionary** to check data while I work on calculation.

### Dependencies

* Python 3.9.4

* Pandas.py
```
pip3 install pandas
```

* SciPy
```
pip3 install scipy
```

## Authors

Ege Çam  
[@egecamx](https://twitter.com/egecamx)  

## Inspiration & Acknowledgments

* [Mosh's Tutorial on ML with Python](https://www.youtube.com/watch?v=7eh4d6sabA0&t=1728s)
* [Jack Bandy's article on recommendation systems](https://towardsdatascience.com/a-simple-song-recommender-system-in-python-tutorial-3e4c111198d6)
