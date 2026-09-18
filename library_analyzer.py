import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime, timedelta


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="📚 Library Analyzer",
    page_icon="📚",
    layout="wide"
)


# ============================================
# 🎚️ SINGLE SLIDER - DARKNESS CONTROL
# ============================================

with st.sidebar:

    st.header("🌙 Darkness Slider")

    darkness = st.slider(
        "🖤 Dark Level",
        0,
        100,
        75
    )

    # ========================================
    # DATA FORM
    # ========================================

    with st.form("add_record"):

        c1, c2 = st.columns(2)

        with c1:
            book_id = st.text_input(
                "Book ID",
                "B101"
            )

            title = st.text_input(
                "Title",
                "Python Basics"
            )

        with c2:
            student_id = st.text_input(
                "Student ID",
                "S001"
            )

            borrow_date = st.date_input(
                "Borrow",
                value=datetime.now().date()
            )

        return_date = st.date_input(
            "Return",
            value=None
        )

        submitted = st.form_submit_button("➕ Add")


# ============================================
# 🎨 BACKGROUND COLOR
# ============================================

dark_value = int(255 - (darkness * 2.5))

# CSS / HTML color
bg_color = (
    f"rgb({dark_value // 3},"
    f"{dark_value // 4},"
    f"{dark_value // 2})"
)

