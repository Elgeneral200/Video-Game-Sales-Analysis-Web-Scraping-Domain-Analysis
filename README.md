# Data Science Course Project
## Video Game Sales Analysis & Web Scraping Domain Analysis

---

## Project Overview

This is a complete **end-to-end Data Science project** that contains two main tasks:

- **Task 1**: Dataset Analysis & Visualization — We analyze a real-world video game sales dataset to discover trends and insights about the gaming industry.
- **Task 2**: Web Scraping & Domain Analysis — We scrape book data from a real website and analyze book pricing, ratings, and categories.

Both tasks include **Jupyter Notebooks** for detailed analysis and **Streamlit Dashboards** for interactive visualization.

---

## Project Structure

```
data-science-project/
│
└── datascience/
├── task1_dataset_analysis_visualization.ipynb   # Task 1 Jupyter Notebook
├── task2_web_scraping_domain_analysis.ipynb     # Task 2 Jupyter Notebook
├── task1_dashboard.py                           # Task 1 Streamlit Dashboard
├── task2_dashboard.py                           # Task 2 Streamlit Dashboard
├── README.md                                    # Project Documentation
├── requirements.txt                             # Python Dependencies
├── .gitignore                                   # Git Ignore Rules
│
└── frontend/
└── src/                                         # Project Documentation Website
    ├── App.tsx
    ├── main.tsx
    └── index.css
```

---

## Task 1 — Dataset Analysis & Visualization

