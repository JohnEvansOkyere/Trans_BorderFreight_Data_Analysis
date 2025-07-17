# North American Freight Data Analysis


Certainly! Here’s a concise, stakeholder-friendly methodology section you can use in your documentation or reporting:

---

## Methodology for Reproducibility

To ensure transparency and reproducibility, our analysis followed a clear, step-by-step methodology:

### 1. **Data Collection**
- Gathered raw monthly freight data (2020–2024) from the Bureau of Transportation Statistics.
- Data includes all major North American trade corridors and transportation modes.

### 2. **Data Preparation**
- **Standardization:** Unified column names and formats across all files.
- **Merging:** Combined monthly files by type (dot1, dot2, dot3) into consolidated datasets.
- **Source Tracking:** Added a column to track the original file for each record.

### 3. **Data Cleaning**
- Checked for and removed duplicates.
- Identified and handled missing or null values.
- Ensured all coded columns (e.g., state, mode, port) were mapped to human-readable names using official codebooks.

### 4. **Data Transformation**
- Applied mapping scripts to convert all codes to descriptive labels.
- Created both “cleaned” (mapped only) and “enriched” (original + mapped) datasets for full transparency.

### 5. **Exploratory Data Analysis (EDA)**
- Used Jupyter notebooks for all analysis and visualization.
- Analyzed freight patterns by mode, region, and time.
- Assessed operational efficiency (cost per weight, route analysis).
- Evaluated environmental impact and cross-border trade flows.
- Identified seasonal trends and infrastructure utilization.

### 6. **Visualization & Reporting**
- Produced clear, professional charts and tables for all key findings.
- Documented all steps, code, and business logic in the analysis notebooks.
- Summarized actionable recommendations for stakeholders.

### 7. **Reproducibility**
- All scripts and notebooks are version-controlled and available in the repository.
- Dependencies are listed in `requirements.txt` for easy environment setup.
- Data processing and analysis steps are fully documented and can be rerun end-to-end.

---

**Summary:**  
Every step of this analysis—from data collection to recommendations—can be reproduced by following the scripts and notebooks provided. This ensures that results are transparent, verifiable, and ready for future updates or deeper dives.

If you need a more technical or step-by-step version for data scientists, let me know!


## 📊 Project Overview

This comprehensive data analysis project examines North American transborder freight movements across the United States, Canada, and Mexico. The analysis leverages multi-year freight data (2020-2024) to identify operational inefficiencies, understand movement patterns, and provide actionable insights for transportation stakeholders, including the Bureau of Transportation Statistics (BTS).

**Key Capabilities:**
- **Multi-modal Analysis:** Vessel, Air, Truck, Rail, Pipeline, and other transport modes
- **Cross-border Trade:** US-Mexico and US-Canada freight flow analysis
- **Temporal Trends:** Seasonal patterns and year-over-year comparisons
- **Geographic Insights:** State, province, and port district-level analysis
- **Operational Efficiency:** Cost-per-weight analysis and route optimization insights

## 🎯 Business Objectives

### Primary Analysis Goals
1. **Freight Movement Patterns:** Identify dominant transportation patterns across modes, regions, and time periods
2. **Operational Efficiency:** Assess cost/weight inefficiencies and highlight optimization opportunities
3. **Environmental Impact:** Evaluate transportation modes by weight capacity and regional distribution
4. **Cross-border Trade Analysis:** Understand US-Mexico and US-Canada trade flows and patterns
5. **Seasonal Trends:** Uncover temporal patterns and economic disruption impacts
6. **Infrastructure Utilization:** Analyze port district and containerization efficiency
7. **Actionable Recommendations:** Provide data-driven insights for transportation planning

### Stakeholder Value
- **Transportation Planners:** Route optimization and infrastructure investment decisions
- **Policy Makers:** Cross-border trade policy and regulatory insights
- **Logistics Companies:** Operational efficiency and market opportunity identification
- **Environmental Analysts:** Mode-specific impact assessment and sustainability planning

## 📁 Project Structure

```
Freight_Data_Analysis/
├── data/                          # Raw freight data (2020-2024)
│   ├── 2020/                     # Monthly data by year
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   └── codes-north-american-transborder-freight-raw-data.pdf
├── preprocess/                    # Data processing pipeline
│   ├── combining.py              # File aggregation and standardization
│   ├── renaming_mappin.py        # Column mapping and value transformation
│   └── renaming.py               # Legacy mapping script
├── notebooks/                     # Analysis and visualization
│   ├── freight_eda_analysis.ipynb    # Main analysis notebook
│   ├── eda_analysis_original.ipynb   # Original exploratory analysis
│   ├── eda.ipynb                     # Additional EDA
│   └── worked_data/                  # Processed data outputs
├── worked_data/                   # Consolidated processed datasets
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git exclusions for large files
└── README.md                      # Project documentation
```

## 🔄 Data Processing Pipeline

### 1. Data Aggregation (`combining.py`)
- **Input:** Monthly CSV files scattered across year/month directories
- **Process:** Recursively finds and combines files by type (dot1, dot2, dot3)
- **Output:** Consolidated datasets with standardized column names
- **Features:** Error handling, source file tracking, data type preservation

### 2. Data Mapping (`renaming_mappin.py`)
- **Input:** Raw coded data with numeric/abbreviated values
- **Process:** Comprehensive mapping of all categorical variables to human-readable formats
- **Mappings Include:**
  - **Transport Modes:** 1→Vessel, 3→Air, 5→Truck, 6→Rail, etc.
  - **Geographic Data:** State codes, port districts, country codes
  - **Trade Types:** 1→Export, 2→Import
  - **Containerization:** X→Containerized, 0→Non-Containerized
