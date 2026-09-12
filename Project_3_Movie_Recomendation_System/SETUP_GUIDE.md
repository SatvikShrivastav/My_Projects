# Setup Guide

## Prerequisites

Install:

- Python 3
- Git
- Jupyter Notebook (or use Google Colab)

## Local Setup

### Step 1 — Create a project folder

```bash
mkdir Movie-Recommendation-System
cd Movie-Recommendation-System
```

### Step 2 — Copy project files

Place these files in the folder:

- `Movie_Recommendation_System(2).ipynb`
- `movies.csv`
- `README.md`

### Step 3 — Create and activate a virtual environment

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

### Step 4 — Install packages

```bash
pip install numpy pandas scikit-learn jupyter
```

### Step 5 — Fix the dataset path

The original notebook uses:

```python
pd.read_csv('/content/movies.csv')
```

For local execution, use:

```python
pd.read_csv('movies.csv')
```

### Step 6 — Start Jupyter

```bash
jupyter notebook
```

Open the notebook and run all cells in order.

### Step 7 — Test the recommender

Enter a movie title when the notebook asks for your favourite movie. The system will print similar movies.

## Google Colab Setup

1. Upload the notebook to Google Colab.
2. Upload the dataset and name it `movies.csv`.
3. Run the cells from top to bottom.
4. When prompted, enter a movie title.

## GitHub Upload

From the project folder:

```bash
git init
git add .
git commit -m "Initial commit - Movie Recommendation System"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

Before pushing, make sure large/unnecessary files such as `venv/`, `__pycache__/`, and `.ipynb_checkpoints/` are excluded.

Recommended `.gitignore`:

```text
venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
```

## Final Repository Checklist

- [ ] Notebook opens correctly
- [ ] `movies.csv` is present or documented as required
- [ ] Dataset path is correct
- [ ] Dependencies are documented
- [ ] README is present
- [ ] Documentation is present
- [ ] Setup guide is present
- [ ] Notebook runs from top to bottom
- [ ] GitHub repository has a clear description
