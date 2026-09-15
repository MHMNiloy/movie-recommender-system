import streamlit as st
import pandas as pd
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background: #0b0b0f;
        color: white;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #a1a1aa;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .movie-card {
        background: #15151c;
        padding: 18px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 1px solid #252530;
        height: 100%;
    }

    .movie-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 10px;
    }

    .section-title {
        font-size: 1.7rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD + PREPARE DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")

    movies = movies.merge(credits, on="title")

    movies = movies[
        [
            "movie_id",
            "title",
            "overview",
            "genres",
            "keywords",
            "cast",
            "crew"
        ]
    ]

    movies.dropna(inplace=True)

    def convert(obj):
        return [i["name"] for i in literal_eval(obj)]

    def convert3(obj):
        return [i["name"] for i in literal_eval(obj)[:3]]

    def fetch_director(obj):
        return [
            i["name"]
            for i in literal_eval(obj)
            if i["job"] == "Director"
        ]

    movies["genres"] = movies["genres"].apply(convert)
    movies["keywords"] = movies["keywords"].apply(convert)
    movies["cast"] = movies["cast"].apply(convert3)
    movies["crew"] = movies["crew"].apply(fetch_director)

    movies["overview"] = movies["overview"].apply(lambda x: x.split())

    movies["genres"] = movies["genres"].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

    movies["keywords"] = movies["keywords"].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

    movies["cast"] = movies["cast"].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

    movies["crew"] = movies["crew"].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

    movies["tags"] = (
        movies["overview"]
        + movies["genres"]
        + movies["keywords"]
        + movies["cast"]
        + movies["crew"]
    )

    new_df = movies[["movie_id", "title", "tags"]].copy()

    new_df["tags"] = new_df["tags"].apply(
        lambda x: " ".join(x).lower()
    )

    # Same stemming approach as your notebook
    ps = PorterStemmer()

    def stem(text):
        return " ".join(ps.stem(i) for i in text.split())

    new_df["tags"] = new_df["tags"].apply(stem)

    # Same CountVectorizer settings as your notebook
    cv = CountVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = cv.fit_transform(new_df["tags"]).toarray()

    similarity = cosine_similarity(vectors)

    return movies, new_df, similarity


movies, new_df, similarity = load_data()


# --------------------------------------------------
# RECOMMENDATION FUNCTION
# --------------------------------------------------

def recommend(movie):

    movie_index = new_df[
        new_df["title"] == movie
    ].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:

        movie_index = i[0]

        recommendations.append({
            "title": new_df.iloc[movie_index].title,
            "score": round(float(i[1]) * 100, 1)
        })

    return recommendations


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎬 Movie Recommender</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to your favorites using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# MOVIE SELECTOR
# --------------------------------------------------

movie_titles = sorted(new_df["title"].unique())

selected_movie = st.selectbox(
    "🎥 Choose a movie",
    movie_titles,
    index=movie_titles.index("Batman")
    if "Batman" in movie_titles else 0
)


if st.button("🚀 Recommend Movies", type="primary"):

    recommendations = recommend(selected_movie)

    st.markdown(
        f'<div class="section-title">'
        f'Because you liked "{selected_movie}"'
        f'</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">
                        {movie["title"]}
                    </div>
                    <p style="color:#a1a1aa;">
                        Similarity: {movie["score"]}%
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🎬 Movie Recommender")

    st.markdown("---")

    st.markdown("### 🤖 Model")

    st.write("Content-Based Filtering")

    st.markdown("### 🧠 Algorithm")

    st.write("CountVectorizer + Cosine Similarity")

    st.markdown("### 📊 Dataset")

    st.write(f"{len(new_df):,} movies")

    st.markdown("---")

    st.caption(
        "Built with Python, Pandas, Scikit-learn & Streamlit"
    )
