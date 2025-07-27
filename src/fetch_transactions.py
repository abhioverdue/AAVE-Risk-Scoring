import requests
import time
from config import COVALENT_API_KEY, BASE_URL, CHAIN_ID

def fetch_transactions(wallet):
    url = f"{BASE_URL}/{CHAIN_ID}/address/{wallet}/transactions_v2/"
    params = {"key": COVALENT_API_KEY, "page-size": 100}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"❌ Error fetching for {wallet}: {response.status_code}")
        return []
    return response.json().get("data", {}).get("items", [])

def fetch_all(wallets):
    all_tx = {}
    for i, wallet in enumerate(wallets):
        print(f"[{i+1}/{len(wallets)}] Fetching {wallet}...")
        txs = fetch_transactions(wallet)
        all_tx[wallet] = txs
        print(f"✅ {wallet} - {len(txs)} txs fetched")
        time.sleep(1.2)  # Respect Covalent rate limit
    return all_tx
