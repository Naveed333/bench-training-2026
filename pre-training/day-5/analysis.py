import pandas as pd
import os

# Load the dataset
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "titanic.csv"))

print("=" * 55)
print("        TITANIC DATASET ANALYSIS")
print("=" * 55)

# ── Q1: Survived vs didn't survive --────────────────────────
print("\nQ1. Survived vs. Did Not Survive")
print("-" * 40)
counts = df["Survived"].value_counts()
print(f"   counts value is. ::: : {counts[1]}")  # Debug statement to check counts
total = len(df)
for val, label in [(1, "Survived"), (0, "Did Not Survive")]:
    print(f"  {label:<18}: {counts[val]:>4}  ({counts[val]/total*100:.1f}%)")

# ── Q2: Survival rate by passenger class ────────────────────
print("\nQ2. Survival Rate by Passenger Class")
print("-" * 40)
by_class = df.groupby("Pclass")["Survived"].mean() * 100
for pclass, rate in by_class.items():# item breaks a dictionary into list of (key, value) pairs
    label = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}[pclass] # replacing if else
    print(f"  {label}: {rate:.1f}%")

# ── Q3: Average age of survivors vs non-survivors ───────────
print("\nQ3. Average Age: Survivors vs. Non-Survivors")
print("-" * 40)
avg_age = df.groupby("Survived")["Age"].mean()
print(f"  Survivors     : {avg_age[1]:.1f} years")
print(f"  Non-Survivors : {avg_age[0]:.1f} years")

# ── Q4: Embarkation port with highest survival rate ─────────
print("\nQ4. Survival Rate by Embarkation Port")
print("-" * 40)
port_map = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
by_port = df.groupby("Embarked")["Survived"].mean() * 100
for port, rate in by_port.sort_values(ascending=False).items():
    print(f"  {port_map.get(port, port):<14}: {rate:.1f}%")
best_port = by_port.idxmax()
print(f"  Highest: {port_map.get(best_port, best_port)}")

# ── Q5: Missing ages → fill with median per class ───────────
print("\nQ5. Missing Age Values")
print("-" * 40)
missing_before = df["Age"].isna().sum()
print(f"  Missing age values: {missing_before}")
# Fill missing Age with median age of the passenger's class
df["Age"] = df.groupby("Pclass")["Age"].transform(
    lambda x: x.fillna(x.median())
)
missing_after = df["Age"].isna().sum()
print(f"  After filling with class median: {missing_after} missing")

# ── Q6: Oldest surviving passenger ──────────────────────────
print("\nQ6. Oldest Surviving Passenger")
print("-" * 40)
oldest = df[df["Survived"] == 1].sort_values("Age", ascending=False).iloc[0]
print(f"  Name  : {oldest['Name']}")
print(f"  Age   : {oldest['Age']:.0f}")
print(f"  Class : {oldest['Pclass']}")

# ── Q7: Survival rate by gender ─────────────────────────────
print("\nQ7. Survival Rate by Gender")
print("-" * 40)
by_sex = df.groupby("Sex")["Survived"].mean() * 100
print(f"  Women : {by_sex['female']:.1f}%")
print(f"  Men   : {by_sex['male']:.1f}%")

# ── Q8: AgeGroup column + survival rate per group ───────────
print("\nQ8. Survival Rate by Age Group")
print("-" * 40)
def age_group(age):
    if age < 18:
        return "Child (<18)"
    elif age <= 60:
        return "Adult (18-60)"
    else:
        return "Senior (60+)"

df["AgeGroup"] = df["Age"].apply(age_group)
by_group = df.groupby("AgeGroup")["Survived"].mean() * 100
for group in ["Child (<18)", "Adult (18-60)", "Senior (60+)"]:
    print(f"  {group:<16}: {by_group[group]:.1f}%")

# ── Q9: 3rd class survival rate by gender ───────────────────
print("\nQ9. 3rd Class: Survival Rate by Gender")
print("-" * 40)
third_class = df[df["Pclass"] == 3]
third_by_sex = third_class.groupby("Sex")["Survived"].mean() * 100
print(f"  Women : {third_by_sex['female']:.1f}%")
print(f"  Men   : {third_by_sex['male']:.1f}%")

# ── Q10: Drop rows with missing Cabin ───────────────────────
print("\nQ10. Rows Remaining After Dropping Missing Cabin")
print("-" * 40)
original_count = len(df)
df_cabin = df.dropna(subset=["Cabin"])
remaining = len(df_cabin)
pct_kept = remaining / original_count * 100
print(f"  Original rows : {original_count}")
print(f"  Rows remaining: {remaining}")
print(f"  % of data kept: {pct_kept:.1f}%")

