import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


st.set_page_config(page_title="Medical APP Growth Simulator", layout="wide")


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


def plot_line(x, y1, y2=None, title="", ylabel="", label1="Scenario 1", label2="Scenario 2"):
    fig, ax = plt.subplots()
    ax.plot(x, y1, linewidth=2, label=label1)
    if y2 is not None:
        ax.plot(x, y2, linewidth=2, label=label2)
        ax.legend()
    ax.set_title(title)
    ax.set_xlabel("Days")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    return fig


def plot_bar(values, title=""):
    fig, ax = plt.subplots()
    ax.bar(["Morning", "Afternoon", "Evening"], values, color=["#60a5fa", "#fbbf24", "#34d399"])
    ax.set_title(title)
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Check-ins")
    return fig


def main():
    st.title("📈 User Growth & Check-in Simulator")
    st.write("Adjust the parameters in the sidebar to explore user growth, activity, and daily check-ins.")

    st.sidebar.header("Simulation Controls")
    K = st.sidebar.slider("Maximum users (K)", 1000, 50000, 10000, 500)
    U0 = st.sidebar.slider("Initial users (U0)", 10, 5000, 500, 10)
    p = st.sidebar.slider("Active user percentage", 0.1, 1.0, 0.6, 0.05)
    c = st.sidebar.slider("Check-ins per active user", 0.5, 10.0, 2.0, 0.5)
    days = st.sidebar.slider("Simulation days", 7, 365, 60, 1)
    r1 = st.sidebar.slider("Scenario 1 growth rate", 0.01, 1.0, 0.10, 0.01)
    r2 = st.sidebar.slider("Scenario 2 growth rate", 0.01, 1.0, 0.20, 0.01)

    t1, users1, active1, check1, m1, a1, e1 = simulate(K=K, U0=U0, r=r1, p=p, c=c, days=days)
    t2, users2, active2, check2, m2, a2, e2 = simulate(K=K, U0=U0, r=r2, p=p, c=c, days=days)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Scenario 1 Final Users", f"{users1[-1]:,.0f}")
    col2.metric("Scenario 1 Daily Check-ins", f"{check1[-1]:,.0f}")
    col3.metric("Scenario 2 Final Users", f"{users2[-1]:,.0f}")
    col4.metric("Scenario 2 Daily Check-ins", f"{check2[-1]:,.0f}")

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.pyplot(plot_line(t1, users1, title="User Growth (Scenario 1)", ylabel="Total Users"), clear_figure=True)
        st.pyplot(plot_line(t1, check1, title="Daily Check-ins (Scenario 1)", ylabel="Check-ins"), clear_figure=True)

    with chart_col2:
        st.pyplot(
            plot_line(
                t1,
                users1,
                y2=users2,
                title=f"Growth Comparison (r={r1:.2f} vs r={r2:.2f})",
                ylabel="Total Users",
            ),
            clear_figure=True,
        )
        st.pyplot(
            plot_bar([m1[-1], a1[-1], e1[-1]], title="Peak Activity Distribution (Last Day - Scenario 1)"),
            clear_figure=True,
        )

    st.subheader("Summary")
    st.write(
        f"Over **{days} days**, Scenario 2 reaches **{users2[-1]:,.0f} users**, compared with "
        f"**{users1[-1]:,.0f} users** in Scenario 1."
    )


if __name__ == "__main__":
    main()