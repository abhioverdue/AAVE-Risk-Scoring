import pandas as pd

def extract_features(transactions):
    rows = []
    for wallet, txs in transactions.items():
        tx_count = len(txs)
        failed = sum(1 for tx in txs if not tx.get("successful", True))
        total_value = sum(int(tx.get("value", 0)) for tx in txs)
        avg_gas = sum(int(tx.get("gas_spent", 0)) for tx in txs) / tx_count if tx_count else 0

        rows.append({
            "wallet_id": wallet,
            "tx_count": tx_count,
            "fail_ratio": failed / tx_count if tx_count else 0,
            "total_value_eth": total_value / 1e18,
            "avg_gas": avg_gas,
        })
    return pd.DataFrame(rows)
