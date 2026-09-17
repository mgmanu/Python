import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="📚 Library Analyzer", page_icon="📚", layout="wide")

# ============================================
# 🎚️ SINGLE SLIDER - BULLETPROOF BACKGROUND!
# ============================================
with st.sidebar:
    st.header("🌙 **Darkness Slider**")
    
    # ONE MAGIC SLIDER
    darkness = st.slider("🖤 Dark Level", 0, 100, 75)
    
    # Data form
    with st.form("add_record"):
        c1, c2 = st.columns(2)
        with c1: book_id = st.text_input("Book ID", "B101"); title = st.text_input("Title", "Python Basics")
        with c2: student_id = st.text_input("Student ID", "S001"); borrow_date = st.date_input("Borrow", value=datetime.now().date())
        return_date = st.date_input("Return", value=None)
        submitted = st.form_submit_button("➕ Add")

# ============================================
# 🔧 BULLETPROOF CSS - 100% WORKING!
# ============================================
dark_value = 255 - (darkness * 2.5)  # 255→0 as slider goes 0→100
bg_color = f"rgb({dark_value//3},{dark_value//4},{dark_value//2})"
accent_color = "#00d4ff"

st.markdown(f"""
<style>
    /*! BULLETPROOF BACKGROUND - WORKS EVERY TIME !*/
    section[data-testid="stAppViewContainer"] {{
        background: {bg_color} !important;
    }}
    
    .main {{
        background: {bg_color} !important;
    }}
    
    /* Sidebar */
    .css-1d391kg, section[data-testid="stSidebar"] {{
        background: {bg_color} !important;
    }}
    
    /* NEW Streamlit selectors (2025) */
    .stApp {{
        background: {bg_color} !important;
    }}
    
    /* Container transparency */
    .block-container {{
        background: transparent !important;
        padding-top: 2rem;
    }}
    
    /* GLOWING ACCENTS */
    .stMetric > label {{
        color: {accent_color} !important;
        font-size: 16px !important;
    }}
    .stMetric > div > div {{
        color: white !important;
        font-size: 24px !important;
    }}
    
    /* Tabs */
    [data-testid="stHorizontalBlock"] div[style*="background"] {{
        background: {accent_color} !important;
        border-radius: 10px !important;
    }}
    
    /* GLASS DATAFRAME */
    .element-container .dataframe {{
        background: rgba(255,255,255,0.1) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    
    /* TITLE GLOW */
    h1 {{
        color: {accent_color} !important;
        text-shadow: 0 0 20px {accent_color};
        font-size: 2.8rem !important;
    }}
    
    /* BUTTONS */
    button {{
        background: linear-gradient(45deg, {accent_color}, #ffffff20) !important;
        border-radius: 20px !important;
        color: white !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }}
</style>
""", unsafe_allow_html=True)

# BIG LIVE PREVIEW (PROOF IT WORKS!)
st.markdown(f"""
<div style='width:100%; height:200px; background: {bg_color}; 
            border-radius:20px; display:flex; align-items:center; justify-content:center;
            color:{accent_color}; font-size:28px; font-weight:bold; 
            box-shadow: 0 10px 40px rgba(0,0,0,0.5); margin:20px 0;'>
    🎚️ Darkness: {darkness}% | {bg_color}
</div>
""", unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center;">📚 Library Book Borrowing Analyzer - Darkness {darkness}%</h1>', unsafe_allow_html=True)

# Data loading
@st.cache_data
def load_sample_data():
    np.random.seed(42); n_records = 200
    dates = pd.date_range('2025-01-01', periods=n_records, freq='2D').strftime('%Y-%m-%d')
    return_dates = [None if np.random.random()<0.3 else 
                   (pd.to_datetime(dates[i]) + timedelta(days=np.random.randint(5,30))).strftime('%Y-%m-%d') 
                   for i in range(n_records)]
    return pd.DataFrame({
        'book_id': np.random.choice(['B101','B102','B103','B104','B105','B106'], n_records),
        'title': np.random.choice(['Python Basics','Data Structures','Electronics','Algorithms','ML Basics','Web Dev'], n_records),
        'student_id': [f'S{i+1:03d}' for i in np.random.randint(0, 100, n_records)],
        'date_borrowed': dates, 'date_returned': return_dates
    })

if 'df' not in st.session_state:
    st.session_state.df = load_sample_data()
df = st.session_state.df.copy()

if submitted:
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([{
        'book_id': book_id, 'title': title, 'student_id': student_id,
        'date_borrowed': str(borrow_date), 'date_returned': str(return_date) if return_date else None
    }])], ignore_index=True)
    st.rerun()

# Metrics + Charts
col1, col2, col3, col4 = st.columns(4)
col1.metric("📊 Total Records", len(df))
col2.metric("📦 Issued", df['date_returned'].isna().sum())
col3.metric("🏆 Top Book", df['book_id'].value_counts().index[0])
col4.metric("👤 Top Student", df['student_id'].value_counts().index[0])

tab1, tab2, tab3 = st.tabs(["📊 Overview", "🏆 Books", "👥 Students"])

with tab1:
    st.dataframe(df.tail(10), width="stretch")
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(8,5), facecolor=bg_color)
        book_counts = df['book_id'].value_counts().head(10)
        sns.barplot(x=book_counts.values, y=book_counts.index, ax=ax, palette='plasma')
        ax.set_title('Top 10 Books', color=accent_color); ax.tick_params(colors='white')
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots(figsize=(8,5), facecolor=bg_color)
        status = df['date_returned'].isna().value_counts()
        plt.pie(status.values, labels=['Returned','Issued'], autopct='%1.1f%%', colors=['#00d4ff','#ff6b6b'])
        plt.title('Status', color=accent_color)
        st.pyplot(fig)

with tab2:
    fig = px.bar(df['book_id'].value_counts().head(10), color_discrete_sequence=['#00d4ff','#ff6b6b'])
    fig.update_layout(paper_bgcolor=bg_color, plot_bgcolor=bg_color, font_color='white', title_font_color=accent_color)
    st.plotly_chart(fig, width="stretch")

with tab3:
    student_counts = df['student_id'].value_counts().head(20)
    student_df = pd.DataFrame({'student': student_counts.index, 'count': student_counts.values})
    fig = px.treemap(student_df, path=['student'], values='count', color_discrete_sequence=['#00d4ff','#ff6b6b'])
    fig.update_layout(paper_bgcolor=bg_color, plot_bgcolor=bg_color, font_color='white', title_font_color=accent_color)
    st.plotly_chart(fig, width="stretch")
