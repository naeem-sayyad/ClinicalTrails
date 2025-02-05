from pytrials.client import ClinicalTrials
import pandas as pd

# Initialize ClinicalTrials client
ct = ClinicalTrials()

# Define search parameters
search_expression = "Phase 3 AND Completed"

# Use only valid CSV fields
fields = [
    "NCT Number",       # Unique Identifier
    "Study Title",      # Title of the study
    "Study URL",        # Link to ClinicalTrials.gov
    "Study Status",     # Overall status (Completed, Recruiting, etc.)
    "Conditions",       # Disease or condition studied
    "Interventions",    # Treatment or intervention type
    "Phases",           # Phase of the trial
    "Enrollment",       # Number of participants
    "Start Date",       # When the study began
    "Completion Date"   # When the study was completed
]

max_studies = 500  # Fetch up to 500 studies

# Fetch study data
study_fields = ct.get_study_fields(
    search_expr=search_expression,
    fields=fields,
    max_studies=max_studies,
    fmt="csv"
)

# Convert to DataFrame
df = pd.DataFrame(study_fields[1:], columns=study_fields[0])

# Display first few rows
print(df.head())

# Save to CSV for further analysis
df.to_csv("clinical_trials_data.csv", index=False)
print("Clinical trials data saved to 'clinical_trials_data.csv'")
