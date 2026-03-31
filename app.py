import numpy as np
import matplotlib.pyplot as plt

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
    
    # Total Users using Logistic Growth
    users = logistic_growth(t, K, U0, r)
    
    # Active Users
    active_users = users * p
    
    # Daily Check-ins
    checkins = active_users * c
    
    # Peak Time Distribution
    morning = checkins * 0.4
    afternoon = checkins * 0.25
    evening = checkins * 0.35
    
    return t, users, active_users, checkins, morning, afternoon, evening


# -----------------------------
# Scenario 1
# -----------------------------
t1, users1, active1, check1, m1, a1, e1 = simulate(
    K=10000,     # Maximum users
    U0=500,      # Initial users
    r=0.1,       # Growth rate
    p=0.6,       # Active percentage
    c=2,         # Check-ins per active user
    days=60
)

# -----------------------------
# Scenario 2 (Higher Growth Rate)
# -----------------------------
t2, users2, active2, check2, m2, a2, e2 = simulate(
    K=10000,
    U0=500,
    r=0.2,
    p=0.6,
    c=2,
    days=60
)

# -----------------------------
# Print Final Results
# -----------------------------
print("------ Scenario 1 ------")
print("Final Users:", round(users1[-1], 2))
print("Final Daily Check-ins:", round(check1[-1], 2))

print("\n------ Scenario 2 ------")
print("Final Users:", round(users2[-1], 2))
print("Final Daily Check-ins:", round(check2[-1], 2))


# -----------------------------
# Plot 1: User Growth (Scenario 1)
# -----------------------------
plt.figure()
plt.plot(t1, users1)
plt.title("User Growth (Scenario 1)")
plt.xlabel("Days")
plt.ylabel("Total Users")
plt.show()


# -----------------------------
# Plot 2: Daily Check-ins (Scenario 1)
# -----------------------------
plt.figure()
plt.plot(t1, check1)
plt.title("Daily Check-ins (Scenario 1)")
plt.xlabel("Days")
plt.ylabel("Check-ins")
plt.show()


# -----------------------------
# Plot 3: Growth Comparison
# -----------------------------
plt.figure()
plt.plot(t1, users1)
plt.plot(t2, users2)
plt.title("User Growth Comparison (r=0.1 vs r=0.2)")
plt.xlabel("Days")
plt.ylabel("Total Users")
plt.show()


# -----------------------------
# Plot 4: Peak Activity (Last Day - Scenario 1)
# -----------------------------
plt.figure()
plt.bar(["Morning", "Afternoon", "Evening"],
        [m1[-1], a1[-1], e1[-1]])
plt.title("Peak Activity Distribution (Last Day - Scenario 1)")
plt.xlabel("Time of Day")
plt.ylabel("Check-ins")
plt.show()