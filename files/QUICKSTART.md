# 🚀 CineMatch - Quick Start (5 Minutes)

## ⚡ TL;DR - Get Running in 5 Minutes

### 1. **Prepare Files**
```
movie_recommender/
├── movie_recommender_app.py     (provided)
├── requirements.txt              (provided)
├── tmdb_5000_movies.csv         (download from Kaggle)
└── tmdb_5000_credits.csv        (download from Kaggle)
```

### 2. **Open Project in PyCharm**
- File → Open → Select `movie_recommender` folder
- Wait for PyCharm to index files

### 3. **Create Virtual Environment**
- Settings → Project → Python Interpreter → ⚙️ → Add
- Select "New Environment" → "Venv" → Create

### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5. **Run App**
```bash
streamlit run movie_recommender_app.py
```

**That's it! 🎉 Open http://localhost:8501**

---

## 📊 UI Overview

```
┌─────────────────────────────────────────────┐
│         🎬 CineMatch - Header               │  ← Cinema-inspired red gradient
│    "Discover movies you'll love based..."   │
├─────────────────────────────────────────────┤
│  📊 Sidebar: Database Stats                 │  ← Quick metrics
├─────────────────────────────────────────────┤
│  🎥 Pick a movie you love: [Dropdown]       │  ← Search input
│  # Recommendations: [5]                     │  ← Adjustable count
├─────────────────────────────────────────────┤
│  🍿 Recommended for You                     │
│                                             │
│  #1 Movie Title A ────────── 92% match ✓   │  ← Ranked results
│  #2 Movie Title B ────────── 89% match ✓   │  ← With similarity scores
│  #3 Movie Title C ────────── 87% match ✓   │  ← Hover effects
│  ...                                        │
├─────────────────────────────────────────────┤
│  [📥 Export Results] [Download CSV]         │  ← Export option
└─────────────────────────────────────────────┘
```

---

## 🎨 Design Highlights

| Aspect | Choice | Why |
|--------|--------|-----|
| **Primary Color** | Netflix Red (#e50914) | Matches subject matter (cinema) |
| **Background** | Dark Theme (#141414) | Reduces eye strain, modern aesthetic |
| **Typography** | Segoe UI / System Sans | Clean, legible, no decoration |
| **Layout** | Left-aligned, spacious | Information hierarchy, scannable |
| **Animations** | Subtle hover effects | Responsive without distraction |
| **Cards** | Left red border accent | Distinctive, not templated |

---

## 🛠️ What's Inside

### **movie_recommender_app.py**
- 350+ lines of production-ready code
- Streamlit UI with custom CSS styling
- Data processing pipeline
- Caching for performance
- Export functionality

### **Key Features**
✓ Fast recommendations (cached data)
✓ Searchable movie dropdown
✓ Adjustable number of results
✓ Similarity score display
✓ Export to CSV
✓ Mobile responsive
✓ Dark theme optimized
✓ Netflix-inspired design

---

## 📥 Download Kaggle Dataset

1. Go to: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
2. Click "Download" (requires Kaggle account)
3. Extract the zip file
4. Copy these two CSV files to your project folder:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

**Files needed:**
- `tmdb_5000_movies.csv` (4.8 MB, ~5000 movies)
- `tmdb_5000_credits.csv` (2.6 MB, cast & crew data)

---

## 💻 System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|------------|
| Python | 3.8 | 3.10+ |
| RAM | 2 GB | 4+ GB |
| Storage | 500 MB | 1+ GB |
| OS | Any | macOS/Linux |

---

## 🔍 First Run Walkthrough

1. **App Starts** → Loads data (10-30 sec first time)
2. **Select a Movie** → Type or click dropdown (e.g., "Avatar")
3. **Set Count** → Adjust if you want more/fewer (default: 5)
4. **View Results** → See ranked recommendations with scores
5. **Export** → Download CSV if needed
6. **Try Another** → Select new movie (instant, cached)

---

## ⚙️ PyCharm Configuration (Simple Method)

### In PyCharm Terminal:
```bash
# Make sure you're in project folder
cd movie_recommender

# Activate virtual environment (if not auto-activated)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run movie_recommender_app.py
```

### That's it! Open the local URL shown in terminal.

---

## 🎯 Customization Ideas

Want to modify the app? Here are some ideas:

### Change the color theme
```python
# Line 24 in movie_recommender_app.py
--primary: #e50914;  # Change to #00A8E1 (Amazon), #1CE783 (Hulu), etc.
```

### Show more/fewer recommendations
```python
# Line 195
max_value=20  # Was 10, now shows up to 20
```

### Add movie posters
```python
# Would require OMDB API or adding poster URLs to CSV
# Advanced modification
```

### Change similarity threshold
```python
# Filter out low-similarity recommendations
if score > 0.5:  # Only show >50% match
    recommendations.append(...)
```

---

## 🐛 If Something Goes Wrong

| Error | Fix |
|-------|-----|
| `No module named 'streamlit'` | Run: `pip install streamlit` |
| `CSV files not found` | Download from Kaggle, place in project folder |
| `Port 8501 already in use` | Run: `streamlit run movie_recommender_app.py --server.port 8502` |
| `Slow performance` | First run is slow (caching). Try again. |
| `CSV encoding error` | Already handled in code, shouldn't occur |

---

## 📚 Learn More

- **Streamlit Docs**: https://docs.streamlit.io
- **Dataset Info**: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- **Cosine Similarity**: https://en.wikipedia.org/wiki/Cosine_similarity
- **Content-Based Filtering**: https://en.wikipedia.org/wiki/Recommender_system

---

## 🚀 Next Steps

1. ✅ Download files
2. ✅ Get CSV data from Kaggle
3. ✅ Set up Python environment
4. ✅ Run the app
5. 🎬 Try it out!
6. 🎨 Customize colors/features
7. 📱 Deploy to Streamlit Cloud (optional)

---

**Questions? See SETUP_GUIDE.md for detailed instructions.**

**Ready? Let's go! 🎬🍿**
