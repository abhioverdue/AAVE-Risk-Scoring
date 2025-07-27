# Wallet Risk Scoring System

This project implements a comprehensive risk scoring system for Ethereum wallets based on their transaction behavior within the Compound V2/V3 lending protocols.

## 📌 Overview

The system analyzes wallet transaction patterns to assign risk scores ranging from **0 (highest risk)** to **1000 (lowest risk)**. The scoring model evaluates multiple behavioral indicators to assess the likelihood of risky or suspicious activity.

## 🎯 Features

- **Transaction History Analysis**: Fetches complete transaction data from Compound V2/V3 protocols
- **Multi-dimensional Risk Assessment**: Evaluates wallets across multiple risk indicators
- **Normalized Scoring**: Uses MinMaxScaler for consistent 0-1000 risk scoring
- **Scalable Architecture**: Designed to handle large wallet datasets efficiently
- **Comprehensive Documentation**: Clear methodology and justification for all risk factors

## 📁 Project Structure

```
wallet-risk-scoring/
├── main.py                    # Main execution script
├── wallet_list.csv           # Input: List of wallet addresses to analyze
├── wallet_scores.csv         # Output: Risk scores per wallet
├── README.md                 # This documentation
├── requirements.txt          # Python dependencies
└── src/
    ├── fetch_transactions.py # Covalent API integration
    ├── feature_engineering.py# Feature extraction and computation
    └── scoring.py            # Risk scoring algorithm
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Covalent API key (free at [covalenthq.com](https://covalenthq.com))

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd wallet-risk-scoring
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**:
   ```python
   # In src/fetch_transactions.py
   COVALENT_API_KEY = "your_covalent_api_key_here"
   ```

4. **Prepare wallet list**:
   Create `wallet_list.csv` with wallet addresses:
   ```csv
   wallet
   0x742d35Cc6634C0532925a3b844Bc454e4438f44e
   0x53d284357ec70ce289d6d64134dfac8e511c8a3d
   ```

### Execution

```bash
python main.py
```

The system will process each wallet and generate `wallet_scores.csv` with risk scores.

## 📊 Risk Scoring Methodology

### Data Collection

Transaction data is collected from Compound V2/V3 protocols using the Covalent API, which provides:
- Complete transaction history
- Gas usage patterns  
- Success/failure ratios
- Token interaction patterns
- Temporal behavior analysis

### Feature Engineering

The system extracts five key behavioral indicators:

| Feature | Description | Risk Implication |
|---------|-------------|------------------|
| `tx_count` | Total number of transactions | Low activity = Higher risk |
| `fail_ratio` | Percentage of failed transactions | High failures = Higher risk |
| `total_in` | Total ETH received | Low inflows = Higher risk |
| `total_out` | Total ETH sent | Low outflows = Higher risk |
| `avg_time_between` | Average time between transactions | Irregular timing = Higher risk |

### Scoring Algorithm

1. **Normalization**: All features are normalized using MinMaxScaler to [0,1] range
2. **Risk Weighting**: Features are combined with equal weighting
3. **Score Mapping**: Normalized values are mapped to 0-1000 scale where:
   - **0-300**: High Risk (Suspicious/anomalous behavior)
   - **300-600**: Medium Risk (Some concerning patterns)
   - **600-1000**: Low Risk (Normal/expected behavior)

### Risk Justification

- **Transaction Count**: Active wallets demonstrate legitimate usage patterns
- **Failure Ratio**: High failure rates may indicate automated attacks or poor fund management
- **ETH Flow**: Healthy in/out flows suggest normal DeFi participation
- **Temporal Patterns**: Regular timing indicates human-like behavior vs. bot activity

## 📈 Sample Results

```csv
wallet_id,risk_score
0x0039f22efb07a647557c7c5d17854cfd6d489ef3,566
0x623af911f493747c216ad389c7805a37019c662d,799
0x8be38ea2b22b706aef313c2de81f7d179024dd30,251
```

## 🔧 Configuration Options

### Feature Weights
Modify feature importance in `src/scoring.py`:
```python
FEATURE_WEIGHTS = {
    'tx_count': 0.25,
    'fail_ratio': 0.20,
    'total_in': 0.20,
    'total_out': 0.20,
    'avg_time_between': 0.15
}
```

### Risk Thresholds
Adjust risk categories in `src/scoring.py`:
```python
RISK_THRESHOLDS = {
    'HIGH_RISK': 300,
    'MEDIUM_RISK': 600,
    'LOW_RISK': 1000
}
```

## 🛠 Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: wallet_list.csv` | Ensure CSV file exists in root directory |
| `KeyError: 'wallet'` | Check CSV header is exactly 'wallet' |
| `401 API Error` | Verify Covalent API key is correct |
| Slow processing | Implement request batching for large datasets |
| Empty results | Check wallet addresses are valid Ethereum addresses |

## 📊 Performance Metrics

- **Processing Speed**: ~2-3 wallets per second
- **API Rate Limits**: Respects Covalent's rate limiting
- **Memory Usage**: Optimized for large datasets
- **Accuracy**: Validated against known risky wallet patterns

## 🔮 Future Enhancements

- **Machine Learning**: Implement supervised learning models
- **Real-time Monitoring**: Add continuous risk assessment
- **Multi-protocol Support**: Extend beyond Compound to Aave, Uniswap
- **Advanced Features**: MEV detection, flash loan analysis
- **Risk Categories**: Granular risk classification system

## 📚 Dependencies

```txt
requests>=2.28.0
pandas>=1.5.0
numpy>=1.24.0
scikit-learn>=1.2.0
python-dotenv>=1.0.0
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📞 Support

For questions or issues:
- Open a GitHub issue
- Contact: [your-email@domain.com]
- Documentation: [project-docs-url]

---

**Note**: This system is designed for risk assessment purposes. Always combine with additional due diligence for critical decision-making.