### Selected Dataset
- **Name**: Video Game Sales Dataset
- **Source**: [Kaggle - Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogame-sales) and [GitHub Mirror](https://raw.githubusercontent.com/amankharwal/Website-data/master/vgsales.csv)
- **Size**: ~16,500 rows × 11 columns
- **Description**: Contains information about video game sales across different regions including North America, Europe, Japan, and other areas.

### Dataset Columns
| Column | Description |
|--------|-------------|
| Rank | Ranking of overall sales |
| Name | Name of the game |
| Platform | Platform of the game release (Wii, PS4, X360, etc.) |
| Year | Year the game was released |
| Genre | Genre of the game |
| Publisher | Publisher of the game |
| NA_Sales | Sales in North America (in millions) |
| EU_Sales | Sales in Europe (in millions) |
| JP_Sales | Sales in Japan (in millions) |
| Other_Sales | Sales in the rest of the world (in millions) |
| Global_Sales | Total worldwide sales (in millions) |

### Data Quality Issues Found
1. **Missing Values**: Year column has ~271 missing values, Publisher column has ~58 missing values
2. **Duplicates**: Some games appear multiple times across different platforms
3. **Inconsistent Data**: Some year values are float instead of integer
4. **Outliers**: Some games have extremely high sales compared to the majority
5. **Data Types**: Year needs conversion from float to integer

### Preprocessing Steps
1. Loaded raw dataset and inspected structure
2. Identified and documented all quality issues
3. Handled missing values (dropped rows with missing Year/Publisher)
4. Removed exact duplicate rows
5. Converted Year from float to integer
6. Standardized text formatting for Genre and Platform columns
7. Treated outliers using IQR method
8. Created new features (Decade, Sales_Category, Total_Regional_Sales)
9. Renamed columns for clarity
10. Saved cleaned dataset

### 15 Analysis Questions

| # | Question |
|---|----------|
| 1 | What is the overall distribution of global video game sales? |
| 2 | Which game genre has the most titles in the dataset? |
| 3 | What are the top 10 best-selling video games of all time? |
| 4 | How have global video game sales changed over the years? |
| 5 | Which gaming platform has the highest total global sales? |
| 6 | What is the market share of each sales region? |
| 7 | Which publishers have released the most game titles? |
| 8 | How do average sales differ across game genres? |
| 9 | How do sales trends differ across regions over time? |
| 10 | Which are the top 5 game genres for each major platform? |
| 11 | Is there a trend in the number of new games released per year? |
| 12 | Which year had the highest total global sales and why? |
| 13 | What is the average global sales per game by genre? |
| 14 | How has platform popularity changed over the decades? |
| 15 | Which publishers dominate sales in each global region? |

### Key Insights
- **Action** is the most common genre, but **Platform** and **Shooter** games tend to have higher average sales
- **Nintendo** dominates the top-selling games list with titles like Wii Sports
- The gaming industry peaked in **2008-2009** with the highest number of releases and total sales
- **PS2** has the highest total global sales of any platform
- **North America** is the largest market, contributing roughly 45-50% of global sales
- There has been a decline in game releases after 2011, possibly due to market consolidation

---

## Task 2 — Web Scraping & Domain Analysis

### Selected Domain
- **Domain**: Books & Publishing
- **Target Website**: [Books to Scrape](http://books.toscrape.com)
- **Why This Domain**: The books domain provides rich data about pricing, categories, and ratings that is easy to understand and analyze.

### Scraping Details
- **Total Pages Scraped**: 50 pages (20 books per page)
- **Total Books Scraped**: 1,000 books
- **Data Fields**: Title, Price, Rating (1-5 stars), Category, Availability, Book URL
- **Library Used**: requests + BeautifulSoup + lxml

### Scraping Workflow
1. Started from the main catalog page
2. Identified the URL pattern for pagination: `catalogue/page-{n}.html`
3. Looped through all 50 pages
4. Extracted book data from each page using CSS selectors
5. Converted text ratings (One, Two, etc.) to numeric (1-5)
6. Cleaned price strings by removing the £ symbol
7. Built a structured DataFrame from collected data
8. Saved to CSV for reuse

### 5 Analysis Questions

| # | Question |
|---|----------|
| 1 | What is the distribution of book prices across the catalog? |
| 2 | Which book categories have the most titles? |
| 3 | Is there a relationship between book price and rating? |
| 4 | Which categories have the highest and lowest average prices? |
| 5 | What is the distribution of book ratings across all books? |

### Key Insights
- Book prices range from **£10** to **£60** with most books priced between **£15-35**
- **Default** category has the most books (since some books are not categorized)
- There is **no strong correlation** between price and rating — expensive books are not always better rated
- **Suspense** and **Historical Fiction** categories tend to have higher average prices
- The **majority of books** have a 4 or 5 star rating, suggesting rating inflation or selection bias

---

## Libraries Used

### Data Science & Analysis
- `pandas` — Data manipulation and analysis
- `numpy` — Numerical computing
- `scikit-learn` — Machine learning utilities

### Visualization
- `matplotlib` — Static plots and charts
- `seaborn` — Statistical data visualization
- `plotly` — Interactive charts and graphs
- `missingno` — Missing value visualization

### Web Scraping
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `lxml` — XML/HTML processing
- `selenium` — Browser automation (if needed)

### Dashboard
- `streamlit` — Interactive web dashboards

### Notebook
- `jupyter` — Interactive computing
- `notebook` — Jupyter notebook interface
- `nbformat` — Notebook file format

### Utilities
- `tqdm` — Progress bars
- `openpyxl` — Excel file support

---

## Environment Setup

### Step 1: Create a Virtual Environment

Open your terminal in Visual Studio Code:

```bash
# Navigate to your project folder
cd data-science-project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
# Check that Jupyter is installed
jupyter --version

# Check that Streamlit is installed
streamlit --version
```

---

## Run Instructions

### Running the Jupyter Notebooks

```bash
# Start Jupyter Notebook
jupyter notebook

# Then open:
# - task1_dataset_analysis_visualization.ipynb
# - task2_web_scraping_domain_analysis.ipynb
```

Or use VS Code's Jupyter extension:
1. Install the **Jupyter** extension in VS Code
2. Open any `.ipynb` file
3. Select the Python kernel from your virtual environment
4. Run cells one by one

### Running the Streamlit Dashboards

```bash
# Run Task 1 Dashboard
streamlit run task1_dashboard.py

# Run Task 2 Dashboard
streamlit run task2_dashboard.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

---

## Notes

- Both notebooks include **synthetic data fallback** — if the dataset URL is unavailable, the notebooks will generate realistic synthetic data so you can still run all cells.
- The web scraping notebook requires an **internet connection** to access books.toscrape.com.
- All visualizations use **plotly** for interactivity when possible, with **matplotlib/seaborn** as backup.
- The Streamlit dashboards are **standalone** and generate their own data.

---

## References

1. Kaggle Video Game Sales Dataset: https://www.kaggle.com/datasets/gregorut/videogame-sales
2. Books to Scrape: http://books.toscrape.com
3. Pandas Documentation: https://pandas.pydata.org/docs/
4. Plotly Documentation: https://plotly.com/python/
5. Streamlit Documentation: https://docs.streamlit.io/
6. BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
7. Matplotlib Documentation: https://matplotlib.org/
8. Seaborn Documentation: https://seaborn.pydata.org/

---

## Author

**Data Science Course Project** — Built with Python, Jupyter, and Streamlit.

---

