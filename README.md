# Movie Recommender System

A content-based movie recommender built with Streamlit. Pick a movie and get 5 similar titles with posters fetched from TMDB.

**Live app:** https://movie-recommender-rqh7b2yry5vau3knmhbutu.streamlit.app/
**Repo:** https://github.com/tejash5489-lang/movie-recommender

## How it works

Movies are represented as tag vectors (genres, cast, crew, keywords, overview) and compared with cosine similarity. Rather than shipping the full 4806x4806 similarity matrix, `similarity.pkl` stores only each movie's top-5 nearest neighbors, keeping the file under 1MB instead of ~184MB. See `main.ipynb` for how the vectors and similarity table are built from the TMDB 5000 dataset (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`).

## Running locally

```bash
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml` with your own [TMDB API key](https://www.themoviedb.org/settings/api):

```toml
TMDB_API_KEY = "your-tmdb-api-key"
```

Then run:

```bash
streamlit run app.py
```

## Deploying

Deployed on [Streamlit Community Cloud](https://share.streamlit.io): connect this repo, set the main file to `app.py`, and add `TMDB_API_KEY` under the app's Secrets settings.
