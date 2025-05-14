# week-8-python
COVID-19 Global Data Tracker
Project Overview
The COVID-19 Global Data Tracker is a data analysis project that explores global COVID-19 trends using the Our World in Data dataset. It analyzes cases, deaths, vaccinations, and other metrics across countries, providing visualizations and insights through a Jupyter Notebook.
Objectives

Import and clean COVID-19 global data
Analyze time trends for cases, deaths, and vaccinations
Compare metrics across countries
Visualize trends with charts and maps
Summarize findings in a narrative report

Repository Structure
COVID-19-Global-Data-Tracker/
├── COVID-19_Global_Data_Tracker.ipynb  # Main Jupyter Notebook
├── README.md                          # Project documentation
└── requirements.txt                   # Python dependencies

Prerequisites

Python 3.8+
Jupyter Notebook or JupyterLab
Internet access (to download the dataset)

Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/COVID-19-Global-Data-Tracker.git
cd COVID-19-Global-Data-Tracker


Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

The requirements.txt includes:
pandas
matplotlib
seaborn
plotly


Launch Jupyter Notebook:
jupyter notebook

Open COVID-19_Global_Data_Tracker.ipynb in the Jupyter interface.


Usage

Run the Notebook: Execute the cells in COVID-19_Global_Data_Tracker.ipynb sequentially to:
Load and clean the dataset from Our World in Data
Perform exploratory data analysis (EDA)
Generate visualizations (line charts, bar plots, choropleth map)
Review key insights in the narrative section


Customize Analysis: Modify the countries list in the notebook to analyze different countries or adjust visualization parameters.
Export Results: Use Jupyter's "Download as PDF" feature or take screenshots for presentations.

Data Source

Our World in Data COVID-19 Dataset: https://github.com/owid/covid-19-data
The notebook directly loads the dataset from the URL, so no manual download is required.

Key Features

Time Series Analysis: Tracks total cases, deaths, and vaccinations over time.
Country Comparisons: Visualizes metrics for selected countries (e.g., Kenya, USA, India).
Choropleth Map: Displays global case density using Plotly.
Insights: Summarizes findings, such as vaccination progress and death rate variations.

Example Visualizations

Line charts showing case and death trends
Bar plots comparing vaccination rates
Global choropleth map of cases per million

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/new-analysis).
Commit changes (git commit -m "Add new analysis feature").
Push to the branch (git push origin feature/new-analysis).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Our World in Data for providing the dataset
Python data science community for tools like pandas, matplotlib, seaborn, and plotly

Created by [Your Name], May 14, 2025
