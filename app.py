import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Medical App Daily Check-ins",
    layout="wide"
)

# -----------------------------
# Title & Description
# -----------------------------
st.title("🏥 Medical App Daily Check-ins Dashboard")

st.markdown("""
This application predicts **daily usage of a health monitoring app** using:

- 📈 Logistic Growth Model  
- 👥 Active User Analysis  
- 🔍 Sensitivity Analysis  
- ⏰ Peak Activity Distribution  

It helps understand how users interact with a medical app over time.
""")

# -----------------------------
# Input Section (NO SLIDERS)
# -----------------------------
st.header("🔧 Enter Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    K = st.number_input("Maximum Users (K)", value=10000)
    U0 = st.number_input("Initial Users (U0)", value=500)

with col2:
    r = st.number_input("Growth Rate (r)", value=0.1, format="%.2f")
    p = st.number_input("Active User % (p)", value=0.6, format="%.2f")

with col3:
    c = st.number_input("Check-ins per User (c)", value=2)
    days = st.number_input("Number of Days", value=60)

# -----------------------------
# Logistic Growth Function
# -----------------------------
def logistic_growth(t, K, U0, r):
    return K / (1 + ((K - U0) / U0) * np.exp(-r * t))

# -----------------------------
# Simulation Function
# -----------------------------
def simulate(K, U0, r, p, c, days):
    t = np.arange(0, days)
    
    users = logistic_growth(t, K, U0, r)
    active_users = users * p
    checkins = active_users * c
    
    morning = checkins * 0.4
    afternoon = checkins * 0.25
    evening = checkins * 0.35
    
    return t, users, active_users, checkins, morning, afternoon, evening

# -----------------------------
# Run Simulation Button
# -----------------------------
if st.button("🚀 Run Simulation"):

    # Scenario 1
    t1, users1, active1, check1, m1, a1, e1 = simulate(K, U0, r, p, c, days)

    # Scenario 2 (Sensitivity Analysis)
    r2 = r * 2
    t2, users2, active2, check2, m2, a2, e2 = simulate(K, U0, r2, p, c, days)

    # -----------------------------
    # Key Metrics
    # -----------------------------
    st.header("📊 Key Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Final Users", f"{int(users1[-1])}")
        st.metric("Final Daily Check-ins", f"{int(check1[-1])}")

    with col2:
        st.metric("Growth Rate Used", r)
        st.metric("Higher Growth Scenario (r × 2)", round(r2, 2))

    # -----------------------------
    # Plot 1: User Growth
    # -----------------------------
    st.subheader("📈 User Growth Over Time")

    fig1, ax1 = plt.subplots()
    ax1.plot(t1, users1, label="Base Growth")
    ax1.plot(t2, users2, linestyle='--', label="Higher Growth")
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Users")
    ax1.legend()
    st.pyplot(fig1)

    # -----------------------------
    # Plot 2: Daily Check-ins
    # -----------------------------
    st.subheader("📊 Daily Check-ins")

    fig2, ax2 = plt.subplots()
    ax2.plot(t1, check1)
    ax2.set_xlabel("Days")
    ax2.set_ylabel("Check-ins")
    st.pyplot(fig2)

    # -----------------------------
    # Plot 3: Peak Activity
    # -----------------------------
    st.subheader("⏰ Peak Activity Distribution (Last Day)")

    fig3, ax3 = plt.subplots()
    ax3.bar(
        ["Morning", "Afternoon", "Evening"],
        [m1[-1], a1[-1], e1[-1]]
    )
    st.pyplot(fig3)

    # -----------------------------
    # Explanation Section
    # -----------------------------
    st.header("🧠 Interpretation")

    st.markdown(f"""
    ### 📌 What This Means:

    - The app is expected to reach **{int(users1[-1])} users** in {days} days.
    - Around **{int(check1[-1])} daily check-ins** indicate strong engagement.
    - Increasing growth rate significantly boosts adoption (see dashed line).
    - Peak usage occurs mostly during:
        - 🌅 Morning (40%)
        - 🌇 Evening (35%)
        - ☀️ Afternoon (25%)

    ### 💡 Business Insight:
    - Focus notifications in **morning & evening**
    - Improve onboarding to increase growth rate
    - Boost engagement to increase active user %

    This model helps in **planning infrastructure, marketing strategy, and feature optimization**.
    """)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Developed for 📊 Data Science Project | Medical App Analytics")