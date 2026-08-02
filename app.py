import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={st.secrets['TMDB_API_KEY']}&language=en-US"
    response = requests.get(url)
    data = response.json()

    poster_path = data.get("poster_path")
    if not poster_path:
        return "https://placehold.co/500x750?text=No+Poster"
    return "https://image.tmdb.org/t/p/w500" + poster_path

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    top_matches=similarity[movie_index]

    recommended_movies=[]
    recommended_movies_posters=[]
    for idx, _score in top_matches:
        movie_id=movies.iloc[idx].id
        recommended_movies.append(movies.iloc[idx].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


# similarity.pkl and movie_dict.pkl are trusted artifacts built by this project's own main.ipynb.
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# List of per-movie top-5 (neighbor_index, score) pairs, not a full N x N matrix (see main.ipynb).
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select a movie',
movies['title'].values)

if st.button('Recommendation'):
    names,posters = recommend(selected_movie_name)


    col1, col2, col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2] )
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])