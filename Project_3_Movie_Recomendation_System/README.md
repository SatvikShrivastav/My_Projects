# Movie Recommendation System

A content-based **Movie Recommendation System** built with Python, Pandas and scikit-learn. The project recommends movies similar to a movie entered by the user by comparing movie metadata such as genres, keywords, tagline, cast, and director.

## Project Overview

The notebook follows these main steps:

1. Import the required Python libraries.
2. Load the movie dataset from CSV.
3. Select relevant movie features: `genres`, `keywords`, `tagline`, `cast`, and `director`.
4. Replace missing values in those features with empty strings.
5. Combine the selected features into one text field.
6. Convert the combined text into TF-IDF feature vectors.
7. Calculate cosine similarity between all movie vectors.
8. Accept a movie name from the user.
9. Find the closest matching title using `difflib`.
10. Sort movies by similarity score and display recommendations.

## Dataset

The supplied CSV contains **4,803 movies and 24 columns**. The recommendation logic uses these columns:

- `title`
- `genres`
- `keywords`
- `tagline`
- `cast`
- `director`
- `index`

The notebook expects the CSV to be available as `movies.csv`.

## Technologies Used

- Python 3
- NumPy
- Pandas
- scikit-learn
- difflib
- Jupyter Notebook / Google Colab

## How the Recommendation Works

The system uses a **content-based filtering** approach.

The selected text features are combined:

`genres + keywords + tagline + cast + director`

`TfidfVectorizer` converts this combined text into numerical feature vectors. **Cosine similarity** is then used to measure how similar movies are to each other.

When the user enters a movie title, `difflib.get_close_matches()` helps find a close title from the dataset. The system then retrieves the corresponding similarity scores, sorts them in descending order, and prints up to 29 recommended movie titles.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install numpy pandas scikit-learn jupyter
```

### 4. Add the dataset

Place the supplied dataset in the project folder and rename it to:

```text
movies.csv
```

The notebook currently loads:

```python
movies_data = pd.read_csv('/content/movies.csv')
```

For local Jupyter use, change it to:

```python
movies_data = pd.read_csv('movies.csv')
```

### 5. Run the notebook

```bash
jupyter notebook
```

Open:

```text
Movie_Recommendation_System(2).ipynb
```

Run the cells from top to bottom.

## Example Usage

When prompted:

```text
Enter your favourite movie name:
```

enter a movie title available in the dataset, for example:

```text
Avatar
```

The notebook then prints:

```text
Movies suggested for you:
1. ...
2. ...
3. ...
```

## Project Structure

```text
Movie-Recommendation-System/
├── Movie_Recommendation_System(2).ipynb
├── movies.csv
├── README.md
├── DOCUMENTATION.md
├── SETUP_GUIDE.md
└── Movie_Recommendation_System_Setup_Guide.pptx
```

## Notes

- The project is based on the supplied notebook and dataset.
- The current implementation is notebook/console based; it does not include a web interface.
- The similarity matrix is calculated for the complete dataset, so memory usage can increase with larger datasets.
- The notebook assumes that a close title is found by `difflib`; an invalid/unmatched input can cause an indexing error.

## Future Improvements

Possible extensions include:

- Add a Streamlit or Flask web interface.
- Add posters and movie descriptions.
- Improve title-search handling for unmatched inputs.
- Save precomputed vectors/similarity data for faster startup.
- Add filters such as genre, language, rating, or release year.
- Deploy the application online.

## License

Add the license you want to use for your GitHub repository (for example, MIT) before publishing.
