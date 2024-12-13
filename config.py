import os
from dotenv import load_dotenv

DATASET_NAME = "Falah/research_paper_in_ml"
TOGETHER_TOKEN = os.getenv("TOGETHER_API_KEY")
HG_TOKEN = os.getenv("hugging_face_key")
EVAL_MODEL= "sentence-transformers/all-MiniLM-L6-v2"
CSV_FILE_PATH = "data/research_ideas.csv"
EVALUATION_FILE_PATH = "data/evaluation_ideas.csv"
ABS_IMAGE_PATH= "images/abstract_length_distribution.png"
IDEAS_FILE_PATH = "data/refined_research_ideas.txt"
PROCESSED_IDEAS = "data/cleaned_input.txt"
STAT_IMAGE_PATH = "images/hypotheses_statistics.png"
GENERATION_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
