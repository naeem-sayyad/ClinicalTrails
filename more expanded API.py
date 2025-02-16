import pandas as pd
from pytrials.client import ClinicalTrials

# Initialize ClinicalTrials client
ct = ClinicalTrials()

# Define search expression for Phase 2 & Phase 3 completed trials
search_expression = "(Phase 2 OR Phase 3) AND Completed"

# Valid fields list for ClinicalTrials API (CSV format)
fields = [
    "NCT Number", "Study Title", "Study URL", "Study Status",
    "Brief Summary", "Conditions", "Interventions", "Enrollment",
    "Primary Outcome Measures", "Secondary Outcome Measures", "Other Outcome Measures",
    "Sex", "Age", "Funder Type", "Study Type", "Study Design",
    "Start Date", "Completion Date"
]

max_studies_per_request = 1000  # API limit per request
num_batches = 5  # Fetch 5000 trials in 5 batches

# Empty list to store batch results
all_data = []

for i in range(num_batches):
    offset = i * max_studies_per_request  # Calculate offset for each batch
    study_fields = ct.get_study_fields(
        search_expr=search_expression,
        fields=fields,
        max_studies=max_studies_per_request,
        fmt="csv"
    )

    # Convert batch to DataFrame and store
    batch_df = pd.DataFrame(study_fields[1:], columns=study_fields[0])
    all_data.append(batch_df)

# Concatenate all batches into a single DataFrame
df = pd.concat(all_data, ignore_index=True)

# Save dataset to CSV
df.to_csv("expanded_clinical_trials_v2.csv", index=False)

# Display first few rows
print("Expanded Clinical Trials Dataset:")
print(df.head())