from datasets import load_dataset
import pandas as pd
import os

# 确保dataset目录存在
os.makedirs('dataset', exist_ok=True)

# 加载ETTh1数据集
dataset = load_dataset('thuml/Time-Series-Library', 'ETTh1')

# 将训练集保存为CSV
print("Saving ETTh1 dataset...")
dataset['train'].to_csv('dataset/ETTh1.csv', index=False)
print("Dataset saved successfully!")