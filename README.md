# Reversal 2.0

`Reversal2.0.ipynb` is a research notebook for short-term reversal analysis and option profitability confidence estimation.

## Notebook Contents

1. `Probability of Success Reversal`
   Measures how often a ticker recovers after a large intraday drop using CSV data under `reversal_data/`.
2. `Black Scholes Methods for Profitability Confidence Interval`
   Estimates option profitability confidence with a Black-Scholes pricing framework and bootstrap simulations.
3. `Geometric Brownian Motion Methods for Profitability Confidence Interval`
   Simulates option outcomes with GBM paths under configurable drift and volatility assumptions.
4. `Rolling Sigma`
   Plots rolling annualized volatility for selected tickers.

## Data Layout

Place per-ticker CSV files in:

```text
reversal_data/
  TQQQ.csv
  SOXL.csv
  ...
```

The notebook expects columns such as `Date`, `Open`, `High`, `Low`, `Adj Close`, and `Max Drop`.

## Dependencies

Install the Python packages used in the notebook:

```bash
pip install numpy pandas matplotlib scipy yfinance notebook
```

## Usage

Open the notebook from the repository root so `Path.cwd()` resolves correctly:

```bash
jupyter notebook Reversal2.0.ipynb
```

Update the user-config sections inside each code cell to change:

- Tickers
- Drop threshold and recovery target
- Strike, call cost, expiry date
- Confidence level, risk-free rate, bootstrap count
- GBM path count and volatility method

## Output

Depending on the cell settings, the notebook can generate:

- Reversal success-rate comparisons
- Option profitability confidence intervals
- Rolling sigma charts
- `success_rate_comparison.png`
