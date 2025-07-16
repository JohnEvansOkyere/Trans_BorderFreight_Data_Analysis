import os
import glob
import pandas as pd

DATA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../worked_data'))

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def standardize_columns(df):
    df.columns = [str(col).strip().upper() for col in df.columns]
    return df

def find_csv_files(pattern):
    # Recursively find all files matching the pattern in DATA_ROOT
    return glob.glob(os.path.join(DATA_ROOT, '**', pattern), recursive=True)

def combine_files(pattern):
    files = find_csv_files(pattern)
    dfs = []
    for file in files:
        try:
            df = pd.read_csv(file, dtype=str)
            df = standardize_columns(df)
            df['SOURCE_FILE'] = os.path.basename(file)
            dfs.append(df)
        except Exception as e:
            print(f"Failed to read {file}: {e}")
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    # Combine dot1_*.csv
    print("Combining dot1_*.csv files...")
    dot1_all = combine_files('dot1_*.csv')
    dot1_all.to_csv(os.path.join(OUTPUT_DIR, 'dot1_all.csv'), index=False)
    print(f"Saved dot1_all.csv with shape {dot1_all.shape}")

    # Combine dot2_*.csv
    print("Combining dot2_*.csv files...")
    dot2_all = combine_files('dot2_*.csv')
    dot2_all.to_csv(os.path.join(OUTPUT_DIR, 'dot2_all.csv'), index=False)
    print(f"Saved dot2_all.csv with shape {dot2_all.shape}")

    # Combine dot3_*.csv
    print("Combining dot3_*.csv files...")
    dot3_all = combine_files('dot3_*.csv')
    dot3_all.to_csv(os.path.join(OUTPUT_DIR, 'dot3_all.csv'), index=False)
    print(f"Saved dot3_all.csv with shape {dot3_all.shape}") 