import pandas as pd

# =========================
# LOCKED RULE ENGINE
# =========================
# NOTE:
# - PAPER TEST ONLY
# - NO API
# - NO LIVE TRADING
# - INPUT: pump60d_master.csv
# - OUTPUT: labeled dataframe
# =========================

def apply_rule_engine(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # default
    out["decision"] = "IGNORE"

    # basic safety
    if "pump_60d_%" not in out.columns:
        raise ValueError("Missing pump_60d_% column")

    # RULES (LOCKED)
    out.loc[
        (out["pump_60d_%"] >= 30) & (out["pump_60d_%"] < 50),
        "decision"
    ] = "TARGET_30_50"

    out.loc[
        (out["pump_60d_%"] >= 50) & (out["pump_60d_%"] < 100),
        "decision"
    ] = "MID_RUN"

    out.loc[
        (out["pump_60d_%"] >= 100),
        "decision"
    ] = "RUNNER"

    return out