- **Output:** Both cleaned (mapped only) and enriched (original + mapped) datasets

### 3. Data Quality Assurance
- **Null Value Handling:** Comprehensive treatment of missing data
- **Data Type Consistency:** String preservation for categorical variables
- **Error Logging:** Detailed processing logs for troubleshooting
- **Validation:** Shape and content verification at each step

## 📈 Analysis Capabilities

### Freight Movement Analysis
- **Mode Distribution:** Transportation mode preferences by region and time
- **Geographic Patterns:** State and port district freight flow analysis
- **Temporal Trends:** Seasonal variations and year-over-year comparisons
- **Cross-border Flows:** US-Mexico and US-Canada trade pattern analysis

### Operational Efficiency Assessment
- **Cost-per-Weight Analysis:** Identification of inefficient routes and modes
- **Route Optimization:** Port district and transportation mode efficiency ranking
- **Freight Charge Analysis:** Cost structure analysis across different modes
- **Capacity Utilization:** Weight distribution and containerization efficiency

### Environmental Impact Evaluation
- **Mode Comparison:** Weight-based environmental impact assessment
- **Regional Distribution:** Geographic concentration of freight movements
- **Containerization Analysis:** Efficiency of containerized vs. non-containerized freight
- **Sustainability Metrics:** Transportation mode environmental footprint

### Business Intelligence
- **Market Trends:** Emerging patterns in freight movement
- **Infrastructure Insights:** Port and transportation network utilization
- **Economic Indicators:** Trade value and volume correlation analysis
- **Risk Assessment:** Supply chain vulnerability identification

## 🛠️ Technical Implementation

### Data Sources
- **Primary Data:** North American transborder freight CSV files (2020-2024)
- **Codebook:** Official mapping documentation for data interpretation
- **Coverage:** Monthly data across 4+ years, multiple transportation modes
- **Scale:** Millions of freight records with comprehensive geographic coverage

### Technology Stack
```python
# Core Dependencies
pandas>=2.0.0      # Data manipulation and analysis
numpy>=1.24.0      # Numerical computing
tqdm>=4.65.0       # Progress tracking
loguru>=0.7.0      # Advanced logging

# Analysis and Visualization
matplotlib         # Plotting and visualization
seaborn           # Statistical data visualization
jupyter           # Interactive analysis environment
```

### Performance Characteristics
- **Data Volume:** Handles multi-million record datasets efficiently
- **Processing Speed:** Optimized for large-scale data transformation
- **Memory Management:** Efficient handling of large CSV files
- **Scalability:** Modular design for easy extension and modification

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- 8GB+ RAM (recommended for large datasets)
- Git for version control

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd Freight_Data_Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Data Processing Workflow
```bash
# 1. Aggregate monthly data files
python preprocess/combining.py

# 2. Apply mappings and transformations
python preprocess/renaming_mappin.py

# 3. Verify outputs in worked_data/ directory
ls worked_data/
```

### Analysis Execution
```bash
# Launch Jupyter environment
jupyter lab

# Open and run the main analysis notebook
notebooks/freight_eda_analysis.ipynb
```

## 📊 Key Insights and Deliverables

### Analytical Outputs
- **Freight Movement Patterns:** Mode distribution and geographic flow analysis
- **Efficiency Metrics:** Cost-per-weight ratios and route optimization insights
- **Environmental Impact:** Transportation mode sustainability assessment
- **Trade Flow Analysis:** Cross-border commerce patterns and trends
- **Infrastructure Utilization:** Port and transportation network efficiency

### Visualization Portfolio
- **Interactive Charts:** Mode distribution, geographic patterns, temporal trends
- **Statistical Analysis:** Correlation matrices, regression analysis, outlier detection
- **Business Dashboards:** Executive-level summaries and key performance indicators
- **Technical Reports:** Detailed methodology and statistical validation

### Actionable Recommendations
- **Route Optimization:** Identified inefficient routes and suggested improvements
- **Mode Selection:** Transportation mode recommendations based on efficiency analysis
- **Infrastructure Investment:** Port and transportation network enhancement priorities
- **Policy Implications:** Cross-border trade policy and regulatory recommendations

## 🔮 Future Enhancements

### Planned Improvements
- **Real-time Data Integration:** API connections for live freight data
- **Advanced Analytics:** Machine learning models for predictive insights
- **Interactive Dashboards:** Web-based visualization tools for stakeholders
- **Automated Reporting:** Scheduled generation of business intelligence reports

### Research Opportunities
- **External Data Integration:** Economic indicators, fuel prices, weather data
- **Advanced Modeling:** Supply chain optimization and forecasting
- **Geospatial Analysis:** GIS integration for enhanced geographic insights
- **Sustainability Metrics:** Carbon footprint and environmental impact modeling

## 📞 Support and Collaboration

### Contributing
This project welcomes contributions from data scientists, transportation analysts, and domain experts. Please review the codebase and submit pull requests for improvements.

### Documentation
- **Code Documentation:** Comprehensive inline comments and function documentation
- **Process Documentation:** Detailed workflow and methodology documentation
- **Business Context:** Stakeholder-focused insights and recommendations

### Contact
For questions, suggestions, or collaboration opportunities, please contact the project maintainer or open an issue in the repository.

---

**Prepared by a professional data analyst with 10+ years of experience in transportation analytics, supply chain optimization, and business intelligence.**

*This analysis provides actionable insights for transportation stakeholders, policy makers, and logistics professionals seeking to optimize North American freight operations and enhance cross-border trade efficiency.* 