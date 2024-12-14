# Automated_Hypothesis_Generation

Name: Meghana Maringanti

Course: INFO 555 - Applied NLP - University of Arizona

This repository contains the necessary files, scripts, and data for the automated Hypothesis Generation. 

---

## Repository Structure

A pdf file of the paper write-up.

### Directories and Files
- **data/**  
  - `refined_research_ideas.txt` - Contains all ideas
  - `cleaned_input.txt` - Contains all ideas after cleaning (removing numericals and symbols)
  - `research_questions.csv` - Contains the generated research questions and their categories
  - `evaluation_scores.csv` - Contains relevance and feasibility scores for generated questions

- **images/**  
  - Contains visualizations used in the write-up.  

### Additional Files
- `requirements.txt` - Python package dependencies.   
- `Automated_Hypothesis_Generation.ipynb` - Notebook for Hypothesis Generation.
- `config.py` - Contains all the variables
- `.gitignore`file

THe dataset used in this project is taken from Hugging face.

**Citation:**

@dataset{falah_covid19_sarscov2_research_dataset,
  author = {Falah.G.Salieh},
  title = {COVID-19 and SARS-CoV-2 Research Papers Dataset},
  year = {2023},
  publisher = {Hugging Face},
  version = {1.0},
  location = {Online},
  url = {https://huggingface.co/datasets/falah/research_paper_in_ml}
} 




