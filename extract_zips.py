import zipfile
import os
from pathlib import Path

def extract_all_zips(root_dir):
    for path in Path(root_dir).rglob('*.zip'):
        print(f"Extracting {path}...")
        try:
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(path.parent)
            print(f"Successfully extracted {path}")
        except Exception as e:
            print(f"Error extracting {path}: {e}")

if __name__ == "__main__":
    extract_all_zips('dataset')