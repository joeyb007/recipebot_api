import pandas as pd
from pathlib import Path
# Goal: manipulate cleaned recipes into JSON data for model training.
BASE_DIR = Path(__file__).resolve().parents[2]
PATH_TO_SEED_LABELS = BASE_DIR / 'data' / 'CSV_data' / 'seed_labeling_unlabeled.csv'
PATH_TO_CLEANED_DATA = BASE_DIR / 'data' / 'CSV_data' / 'recipes_cleaned.csv'

seed_labeled_data = pd.read_csv(PATH_TO_SEED_LABELS)
if __name__ == '__main__':
    print(seed_labeled_data)