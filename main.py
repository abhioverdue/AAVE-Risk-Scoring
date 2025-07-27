import pandas as pd
from src.fetch_transactions import fetch_all
from src.feature_engineering import extract_features
from src.risk_scoring import score_wallets

# 1. Load wallet list
wallet_df = pd.read_csv("wallet_list.csv")
wallets = wallet_df.iloc[:, 0].dropna().unique().tolist()

# 2. Fetch all transactions
transactions = fetch_all(wallets)

# 3. Extract features
features_df = extract_features(transactions)

# 4. Score wallets
scored_df = score_wallets(features_df)

# 5. Save result
scored_df.to_csv("wallet_scores.csv", index=False)
print("✅ Scores saved to wallet_scores.csv")
