"""import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7e89460c9538644483e0e5567b5348c8&language=en-US'.format(movie_id))
    data = response.json()
    st.text(data)
    st.text('https://api.themoviedb.org/3/movie/{}?api_key=7e89460c9538644483e0e5567b5348c8&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkI','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie recommender system')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",movies['title'].values) 
if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])

    with col4:
        st.header(names[3])
        st.image(posters[3])

    with col5:
        st.header(names[4])
        st.image(posters[4])
------------------------------------------------------------------------------------

"""

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=7e89460c9538644483e0e5567b5348c8&language=en-US'
        response = requests.get(url)
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except:
        return "https://via.placeholder.com/500x750?text=Error+Loading+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])