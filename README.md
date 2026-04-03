# Quantum Market Breadth

**Historical-first market breadth intelligence platform powered by Q-BRAM v2 engine and Twelve Data API**

## 🎯 Mission
Build the most comprehensive historical analysis of market breadth indicators to validate the proprietary Q-BRAM v2 engine and provide institutional-grade market intelligence.

## 🏗️ Architecture
- **Historical Data Engine**: 2000-2024 NIFTY 500 + S&P 500 historical data
- **Q-BRAM v2 Engine**: 7-component scoring system with 5-state regime detection
- **Analysis Engine**: Correlation, backtesting, and crisis detection capabilities
- **Validation Engine**: Statistical significance and Monte Carlo simulations
- **Visualization Layer**: Interactive historical analysis dashboard

## 📊 Core Features
- **Historical Q-BRAM Analysis** (2000-2024)
- **Crisis Detection Validation** (Black Swan events)
- **Component Performance Analysis** (Individual indicator effectiveness)
- **Backtesting Framework** (61.8% win rate validation)
- **What-If Simulator** (Parameter optimization)
- **Statistical Validation** (Significance testing)

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Quantum_Market_Breadth.git
cd Quantum_Market_Breadth

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your Twelve Data API key to .env

# Run with Docker (recommended)
docker-compose up

# Or run locally
uvicorn src.main:app --reload --port 8000
