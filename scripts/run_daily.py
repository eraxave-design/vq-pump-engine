import pandas as pd
from engine.rule_engine_locked import apply_rule_engine

INPUT_CSV = "data/pump60d_master.csv"
OUTPUT_CSV = "outputs/daily_labeled.csv"

def main():
    df = pd.read_csv(INPUT_CSV)
    df_labeled = apply_rule_engine(df)
    df_labeled.to_csv(OUTPUT_CSV, index=False)
    print("Daily run completed.")

if __name__ == "__main__":
    main()
