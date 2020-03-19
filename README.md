# __Predicting clinical genetic variants that will have conflicting classifications by clinicians__
# Background:
Genetic testing is an important part of disease diagnosis and continues to grow in capacity (in terms of number of patients and detected diseases) as gene sequencing technologies develop. Patients can undergo genetic testing for numerous reasons, among which are preemptive screening for inherited diseases and diagnosis confirmation. In the first case, genetic testing is done when the patient has a family history of a disease and would like to know the likelihood of getting it in the future. In the latter case, a doctor sends a DNA sample to test for the presence of a disease-related mutation after the patient reports symptoms of disease. Thus, genetic testing provides results that have serious implications for guiding treatment and healthcare planning. 
Once the decision to perform genetic testing is made, patients submit a sample of their DNA for testing against a large panel of known mutations, also known as variants. After their sample is run and variants are found, an in-house clinical geneticist makes the determination of where on a five-step scale the variant lies: 

- Benign
- Likely Benign
- VUS (Variant of Uncertain Significance)
- Likely Pathogenic
- Pathogenic

Where benign is an indication of no disease, VUS stands for a variant of uncertain significance, and pathogenic means disease is present. Many genetic variants, or mutations, are benign. Thus it is important to note here that ‘mutation’ is not synonymous with disease. 
This classification is based upon a number of factors such as published literature and studies on that particular variant. There are multiple in silico predictors of deleteriousness, or harmfulness, based upon amino acid changes of a variant. However, these predictors are limited to protein-expressing genes and, by themselves, are not reliable for predicting disease. Some labs do use in silico predictors in conjunction with other resources when making their classification while others do not. Consequently, the same mutation can be classified as pathogenic by one lab and benign by another. 

# Problem: 
A large problem in genetic testing is that some mutations are consistently classified, while other mutations receive conflicting classifications when tested at different laboratories. This project aims to address the following question: Can we predict whether or not a mutation will have conflicting classifications by two or more labs based upon the features of the mutation? 	 	 	
The resultant model from this project can help both patients and caregivers decide whether or not to send out DNA samples to different labs when testing for a particular mutant. If they know the mutant of interest is likely to have conflicting classifications, it would be worthwhile to get additional labs’ opinions before making major treatment or healthcare decisions.  
Additionally, this model can reveal trends in mutants that are likely to be conflictingly classified, and may highlight patterns in classification processes that can be standardized.

# Data:
I will be using a Kaggle dataset (https://www.kaggle.com/kevinarvai/clinvar-conflicting), originally taken from ClinVar (https://www.ncbi.nlm.nih.gov/clinvar/). ClinVar is an online repository of genetic mutations and their features, updated in real time by submitters who submit their data to the database. Submitters to ClinVar include academic institutions, genetic testing laboratories, and hospitals. 
The Kaggle dataset I am using includes data up until April 7th, 2018. Each of the 65,188 data entries has 46 features. All of the data points are genetic variants that have two or more classifications on the five-step scale outlined above. The ‘CLASS’ column contains a binary value for each data entry, either 0 = consistent classifications or 1 = conflicting classifications.

# Data Cleaning:
Jupyter Notebook: [Data cleaning notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/data_cleaning_notebook.ipynb)

# NLP of Alleles:
Jupyter Notebook: [NLP notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/geneseq_nlp_notebook.ipynb)

# Uniprot Data Wrangling:
Jupyter Notebook: [Uniprot data wrangling notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/uniprot_data_wrangling_notebook.ipynb)

# Exploratory Data Analysis:
Jupyter Notebook: [Exploratory data analysis notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/exploratory_data_analysis.ipynb)

# Statistical Data Analysis:
Jupyter notebook: [Statistical data analysis notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/statistical_analysis_notebook.ipynb)

# Machine Learning Models:
Jupyter Notebooks: 
- [Logistic Regression Notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/logistic_regression_model.ipynb)
- [Decision Tree Notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/decision_tree_model.ipynb)
- [Random Forest Notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/random_forest_model.ipynb)
- [XGBoost Notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/xgboost_model.ipynb)

# Final Model Analysis:
Jupyter Notebook: [Final model comparison notebook](https://github.com/gksullan/conflicting_geneticvariants/blob/master/final_model_results.ipynb)

# Final Best Models Hyperparameter Table:
Pickle File: [Final Hyperparameters](https://github.com/gksullan/conflicting_geneticvariants/blob/master/hyperparameter_tables/final_best_models.pkl)



