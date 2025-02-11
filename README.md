# Data Science Project: Passport Index & Economic Indicators Analysis

## Project Overview
This project explores relationships between a country's passport strength and various economic and educational indicators. We integrate web-scraped datasets, preprocess them, conduct hypothesis testing, and apply machine learning models to analyze trends and make predictions.

## Contributors
- **Muhammad Omer Chaudhry** (mchaud11)
- **Emre Arslan** (earslan)
- **Seyit Metin Barut** (sbarut)
- **Can Tulpar** (ctulpar)

## Links
Poster - https://app.luminpdf.com/viewer/67abaa776ebfc1bf3f009768 

Video Demo - https://drive.google.com/file/d/1k3hgHufLlV4vUuNNuPT7IdHnfcmeLwEL/view?usp=sharing


## Project Structure
```
├── main.py              # Main script to execute data pipeline
├── models.py            # Hypothesis testing and machine learning models
├── preprocessor.py      # Data cleaning and preprocessing
├── scraper.py           # Web scraping for data collection
├── visualization.py     # Data visualization scripts
├── data/                # Raw scraped datasets
├── preprocessed_data/   # Cleaned and processed datasets
├── results/             # Outputs, including clustered data and visualizations
└── README.md            # Project documentation
```

## Data Sources
The project gathers data from multiple sources:
- **Passport Index**: Henley Passport Index
- **Education Rankings**: DataPandas ranking
- **Trade Data**: Import/export values from Wikipedia
- **Cognitive Indicators**: Average IQ & literacy rate (World Population Review)
- **Economic Indicators**: GDP per capita (World Bank)

## Methodology
1. **Data Collection**: 
   - Web scrapers (`scraper.py`) collect data from various online sources.
   - CSV files are loaded into Pandas DataFrames.

2. **Preprocessing**:
   - Handling missing values and duplicate records.
   - Standardizing column names and numerical data.
   - Merging datasets by country (`preprocessor.py`).

3. **Hypothesis Testing** (`models.py`):
   - **Claim #1**: Education levels and passport indices are not independent (Chi-Square Test, p=0.89, Accept Null Hypothesis).
   - **Claim #2**: High/low literacy rate countries have significantly different passport indices (Two-Sample T-Test, p<0.001, Reject Null Hypothesis).
   - **Claim #3**: High/low GDP per capita countries have significantly different passport indices (Two-Sample T-Test, p<0.001, Reject Null Hypothesis).

4. **Machine Learning Models**:
   - **Logistic Regression**: Predicts passport strength categories based on economic and educational factors.
   - **Linear Regression**: Predicts exact passport index values.
   - **KMeans Clustering**: Groups countries based on similarities in GDP, education, and cognitive indicators.

5. **Visualization (`visualization.py`)**:
   - Scatter plots and regression analysis.
   - 2D and 3D cluster visualizations.
   - Confusion matrices for classification models.

## Results & Interpretation
- **Education levels** do not significantly influence passport index.
- **Literacy rate and GDP per capita** are strong predictors of passport strength.
- **KMeans clustering** shows distinct country groupings based on economic development and passport strength.
- **Logistic regression achieves 74.7% accuracy** when predicting passport strength categories.
- **Silhouette scores suggest moderate clustering effectiveness**, with GDP and education as the most relevant factors.
- **Bar Graph Analysis**: Education index was the strongest predictor, followed by GDP per capita, while literacy rate had the least impact.

## Running the Project
### Setup
Ensure you have Python installed, then install dependencies:
```bash
pip install -r requirements.txt
```

### Execute Data Pipeline
```bash
python main.py
```

### Run Tests
```bash
pytest
```

### Generate Visualizations
```bash
python visualization.py
```

## Future Improvements
- Expand dataset to include additional economic and social indicators.
- Explore alternative clustering algorithms for better country categorization.
- Improve data handling for missing values and standardize feature selection.
- Integrate deep learning models for more advanced predictions.

---
This project highlights the connection between national development factors and passport strength using statistical tests and machine learning models.

