# India Road Safety Analysis — 2023

## Project Overview

This project analyzes road accident data in India for 2023 using Python and Pandas. The aim is to explore differences in reported road accident cases, injuries, and deaths across Indian states.

## Objectives

* Identify states with the highest number of reported road accident cases.
* Compare states by reported injuries and deaths.
* Summarize state-level road accident statistics.
* Validate state totals against the official All India total.
* Prepare CSV outputs for further analysis and visualization in Power BI.

## Dataset

* **Source:** Government of India, data.gov.in
* **Dataset file:** `NCRB_ADSI_2023_Table_1A.2_2.csv`
* **Year:** 2023
* **Data fields used:** State/UT, road accident cases, injured people, and deaths.

The analysis separates state-level records from Union Territory, All India, and city summary rows.

## Tools and Technologies

* Python
* Pandas
* CSV data files
* Matplotlib

## Analysis Performed

* Selected state-level records from the original dataset.
* Ranked states by reported road accident cases, injuries, and deaths.
* Calculated a descriptive ratio of deaths to reported road accident cases.
* Compared state totals with the official All India total.
* Exported summary tables to CSV files.

## Key Findings

* Tamil Nadu had the highest reported road accident case count among the states in this dataset.
* Uttar Pradesh had the highest reported road accident deaths among the states.
* Tamil Nadu had the highest reported number of injured people among the states.
* State totals plus Union Territory totals matched the official All India totals for cases, injuries, and deaths.

These findings describe reported counts. They do not, by themselves, establish which state is safest or most dangerous because population, traffic exposure, and other factors are not accounted for.

## Output Files

* `outputs/state_road_accident_summary.csv`
* `outputs/top_10_states_by_accidents.csv`
* `outputs/top_10_states_by_injuries.csv`
* `outputs/top_10_states_by_deaths.csv`

## Future Improvements

* Explore city-level accident patterns and additional road safety indicators.
* Improve data visualizations and add more insights using Python.

## Disclaimer

This project is for educational and analytical purposes. Findings depend on the definitions and coverage of the original dataset.

## DATA SOURCE
https://ap.data.gov.in/resource/stateutcity-wise-number-cases-reported-and-persons-injured-and-died-due-traffic-accidents

## Graphs

* `output/top_10_states_by_accidents.png` — Top 10 states by reported road accident cases.
* `output/top_10_states_by_deaths.png` — Top 10 states by reported road accident deaths.
* `output/top_10_states_by_injuries.png` — Top 10 states by reported injuries.
