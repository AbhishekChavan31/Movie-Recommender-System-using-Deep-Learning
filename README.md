### This project is a Machine Learning Project and this is designed to give the user 
### recommendations of the movies from his first choice

<h6>
    Dataset were found from the website of TMDB. This is a website that stores the world 
    wide movies data with around 5000 movies during this project was created.
    Data cleaning was a huge task. Only some of the few columns were taken from the provided
    columns. Those columns were than filtered to get the required info only. Refer to my .ipynb file
    that I am also attaching with this repo.
    
    The movies are compared based on their story line, cast, director, genres etc. So that is what
    we are trying to do. We want to merge these columns and create the "tags" column that only
    contains some keywords that will help us in making similarity comparisons.

    Then we use the column Vectorizer to make a vectorized format of the words in the tags.
    With this vectors, I can now check its cosine similarity with every other vector. 
    cosine_similarity here is a good measure because it has large number of dimensions and 
    Euclidean distances will not provide correct similarity for the movies and Euclidean 
    distances is only appropriate for 2 dimensions only.

    When we have the similarity matrix, I can now use a index and find the similarities of 
    all the movies with the movie at that particular index. I can sort those similarity values
    to get them in decreasing order and take indices of first few to find the recommendations 
    from the movies dataset.

    To render this stuff on the browser, I am using streamlit.io because it is easy to use 
    and to build the frontend rather than coding the entire frontend from me.

    Displaying the movie poster requires to create account in tmdb and then goto API references.
    Then create our API key by providing some information. There is a specific URL to get the movie 
    data from the API by attaching the movie_id and your API key. That data contains the poster_path.
    To fetch the actual poster, there is another path to use
        movie_data = https://api.themoviedb.org/3/movie/{movie_id}?api_key={your_api_key}
        poster_path = https://image.tmdb.org/t/p/w500/{poster_path}

    You can also choose the number of recommendations you want using the slider.
</h6>

