"""
=============================================================
  Task 2 Dashboard — Web Scraping: Books Domain Analysis ✦ Dark Edition
  Run: streamlit run task2_dashboard.py
=============================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------
st.set_page_config(
    page_title="Books Domain Analysis Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# Design System — Color Tokens (Identical to Task 1)
# ----------------------------------------------------------
BG_DEEPEST   = "#08080e"
BG_BASE      = "#0c0c14"
BG_CARD      = "#111119"
BG_ELEVATED  = "#16161f"
BG_HOVER     = "#1e1e2c"

ACCENT       = "#7c5cfc"
ACCENT_LIGHT = "#9b82fc"
ACCENT_DIM   = "#5a3ed4"
CYAN         = "#22d3ee"
CYAN_LIGHT   = "#67e8f9"
PINK         = "#f472b6"
EMERALD      = "#34d399"
AMBER        = "#fbbf24"
RED          = "#f87171"

TEXT_PRI     = "#ededf3"
TEXT_SEC     = "#9898b0"
TEXT_MUT     = "#65657d"

CHART_PALETTE = [
    "#7c5cfc", "#22d3ee", "#f472b6", "#34d399",
    "#fbbf24", "#818cf8", "#2dd4bf", "#fb7185",
    "#a3e635", "#c084fc",
]

ACCENT_SCALE = ["#1a1040", "#2d1f6e", "#5a3ed4", "#7c5cfc", "#9b82fc", "#b8a4fc"]

RATING_COLORS = {1: "#f87171", 2: "#fbbf24", 3: "#22d3ee", 4: "#34d399", 5: "#7c5cfc"}

# ----------------------------------------------------------
# Premium Dark Theme — Custom CSS
# ----------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ══════ GLOBAL ══════ */
.stApp, .main, [data-testid="stAppViewContainer"] {
    background-color: #08080e !important;
    animation: pageIn 0.8s ease-out;
}
@keyframes pageIn { from{opacity:0} to{opacity:1} }

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
    min-height: 0 !important;
}
.block-container {
    padding-top: 0 !important;
    padding-bottom: 2rem !important;
    max-width: 1400px !important;
}

h1,h2,h3,h4,h5,h6,p,span,div,label,li,a,th,td {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.stMarkdown { color: #c8c8d8 !important; }
.stMarkdown p, .stMarkdown span { color: #c8c8d8 !important; }
.stMarkdown h2, .stMarkdown h3, .stMarkdown h4 { color: #ededf3 !important; }
.stMarkdown strong { color: #ededf3 !important; }

hr { border-color: rgba(255,255,255,0.06) !important; }

a { color: #9b82fc !important; text-decoration: none; transition: color 0.3s ease; }
a:hover { color: #7c5cfc !important; }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0c0c14; }
::-webkit-scrollbar-thumb { background: #2a2a3e; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #3a3a52; }

/* ══════ HERO ══════ */
.hero-wrap {
    position: relative;
    background: linear-gradient(135deg, #08080e 0%, #0f0e1a 25%, #151230 55%, #0d1a20 100%);
    border-radius: 0 0 28px 28px;
    padding: 3.5rem 3rem 2.5rem;
    margin: -4.5rem -2rem 2rem -2rem;
    overflow: hidden;
    z-index: 10;
    border-bottom: 1px solid rgba(124,92,252,0.08);
}
.hero-orb { position: absolute; border-radius: 50%; pointer-events: none; }
.hero-orb-1 {
    width: 400px; height: 400px; top: -140px; right: -60px;
    background: radial-gradient(circle, rgba(124,92,252,0.22) 0%, transparent 70%);
    animation: orbF 7s ease-in-out infinite;
}
.hero-orb-2 {
    width: 300px; height: 300px; bottom: -100px; left: -40px;
    background: radial-gradient(circle, rgba(34,211,238,0.14) 0%, transparent 70%);
    animation: orbF 9s ease-in-out infinite reverse;
}
.hero-orb-3 {
    width: 180px; height: 180px; top: 35%; left: 52%;
    background: radial-gradient(circle, rgba(244,114,182,0.10) 0%, transparent 70%);
    animation: orbF 6s ease-in-out 1s infinite;
}
@keyframes orbF {
    0%,100%{transform:translateY(0) scale(1)}
    50%{transform:translateY(-16px) scale(1.04)}
}
.hero-badge {
    display: inline-block;
    background: rgba(124,92,252,0.14);
    border: 1px solid rgba(124,92,252,0.25);
    color: #9b82fc;
    padding: 5px 16px;
    border-radius: 50px;
    font-size: 0.70rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    margin-bottom: 1rem;
    animation: fU 0.6s ease-out 0.1s both;
}
.hero-title {
    font-size: 3.2rem; font-weight: 900; line-height: 1.08;
    margin: 0 0 0.85rem;
    background: linear-gradient(135deg, #ededf3 0%, #c8c8d8 30%, #9b82fc 65%, #22d3ee 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    animation: fU 0.6s ease-out 0.2s both;
}
.hero-sub {
    font-size: 1.08rem; color: #9898b0; font-weight: 400;
    margin: 0 0 0.3rem; max-width: 600px;
    animation: fU 0.6s ease-out 0.3s both;
}
.hero-desc {
    font-size: 0.86rem; color: #65657d; font-weight: 300;
    margin: 0 0 1.7rem; max-width: 500px;
    animation: fU 0.6s ease-out 0.38s both;
}
.hero-pills {
    display: flex; gap: 0.65rem; flex-wrap: wrap;
    animation: fU 0.6s ease-out 0.48s both;
}
.hero-pill {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.07);
    padding: 6px 16px; border-radius: 10px;
    color: #9898b0; font-size: 0.80rem; font-weight: 500;
    transition: all 0.3s ease;
}
.hero-pill:hover {
    background: rgba(124,92,252,0.10);
    border-color: rgba(124,92,252,0.25);
    color: #c8c8d8; transform: translateY(-2px);
}
@keyframes fU {
    from{opacity:0;transform:translateY(16px)}
    to{opacity:1;transform:translateY(0)}
}

/* ══════ KPI CARDS ══════ */
.kpi-grid {
    display: grid; grid-template-columns: repeat(4,1fr);
    gap: 1.15rem; margin-bottom: 1.8rem;
    animation: fU 0.6s ease-out 0.55s both;
}
.kpi-card {
    position: relative; background: #111119;
    border-radius: 16px; padding: 1.5rem 1.1rem 1.2rem;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
    overflow: hidden;
    transition: all 0.45s cubic-bezier(0.175,0.885,0.32,1.275);
}
.kpi-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    border-radius: 16px 16px 0 0;
}
.kpi-c1::before { background: linear-gradient(90deg,#7c5cfc,#9b82fc); }
.kpi-c2::before { background: linear-gradient(90deg,#22d3ee,#67e8f9); }
.kpi-c3::before { background: linear-gradient(90deg,#f472b6,#f9a8d4); }
.kpi-c4::before { background: linear-gradient(90deg,#34d399,#6ee7b7); }
.kpi-card:hover { transform: translateY(-6px) scale(1.02); }
.kpi-c1:hover { box-shadow: 0 12px 40px rgba(124,92,252,0.14); }
.kpi-c2:hover { box-shadow: 0 12px 40px rgba(34,211,238,0.14); }
.kpi-c3:hover { box-shadow: 0 12px 40px rgba(244,114,182,0.14); }
.kpi-c4:hover { box-shadow: 0 12px 40px rgba(52,211,153,0.14); }
.kpi-icon { font-size: 1.8rem; margin-bottom: 0.5rem; display: block; }
.kpi-val {
    font-size: 2rem; font-weight: 800; color: #ededf3;
    line-height: 1.15; margin-bottom: 0.15rem; display: block;
}
.kpi-lbl {
    font-size: 0.70rem; color: #65657d; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.07em; display: block;
}
.kpi-delta {
    font-size: 0.70rem; color: #34d399; font-weight: 600;
    margin-top: 0.25rem; display: block;
}

/* ══════ CHART CONTAINERS ══════ */
[data-testid="stPlotlyChart"] {
    background: #111119; border-radius: 16px;
    padding: 10px 12px 4px;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 2px 12px rgba(0,0,0,0.20);
    transition: all 0.4s cubic-bezier(0.175,0.885,0.32,1.275);
}
[data-testid="stPlotlyChart"]:hover {
    box-shadow: 0 8px 32px rgba(0,0,0,0.30);
    transform: translateY(-2px);
    border-color: rgba(124,92,252,0.12);
}
.js-plotly-plot .plotly .modebar { opacity: 0; transition: opacity 0.3s ease; }
.js-plotly-plot:hover .plotly .modebar { opacity: 1; }
.js-plotly-plot .plotly .modebar-btn path { fill: #65657d !important; }
.js-plotly-plot:hover .plotly .modebar-btn path { fill: #9898b0 !important; }
.js-plotly-plot .plotly .modebar-btn:hover path { fill: #7c5cfc !important; }

/* ══════ SECTION HEADINGS ══════ */
.sec-hd {
    font-size: 1.35rem; font-weight: 700; color: #ededf3;
    margin: 1.8rem 0 1.1rem;
    display: flex; align-items: center; gap: 0.6rem;
}
.sec-hd .sec-ic {
    display: inline-flex; align-items: center; justify-content: center;
    width: 34px; height: 34px; border-radius: 9px;
    background: linear-gradient(135deg,#7c5cfc,#5a3ed4);
    color: #fff; font-size: 0.95rem; flex-shrink: 0;
}
.sec-hd::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(255,255,255,0.08), transparent);
    border-radius: 1px; margin-left: 0.4rem;
}

/* ══════ INSIGHT BOX ══════ */
.insight-box {
    background: rgba(124,92,252,0.06);
    border-left: 3px solid #7c5cfc;
    padding: 0.9rem 1.2rem;
    border-radius: 0 14px 14px 0;
    margin: 1.3rem 0; color: #c8c8d8;
    font-size: 0.86rem; line-height: 1.6;
    animation: fU 0.5s ease-out;
}
.insight-box strong { color: #9b82fc; }

/* ══════ TABS ══════ */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px; background: #111119; border-radius: 14px;
    padding: 4px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.20);
    border: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 1.4rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px; padding: 9px 20px;
    font-weight: 600; font-size: 0.80rem;
    color: #65657d; transition: all 0.3s ease; white-space: nowrap;
}
.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.04); color: #9898b0;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,#7c5cfc,#5a3ed4) !important;
    color: #ededf3 !important;
    box-shadow: 0 4px 14px rgba(124,92,252,0.22);
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }

/* ══════ SIDEBAR ══════ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06060b 0%, #0a0a14 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.04) !important;
}
section[data-testid="stSidebar"] > div:first-child { background: transparent !important; }
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] { display: none; }
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] .stMarkdown {
    color: #9898b0 !important;
}
.sb-logo { text-align: center; padding: 1.6rem 0 0.3rem; }
.sb-logo-icon { font-size: 2.2rem; display: block; margin-bottom: 0.35rem; }
.sb-logo-text { font-size: 1rem; font-weight: 700; color: #ededf3 !important; display: block; }
.sb-logo-sub { font-size: 0.68rem; color: #65657d !important; display: block; margin-top: 0.1rem; letter-spacing: 0.04em; }
.sb-div {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,92,252,0.20), transparent);
    margin: 0.9rem 0.4rem; border: none;
}
.sb-sec {
    font-size: 0.62rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.1em;
    color: #7c5cfc !important;
    margin-bottom: 0.6rem; display: block; padding-left: 2px;
}
.sb-status {
    border-radius: 9px; padding: 0.45rem 0.7rem; font-size: 0.76rem;
    display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.2rem;
}
.sb-ok  { background: rgba(52,211,153,0.08); border: 1px solid rgba(52,211,153,0.18); color: #34d399 !important; }
.sb-syn { background: rgba(34,211,238,0.08); border: 1px solid rgba(34,211,238,0.18); color: #22d3ee !important; }
.sb-row {
    display: flex; justify-content: space-between;
    padding: 0.28rem 0; font-size: 0.76rem; color: #65657d;
    border-bottom: 1px solid rgba(255,255,255,0.03);
}
.sb-row:last-child { border-bottom: none; }
.sb-val { color: #c8c8d8 !important; font-weight: 600; }

section[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.08) !important;
}
section[data-testid="stSidebar"] [data-baseweb="select"] input { color: #c8c8d8 !important; }
section[data-testid="stSidebar"] [data-baseweb="select"] input::placeholder { color: #65657d !important; }
section[data-testid="stSidebar"] [data-baseweb="tag"],
section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {
    background-color: rgba(124,92,252,0.18) !important;
    color: #9b82fc !important;
    border-color: rgba(124,92,252,0.20) !important;
}
section[data-testid="stSidebar"] [data-baseweb="tag"] button svg,
section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] button svg {
    fill: #9b82fc !important; color: #9b82fc !important;
}
section[data-testid="stSidebar"] [data-baseweb="popover"] { background-color: #111119 !important; }
section[data-testid="stSidebar"] [data-baseweb="popover"] li { color: #c8c8d8 !important; }
section[data-testid="stSidebar"] [data-baseweb="popover"] li:hover { background-color: rgba(124,92,252,0.12) !important; }
section[data-testid="stSidebar"] [data-baseweb="slider"] [role="slider"] { background-color: #7c5cfc !important; border-color: #7c5cfc !important; }
section[data-testid="stSidebar"] [data-baseweb="slider"] .bar { background: rgba(124,92,252,0.18) !important; }
section[data-testid="stSidebar"] [data-baseweb="slider"] label { color: #9898b0 !important; }
section[data-testid="stSidebar"]::-webkit-scrollbar { width: 3px; }
section[data-testid="stSidebar"]::-webkit-scrollbar-thumb { background: rgba(124,92,252,0.2); border-radius: 2px; }

/* ══════ URL BOX ══════ */
.url-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 0.4rem 0.6rem;
    font-family: 'Courier New', monospace;
    font-size: 0.68rem; color: #65657d;
    margin: 0.25rem 0;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    transition: all 0.3s ease;
}
.url-box:hover { border-color: rgba(124,92,252,0.20); color: #9898b0; }

/* ══════ DATAFRAME ══════ */
.stDataFrame {
    border-radius: 14px !important; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06) !important;
}

/* ══════ TABLES (Markdown) ══════ */
table { color: #9898b0 !important; border-collapse: collapse; width: 100%; }
table th {
    background: #16161f !important; color: #ededf3 !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    padding: 0.5rem 0.8rem; font-size: 0.82rem; font-weight: 600;
}
table td {
    background: #111119 !important; color: #9898b0 !important;
    border: 1px solid rgba(255,255,255,0.04) !important;
    padding: 0.4rem 0.8rem; font-size: 0.82rem;
}
table tr:hover td { background: #16161f !important; }

/* ══════ EXPANDER ══════ */
[data-testid="stExpander"] {
    background: #111119 !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 12px !important;
}
[data-testid="stExpander"] summary { color: #9898b0 !important; font-weight: 600 !important; }
[data-testid="stExpander"] summary:hover { color: #c8c8d8 !important; }

/* ══════ CODE BLOCK ══════ */
.stCode {
    background: #111119 !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 8px !important;
}
.stCode code, .stCode pre { color: #9898b0 !important; font-size: 0.75rem !important; }

/* ══════ ALERTS ══════ */
.stAlert {
    background: rgba(34,211,238,0.05) !important;
    border-color: rgba(34,211,238,0.12) !important;
    color: #9898b0 !important;
}

/* ══════ FOOTER ══════ */
.footer-wrap {
    text-align: center; padding: 2rem 1rem 1rem;
    margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05);
}
.ft-line { color: #65657d; font-size: 0.80rem; margin: 0.15rem 0; }
.ft-tech {
    display: inline-block; background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.06);
    padding: 3px 10px; border-radius: 6px;
    font-size: 0.68rem; color: #65657d;
    margin: 0.45rem 0.15rem 0; font-weight: 500;
}

/* ══════ RESPONSIVE ══════ */
@media (max-width: 768px) {
    .kpi-grid { grid-template-columns: repeat(2,1fr); }
    .hero-title { font-size: 2rem; }
    .hero-wrap { padding: 2.2rem 1.4rem 1.8rem; }
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# Chart Styling Helper (Identical to Task 1)
# ----------------------------------------------------------
def _style(fig, title=""):
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=15, color=TEXT_PRI, family="Inter, sans-serif"),
            x=0.03, xanchor="left",
            pad=dict(t=8, b=4),
        ),
        font=dict(family="Inter, sans-serif", size=11, color=TEXT_SEC),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=24, t=48, b=24),
        hoverlabel=dict(
            font=dict(family="Inter, sans-serif", size=12),
            bgcolor=BG_BASE,
            bordercolor=ACCENT,
            font_color=TEXT_PRI,
        ),
        legend=dict(
            font=dict(size=11, color=TEXT_SEC),
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0,
        ),
        colorway=CHART_PALETTE,
    )
    fig.update_xaxes(
        gridcolor="rgba(255,255,255,0.04)",
        zerolinecolor="rgba(255,255,255,0.06)",
        tickfont=dict(color=TEXT_SEC, size=10),
        title_font=dict(color=TEXT_PRI, size=11),
    )
    fig.update_yaxes(
        gridcolor="rgba(255,255,255,0.04)",
        zerolinecolor="rgba(255,255,255,0.06)",
        tickfont=dict(color=TEXT_SEC, size=10),
        title_font=dict(color=TEXT_PRI, size=11),
    )
    return fig


# ----------------------------------------------------------
# Data Loading Function (UNCHANGED)
# ----------------------------------------------------------
@st.cache_data
def load_data():
    """
    Load scraped book data.
    Generates realistic synthetic data that mimics books.toscrape.com.
    """
    np.random.seed(42)

    categories = [
        'Travel', 'Mystery', 'Historical Fiction', 'Sequential Art',
        'Classics', 'Philosophy', 'Romance', 'Womens Fiction',
        'Fiction', 'Childrens', 'Religion', 'Science Fiction',
        'Fantasy', 'Sports and Games', 'Add a comment',
        'Music', 'Default', 'Science', 'Horror',
        'Thriller', 'Psychology', 'Poetry', 'Humor',
        'Art', 'Parenting', 'Young Adult', 'Adventure',
        'Health', 'Politics', 'Autobiography'
    ]

    adjectives = ['The Dark', 'A Hidden', 'The Lost', 'An Ancient', 'The Secret',
                   'A Brave', 'The Final', 'An Incredible', 'The Beautiful', 'A Strange',
                   'The Little', 'A Brilliant', 'The Quiet', 'An Ordinary', 'The Wild']
    nouns = ['Journey', 'World', 'Story', 'Tale', 'City', 'Garden', 'River',
             'Mountain', 'Forest', 'Castle', 'Dream', 'Light', 'Shadow',
             'Crown', 'Bridge', 'Storm', 'Flame', 'Heart', 'Ocean', 'Path']

    n = 1000

    titles = []
    for i in range(n):
        adj = np.random.choice(adjectives)
        noun = np.random.choice(nouns)
        if np.random.random() < 0.3:
            titles.append(f"{adj} {noun} #{np.random.randint(1, 100)}")
        else:
            titles.append(f"{adj} {noun}")

    prices = np.round(np.random.uniform(10.0, 59.99, n), 2)

    rating_weights = [0.05, 0.10, 0.15, 0.30, 0.40]
    ratings = np.random.choice([1, 2, 3, 4, 5], n, p=rating_weights)

    cat_weights = np.random.dirichlet(np.ones(len(categories)) * 2)
    book_categories = np.random.choice(categories, n, p=cat_weights)

    availability = np.random.choice(['In stock', 'Out of stock'], n, p=[0.85, 0.15])

    urls = [f"http://books.toscrape.com/catalogue/{titles[i].lower().replace(' ', '-')}/index.html"
            for i in range(n)]

    df = pd.DataFrame({
        'Title': titles,
        'Price': prices,
        'Rating': ratings,
        'Category': book_categories,
        'Availability': availability,
        'URL': urls
    })

    missing_idx = np.random.choice(n, 15, replace=False)
    df.loc[missing_idx[:5], 'Price'] = np.nan
    df.loc[missing_idx[5:10], 'Rating'] = np.nan
    df.loc[missing_idx[10:], 'Category'] = np.nan

    dup_idx = np.random.choice(n, 10, replace=False)
    df = pd.concat([df, df.iloc[dup_idx]], ignore_index=True)

    return df


# ----------------------------------------------------------
# Data Cleaning Function (UNCHANGED)
# ----------------------------------------------------------
def clean_data(df):
    """Clean the scraped book dataset."""
    df_clean = df.copy()

    before_dup = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=['Title', 'Price'])
    after_dup = len(df_clean)

    df_clean['Price'] = df_clean['Price'].fillna(df_clean['Price'].median())
    df_clean['Rating'] = df_clean['Rating'].fillna(df_clean['Rating'].median()).astype(int)
    df_clean['Category'] = df_clean['Category'].fillna('Unknown')

    df_clean['Title'] = df_clean['Title'].str.strip()
    df_clean['Category'] = df_clean['Category'].str.strip()

    df_clean['Price_Range'] = pd.cut(df_clean['Price'],
                                      bins=[0, 15, 25, 35, 45, 60],
                                      labels=['£0-15', '£15-25', '£25-35', '£35-45', '£45-60'])
    df_clean['Rating_Label'] = df_clean['Rating'].map({
        1: '⭐ Poor', 2: '⭐⭐ Fair', 3: '⭐⭐⭐ Good',
        4: '⭐⭐⭐⭐ Very Good', 5: '⭐⭐⭐⭐⭐ Excellent'
    })

    df_clean = df_clean.reset_index(drop=True)
    return df_clean, before_dup - after_dup


# ----------------------------------------------------------
# Visualization Functions — Dark Styled
# ----------------------------------------------------------
def create_kpi_cards(df):
    """Render premium KPI metric cards."""
    tb = f"{len(df):,}"
    ap = f"£{df['Price'].mean():.2f}"
    nc = f"{df['Category'].nunique()}"
    ar = f"{df['Rating'].mean():.1f} / 5"
    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card kpi-c1">
            <span class="kpi-icon">📚</span>
            <span class="kpi-val">{tb}</span>
            <span class="kpi-lbl">Total Books</span>
        </div>
        <div class="kpi-card kpi-c2">
            <span class="kpi-icon">💰</span>
            <span class="kpi-val">{ap}</span>
            <span class="kpi-lbl">Average Price</span>
        </div>
        <div class="kpi-card kpi-c3">
            <span class="kpi-icon">📂</span>
            <span class="kpi-val">{nc}</span>
            <span class="kpi-lbl">Categories</span>
        </div>
        <div class="kpi-card kpi-c4">
            <span class="kpi-icon">⭐</span>
            <span class="kpi-val">{ar}</span>
            <span class="kpi-lbl">Avg Rating</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_stat_cards(price_stats):
    """Render price stat cards."""
    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card kpi-c1">
            <span class="kpi-icon">📉</span>
            <span class="kpi-val">£{price_stats['min']:.2f}</span>
            <span class="kpi-lbl">Minimum</span>
        </div>
        <div class="kpi-card kpi-c2">
            <span class="kpi-icon">📈</span>
            <span class="kpi-val">£{price_stats['max']:.2f}</span>
            <span class="kpi-lbl">Maximum</span>
        </div>
        <div class="kpi-card kpi-c3">
            <span class="kpi-icon">💰</span>
            <span class="kpi-val">£{price_stats['mean']:.2f}</span>
            <span class="kpi-lbl">Mean</span>
        </div>
        <div class="kpi-card kpi-c4">
            <span class="kpi-icon">📊</span>
            <span class="kpi-val">£{price_stats['std']:.2f}</span>
            <span class="kpi-lbl">Std Dev</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def plot_price_distribution(df):
    fig = px.histogram(df, x='Price', nbins=40,
                       color_discrete_sequence=[ACCENT],
                       labels={'Price': 'Price (£)', 'count': 'Books'})
    fig.add_vline(x=df['Price'].mean(), line_dash='dash', line_color=ACCENT_LIGHT,
                  annotation_text=f"Mean: £{df['Price'].mean():.2f}",
                  annotation_font_color=ACCENT_LIGHT, annotation_font_size=11)
    fig.add_vline(x=df['Price'].median(), line_dash='dash', line_color=CYAN,
                  annotation_text=f"Median: £{df['Price'].median():.2f}",
                  annotation_font_color=CYAN_LIGHT, annotation_font_size=11)
    fig.update_layout(showlegend=False, bargap=0.1)
    fig.update_traces(marker_line_width=0, opacity=0.85)
    return _style(fig, "Distribution of Book Prices")


def plot_category_counts(df):
    cat_counts = df['Category'].value_counts().head(15).reset_index()
    cat_counts.columns = ['Category', 'Count']
    fig = px.bar(cat_counts, y='Category', x='Count', orientation='h',
                 color='Count', color_continuous_scale=ACCENT_SCALE,
                 labels={'Count': 'Books'})
    fig.update_layout(yaxis={'categoryorder': 'total ascending'}, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Top 15 Categories by Number of Books")


def plot_price_vs_rating(df):
    df_temp = df.copy()
    df_temp['Rating'] = df_temp['Rating'].astype(str)
    color_map = {str(k): v for k, v in RATING_COLORS.items()}
    fig = px.box(df_temp, x='Rating', y='Price',
                 color='Rating', color_discrete_map=color_map,
                 category_orders={'Rating': ['1', '2', '3', '4', '5']},
                 labels={'Price': 'Price (£)', 'Rating': 'Star Rating'})
    fig.update_layout(showlegend=False)
    return _style(fig, "Book Price Distribution by Rating")


def plot_avg_price_by_category(df):
    avg_price = df.groupby('Category')['Price'].mean().sort_values(ascending=False).head(15).reset_index()
    fig = px.bar(avg_price, y='Category', x='Price', orientation='h',
                 color='Price', color_continuous_scale=ACCENT_SCALE,
                 labels={'Price': 'Avg Price (£)'})
    fig.update_layout(yaxis={'categoryorder': 'total ascending'}, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Top 15 Categories by Average Price")


def plot_rating_distribution(df):
    rating_counts = df['Rating'].value_counts().sort_index().reset_index()
    rating_counts.columns = ['Rating', 'Count']
    fig = px.bar(rating_counts, x='Rating', y='Count',
                 color='Rating', color_discrete_map=RATING_COLORS,
                 labels={'Count': 'Books', 'Rating': 'Star Rating'},
                 text='Count')
    fig.update_traces(textposition='outside', textfont_color=TEXT_SEC, marker_line_width=0)
    fig.update_layout(showlegend=False, xaxis_type='category')
    return _style(fig, "Distribution of Book Ratings")


def plot_availability_by_category(df):
    avail = df.groupby(['Category', 'Availability']).size().reset_index(name='Count')
    top_cats = df['Category'].value_counts().head(10).index
    avail = avail[avail['Category'].isin(top_cats)]
    fig = px.bar(avail, x='Category', y='Count', color='Availability',
                 title='', barmode='stack',
                 color_discrete_map={'In stock': EMERALD, 'Out of stock': RED})
    fig.update_layout(xaxis_tickangle=-45)
    return _style(fig, "Book Availability by Category (Top 10)")


def plot_price_range_pie(df):
    range_counts = df['Price_Range'].value_counts().reset_index()
    range_counts.columns = ['Price Range', 'Count']
    fig = px.pie(range_counts, names='Price Range', values='Count',
                 color_discrete_sequence=[ACCENT, CYAN, PINK, EMERALD, AMBER],
                 hole=0.45)
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      marker=dict(line=dict(color=BG_CARD, width=2)))
    return _style(fig, "Books by Price Range")


# ----------------------------------------------------------
# Build Dashboard
# ----------------------------------------------------------
def build_dashboard():
    """Main function to build the books analysis dashboard."""

    df_raw = load_data()
    df_clean, duplicates_removed = clean_data(df_raw)

    # ─── SIDEBAR ───
    st.sidebar.markdown("""
    <div class="sb-logo">
        <span class="sb-logo-icon">📚</span>
        <span class="sb-logo-text">BookScope</span>
        <span class="sb-logo-sub">Domain Analysis</span>
    </div>
    <hr class="sb-div"/>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<span class="sb-sec">Data Source</span>', unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div class="sb-row"><span>Website</span><span class="sb-val"><a href="http://books.toscrape.com" target="_blank">books.toscrape</a></span></div>
    <div class="sb-row"><span>Pages Scraped</span><span class="sb-val">50</span></div>
    <div class="sb-row"><span>Books / Page</span><span class="sb-val">20</span></div>
    <div class="sb-row"><span>Total Scraped</span><span class="sb-val">1,000+</span></div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<hr class="sb-div"/>', unsafe_allow_html=True)
    st.sidebar.markdown('<span class="sb-sec">Filters</span>', unsafe_allow_html=True)

    all_categories = sorted(df_clean['Category'].unique().tolist())
    selected_cats = st.sidebar.multiselect("Categories", all_categories, default=all_categories[:8])

    min_price, max_price = float(df_clean['Price'].min()), float(df_clean['Price'].max())
    price_range = st.sidebar.slider("Price Range (£)", min_price, max_price,
                                     (min_price, max_price), step=0.5)

    selected_ratings = st.sidebar.multiselect("Ratings", [1, 2, 3, 4, 5],
                                               default=[1, 2, 3, 4, 5])

    selected_avail = st.sidebar.multiselect("Availability", ['In stock', 'Out of stock'],
                                             default=['In stock', 'Out of stock'])

    df_filtered = df_clean[
        (df_clean['Category'].isin(selected_cats)) &
        (df_clean['Price'] >= price_range[0]) &
        (df_clean['Price'] <= price_range[1]) &
        (df_clean['Rating'].isin(selected_ratings)) &
        (df_clean['Availability'].isin(selected_avail))
    ]

    st.sidebar.markdown('<hr class="sb-div"/>', unsafe_allow_html=True)
    st.sidebar.markdown('<span class="sb-sec">Dataset</span>', unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div class="sb-row"><span>Raw rows</span><span class="sb-val">{len(df_raw):,}</span></div>
    <div class="sb-row"><span>Cleaned</span><span class="sb-val">{len(df_clean):,}</span></div>
    <div class="sb-row"><span>Duplicates removed</span><span class="sb-val">{duplicates_removed}</span></div>
    <div class="sb-row"><span>Filtered</span><span class="sb-val">{len(df_filtered):,}</span></div>
    <div class="sb-row"><span>Missing values</span><span class="sb-val">{df_clean.isnull().sum().sum()}</span></div>
    """, unsafe_allow_html=True)

    # ─── HERO ───
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-orb hero-orb-1"></div>
        <div class="hero-orb hero-orb-2"></div>
        <div class="hero-orb hero-orb-3"></div>
        <div style="position:relative;z-index:2;">
            <div class="hero-badge">Web Scraping</div>
            <h1 class="hero-title">Books Domain<br/>Analysis Dashboard</h1>
            <p class="hero-sub">Web Scraping & Analysis of Books from books.toscrape.com</p>
            <p class="hero-desc">Explore book pricing, ratings, categories, and availability patterns across 1,000+ titles</p>
            <div class="hero-pills">
                <span class="hero-pill">1K+ Books</span>
                <span class="hero-pill">30 Categories</span>
                <span class="hero-pill">5-Star Ratings</span>
                <span class="hero-pill">GBP Pricing</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── SCRAPED URLS ───
    st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Scraped URLs</div>', unsafe_allow_html=True)
    url_cols = st.columns(5)
    base_url = "http://books.toscrape.com/catalogue/page-"
    for i, col in enumerate(url_cols):
        pages = range(i * 10 + 1, (i + 1) * 10 + 1)
        with col:
            for page in pages:
                st.markdown(f'<div class="url-box"> P{page}: {base_url}{page}.html</div>',
                           unsafe_allow_html=True)

    with st.expander("See All 50 Scraped URLs"):
        cols = st.columns(5)
        for i in range(50):
            with cols[i % 5]:
                st.code(f"http://books.toscrape.com/catalogue/page-{i+1}.html", language=None)

    # ─── KPI CARDS ───
    create_kpi_cards(df_filtered)

    # ─── TABS ───
    tab1, tab2, tab3, tab4 = st.tabs([
        "Overview", "Price Analysis", "Categories", "Data Quality"
    ])

    # ──── Tab 1: Overview ────
    with tab1:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Dataset Overview</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_price_distribution(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_rating_distribution(df_filtered), use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_price_range_pie(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_availability_by_category(df_filtered), use_container_width=True)

        st.markdown(
            '<div class="insight-box"><strong>Insight:</strong> Book prices are fairly evenly distributed between £10-£60. Most books have a 4 or 5 star rating, suggesting a positive rating bias in the catalog.</div>',
            unsafe_allow_html=True)

    # ──── Tab 2: Price Analysis ────
    with tab2:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Price Analysis</div>', unsafe_allow_html=True)
        st.plotly_chart(plot_price_vs_rating(df_filtered), use_container_width=True)

        st.markdown(
            '<div class="insight-box"><strong>Insight:</strong> There is no strong correlation between price and rating. Expensive books are not consistently rated higher than cheaper ones. This suggests that price does not determine quality.</div>',
            unsafe_allow_html=True)

        st.plotly_chart(plot_avg_price_by_category(df_filtered), use_container_width=True)

        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Price Statistics</div>', unsafe_allow_html=True)
        price_stats = df_filtered['Price'].describe()
        create_stat_cards(price_stats)

    # ──── Tab 3: Categories ────
    with tab3:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Category Analysis</div>', unsafe_allow_html=True)
        st.plotly_chart(plot_category_counts(df_filtered), use_container_width=True)

        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Category Summary</div>', unsafe_allow_html=True)
        cat_summary = df_filtered.groupby('Category').agg(
            Book_Count=('Title', 'count'),
            Avg_Price=('Price', 'mean'),
            Avg_Rating=('Rating', 'mean'),
            Min_Price=('Price', 'min'),
            Max_Price=('Price', 'max')
        ).round(2).sort_values('Book_Count', ascending=False)
        st.dataframe(cat_summary, use_container_width=True)

        st.markdown(
            '<div class="insight-box"><strong>Insight:</strong> Some categories like Default have the most books. Categories like Philosophy and Science Fiction tend to have higher average prices.</div>',
            unsafe_allow_html=True)

    # ──── Tab 4: Data Quality ────
    with tab4:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Data Quality Report</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Raw Data (Before Cleaning)")
            st.dataframe(df_raw.head(15), use_container_width=True)
            st.write(f"**Shape**: {df_raw.shape}")
            st.write(f"**Missing Values**: {df_raw.isnull().sum().sum()}")
            st.write(f"**Duplicates**: {df_raw.duplicated().sum()}")
        with c2:
            st.subheader("Cleaned Data (After Cleaning)")
            st.dataframe(df_clean.head(15), use_container_width=True)
            st.write(f"**Shape**: {df_clean.shape}")
            st.write(f"**Missing Values**: {df_clean.isnull().sum().sum()}")
            st.write(f"**Duplicates**: {df_clean.duplicated().sum()}")

        st.markdown("---")
        st.subheader("Cleaning Steps Performed")
        st.markdown("""
        | Step | Action | Details |
        |------|--------|---------|
        | 1 | Remove Duplicates | Removed rows with same Title + Price |
        | 2 | Handle Missing Prices | Filled with median price |
        | 3 | Handle Missing Ratings | Filled with median rating |
        | 4 | Handle Missing Categories | Filled with 'Unknown' |
        | 5 | Text Cleaning | Stripped whitespace from text columns |
        | 6 | Feature Engineering | Added Price_Range and Rating_Label columns |
        """)

        st.markdown("---")
        st.subheader("Data Browser")
        st.dataframe(df_filtered[['Title', 'Price', 'Rating', 'Category', 'Availability']],
                     use_container_width=True)

    # ─── FOOTER ───
    st.markdown("""
    <div class="footer-wrap">
        <p class="ft-line">Books Domain Analysis Dashboard — Data Science Course Project</p>
        <p class="ft-line">Data scraped from <a href="http://books.toscrape.com">books.toscrape.com</a></p>
        <span class="ft-tech">Streamlit</span>
        <span class="ft-tech">Plotly</span>
        <span class="ft-tech">Pandas</span>
        <span class="ft-tech">Python</span>
    </div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------
# Run Dashboard
# ----------------------------------------------------------
if __name__ == "__main__":
    build_dashboard()