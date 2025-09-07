# Student_At_Risk_Detector


Student at Academic Risk Detector: Developed a machine learning solution to identify students at risk of academic underperformance using educational data, featuring data preprocessing, feature engineering, model training, and actionable insights for early intervention; Tech: Python, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn, Data Analytics, Machine Learning, Data Visualization, Jupyter Notebook, Data Science, Predictive Modeling, EDA.
# Setup:
Run the SetYouUp.ipynb file to get started.
## Data Dictionary

| Column                   | Description                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------|
| student_id               | Unique identifier of the student                                                             |
| full_name                | Complete name of the student                                                                 |
| age                      | Age of the student                                                                           |
| email                    | Email address of the student                                                                 |
| phone_number             | Phone number of the student                                                                  |
| gender                   | Gender of the student                                                                        |
| birth_country            | Country of birth of the student                                                              |
| secondary_address        | Unit or secondary address information                                                        |
| building_number          | Building number of the student's address                                                     |
| street_name              | Street name of the student's address                                                         |
| street_suffix            | Street type/suffix (e.g., Ave, St, Blvd)                                                     |
| city                     | City or suburb of the student's address                                                      |
| postcode                 | Postal code of the student's address                                                         |
| state_abbr               | State abbreviation of the student's address                                                  |
| admission_year           | Year of university admission                                                                 |
| hsc_year                 | Year of High School Certificate (HSC)                                                        |
| program                  | Enrolled academic program                                                                    |
| scholarship              | Indicates if the student has a meritorious scholarship (Yes/No)                             |
| university_transport     | Indicates if the student uses university transportation (Yes/No)                             |
| learning_mode            | Preferred learning mode (e.g., Offline, Online)                                              |
| has_phone                | Indicates if the student uses a smartphone (Yes/No)                                          |
| has_laptop               | Indicates if the student has a personal computer (Yes/No)                                    |
| english_proficiency      | Level of English language proficiency (e.g., Basic, Intermediate, Advanced)                  |
| on_probation             | Indicates if the student has previously been on academic probation (Yes/No)                  |
| is_suspended             | Indicates if the student has previously been suspended (Yes/No)                              |
| has_consulted_teacher    | Indicates if the student has attended teacher consultancy for academic problems (Yes/No)     |
| relationship             | Relationship status (e.g., Single, Married)                                                  |
| co_curricular            | Indicates engagement in co-curricular activities (Yes/No)                                    |
| living_arrangement       | Living arrangement (e.g., With family, Bachelor, Hostel)                                     |
| health_issues            | Indicates if the student has any health issues (Yes/No)                                      |
| disabilities             | Indicates if the student has any physical disabilities (Yes/No)                              |
| target                   | Student's performance target at the end of the semester (e.g., Good, Average)                |
| current_semester         | Current semester/tenure in semesters                                                         |
| study_hours              | Hours of daily study                                                                         |
| study_sessions           | Number of study sessions per day                                                             |
| social_media_hours       | Hours of daily social media usage                                                            |
| average_attendance       | Average class attendance percentage                                                           |
| skills                   | Student's skills (e.g., Programming, Web Development)                                        |
| skills_development_hours | Hours spent daily on skill development                                                       |
| area_of_interest         | Area of academic or professional interest                                                    |
| previous_gpa             | Previous GPA score                                                                           |
| current_gpa              | Current GPA score                                                                            |
| completed_credits        | Number of completed academic credits                                                         |
| has_diploma              | Indicates if the student has a diploma degree (Yes/No)                                      |
| house_income             | Monthly family income                                                                        |
## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         student_at_risk_detector and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── student_at_risk_detector   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes student_at_risk_detector a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

