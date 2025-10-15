from datasets import load_dataset
import pandas as pd


df = pd.read_csv('recipes.csv', chunksize=1000)