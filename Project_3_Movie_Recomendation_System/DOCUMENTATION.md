# Project Documentation

## 1. Introduction

The Movie Recommendation System recommends movies based on the similarity of their available metadata. It is implemented in a Jupyter Notebook using Python.

## 2. Input Data

The supplied dataset contains 4,803 movie records and 24 columns. The notebook uses five text-based features for recommendation:

- genres
- keywords
- tagline
- cast
- director

The movie `title` and `index` columns are used to identify and retrieve movies.

## 3. Data Pre-processing

Missing values in the five selected features are replaced with empty strings. The five fields are then concatenated into one combined text representation for every movie.

## 4. Feature Extraction

`TfidfVectorizer` from scikit-learn converts the combined text into TF-IDF feature vectors.

TF-IDF gives numerical importance to words in the combined movie metadata and creates a representation that can be compared mathematically.

## 5. Similarity Calculation

The notebook applies `cosine_similarity()` to the TF-IDF vectors. This produces a similarity matrix showing how closely each movie matches every other movie.

## 6. User Input and Matching

The user enters a favourite movie title. The notebook creates a list of all titles and uses `difflib.get_close_matches()` to find the closest title in the dataset.

## 7. Recommendation Generation

After identifying the selected movie's index, the system:

1. Gets its similarity scores.
2. Enumerates the movie indexes and scores.
3. Sorts them from highest to lowest similarity.
4. Looks up the corresponding movie titles.
5. Prints the recommendations, up to 29 results.

## 8. Main Libraries

| Library | Purpose |
|---|---|
| NumPy | Numerical computing dependency |
| Pandas | Loading and manipulating the dataset |
| difflib | Finding close movie-title matches |
| TfidfVectorizer | Converting text into TF-IDF vectors |
| cosine_similarity | Measuring similarity between movie vectors |

## 9. Limitations

The current notebook is a basic content-based recommender. It does not use user ratings or collaborative filtering. It also expects the input title to have a close match in the dataset.

The current notebook uses a Google Colab-style path (`/content/movies.csv`), so the dataset path should be changed when running locally.

## 10. Expected Output

The system displays a numbered list beginning with:

`Movies suggested for you:`

and then prints movie titles ordered by their similarity score.
