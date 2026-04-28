"""
=============================================================
  Task 1 Dashboard — Video Game Sales Analysis ✦ Dark Edition
  Run: streamlit run task1_dashboard.py
=============================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------
st.set_page_config(
    page_title="Video Game Sales Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# Design System — Color Tokens
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

REGION_COLORS = {
    "NA_Sales": "#7c5cfc",
    "EU_Sales": "#22d3ee",
    "JP_Sales": "#fbbf24",
    "Other_Sales": "#34d399",
}
REGION_NAMES = {
    "NA_Sales": "North America",
    "EU_Sales": "Europe",
    "JP_Sales": "Japan",
    "Other_Sales": "Other",
}

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
.hero-orb {
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
}
.hero-orb-1 {
    width: 400px; height: 400px;
    top: -140px; right: -60px;
    background: radial-gradient(circle, rgba(124,92,252,0.22) 0%, transparent 70%);
    animation: orbF 7s ease-in-out infinite;
}
.hero-orb-2 {
    width: 300px; height: 300px;
    bottom: -100px; left: -40px;
    background: radial-gradient(circle, rgba(34,211,238,0.14) 0%, transparent 70%);
    animation: orbF 9s ease-in-out infinite reverse;
}
.hero-orb-3 {
    width: 180px; height: 180px;
    top: 35%; left: 52%;
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
    font-size: 3.2rem;
    font-weight: 900;
    line-height: 1.08;
    margin: 0 0 0.85rem;
    background: linear-gradient(135deg, #ededf3 0%, #c8c8d8 30%, #9b82fc 65%, #22d3ee 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fU 0.6s ease-out 0.2s both;
}
.hero-sub {
    font-size: 1.08rem;
    color: #9898b0;
    font-weight: 400;
    margin: 0 0 0.3rem;
    max-width: 600px;
    animation: fU 0.6s ease-out 0.3s both;
}
.hero-desc {
    font-size: 0.86rem;
    color: #65657d;
    font-weight: 300;
    margin: 0 0 1.7rem;
    max-width: 500px;
    animation: fU 0.6s ease-out 0.38s both;
}
.hero-pills {
    display: flex;
    gap: 0.65rem;
    flex-wrap: wrap;
    animation: fU 0.6s ease-out 0.48s both;
}
.hero-pill {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.07);
    padding: 6px 16px;
    border-radius: 10px;
    color: #9898b0;
    font-size: 0.80rem;
    font-weight: 500;
    transition: all 0.3s ease;
}
.hero-pill:hover {
    background: rgba(124,92,252,0.10);
    border-color: rgba(124,92,252,0.25);
    color: #c8c8d8;
    transform: translateY(-2px);
}
@keyframes fU {
    from{opacity:0;transform:translateY(16px)}
    to{opacity:1;transform:translateY(0)}
}

/* ══════ KPI CARDS ══════ */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 1.15rem;
    margin-bottom: 1.8rem;
    animation: fU 0.6s ease-out 0.55s both;
}
.kpi-card {
    position: relative;
    background: #111119;
    border-radius: 16px;
    padding: 1.5rem 1.1rem 1.2rem;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
    overflow: hidden;
    transition: all 0.45s cubic-bezier(0.175,0.885,0.32,1.275);
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
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
    font-size: 2rem;
    font-weight: 800;
    color: #ededf3;
    line-height: 1.15;
    margin-bottom: 0.15rem;
    display: block;
}
.kpi-lbl {
    font-size: 0.70rem;
    color: #65657d;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    display: block;
}
.kpi-delta {
    font-size: 0.70rem;
    color: #34d399;
    font-weight: 600;
    margin-top: 0.25rem;
    display: block;
}

/* ══════ CHART CONTAINERS ══════ */
[data-testid="stPlotlyChart"] {
    background: #111119;
    border-radius: 16px;
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
    font-size: 1.35rem;
    font-weight: 700;
    color: #ededf3;
    margin: 1.8rem 0 1.1rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.sec-hd .sec-ic {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 34px; height: 34px;
    border-radius: 9px;
    background: linear-gradient(135deg,#7c5cfc,#5a3ed4);
    color: #fff;
    font-size: 0.95rem;
    flex-shrink: 0;
}
.sec-hd::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(255,255,255,0.08), transparent);
    border-radius: 1px;
    margin-left: 0.4rem;
}

/* ══════ INSIGHT BOX ══════ */
.insight-box {
    background: rgba(124,92,252,0.06);
    border-left: 3px solid #7c5cfc;
    padding: 0.9rem 1.2rem;
    border-radius: 0 14px 14px 0;
    margin: 1.3rem 0;
    color: #c8c8d8;
    font-size: 0.86rem;
    line-height: 1.6;
    animation: fU 0.5s ease-out;
}
.insight-box strong { color: #9b82fc; }

/* ══════ TABS ══════ */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #111119;
    border-radius: 14px;
    padding: 4px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.20);
    border: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 1.4rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 9px 20px;
    font-weight: 600;
    font-size: 0.80rem;
    color: #65657d;
    transition: all 0.3s ease;
    white-space: nowrap;
}
.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,255,255,0.04);
    color: #9898b0;
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
    margin: 0.9rem 0.4rem;
    border: none;
}
.sb-sec {
    font-size: 0.62rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #7c5cfc !important;
    margin-bottom: 0.6rem;
    display: block;
    padding-left: 2px;
}
.sb-status {
    border-radius: 9px;
    padding: 0.45rem 0.7rem;
    font-size: 0.76rem;
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin-bottom: 0.2rem;
}
.sb-ok  { background: rgba(52,211,153,0.08); border: 1px solid rgba(52,211,153,0.18); color: #34d399 !important; }
.sb-syn { background: rgba(34,211,238,0.08); border: 1px solid rgba(34,211,238,0.18); color: #22d3ee !important; }

.sb-row {
    display: flex;
    justify-content: space-between;
    padding: 0.28rem 0;
    font-size: 0.76rem;
    color: #65657d;
    border-bottom: 1px solid rgba(255,255,255,0.03);
}
.sb-row:last-child { border-bottom: none; }
.sb-val { color: #c8c8d8 !important; font-weight: 600; }

/* Sidebar widgets */
section[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.08) !important;
}
section[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: #c8c8d8 !important;
}
section[data-testid="stSidebar"] [data-baseweb="select"] input::placeholder {
    color: #65657d !important;
}
section[data-testid="stSidebar"] [data-baseweb="tag"],
section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {
    background-color: rgba(124,92,252,0.18) !important;
    color: #9b82fc !important;
    border-color: rgba(124,92,252,0.20) !important;
}
section[data-testid="stSidebar"] [data-baseweb="tag"] button svg,
section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] button svg {
    fill: #9b82fc !important;
    color: #9b82fc !important;
}
section[data-testid="stSidebar"] [data-baseweb="popover"] {
    background-color: #111119 !important;
}
section[data-testid="stSidebar"] [data-baseweb="popover"] li {
    color: #c8c8d8 !important;
}
section[data-testid="stSidebar"] [data-baseweb="popover"] li:hover {
    background-color: rgba(124,92,252,0.12) !important;
}
section[data-testid="stSidebar"] [data-baseweb="slider"] [role="slider"] {
    background-color: #7c5cfc !important;
    border-color: #7c5cfc !important;
}
section[data-testid="stSidebar"] [data-baseweb="slider"] .bar {
    background: rgba(124,92,252,0.18) !important;
}
section[data-testid="stSidebar"] [data-baseweb="slider"] label {
    color: #9898b0 !important;
}
section[data-testid="stSidebar"]::-webkit-scrollbar { width: 3px; }
section[data-testid="stSidebar"]::-webkit-scrollbar-thumb { background: rgba(124,92,252,0.2); border-radius: 2px; }

/* ══════ DATAFRAME ══════ */
.stDataFrame {
    border-radius: 14px !important;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06) !important;
}

/* ══════ ALERTS ══════ */
.stAlert {
    background: rgba(34,211,238,0.05) !important;
    border-color: rgba(34,211,238,0.12) !important;
    color: #9898b0 !important;
}

/* ══════ FOOTER ══════ */
.footer-wrap {
    text-align: center;
    padding: 2rem 1rem 1rem;
    margin-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.05);
}
.ft-line { color: #65657d; font-size: 0.80rem; margin: 0.15rem 0; }
.ft-tech {
    display: inline-block;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.06);
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 0.68rem;
    color: #65657d;
    margin: 0.45rem 0.15rem 0;
    font-weight: 500;
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
# Chart Styling Helper
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
# Data Loading (UNCHANGED)
# ----------------------------------------------------------
@st.cache_data
def load_data():
    try:
        url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/vgsales.csv"
        df = pd.read_csv(url, on_bad_lines="skip")
        if len(df) > 100:
            return df, True
    except Exception:
        pass

    np.random.seed(42)
    n = 16500
    platforms = ['PS2','X360','PS3','Wii','DS','PS4','PS','PC','GBA','PSP',
                 'XOne','NES','SNES','3DS','N64','GB','PSV','DC','SAT','2600','WiiU']
    genres = ['Action','Sports','Misc','Role-Playing','Shooter','Adventure',
              'Racing','Platform','Simulation','Fighting','Strategy','Puzzle']
    publishers = ['Nintendo','Electronic Arts','Activision','Sony Computer Entertainment',
                  'Ubisoft','Take-Two Interactive','THQ','Microsoft Game Studios',
                  'Sega','Bandai Namco Games','Konami Digital Entertainment',
                  'Capcom','Square Enix','Warner Bros. Interactive',
                  'Disney Interactive Studios','Namco Bandai Games','Atari',
                  'Eidos Interactive','LucasArts','Midway Games',
                  'Bethesda Softworks','Deep Silver','Namco',
                  'Codemasters','NCSoft','MTV Games','505 Games']
    prefixes = ['Super','Mega','Grand','Ultra','Pro','Final','Dark','New',
                'Legend of','Battle','Star','Power','Dragon','King of','Wild']
    suffixes = ['World','Quest','Wars','Force','Rush','Strike','Heroes',
                'Legends','Adventure','Odyssey','Chronicles','Fury','Storm']
    bases = ['Racer','Fighter','Soccer','Golf','Tennis','Combat','Arena',
             'Island','Kingdom','Galaxy','Tales','Fantasy','Saga','Dynasty']
    names = []
    for _ in range(n):
        if np.random.random() < 0.5:
            names.append(f"{np.random.choice(prefixes)} {np.random.choice(bases)} {np.random.choice(suffixes)}")
        else:
            names.append(f"{np.random.choice(prefixes)} {np.random.choice(bases)}")

    yw = np.array([0.005 if y<1995 else 0.01 if y<2000 else 0.04 if y<2005
                    else 0.08 if y<2010 else 0.06 if y<2015 else 0.02 for y in range(1980,2024)])
    yw = yw / yw.sum()
    years = np.random.choice(range(1980,2024), n, p=yw)

    na = np.round(np.random.exponential(0.3, n), 2)
    eu = np.round(np.random.exponential(0.22, n), 2)
    jp = np.round(np.random.exponential(0.1, n), 2)
    ot = np.round(np.random.exponential(0.08, n), 2)
    gl = np.round(na+eu+jp+ot, 2)

    ym = np.random.choice([np.nan,1], n, p=[0.02,0.98])
    pm = np.random.choice([np.nan,1], n, p=[0.01,0.99])
    years_na = years * ym
    pub_na = [np.random.choice(publishers) if m==1 else np.nan for m in pm]

    df = pd.DataFrame({
        'Rank': range(1,n+1), 'Name': names,
        'Platform': np.random.choice(platforms, n),
        'Year': years_na, 'Genre': np.random.choice(genres, n),
        'Publisher': pub_na,
        'NA_Sales': na, 'EU_Sales': eu, 'JP_Sales': jp,
        'Other_Sales': ot, 'Global_Sales': gl
    })
    df = df.sort_values('Global_Sales', ascending=False).reset_index(drop=True)
    df['Rank'] = range(1, len(df)+1)
    return df, False


# ----------------------------------------------------------
# Data Preprocessing (UNCHANGED)
# ----------------------------------------------------------
def preprocess_data(df):
    df_raw = df.copy()
    df_clean = df.copy()
    df_clean = df_clean.dropna(subset=['Year'])
    df_clean = df_clean.dropna(subset=['Publisher'])
    df_clean['Year'] = df_clean['Year'].astype(int)
    df_clean = df_clean.drop_duplicates()
    for col in ['Name','Platform','Genre','Publisher']:
        df_clean[col] = df_clean[col].astype(str).str.strip()
    df_clean['Decade'] = (df_clean['Year'] // 10) * 10
    df_clean['Sales_Category'] = pd.cut(
        df_clean['Global_Sales'],
        bins=[0, 0.5, 1, 5, float('inf')],
        labels=['Low','Medium','High','Blockbuster']
    )
    df_clean = df_clean[df_clean['Global_Sales'] > 0]
    df_clean = df_clean.reset_index(drop=True)
    return df_raw, df_clean


# ----------------------------------------------------------
# Visualization Functions — Consistent Dark Styling
# ----------------------------------------------------------
def create_kpi_cards(df):
    tg = f"{len(df):,}"
    ts = f"${df['Global_Sales'].sum():.1f}M"
    av = f"{df['Global_Sales'].mean():.2f}M avg"
    tp = df.groupby('Platform')['Global_Sales'].sum().idxmax()
    tv = f"{df.groupby('Platform')['Global_Sales'].sum().max():.1f}M"
    y1, y2 = int(df['Year'].min()), int(df['Year'].max())
    yc = f"{df['Year'].nunique()} years"
    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card kpi-c1">
            <span class="kpi-icon">🎮</span>
            <span class="kpi-val">{tg}</span>
            <span class="kpi-lbl">Total Games</span>
        </div>
        <div class="kpi-card kpi-c2">
            <span class="kpi-icon">💰</span>
            <span class="kpi-val">{ts}</span>
            <span class="kpi-lbl">Total Revenue</span>
            <span class="kpi-delta">{av}</span>
        </div>
        <div class="kpi-card kpi-c3">
            <span class="kpi-icon">🏆</span>
            <span class="kpi-val">{tp}</span>
            <span class="kpi-lbl">Top Platform</span>
            <span class="kpi-delta">{tv}</span>
        </div>
        <div class="kpi-card kpi-c4">
            <span class="kpi-icon">📅</span>
            <span class="kpi-val">{y1}–{y2}</span>
            <span class="kpi-lbl">Year Range</span>
            <span class="kpi-delta">{yc}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def plot_sales_distribution(df):
    fig = px.histogram(df, x='Global_Sales', nbins=100,
                       color_discrete_sequence=[ACCENT],
                       labels={'Global_Sales':'Global Sales (M)','count':'Games'})
    fig.update_xaxes(range=[0,5])
    fig.update_layout(showlegend=False, bargap=0.1)
    fig.update_traces(marker_line_width=0, opacity=0.85)
    return _style(fig, "Global Sales Distribution")


def plot_genre_counts(df):
    gc = df['Genre'].value_counts().reset_index()
    gc.columns = ['Genre','Count']
    fig = px.bar(gc, x='Genre', y='Count',
                 color='Count', color_continuous_scale=ACCENT_SCALE,
                 labels={'Count':'Games'})
    fig.update_layout(xaxis_tickangle=-45, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Games by Genre")


def plot_top10_games(df):
    t10 = df.nlargest(10, 'Global_Sales')[['Name','Platform','Global_Sales']]
    fig = px.bar(t10, y='Name', x='Global_Sales', orientation='h',
                 color='Global_Sales', color_continuous_scale=ACCENT_SCALE,
                 labels={'Global_Sales':'Sales (M)','Name':''})
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Top 10 Best-Selling Games")


def plot_sales_over_years(df):
    yl = df.groupby('Year')['Global_Sales'].sum().reset_index()
    fig = px.line(yl, x='Year', y='Global_Sales',
                  labels={'Global_Sales':'Total Sales (M)'}, markers=True)
    fig.update_traces(line_color=ACCENT, line_width=3,
                      marker=dict(size=4, color=ACCENT_LIGHT))
    fig.add_scatter(x=yl['Year'], y=yl['Global_Sales'],
                    fill='tozeroy', fillcolor=f"rgba(124,92,252,0.10)",
                    line=dict(color="rgba(124,92,252,0)"), showlegend=False)
    return _style(fig, "Global Sales Over the Years")


def plot_platform_sales(df):
    ps = df.groupby('Platform')['Global_Sales'].sum().nlargest(15).reset_index()
    fig = px.bar(ps, x='Platform', y='Global_Sales',
                 color='Global_Sales', color_continuous_scale=ACCENT_SCALE,
                 labels={'Global_Sales':'Sales (M)'})
    fig.update_layout(coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Sales by Platform (Top 15)")


def plot_regional_market_share(df):
    regions = {'North America': df['NA_Sales'].sum(),
               'Europe': df['EU_Sales'].sum(),
               'Japan': df['JP_Sales'].sum(),
               'Other': df['Other_Sales'].sum()}
    fig = px.pie(names=list(regions.keys()), values=list(regions.values()),
                 color_discrete_sequence=[ACCENT, CYAN, AMBER, EMERALD], hole=0.45)
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      marker=dict(line=dict(color=BG_CARD, width=2)))
    return _style(fig, "Market Share by Region")


def plot_publisher_titles(df):
    pc = df['Publisher'].value_counts().head(15).reset_index()
    pc.columns = ['Publisher','Titles']
    fig = px.bar(pc, y='Publisher', x='Titles', orientation='h',
                 color='Titles', color_continuous_scale=ACCENT_SCALE)
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Top 15 Publishers by Titles")


def plot_genre_avg_sales(df):
    avg = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(avg, x='Genre', y='Global_Sales',
                 color='Global_Sales', color_continuous_scale=ACCENT_SCALE,
                 labels={'Global_Sales':'Avg Sales (M)'})
    fig.update_layout(xaxis_tickangle=-45, coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Average Sales by Genre")


def plot_regional_trends(df):
    yl = df.groupby('Year').agg({'NA_Sales':'sum','EU_Sales':'sum',
                                  'JP_Sales':'sum','Other_Sales':'sum'}).reset_index()
    fig = go.Figure()
    for col in ['NA_Sales','EU_Sales','JP_Sales','Other_Sales']:
        fig.add_trace(go.Scatter(x=yl['Year'], y=yl[col], mode='lines+markers',
                                  name=REGION_NAMES[col],
                                  line=dict(color=REGION_COLORS[col], width=2.5),
                                  marker=dict(size=3)))
    fig.update_layout(xaxis_title='Year', yaxis_title='Sales (M)')
    return _style(fig, "Regional Sales Trends")


def plot_genre_by_platform(df):
    tp = df['Platform'].value_counts().head(6).index.tolist()
    sub = df[df['Platform'].isin(tp)]
    ct = sub.groupby(['Platform','Genre']).size().reset_index(name='Count')
    fig = px.sunburst(ct, path=['Platform','Genre'], values='Count',
                      color='Count', color_continuous_scale=ACCENT_SCALE)
    fig.update_layout(coloraxis_showscale=False)
    return _style(fig, "Genre Distribution by Top Platforms")


def plot_games_per_year(df):
    yl = df.groupby('Year').size().reset_index(name='Games')
    fig = px.bar(yl, x='Year', y='Games',
                 color='Games', color_continuous_scale=ACCENT_SCALE,
                 labels={'Games':'Games'})
    fig.update_layout(coloraxis_showscale=False)
    fig.update_traces(marker_line_width=0)
    return _style(fig, "Games Released Per Year")


def plot_best_year(df):
    yl = df.groupby('Year').agg({'Global_Sales':['sum','count']}).reset_index()
    yl.columns = ['Year','Total_Sales','Game_Count']
    best = yl.loc[yl['Total_Sales'].idxmax()]
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=('Total Sales by Year','Games Released by Year'))
    fig.add_trace(go.Bar(x=yl['Year'], y=yl['Total_Sales'],
                          marker_color=ACCENT, name='Sales', showlegend=False), row=1, col=1)
    fig.add_trace(go.Bar(x=yl['Year'], y=yl['Game_Count'],
                          marker_color=CYAN, name='Games', showlegend=False), row=1, col=2)
    fig.add_vline(x=best['Year'], line_dash='dash', line_color=PINK,
                  annotation_text=f"Peak: {int(best['Year'])}", row=1, col=1)
    fig.update_annotations(font=dict(color=TEXT_SEC, size=11, family='Inter, sans-serif'))
    return _style(fig, f"Peak Year: {int(best['Year'])} — ${best['Total_Sales']:.1f}M in Sales")


def plot_avg_sales_by_genre(df):
    stats = df.groupby('Genre')['Global_Sales'].agg(['mean','median']).reset_index()
    stats = stats.sort_values('mean', ascending=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=stats['Genre'], y=stats['mean'], name='Mean',
                          marker_color=ACCENT))
    fig.add_trace(go.Bar(x=stats['Genre'], y=stats['median'], name='Median',
                          marker_color=AMBER))
    fig.update_layout(xaxis_title='Genre', yaxis_title='Sales (M)',
                      xaxis_tickangle=-45, barmode='group')
    return _style(fig, "Average & Median Sales by Genre")


def plot_platform_decade(df):
    dec = df[df['Decade'] >= 1990]
    pd_ = dec.groupby(['Decade','Platform']).size().reset_index(name='Count')
    tp = dec['Platform'].value_counts().head(8).index
    pd_ = pd_[pd_['Platform'].isin(tp)]
    fig = px.bar(pd_, x='Decade', y='Count', color='Platform',
                 labels={'Count':'Games'}, barmode='group',
                 color_discrete_sequence=CHART_PALETTE)
    fig.update_xaxes(type='category')
    return _style(fig, "Platform Popularity by Decade")


def plot_publisher_by_region(df):
    tp = df['Publisher'].value_counts().head(8).index
    sub = df[df['Publisher'].isin(tp)]
    rp = sub.groupby('Publisher').agg({'NA_Sales':'sum','EU_Sales':'sum',
                                        'JP_Sales':'sum','Other_Sales':'sum'}).reset_index()
    fig = go.Figure()
    for col in ['NA_Sales','EU_Sales','JP_Sales','Other_Sales']:
        fig.add_trace(go.Bar(x=rp['Publisher'], y=rp[col],
                              name=REGION_NAMES[col], marker_color=REGION_COLORS[col]))
    fig.update_layout(xaxis_title='Publisher', yaxis_title='Sales (M)',
                      xaxis_tickangle=-45, barmode='stack')
    return _style(fig, "Top Publishers — Sales by Region")


def plot_correlation_heatmap(df):
    nc = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
    corr = df[nc].corr()
    fig = px.imshow(corr, text_auto='.2f', color_continuous_scale='RdBu_r', aspect='auto')
    fig.update_traces(textfont=dict(size=12, family='Inter, sans-serif'), xgap=3, ygap=3)
    return _style(fig, "Correlation Heatmap — Sales Columns")


# ----------------------------------------------------------
# Build Dashboard
# ----------------------------------------------------------
def build_dashboard():
    df_raw, loaded_from_url = load_data()
    df_raw_orig, df_clean = preprocess_data(df_raw)

    # ─── SIDEBAR ───
    st.sidebar.markdown("""
    <div class="sb-logo">
        <span class="sb-logo-icon">🎮</span>
        <span class="sb-logo-text">GamePulse</span>
        <span class="sb-logo-sub">Analytics Dashboard</span>
    </div>
    <hr class="sb-div"/>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<span class="sb-sec"> Data Source</span>', unsafe_allow_html=True)
    if loaded_from_url:
        st.sidebar.markdown('<div class="sb-status sb-ok">Live dataset loaded</div>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<div class="sb-status sb-syn">Synthetic data</div>', unsafe_allow_html=True)

    st.sidebar.markdown('<hr class="sb-div"/>', unsafe_allow_html=True)
    st.sidebar.markdown('<span class="sb-sec">Filters</span>', unsafe_allow_html=True)

    all_platforms = sorted(df_clean['Platform'].unique().tolist())
    selected_platforms = st.sidebar.multiselect("Platforms", all_platforms, default=all_platforms[:5])

    all_genres = sorted(df_clean['Genre'].unique().tolist())
    selected_genres = st.sidebar.multiselect("Genres", all_genres, default=all_genres)

    min_year, max_year = int(df_clean['Year'].min()), int(df_clean['Year'].max())
    year_range = st.sidebar.slider("Year Range", min_year, max_year, (2000, 2015))

    df_filtered = df_clean[
        (df_clean['Platform'].isin(selected_platforms)) &
        (df_clean['Genre'].isin(selected_genres)) &
        (df_clean['Year'] >= year_range[0]) &
        (df_clean['Year'] <= year_range[1])
    ]

    st.sidebar.markdown('<hr class="sb-div"/>', unsafe_allow_html=True)
    st.sidebar.markdown('<span class="sb-sec">Dataset</span>', unsafe_allow_html=True)
    st.sidebar.markdown(f"""
    <div class="sb-row"><span>Raw rows</span><span class="sb-val">{len(df_raw_orig):,}</span></div>
    <div class="sb-row"><span>Cleaned</span><span class="sb-val">{len(df_clean):,}</span></div>
    <div class="sb-row"><span>Filtered</span><span class="sb-val">{len(df_filtered):,}</span></div>
    <div class="sb-row"><span>Columns</span><span class="sb-val">{df_clean.shape[1]}</span></div>
    """, unsafe_allow_html=True)

    # ─── HERO ───
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-orb hero-orb-1"></div>
        <div class="hero-orb hero-orb-2"></div>
        <div class="hero-orb hero-orb-3"></div>
        <div style="position:relative;z-index:2;">
            <div class="hero-badge">Analytics Dashboard</div>
            <h1 class="hero-title">Video Game Sales<br/>Dashboard</h1>
            <p class="hero-sub">An interactive analysis of global video game sales data spanning four decades</p>
            <p class="hero-desc">Explore trends, discover insights, and analyze the gaming industry through rich visualizations</p>
            <div class="hero-pills">
                <span class="hero-pill">16K+ Games</span>
                <span class="hero-pill">40+ Years</span>
                <span class="hero-pill">4 Regions</span>
                <span class="hero-pill">12 Genres</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── KPI ───
    create_kpi_cards(df_filtered)

    # ─── TABS ───
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Overview","Sales Analysis","Platforms & Genres","Publishers","Data Quality"]
    )

    with tab1:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Dataset Overview</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_sales_distribution(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_genre_counts(df_filtered), use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_regional_market_share(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_games_per_year(df_filtered), use_container_width=True)
        st.markdown('<div class="insight-box"><strong>Insight:</strong> Most games have very low sales, while a few blockbuster titles dominate the market. Action and Sports genres lead in number of titles.</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Sales Analysis</div>', unsafe_allow_html=True)
        st.plotly_chart(plot_top10_games(df_filtered), use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_sales_over_years(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_best_year(df_filtered), use_container_width=True)
        st.plotly_chart(plot_regional_trends(df_filtered), use_container_width=True)
        st.markdown('<div class="insight-box"><strong>Insight:</strong> The gaming industry peaked around 2008-2009. North America is the largest market contributing roughly 45% of global sales.</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Platforms & Genres</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_platform_sales(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_genre_avg_sales(df_filtered), use_container_width=True)
        st.plotly_chart(plot_genre_by_platform(df_filtered), use_container_width=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_platform_decade(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_avg_sales_by_genre(df_filtered), use_container_width=True)
        st.markdown('<div class="insight-box"><strong>Insight:</strong> PS2 leads in total sales. Platform games tend to have the highest average sales. Each generation of consoles brings new market leaders.</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Publisher Analysis</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(plot_publisher_titles(df_filtered), use_container_width=True)
        with c2:
            st.plotly_chart(plot_publisher_by_region(df_filtered), use_container_width=True)
        st.markdown('<div class="insight-box"><strong>Insight:</strong> Nintendo, Electronic Arts, and Activision are the top publishers. Nintendo dominates in global sales while EA leads in number of titles.</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="sec-hd"><span class="sec-ic"></span> Data Quality Report</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Raw Data Sample")
            st.dataframe(df_raw_orig.head(10), use_container_width=True)
            st.write(f"**Shape**: {df_raw_orig.shape}")
        with c2:
            st.subheader("Cleaned Data Sample")
            st.dataframe(df_clean.head(10), use_container_width=True)
            st.write(f"**Shape**: {df_clean.shape}")

        st.markdown("---")
        st.subheader("Missing Values Summary")
        missing_raw = df_raw_orig.isnull().sum()
        missing_raw = missing_raw[missing_raw > 0]
        if len(missing_raw) > 0:
            fig_m = px.bar(x=missing_raw.index, y=missing_raw.values,
                           labels={'x':'Column','y':'Missing Count'},
                           color=missing_raw.values,
                           color_continuous_scale=["#1a0a0a","#5a2020","#f87171"])
            fig_m.update_layout(coloraxis_showscale=False)
            st.plotly_chart(_style(fig_m, "Missing Values by Column (Raw Data)"), use_container_width=True)
        else:
            st.info("No missing values found in the raw data.")

        st.markdown("---")
        st.subheader("Correlation Heatmap")
        st.plotly_chart(plot_correlation_heatmap(df_filtered), use_container_width=True)

        st.markdown("---")
        st.subheader("Data Statistics")
        st.dataframe(df_filtered.describe(), use_container_width=True)

    # ─── FOOTER ───
    st.markdown("""
    <div class="footer-wrap">
        <p class="ft-line">Video Game Sales Dashboard — Data Science Course Project</p>
        <p class="ft-line" style="margin-bottom:0.3rem;">Crafted with care for data-driven insights</p>
        <span class="ft-tech">Streamlit</span>
        <span class="ft-tech">Plotly</span>
        <span class="ft-tech">Pandas</span>
        <span class="ft-tech">Python</span>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    build_dashboard()