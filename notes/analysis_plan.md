# Analysis Plan

## 1. Baseline model
- Height → Mass
- Identify best functional form

## 2. Variable enrichment
- Test categorical variables:
  - gender
  - species
- Create dummy variables (via segmentation in Tableau)

## 3. Model comparison
- Compare R² and p-values across specifications
- Evaluate interpretability vs performance

## Baseline Model Results

Several functional forms were tested to model the relationship between character height and mass.

| Model | R² | p-value |
|------|----|---------|
| Linear | 0.017 | 0.323 |
| Logarithmic | 0.020 | 0.291 |
| Exponential | 0.427 | < 0.0001 |
| Power | 0.449 | < 0.0001 |
| Polynomial | 0.022 | 0.742 |

The Power model provides the best baseline performance, explaining approximately 45% of the variance in mass. This baseline model will be used as a reference for further improvements through additional variables.

## Gender-based Modeling

Segmenting the Power model by gender reveals substantial heterogeneity.  
The model performs extremely well for male characters (R² = 0.81), while no statistically significant relationship is observed for female characters.  
Results for non-standard gender categories are not interpretable due to insufficient sample sizes.


## 4. Robustness checks
- Remove extreme outliers
- Compare results

## 5. Final model selection
- Choose best compromise model
- Prepare final visualization and interpretation
