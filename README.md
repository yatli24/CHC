# UCSB Climate Hazards Center Data Science Capstone

## Project Description
Assessing GCM precipitation forecast skill is critical for guiding humanitarian decision-making in regions dependent on rain-fed agriculture. We conduct a comprehensive evaluation of General Circulation Models (GCMs) and introduce both a Skilled Multi-Model Ensemble (SMME) and a custom machine learning model. Our approach automates the skill evaluation process for processing large-scale climate data, improving the speed, scalability, and reproducibility of climate forecast assessments.

## Repository Guide
This repository is split into four main folders: Jupyter notebooks, SMME text files, figures, and scripts/preprocessing. 

- The 'Jupyter Notebooks' folder contains all of the Jupyter notebooks written. This folder is further split into ML, documented, and unused. The machine learning scripts are separated from the rest of the documented ones due to them not being fully developed. However, they are still functional and can be run. The documented notebooks are also split into 'monthly' and 'seasonal', distinguishing them by the trends they observe. The unused notebooks contain our scratch work that ended up not being used in our final product. 

- The 'SMME Text Files' folder contains the descriptions for our different SMME models (short, medium, and long lead times), as well as our general SMME model. 

- The 'Figures' folder contains all of the plots and figures we've created. This is further divided into several folders (i.e. 'monthly_metrics', 'seasonal_metrics', etc.).

- The 'scripts/pre-processing' folder contains our scripts for data pre-processing (data conversion, cleaning, and merging).

- The 'outdated' folder contains scripts that may still be used for analyses, but must be updated to match certain conventions (i.e naming conventions, code structure), as well as analysis direction (i.e files analyze one region or season at a time)

## Dependencies
numpy version 2.0.2

pandas version 2.2.2

xarray version 2025.3.1

matplotlib version 3.10.0, mainly used matplotlib.pyplot

seaborn version 0.13.2

cartopy version 0.24.1

xgboost version 2.1.4

sklearn version 1.6.1

shap version 0.47.2

os module (built-in)

## References
Gebrechorkos, S. H., Pan, M., Beck, H. E., & Sheffield, J. (2022). Performance of State‐of‐the‐Art C3S European Seasonal Climate Forecast Models for Mean and Extreme Precipitation Over Africa. Water Resources Research, 58(3). https://doi.org/10.1029/2021wr031480

Slater, L. J., Villarini, G., & Bradley, A. A. (2016). Evaluation of the skill of North-American Multi-Model Ensemble (NMME) Global Climate Models in predicting average and extreme precipitation and temperature over the continental USA. Climate Dynamics, 53(12), 7381–7396. https://doi.org/10.1007/s00382-016-3286-1 

## People
Created By Johnson Sy Leung, Ivan Li, Hannah Kim, Edwin Yang, Sanchit Mehrotra, and Sophie Shi

Advisesd by Laura Harrison and Greg Husak from the UCSB Climate Hazards Center
