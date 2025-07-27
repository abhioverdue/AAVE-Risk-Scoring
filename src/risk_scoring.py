from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def score_wallets(df):
    feature_cols = ["tx_count", "fail_ratio", "total_value_eth", "avg_gas"]
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df[feature_cols])
    df["risk_score"] = (1 - df_scaled[:, 1]) * 0.3 + df_scaled[:, 0] * 0.2 + df_scaled[:, 2] * 0.3 + (1 - df_scaled[:, 3]) * 0.2
    df["risk_score"] = (df["risk_score"] * 1000).round().astype(int)
    return df[["wallet_id", "risk_score"]]
