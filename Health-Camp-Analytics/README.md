Health Camp Analytics

📌 Project Overview

Health Camp Analytics is a Data Analytics project developed using Python and Pandas to analyze healthcare camp participation data. The project combines multiple datasets containing patient registrations, health camp details, and attendance records to create a unified dataset for analysis and visualization.

---

🎯 Objectives

- Load and explore healthcare datasets.
- Merge patient registration, attendance, and camp details.
- Identify and handle missing values.
- Create a cleaned dataset for analysis.
- Generate visual insights using charts and graphs.

---

🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Files
- Data Cleaning & Analysis

---

📂 Dataset Information

1. Train Dataset

Contains patient registration details.

Records: 75,278

2. First Health Camp Attended Dataset

Contains attendance details and health scores.

Records: 6,218

3. Health Camp Detail Dataset

Contains information about health camps.

Records: 65

---

📁 Project Structure

Health-Camp-Analytics/

├── data/

│ ├── Train.csv

│ ├── First_Health_Camp_Attended.csv

│ └── Health_Camp_Detail.csv

├── output/

│ ├── cleaned_data.csv

│ ├── camp_categories.png

│ ├── donation_distribution.png

│ └── health_score_distribution.png

├── src/

│ └── health_camp_analysis.py

└── README.md

---

🔄 Data Processing Workflow

1. Imported datasets using Pandas.
2. Explored dataset dimensions and column information.
3. Merged attendance and registration datasets.
4. Combined camp details with participant data.
5. Identified missing values.
6. Generated a cleaned dataset.
7. Exported the final dataset.
8. Created visualizations for analysis.

---

📊 Results

Dataset Summary

Dataset| Records| Columns
Train Dataset| 75,278| 8
Camp Dataset| 65| 6
Attendance Dataset| 6,218| 5
Merged Dataset| 6,218| 16

Missing Values Found

Column| Missing Values
Registration_Date| 45
Unnamed: 4| 6,218

---

📈 Visualizations

Health Camp Categories

"Health Camp Categories" (output/camp_categories.png)

Donation Distribution

"Donation Distribution" (output/donation_distribution.png)

Health Score Distribution

"Health Score Distribution" (output/health_score_distribution.png)

---

🔍 Key Insights

- Successfully merged healthcare datasets into a single analytical dataset.
- Created a cleaned dataset containing 6,218 participant records.
- Identified missing values and data quality issues.
- Generated visualizations to understand camp categories, donations, and health scores.
- Prepared the data for future analytics and machine learning applications.

---

🚀 Future Enhancements

- Advanced exploratory data analysis (EDA)
- Predictive analytics using machine learning
- Patient participation forecasting
- Interactive dashboards using Power BI or Tableau
- Health score trend analysis

---

👩‍💻 Author

Nikitha Thanikonda

Data Analytics Project

---

⭐ Project Outcome

Built a complete Health Camp Analytics solution using Python, Pandas, and Matplotlib by integrating healthcare datasets, cleaning data, identifying missing values, and generating visual insights to support data-driven decision-making.