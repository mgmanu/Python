import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Library Book Borrowing System",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body { background-color: #f5f9ff; }
.metric-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}
.metric-value {
    font-size: 36px;
    font-weight: bold;
    color: #2563eb;
}
.metric-label {
    font-size: 16px;
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

st.title("Library Book Borrowing System")

FINE_PER_DAY = 5

# ---------------- BOOK DATA (REAL TITLES) ----------------
genres = {
    "Computer Science": [
        "Programming in C", "Python Programming", "Data Structures",
        "Algorithms", "Operating Systems", "DBMS",
        "Computer Networks", "Software Engineering",
        "Cyber Security", "Web Technologies"
    ],
    "Data Science": [
        "Statistics for Data Science", "Data Analysis with Python",
        "Machine Learning Basics", "Data Visualization",
        "Big Data Analytics", "Exploratory Data Analysis",
        "SQL for Data Science", "Time Series Analysis",
        "Business Analytics", "Probability for DS"
    ],
    "Artificial Intelligence": [
        "AI Fundamentals", "Machine Learning",
        "Deep Learning", "Neural Networks",
        "Natural Language Processing", "Computer Vision",
        "Reinforcement Learning", "Expert Systems",
        "AI Ethics", "Robotics"
    ],
    "UPSC": [
        "Indian Polity", "Indian Economy",
        "Indian History", "World History",
        "Indian Geography", "World Geography",
        "Environment Studies", "Ethics GS",
        "Governance", "Current Affairs"
    ],
    "CAT": [
        "Quantitative Aptitude", "Logical Reasoning",
        "Data Interpretation", "Verbal Ability",
        "Arithmetic", "Algebra",
        "Geometry", "Number System",
        "CAT Mock Tests", "CAT Previous Papers"
    ],
    "GATE": [
        "Engineering Mathematics", "Digital Logic",
        "Computer Organization", "Theory of Computation",
        "Compiler Design", "Discrete Mathematics",
        "Signals and Systems", "Control Systems",
        "Electromagnetic Theory", "GATE Previous Papers"
    ],
    "Mathematics": [
        "Calculus", "Linear Algebra",
        "Probability Theory", "Statistics",
        "Numerical Methods", "Vector Algebra",
        "Differential Equations", "Real Analysis",
        "Abstract Algebra", "Graph Theory"
    ],
    "Physics": [
        "Classical Mechanics", "Quantum Mechanics",
        "Thermodynamics", "Electrodynamics",
        "Optics", "Solid State Physics",
        "Nuclear Physics", "Atomic Physics",
        "Physics 11th", "Physics 12th"
    ],
    "Commerce": [
        "Financial Accounting", "Cost Accounting",
        "Business Studies", "Economics",
        "Company Law", "Income Tax",
        "Auditing", "Marketing Management",
        "Human Resource Management", "Banking and Insurance"
    ],
    "Literature": [
        "English Literature", "Indian Literature",
        "World Literature", "Poetry",
        "Drama", "Modern Fiction",
        "Classical Novels", "Short Stories",
        "Literary Criticism", "Creative Writing"
    ]
}

# Create library
library = {}
for genre, books in genres.items():
    for book in books:
        library[book] = {"genre": genre, "copies": 3}

# ---------------- SESSION STATE ----------------
if "library" not in st.session_state:
    st.session_state.library = library.copy()

if "borrowers" not in st.session_state:
    st.session_state.borrowers = pd.DataFrame(
        columns=["Student Name", "Book Title", "Genre",
                 "Borrow Date", "Return Date", "Renewed"]
    )

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Library Inventory", "Borrow Book",
     "Renew Book", "Borrow Records & Fine", "Analytics"]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Books</div>
            <div class="metric-value">{len(st.session_state.library)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Available Copies</div>
            <div class="metric-value">
            {sum(v['copies'] for v in st.session_state.library.values())}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Borrowed Books</div>
            <div class="metric-value">{len(st.session_state.borrowers)}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- INVENTORY ----------------
elif menu == "Library Inventory":
    df = pd.DataFrame(
        [[k, v["genre"], v["copies"]] for k, v in st.session_state.library.items()],
        columns=["Book Title", "Genre", "Available Copies"]
    )
    st.dataframe(df, use_container_width=True)

# ---------------- BORROW BOOK ----------------
elif menu == "Borrow Book":
    student = st.text_input("Student Name")
    book = st.selectbox("Select Book", list(st.session_state.library.keys()))
    borrow_date = st.date_input("Borrow Date", date.today())

    if st.button("Borrow"):
        if student.strip() == "":
            st.error("Student name required")
        elif st.session_state.library[book]["copies"] <= 0:
            st.error("Book not available")
        else:
            return_date = borrow_date + timedelta(days=15)
            st.session_state.library[book]["copies"] -= 1
            st.session_state.borrowers.loc[len(st.session_state.borrowers)] = [
                student, book,
                st.session_state.library[book]["genre"],
                borrow_date, return_date, "No"
            ]
            st.success("Book issued successfully")

# ---------------- RENEW BOOK ----------------
elif menu == "Renew Book":
    if not st.session_state.borrowers.empty:
        idx = st.selectbox("Select Record", st.session_state.borrowers.index)
        if st.button("Renew"):
            st.session_state.borrowers.at[idx, "Return Date"] += timedelta(days=15)
            st.session_state.borrowers.at[idx, "Renewed"] = "Yes"
            st.success("Book renewed")

# ---------------- RECORDS & FINE ----------------
elif menu == "Borrow Records & Fine":
    if not st.session_state.borrowers.empty:
        df = st.session_state.borrowers.copy()
        today = date.today()
        df["Fine Amount"] = df["Return Date"].apply(
            lambda d: max(0, (today - d).days * FINE_PER_DAY)
        )
        st.dataframe(df, use_container_width=True)

# ---------------- ANALYTICS ----------------
elif menu == "Analytics":
    if not st.session_state.borrowers.empty:
        df = st.session_state.borrowers.copy()
        df["Borrow Month"] = pd.to_datetime(df["Borrow Date"]).dt.month
        df["Borrow Duration"] = (
            pd.to_datetime(df["Return Date"]) -
            pd.to_datetime(df["Borrow Date"])
        ).dt.days

        fig1, ax1 = plt.subplots()
        df["Genre"].value_counts().plot(kind="bar", color="#2563eb", ax=ax1)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots()
        df["Borrow Month"].value_counts().sort_index().plot(
            kind="line", marker="o", color="green", ax=ax2
        )
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots()
        ax3.hist(df["Borrow Duration"], bins=10,
                 color="red", edgecolor="black")
        st.pyplot(fig3)
