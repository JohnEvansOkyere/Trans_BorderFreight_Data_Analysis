# North American Freight Data Analysis

## Project Overview
This project provides a comprehensive, data-driven analysis of North American transborder freight, focusing on identifying inefficiencies, understanding movement patterns, and supporting actionable recommendations for the Bureau of Transportation Statistics (BTS) and other stakeholders. The analysis leverages multi-year, multi-country freight data, fully mapped to human-readable formats for clarity and transparency.

## Objectives
- Identify dominant freight movement patterns across modes, regions, and time.
- Assess operational efficiency and highlight cost/weight inefficiencies.
- Evaluate environmental impact by mode and region.
- Analyze cross-border trade between the US, Mexico, and Canada.
- Uncover seasonal trends and economic disruption impacts.
- Assess infrastructure utilization and containerization efficiency.
- Provide actionable recommendations and professional visualizations.

## Data Sources
- **Raw Data:** CSV files for each month/year, stored in `data/`.
- **Codebook:** `codes-north-american-transborder-freight-raw-data.pdf` for mapping coded columns to human-readable values.
- **Processed Data:** Cleaned, merged, mapped, and enriched CSVs in `worked_data/` and `notebooks/worked_data/`.

## Project Structure
```
Freight_Data_Analysis/
├── data/                  # Raw data and codebook
├── preprocess/            # Data cleaning, merging, mapping scripts
├── notebooks/             # Jupyter notebooks for EDA and analysis
├── worked_data/           # Processed and mapped data outputs
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Workflow & Process

### 1. Data Preprocessing
- **Merging:** All monthly CSVs are merged by year and mode using `preprocess/freight_merged_data.py` and `preprocess/combining.py`.
- **Cleaning:** Standardizes column names, handles missing values, and logs issues.
- **Mapping:** All coded columns (e.g., state, country, mode, port) are mapped to human-readable values using `preprocess/renaming.py` and the provided codebook.
- **Enrichment:** Both cleaned and enriched (original + mapped columns) datasets are saved for transparency.

### 2. Mapped-Only Data Creation
- **Mapped-Only Files:** `preprocess/keep_mapped_only.py` drops all original coded columns, retaining only mapped (human-readable) columns and key numeric fields.
- **Output:** Files like `dot1_all_mapped_only.csv`, `dot2_all_mapped_only.csv`, and `dot3_all_mapped_only.csv` in `worked_data/`.

### 3. Exploratory Data Analysis (EDA)
- **Notebook:** The main EDA is performed in a Jupyter notebook (e.g., `freight_insight.ipynb`).
- **Analysis Includes:**
  - Freight movement patterns by mode, region, and time
  - Operational efficiency (cost per weight, route analysis)
  - Environmental impact (weight by mode/region)
  - Cross-border trade flows
  - Seasonal trends in movement and cost
  - Economic disruption impact (correlation of value and movement)
  - Infrastructure utilization (ports/districts)
  - Containerization efficiency
- **Professional Visualizations:** All insights are supported by clear, stakeholder-ready charts and tables.

### 4. Recommendations & Reporting
- **Actionable Recommendations:** Top inefficiencies and improvement opportunities are highlighted.
- **Documentation:** All steps, code, and methodology are fully documented for reproducibility.

## Usage Instructions

### Environment Setup
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Data Processing
1. Run preprocessing scripts in order:
   - `python preprocess/freight_merged_data.py`
   - `python preprocess/combining.py`
   - `python preprocess/renaming.py`
   - `python preprocess/keep_mapped_only.py`
2. Check `worked_data/` and `notebooks/worked_data/` for output files.

### Analysis
1. Open the main EDA notebook (e.g., `notebooks/freight_insight.ipynb`) in JupyterLab or Jupyter Notebook.
2. Run all cells to reproduce the analysis and visualizations.
3. Review the markdown commentary for business context and actionable insights.

## Recommendations for Future Work
- Integrate external economic indicators (e.g., GDP, fuel prices) for deeper disruption analysis.
- Automate mapping updates if new codes are introduced in future data.
- Explore advanced analytics (forecasting, optimization) for predictive insights.
- Develop dashboards for real-time monitoring and stakeholder reporting.

## Contact
For questions, suggestions, or collaboration, please contact the project maintainer or open an issue in the repository.

---
*Prepared with a commitment to clarity, rigor, and stakeholder value by a professional data analyst with 10 years of experience.* 