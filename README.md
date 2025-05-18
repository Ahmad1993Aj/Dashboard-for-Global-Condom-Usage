# Interactive Exploratory Data Visualization App

An interactive Streamlit web app for performing Exploratory Data Analysis (EDA) on datasets. This project focuses on analyzing a global dataset on condom usage, enabling users to explore trends, uncover patterns, and visualize correlations related to sexual health awareness, sales, and campaigns.

## 📊 Features

- **Data Preview**:
  - Display the first few rows of the dataset
  - View column information
  - Detect missing values and duplicates

- **Exploratory Data Analysis (EDA)**:
  - Boxplots for outlier detection
  - Frequency distributions for categorical columns
  - Mean and histogram plots for numerical columns
  - Bar plots for categorical feature distributions

- **Correlation Analysis**:
  - Heatmap showing correlation between numerical features

- **Country-based Filtering** *(Planned)*:
  - Visualize awareness and sales by country over time

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**:
  - [Streamlit](https://streamlit.io/) – for the interactive web interface
  - [Pandas](https://pandas.pydata.org/) – for data manipulation
  - [Seaborn](https://seaborn.pydata.org/) and [Matplotlib](https://matplotlib.org/) – for data visualization

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Ahmad1993Aj/Dashboard-for-Global-Condom-Usage.git
```
### 2. Run the app
```bash
streamlit run EDV_2.py
```
## 📁 Project Structure:
├── EDV_2.py          # Main Streamlit App File
├── EDV.py            # Alternate version of the App
├── EDV.ipynb
└── README.md         # Project description

