import streamlit as st
import pandas as pd
import numpy as np
import requests as requests

st.write("Top Movies ")


# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     def lowercase(x): return str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)



# fetch movies list from the API
response = requests.get(
    'https://api.themoviedb.org/3/movie/popular?api_key=d9604e1674b0955abd840336ad75a8e5&language=en-US&page=1')
movies = response.json()['results']

# get movie genres
genre_response = requests.get(
        'https://api.themoviedb.org/3/genre/movie/list?api_key=d9604e1674b0955abd840336ad75a8e5&language=en-US')
genres = genre_response.json()['genres']


# build a dictionary of genres
genres_dict = {}
for genre in genres:
        genres_dict[genre['id']] = genre['name']


# create sidebar with movie genre selection
genre_list = list(genres_dict.values())
selected_genre = st.sidebar.multiselect('Genre', genre_list)



# display  top movie as hero banner

# st.write("Trending Movie ")
# st.title(movies[0]['title'])
# st.markdown('**Popularity:** ' + str(movies[0]['popularity']))
# st.markdown('**Vote Average:** ' + str(movies[0]['vote_average']))
# st.markdown('**Release Date:** ' + str(movies[0]['release_date']))
# st.markdown('**Overview:** ' + str(movies[0]['overview']))
# st.image('https://image.tmdb.org/t/p/w500' + movies[0]['poster_path'])

# filter movies by selected genre in one line 
@st.cache
def filter_movies(movies, genres):
        filtered_movies = []
        for movie in movies:
                movie_genre_ids = movie['genre_ids']
                movie_genres = []
                for genre_id in movie_genre_ids:
                        movie_genres.append(genres_dict[genre_id])
                if set(movie_genres).intersection(set(genres)):
                        filtered_movies.append(movie)
        return filtered_movies


data_load_state = st.text('Loading data...')


# display movies with image, title and genre as small cards in one line
if selected_genre:
    movies = filter_movies(movies, selected_genre)
for movie in movies:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(movie['title'])
        st.image('https://image.tmdb.org/t/p/w500' +
                         movie['poster_path'])

       
                
        with col2:
               st.write(movie['overview'])

# display movie trailers on button click


        if st.button('Trailer', key=movie['id']):
                trailer_response = requests.get('https://api.themoviedb.org/3/movie/' + str(movie['id']) + '/videos?api_key=d9604e1674b0955abd840336ad75a8e5&language=en-US')
                trailer = trailer_response.json()['results'][0]
                st.video('https://www.youtube.com/watch?v=' + trailer['key'])






# dislay movie per genre
# for genre in selected_genre:
#         st.write(genre)
#         for movie in movies:
#                 movie_genre_ids = movie['genre_ids']
#                 movie_genres = []
#                 for genre_id in movie_genre_ids:
#                         movie_genres.append(genres_dict[genre_id])
#                 if genre in movie_genres:
#                         st.write(movie['title'])
#                         st.image('https://image.tmdb.org/t/p/w500' + movie['poster_path'])
#                         st.write(movie['overview'])
#                         st.write(movie['release_date'])























        









# # create a list of movie titles and images for each movie
# movie_titles = [movie['title'] for movie in movies]
# movie_images = [movie['poster_path'] for movie in movies]

# # create a dictionary of movie titles and images
# movie_dict = dict(zip(movie_titles, movie_images))

# # display the movie titles as a dropdown
# movie = st.selectbox('Select a movie', movie_titles)

# # display the movie image
# st.image('https://image.tmdb.org/t/p/w500/' + movie_dict[movie])


# # create a sidebar of movie titles and images
# st.sidebar.header('Top Movies')
# for movie in movies:
#         st.sidebar.image('https://image.tmdb.org/t/p/w500/' + movie['poster_path'], width=100)
#         st.sidebar.write(movie['title'])




# # go through the list and display movies as cards in a grid  columns and make them clickable
# for movie in movies:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.image('https://image.tmdb.org/t/p/w500/' + movie['poster_path'])
#     with col2:
#         st.write(movie['title'])
#     with col3:
#         st.write(movie['overview'])


