# Matplotlib color
bg_color_mpl = (
    (dark_value // 3) / 255,
    (dark_value // 4) / 255,
    (dark_value // 2) / 255
)

accent_color = "#00d4ff"


# ============================================
# 🔧 CSS
# ============================================

st.markdown(
    f"""
    <style>

    /* ========================================
       BACKGROUND
       ======================================== */

    section[data-testid="stAppViewContainer"] {{
        background: {bg_color} !important;
    }}

    .main {{
        background: {bg_color} !important;
    }}

    section[data-testid="stSidebar"] {{
        background: {bg_color} !important;
    }}

    .stApp {{
        background: {bg_color} !important;
    }}

    .block-container {{
        background: transparent !important;
        padding-top: 2rem;
    }}


    /* ========================================
       METRICS
       ======================================== */

    .stMetric > label {{
        color: {accent_color} !important;
        font-size: 16px !important;
    }}

    .stMetric > div > div {{
        color: white !important;
        font-size: 24px !important;
    }}


    /* ========================================
       DATAFRAME
       ======================================== */

    .element-container .dataframe {{
        background: rgba(255,255,255,0.1) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }}


    /* ========================================
       TITLE
       ======================================== */

    h1 {{
        color: {accent_color} !important;
        text-shadow: 0 0 20px {accent_color};
        font-size: 2.8rem !important;
    }}


    /* ========================================
       BUTTONS
       ======================================== */

    button {{
        background: linear-gradient(
            45deg,
            {accent_color},
            #ffffff20
        ) !important;

        border-radius: 20px !important;
        color: white !important;
        font-weight: bold !important;

        box-shadow:
            0 4px 15px rgba(0,0,0,0.3) !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================
# 🎚️ LIVE DARKNESS PREVIEW
# ============================================

st.markdown(
    f"""
    <div style="
        width:100%;
        height:200px;
        background:{bg_color};
        border-radius:20px;
        display:flex;
        align-items:center;
        justify-content:center;
        color:{accent_color};
        font-size:28px;
        font-weight:bold;
        box-shadow:0 10px 40px rgba(0,0,0,0.5);
        margin:20px 0;
    ">

        🎚️ Darkness: {darkness}% | {bg_color}

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================
# 📚 MAIN TITLE
# ============================================

st.markdown(
    f"""
    <h1 style="text-align:center;">
        📚 Library Book Borrowing Analyzer
        - Darkness {darkness}%
    </h1>
    """,
    unsafe_allow_html=True
)


# ============================================
# 📊 DATA LOADING
# ============================================

@st.cache_data
def load_sample_data():

    np.random.seed(42)

    n_records = 200

    dates = pd.date_range(
        "2025-01-01",
        periods=n_records,
        freq="2D"
    ).strftime("%Y-%m-%d")

    return_dates = [
        None
        if np.random.random() < 0.3
        else (
            pd.to_datetime(dates[i])
            + timedelta(days=np.random.randint(5, 30))
        ).strftime("%Y-%m-%d")

        for i in range(n_records)
    ]

    return pd.DataFrame(
        {
            "book_id": np.random.choice(
                [
                    "B101",
                    "B102",
                    "B103",
                    "B104",
                    "B105",
                    "B106"
                ],
                n_records
            ),

            "title": np.random.choice(
                [
                    "Python Basics",
                    "Data Structures",
                    "Electronics",
                    "Algorithms",
                    "ML Basics",
                    "Web Dev"
                ],
                n_records
            ),

            "student_id": [
                f"S{i + 1:03d}"
                for i in np.random.randint(
                    0,
                    100,
                    n_records
                )
            ],

            "date_borrowed": dates,

            "date_returned": return_dates
        }
    )


# ============================================
# SESSION STATE
# ============================================

if "df" not in st.session_state:

    st.session_state.df = load_sample_data()


df = st.session_state.df.copy()


# ============================================
# ➕ ADD NEW RECORD
# ============================================

if submitted:

    new_record = pd.DataFrame(
        [
            {
                "book_id": book_id,
                "title": title,
                "student_id": student_id,
                "date_borrowed": str(borrow_date),
                "date_returned": (
                    str(return_date)
                    if return_date
                    else None
                )
            }
        ]
    )

    st.session_state.df = pd.concat(
        [
            st.session_state.df,
            new_record
        ],
        ignore_index=True
    )

    st.rerun()


# ============================================
# 📊 METRICS
# ============================================

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "📊 Total Records",
    len(df)
)


col2.metric(
    "📦 Issued",
    df["date_returned"].isna().sum()
)


col3.metric(
    "🏆 Top Book",
    df["book_id"].value_counts().index[0]
)


col4.metric(
    "👤 Top Student",
    df["student_id"].value_counts().index[0]
)


# ============================================
# 📑 TABS
# ============================================

tab1, tab2, tab3 = st.tabs(
    [
        "📊 Overview",
        "🏆 Books",
        "👥 Students"
    ]
)


# ============================================
# 📊 TAB 1 - OVERVIEW
# ============================================

with tab1:

    st.dataframe(
        df.tail(10),
        width="stretch"
    )


    col1, col2 = st.columns(2)


    # ========================================
    # 📚 TOP BOOKS BAR CHART
    # ========================================

    with col1:

        fig, ax = plt.subplots(
            figsize=(8, 5),
            facecolor=bg_color_mpl
        )

        book_counts = (
            df["book_id"]
            .value_counts()
            .head(10)
        )

        sns.barplot(
            x=book_counts.values,
            y=book_counts.index,
            ax=ax,
            palette="plasma",
            hue=book_counts.index,
            legend=False
        )

        ax.set_title(
            "Top 10 Books",
            color=accent_color
        )

        ax.tick_params(
            colors="white"
        )

        ax.set_facecolor(
            bg_color_mpl
        )

        for spine in ax.spines.values():
            spine.set_color("white")

        st.pyplot(fig)


    # ========================================
    # 📦 STATUS PIE CHART
    # ========================================

    with col2:

        fig, ax = plt.subplots(
            figsize=(8, 5),
            facecolor=bg_color_mpl
        )

        status = (
            df["date_returned"]
            .isna()
            .value_counts()
        )

        # False = Returned
        # True = Issued

        returned = status.get(False, 0)
        issued = status.get(True, 0)

        ax.pie(
            [returned, issued],
            labels=["Returned", "Issued"],
            autopct="%1.1f%%",
            colors=[
                "#00d4ff",
                "#ff6b6b"
            ]
        )

        ax.set_title(
            "Status",
            color=accent_color
        )

        st.pyplot(fig)


# ============================================
# 🏆 TAB 2 - BOOKS
# ============================================

with tab2:

    book_counts = (
        df["book_id"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        book_counts,
        color_discrete_sequence=[
            "#00d4ff",
            "#ff6b6b"
        ]
    )

    fig.update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font_color="white",
        title_font_color=accent_color
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ============================================
# 👥 TAB 3 - STUDENTS
# ============================================

with tab3:

    student_counts = (
        df["student_id"]
        .value_counts()
        .head(20)
    )

    student_df = pd.DataFrame(
        {
            "student": student_counts.index,
            "count": student_counts.values
        }
    )


    fig = px.treemap(
        student_df,
        path=["student"],
        values="count",
        color_discrete_sequence=[
            "#00d4ff",
            "#ff6b6b"
        ]
    )


    fig.update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font_color="white",
        title_font_color=accent_color
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )