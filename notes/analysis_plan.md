# 📊 Star Wars Characters — Height vs Mass  
## Analysis Plan & Results (Version 1)

---

## 1. Baseline Model

### Objective
Model the relationship between character height and mass and identify the best functional form.

### Baseline specification
- Dependent variable: **Mass**
- Independent variable: **Height**

Several functional forms were tested to capture potential non-linear relationships.

### Model comparison

| Model        | R²     | p-value   |
|--------------|--------|-----------|
| Linear       | 0.017  | 0.323     |
| Logarithmic  | 0.020  | 0.291     |
| Exponential  | 0.427  | < 0.0001  |
| **Power**    | **0.449** | **< 0.0001** |
| Polynomial  | 0.022  | 0.742     |

### Baseline conclusion
The **Power model** provides the best baseline performance, explaining approximately **45% of the variance** in mass.  
It is statistically significant and clearly outperforms linear, logarithmic, and polynomial specifications.

➡️ This model is retained as the **baseline reference** for further improvements.

---

## 2. Gender-Based Modeling (Variable Enrichment — V1)

To explore heterogeneity in the height–mass relationship, the baseline Power model was segmented by **gender**.

### Results by gender

- **Male**
  - R² = **0.81**
  - p-value < **0.0001**
  - Strong and statistically significant relationship

- **Female**
  - R² = 0.053
  - p-value = 0.521
  - No statistically significant relationship observed

- **Other / Non-standard categories**
  - R² ≈ 1 or undefined
  - Results **not interpretable** due to very small sample sizes

### Interpretation
The relationship between height and mass is **highly heterogeneous** across gender groups.  
The model performs extremely well for male characters, while insufficient data prevents reliable inference for other groups.

---

## 3. Model Comparison Strategy

Models are evaluated based on:
- **Explanatory power** (R²)
- **Statistical significance** (p-values)
- **Interpretability**
- **Stability across subgroups**

The Power model currently represents the best compromise between performance and interpretability.

---

## 4. Robustness Checks (Planned)

- Identify and remove extreme outliers
- Re-estimate baseline and segmented models
- Compare coefficient stability and goodness of fit

---

## 5. Next Steps — Version 2 (V2)

Planned extensions:
- Enrich the model with additional categorical variables:
  - **Species**
  - Potentially other character attributes
- Implement dummy-variable logic via Tableau segmentation
- Evaluate incremental gains in R² and interpretability
- Select a final model balancing complexity and explanatory power
- Prepare final visualizations for publication (Tableau Public + GitHub)
