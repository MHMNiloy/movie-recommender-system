# CineMatch - Movie Recommender UI Setup Guide

## 📋 Overview
This is a Streamlit-based web application that provides movie recommendations using content-based filtering. The UI is designed with a distinctive cinema-inspired aesthetic.

---

## 🛠️ Prerequisites

- Python 3.8 or higher
- PyCharm (Community or Professional edition)
- Git (optional)

---

## 📦 Installation & Setup

### Step 1: Clone/Download Project Files

1. Create a new folder for your project:
   ```bash
   mkdir movie_recommender
   cd movie_recommender
   ```

2. Move the following files into this directory:
   - `movie_recommender_app.py`
   - `requirements.txt`
   - `SETUP_GUIDE.md`

### Step 2: Download Dataset

The app requires TMDB movie data. Download from Kaggle:

1. Go to [Kaggle TMDB Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2. Download:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`
3. Place both CSV files in your project folder

### Step 3: Create Virtual Environment in PyCharm

**Method A: Using PyCharm GUI**

1. Open PyCharm
2. Click **File** → **Open** → Select your `movie_recommender` folder
3. Right-click on the project folder → **Mark Directory as** → **Sources Root**
4. Go to **PyCharm** → **Preferences** (Mac) or **File** → **Settings** (Windows/Linux)
5. Navigate to **Project: movie_recommender** → **Python Interpreter**
6. Click the gear icon ⚙️ → **Add**
7. Select **New Environment**
8. Choose **Venv** (Python 3.8+)
9. Click **Create**

**Method B: Using Terminal**

```bash
# Navigate to project folder
cd movie_recommender

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 4: Install Dependencies

In PyCharm Terminal (or your system terminal):

```bash
# Make sure your venv is activated
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

---

## 🚀 Running the Application

### Method 1: Using PyCharm Run Configuration

1. Open `movie_recommender_app.py` in PyCharm
2. Click **Run** → **Edit Configurations**
3. Click **+** → **Python**
4. Configure as follows:
   - **Name**: Streamlit App
   - **Script path**: `[path-to-project]/movie_recommender_app.py`
   - **Parameters**: `(leave blank)`
   - **Module name**: `streamlit`
   - **Parameters**: `run movie_recommender_app.py`
5. Click **OK**
6. Click the green **Run** button or press `Shift + F10` (Windows/Linux) or `Control + R` (Mac)

### Method 2: Using Terminal

In PyCharm's Terminal (or your system terminal):

```bash
streamlit run movie_recommender_app.py
```

### Method 3: Quick Script in PyCharm

Create a run script:
1. In PyCharm, create a new file: `run_app.py`
2. Add this code:
   ```python
   import subprocess
   import sys
   
   subprocess.run([sys.executable, "-m", "streamlit", "run", "movie_recommender_app.py"])
   ```
3. Right-click on `run_app.py` → **Run 'run_app.py'**

---

## 🌐 Accessing the App

Once running, Streamlit will display:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://[your-ip]:8501
```

Open your browser and navigate to `http://localhost:8501`

---

## 📱 UI Features

### **Header Section**
- Cinema-inspired red gradient background (#e50914)
- Clear value proposition
- Modern typography

### **Input Section**
- Searchable dropdown for movie selection
- Adjustable number of recommendations (1-10)
- Clean, dark-themed interface

### **Recommendation Display**
- Ranked list with similarity scores
- Hover effects for interactivity
- 100% match score indicates percentage similarity
- Export results as CSV

### **Sidebar Statistics**
- Total movies in database
- Feature count

### **Design Elements**
- Dark theme (Netflix-inspired)
- Red accent color (#e50914)
- Smooth transitions and hover effects
- Responsive layout
- Accessible typography

---

## 🔧 Customization

### Change Primary Color

In `movie_recommender_app.py`, modify the CSS:

```python
--primary: #e50914;      # Change this hex code
```

Common alternatives:
- Netflix Red: `#e50914`
- Amazon Prime: `#00A8E1`
- Hulu Green: `#1CE783`
- Disney Blue: `#113CCF`

### Adjust Number of Recommendations

In the sidebar:
```python
num_recs = st.number_input(
    "# Recommendations",
    min_value=1,
    max_value=20,  # Change max here
    value=5,
    step=1
)
```

### Change Font

Modify the font-family in CSS:
```css
font-family: 'Segoe UI', sans-serif;  # Change to your preference
```

---

## 🐛 Troubleshooting

### Error: "No module named 'streamlit'"
```bash
pip install streamlit
```

### Error: "CSV files not found"
- Ensure `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` are in the project folder
- Check file names match exactly (case-sensitive on Mac/Linux)

### Error: "Port 8501 is already in use"
```bash
streamlit run movie_recommender_app.py --server.port 8502
```

### Slow performance
- This is normal for first run (data loading & vectorization)
- Streamlit caches the data, so subsequent runs are instant
- The `@st.cache_resource` decorator handles this automatically

### Memory issues
- Reduce `max_features` in CountVectorizer (default: 5000)
- Modify in code: `CountVectorizer(max_features=2000, ...)`

---

## 📁 Project Structure

```
movie_recommender/
├── venv/                          # Virtual environment
├── movie_recommender_app.py       # Main application
├── requirements.txt               # Dependencies
├── SETUP_GUIDE.md                # This file
├── tmdb_5000_movies.csv          # Movie data (download)
└── tmdb_5000_credits.csv         # Credits data (download)
```

---

## 🎯 How It Works

1. **Data Loading**: Loads and merges movie + credits data
2. **Feature Extraction**: Combines genres, keywords, cast, crew, and overview
3. **Vectorization**: Converts text to numerical vectors using CountVectorizer
4. **Similarity Calculation**: Computes cosine similarity between movies
5. **Recommendation**: Returns top N similar movies based on input

**Recommendation Algorithm**: Content-Based Filtering using Cosine Similarity

---

## 📊 Performance Tips

- **First load**: ~10-30 seconds (data processing)
- **Subsequent selections**: <1 second (cached data)
- **Memory usage**: ~500MB - 1GB

To optimize:
1. Enable Streamlit's cache (already implemented)
2. Run on SSD for faster data loading
3. Close other applications to free RAM

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Click "Deploy"

### Deploy to Heroku

Create `Procfile`:
```
web: streamlit run movie_recommender_app.py --logger.level=error
```

Then deploy:
```bash
git push heroku main
```

---

## 📝 Development Notes

- Python version: 3.8+
- Streamlit version: 1.28.1+
- Total dependencies: 5 packages
- Approximate installation time: 2-5 minutes

---

## 🤝 Support

For Streamlit documentation: https://docs.streamlit.io

For dataset info: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Enjoy discovering movies with CineMatch! 🎬🍿**
