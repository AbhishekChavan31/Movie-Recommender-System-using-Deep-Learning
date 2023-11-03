import streamlit as st
import pickle
import pandas as pd
import requests

# importing the dictionary values of the movies data frame from the pickle file
movies_data = pickle.load(open("new_df_dict.pkl", "rb"))   
movies_with_ratings = pickle.load(open("movies_with_ratings.pkl", 'rb'))

# we are using similarity matrix here, so need to import that too
similarity = pickle.load(open("similarity.pkl", "rb"))

# need to create the data frame back from this dictionary values
movies_data = pd.DataFrame(movies_data)
new_df_with_ratings = pd.DataFrame(movies_with_ratings)


# function to fetch the movie poster based on movie id
def fetch_poster(movie_id):
    # need to send a get request to the tmdb api with that movie_id and api key
    api_key = 'ecece9a913137b29d9d5bedaaa32ec19'
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&&adult=true")
    response = response.json()

    if "poster_path" in response.keys() and response['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + response['poster_path']
    else:
        return None

# need a recommending function to get the names of the similar movies
def recommend(movie_name, number_of_suggestions):
    # have to find the index of that movie name from the movies data frame
    try:
        movie_index = movies_data[movies_data['title'].str.lower() == movie_name.lower()].index[0]
        
        distances = similarity[movie_index]
        
        # need to pick 5 movies out of it with slicing of [1:6] because 0th index is that movie 
        # itself as it will have the highest score of 1 with itself only
        movies_list_indices = distances[1 : number_of_suggestions+1]
        
        # getting movies out of these indices from the movies data
        # i am also going to store the address of the poster based on movie id
        output = []
        posters = []
        for match in movies_list_indices:
            output.append(movies_data.iloc[match[0]]['title'])

            poster = fetch_poster(movies_data.iloc[match[0]]['movie_id'])

            if poster is not None:
                posters.append(f'https://image.tmdb.org/t/p/w500/{poster}')
            else:
                posters.append('./cat_innocent.jpg')

        return (output,posters)
        
    except IndexError:
        print("Movie not found in the Database. Look for typo.")
        return 


st.title("Movie Recommendations are here. Yippy!! :)")

# have to create a select
selected_movie_name = st.selectbox(r"""Select a movie from the Available list of 5000 movies""",
                                    new_df_with_ratings['title']
                                    )
selected_number_of_choices = st.slider("Choose number of recommendations (more the recommendations, slower will be the loading time)", 
                                        min_value=1, max_value=50, value=5)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name, selected_number_of_choices)

    # st.write(recommendations)

    # for name in recommendations[0]:
    #     st.write('<h4>{}</h4>'.format(name), unsafe_allow_html=True)

    i=0
    LIMIT = 5

    while i<selected_number_of_choices:
        with st.container():
            cols = st.columns(LIMIT, gap='medium')

            while i < selected_number_of_choices:
                cols[i % LIMIT].write('''
                            <div style="width:10vw; height: 20vw;">
                                <img src="{}" style="width:100%"/>
                                <h6 style="text-align: center;">{}</h6>
                            </div>
                            '''.format(recommendations[1][i], recommendations[0][i]), unsafe_allow_html=True)
                # print(recommendations[1][i])

                i += 1

                if i % LIMIT == 5:
                    break 

