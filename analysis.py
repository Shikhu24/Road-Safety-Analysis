import pandas as pd

file_path = "NCRB_ADSI_2023_Table_1A.2_2.csv"

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nLast 5 rows:")
print(df.tail())
print("\nFirst 15 location rows:")
print(df[["Sl. No.", "State/Ut/"]].head(15).to_string(index=False))

print("\nLast 15 location rows:")
print(df[["Sl. No.", "State/Ut/"]].tail(15).to_string(index=False))
print("\nFirst 30 locations:")
print(df[["Sl. No.", "State/Ut/"]].head(30).to_string(index=False))
print("\nRows around the transition:")
print(df.iloc[24:35][["Sl. No.", "State/Ut/"]].to_string(index=False))
#Identify section total rows
location_col = "State/Ut/"

total_rows = df[
    df[location_col].astype(str).str.strip().str.startswith("Total")
]

print("Section total rows:")
print(total_rows[["Sl. No.", location_col]].to_string(index=False))
#Count rows in the dataset
print("Total rows:", len(df))

# Check each section total
for label in ["Total (States)", "Total (UTs)",
              "Total (All India)", "Total (Cities)"]:
    print(label, "row count:",
        (df["State/Ut/"].astype(str).str.strip() == label).sum())
# Find section boundaries
location_col = "State/Ut/"

for i, location in enumerate(df[location_col].astype(str).str.strip()):
    if location.startswith("Total"):
        print(i, location)

 # Clean location labels
df["State/Ut/"] = df["State/Ut/"].astype(str).str.strip()

# Separate states
states_df = df.iloc[:28].copy()

# Separate Union Territories
uts_df = df.iloc[29:37].copy()

# Separate cities
cities_df = df.iloc[39:92].copy()

print("State rows:", len(states_df))
print("UT rows:", len(uts_df))
print("City rows:", len(cities_df))  

 # Top 10 states by road accident cases
top_states = states_df.sort_values(
    by="Road Accidents - Cases",
    ascending=False
).head(10)

# print("\nTop 10 States by Road Accident Cases:")
# print(
#     top_states[["State/Ut/", "Road Accidents - Cases"]]
#     .to_string(index=False)
# )

# Top 10 states by road accident deaths
top_deaths = states_df.sort_values(
    by="Road Accidents - Died",
    ascending=False
).head(10)

# print("\nTop 10 States by Road Accident Deaths:")
# print(
#     top_deaths[["State/Ut/", "Road Accidents - Died"]]
#     .to_string(index=False)
# )

# Calculate deaths per 100 reported road accident cases
states_df["Deaths per 100 Cases"] = (
    states_df["Road Accidents - Died"]
    / states_df["Road Accidents - Cases"]
) * 100

top_death_ratio = states_df.sort_values(
    by="Deaths per 100 Cases",
    ascending=False
).head(10)

print("\nTop 10 States by Deaths per 100 Road Accident Cases:")
print(
    top_death_ratio[
        ["State/Ut/", "Road Accidents - Cases",
          "Road Accidents - Died", "Deaths per 100 Cases"]
    ].round(2).to_string(index=False)
)

# Top 10 states by road accident injuries
top_injuries = states_df.sort_values(
    by="Road Accidents - Injured",
    ascending=False
).head(10)

print("\nTop 10 States by Road Accident Injuries:")
print(
    top_injuries[
        ["State/Ut/", "Road Accidents - Injured"]
    ].to_string(index=False)
)


# Summary of road accidents by state
state_summary = states_df[
    [
        "State/Ut/",
        "Road Accidents - Cases",
        "Road Accidents - Injured",
        "Road Accidents - Died"
    ]
].copy()

# print("\nRoad Accident Summary by State:")
# print(state_summary.head(10).to_string(index=False))

# Total road accident cases across states
total_cases = states_df["Road Accidents - Cases"].sum()

# print("Total Road Accident Cases in States:", total_cases)


# Total injured people across states
total_injured = states_df["Road Accidents - Injured"].sum()

# Total deaths across states
total_deaths = states_df["Road Accidents - Died"].sum()

# print("Total Injured People in States:", total_injured)
# print("Total Road Accident Deaths in States:", total_deaths)


# Find the All India total row
all_india = df[
    df["State/Ut/"] == "Total (All India)"
]

# print("\nOfficial All India Total:")
# print(
#     all_india[
#         [
#             "State/Ut/",
#             "Road Accidents - Cases",
#             "Road Accidents - Injured",
#             "Road Accidents - Died"
#         ]
#     ].to_string(index=False)
# )


# Find the Union Territories total
total_uts = df[
    df["State/Ut/"] == "Total (UTs)"
]

# print("\nOfficial Union Territories Total:")
# print(
#     total_uts[
#         [
#             "State/Ut/",
#             "Road Accidents - Cases",
#             "Road Accidents - Injured",
#             "Road Accidents - Died"
#         ]
#     ].to_string(index=False)
# )


# Save state summary to a CSV file
state_summary.to_csv(
    "output/state_road_accident_summary.csv",
    index=False
)

# print("State summary saved successfully!")

# import os

# print("CSV file location:")
# print(os.path.abspath("state_road_accident_summary.csv"))


# Save top 10 states by road accident cases
top_states.to_csv(
    "output/top_10_states_by_accidents.csv",
    index=False
)

# print("Top 10 states CSV saved successfully!")


# Save top 10 states by injuries
top_injuries.to_csv(
    "output/top_10_states_by_injuries.csv",
    index=False
)

# Save top 10 states by deaths
top_deaths.to_csv(
    "output/top_10_states_by_deaths.csv",
    index=False
)

import matplotlib.pyplot as plt

# Top 10 states by road accident cases
top_10 = states_df.nlargest(10, "Road Accidents - Cases")

# # Create bar chart
plt.figure(figsize=(10, 6))
plt.barh(
    top_10["State/Ut/"],
    top_10["Road Accidents - Cases"]
)

plt.xlabel("Number of Road Accident Cases")
plt.ylabel("State")
plt.title("Top 10 States by Road Accident Cases (2023)")
plt.gca().invert_yaxis()
plt.tight_layout()

# # Save the graph
plt.savefig("output/top_10_states_by_accidents.png", dpi=300)
plt.show()

# Top 10 states by road accident deaths
top_deaths = states_df.nlargest(10, "Road Accidents - Died")

plt.figure(figsize=(10, 6))
plt.barh(
    top_deaths["State/Ut/"][::-1],
    top_deaths["Road Accidents - Died"][::-1]
)

plt.title("Top 10 States by Road Accident Deaths (2023)")
plt.xlabel("Number of Deaths")
plt.ylabel("State")
plt.tight_layout()

plt.savefig("output/top_10_states_by_deaths.png")
plt.show()


# Top 10 states by road accident injuries
top_injuries = states_df.nlargest(
    10, "Road Accidents - Injured"
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_injuries["State/Ut/"][::-1],
    top_injuries["Road Accidents - Injured"][::-1]
)

plt.title("Top 10 States by Road Accident Injuries (2023)")
plt.xlabel("Number of Injured People")
plt.ylabel("State")
plt.tight_layout()

plt.savefig("output/top_10_states_by_injuries.png")
plt.show()












