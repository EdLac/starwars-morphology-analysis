# Star Wars – Height & Mass Modeling (Tableau)

## 🧠 Project Status
🚧 Ongoing analysis

This project aims to model the relationship between character height and mass in the Star Wars universe and progressively improve model performance by introducing additional explanatory variables.

## 🎯 Objective
- Identify the best functional form to explain character mass based on height
- Test multiple regression models
- Iteratively improve model fit by adding relevant variables

## 📊 Dataset
- Source: Star Wars API
- Format: JSON
- Key variables currently used:
  - height
  - mass
- Candidate variables for further modeling:
  - gender
  - species (to be explored)
  - character type (biological vs non-biological)

## 🧪 Current Progress
- Data import and JSON flattening in Tableau
- Initial exploratory analysis
- Comparison of regression models:
  - Linear
  - Logarithmic
  - Exponential
  - Power
  - Polynomial

Preliminary results indicate that non-linear models (Power / Exponential) outperform linear specifications.

## 🔜 Next Steps
- Add categorical variables to the model
- Segment analysis by character type
- Assess impact of outliers
- Compare conditional vs global models

## 🛠️ Tools
- Tableau Public
