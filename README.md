#  Intraday Reversal Strategy Backtester

This project is a Python-based quantitative tool designed for traders who seek to **buy the dip** and profit from **short-term reversals**. It systematically identifies significant intraday drawdowns, evaluates recovery potential across future trading days, and quantifies the odds of success. It serves as a **signal generator and validation framework** for short-term reversal strategies, including equity or options trading.

---

##  Part 1: Success Odds Analysis

This module identifies potential **buy-the-dip signals** based on large intraday drops and tracks the recovery performance over a user-defined forward window.

---

###  How It Works

1. **Loads cleaned OHLC data** from an Excel workbook. Each sheet contains 1-year daily data for a stock ticker.
2. **Scans each trading day** for intraday drops that exceed the user-defined threshold (`DROP_THR`).
3. **Measures recovery** as the maximum price rebound over the next `N` trading days.
4. **Marks a signal as "successful"** if the recovery surpasses the user-defined `RECOVER_TARGET`.
5. **Calculates a success rate**, based on how often signals meet the recovery criteria.

---

###  Sample Configuration

```python
# -------- USER CONFIGURATION --------
FILE_PATH       = "Reversal.xlsx"          # Excel file with OHLC data
TICKERS         = ["SMCI"]                 # Ticker(s) to analyze
DROP_THR        = 0.04                     # ≥ 4% intraday drop triggers signal
RECOVER_TARGET  = 0.8                      # ≥ 80% recovery defines success
LOOKAHEAD       = [1, 2, 3, 4, 5]          # Lookahead windows: T+N days
```
### Sample Output

<img width="472" height="148" alt="Screenshot 2025-07-23 at 1 42 22 PM" src="https://github.com/user-attachments/assets/39d6587c-b6e9-4934-af30-32c674085206" />

---

##  Part 2: Confidence Interval of Option Profitability

After identifying dip-reversal signals in Part 1, this module estimates the **profit potential** of buying call options on those days. It uses historical recovery data to simulate returns and builds a **confidence interval (CI)** for expected performance — helping traders evaluate risk-adjusted payoff scenarios.

---

###  Objective

This section helps answer:

>  *“If I buy a call option on a reversal signal day, what’s the expected return distribution?”*

Using a bootstrapped simulation of price paths based on historical recovery behavior, it estimates call option returns via the Black-Scholes model.

---
### How it works
1. Filters signal days from Part 1 based on DROP_THR.
2. Collects log returns of adjusted close from signal date to T+N.
3. Bootstraps thousands of hypothetical return paths using sampled log returns.
4. Simulates option payoff with the Black-Scholes formula for each bootstrapped price.
5. Calculates return %: Return = (Option Payoff − Cost)/Cost
6. Generates confidence intervals of simulated returns for each T+N lookahead window.
---

###  Sample Configuration

```python
TICKERS_TO_RUN   = TICKERS                # subset of tickers from Part 1
CURRENT_SPOT     = yf.Ticker(...).info    # fetching real-time price
STRIKE           = 50                    # strike price
CALL_COST        = 5                   # option premium (5 * 100)
IMPLIED_VOL      = 0.75                 # fallback IV if not using rolling σ
USE_ROLLING_SIGMA= True                   # True for overrides IV with historical σ
ROLL_WIN         = 20                     # rolling window for σ = 4 weeks
CURRENT_DATE     = "2025-07-21"           # pricing date
EXPIRY_DATE      = "2025-08-22"           # expiry date
LOOKAHEAD        = [1, 2, 3, 4, 5]        # 5 days recovery horizons
CONF_LEVEL       = 0.9                    # confidence level
DROP_THR         = 0.04                   # filter: drop ≥ threshold
RISK_FREE        = 0.035                  # annualized r
BOOT_SIMS        = 30_000                 # number of bootstraps
```

### Sample Output

<img width="569" height="173" alt="Screenshot 2025-07-23 at 1 41 51 PM" src="https://github.com/user-attachments/assets/506c1c55-4e4c-46ed-a123-0d94bd82f0e5" />

---

## Part 3: GBM-Simulated Option Profitability (Unconditional)

In this section, we use a **Geometric Brownian Motion (GBM)** model to estimate the **expected profitability of call options**, without conditioning on a specific dip-reversal signal. This is useful for evaluating option performance under a more general forecast, relying on historical drift and volatility patterns or market-assumed parameters.

---

### Objective

This model answers:

>  *“What is the expected return range of this call option, assuming stock follows a GBM process between now and expiry?”*

Unlike Part 2, which conditions on reversal signals, this model simulates stock price paths **unconditionally** and prices call options across those paths using the Black-Scholes formula.

---
### How it works

1. Compute historical daily log returns** from the adjusted close prices of the selected ticker.
2. Estimate drift (μ):
   - If `DRIFT_MODE = "hist"`: use sample mean of historical log returns.
   - If `DRIFT_MODE = "rf"`: use risk-neutral drift = `RISK_FREE / 252`.
     
     $$\mu = \frac{r}{252}$$
     
3. Estimate volatility (σ):
   - By default, use the sample standard deviation of log returns.
   - If `SIGMA_OVERRIDE` is set (e.g., rolling or implied σ), use that instead.
4. Simulate stock paths under the GBM model:
   
   $$\ln S_T = \left( \mu - \frac{1}{2} \sigma^2 \right) T + \sigma \sqrt{T} Z$$
   
   where $Z \sim \mathcal{N}(0,1) $, and T is measured in trading days.
5. Price call options on simulated future prices using the Black-Scholes formula:

   $$C = S \cdot \Phi(d_1) - K e^{-r \tau} \cdot \Phi(d_2)$$

6. Calculate return for each simulated path:

   $$\text{Return} = \frac{\text{Call Price} - \text{Cost}}{\text{Cost}}$$

7. Summarize the simulation results for each `LOOKAHEAD` window:
   - Mean return
   - Confidence interval bounds (e.g., 90% CI)
   - Annualized volatility used

### Sample Configuration

```python
TICKERS_TO_RUN = TICKERS                # subset of loaded tickers
SPOT_NOW       = CURRENT_SPOT           # current stock price
STRIKE         = STRIKE                 # strike price
CALL_COST      = CALL_COST              # premium paid per share
DAYS_TO_EXP    = DAYS_TO_EXP            # calendar days to expiry
LOOKAHEAD      = [1, 2, 3, 4, 5]         # lookahead trading days
CONF_LEVEL     = 0.9                    # 90% confidence interval
DRIFT_MODE     = "rf"                   # "rf" = risk-free drift, "hist" = historical mean
PATHS          = 50_000                 # number of GBM paths
RISK_FREE      = 0.035                  # annualized risk-free rate
SIGMA_OVERRIDE = iv_use                 # optional override for annualized vol
```
### Sample Output

<img width="577" height="153" alt="Screenshot 2025-07-23 at 1 41 11 PM" src="https://github.com/user-attachments/assets/4fbf7f6f-6cf3-4cd7-a40d-a1a07b5c43cf" />

---

## Part 4: Visualizing Rolling Volatility (σ)

This section helps traders visualize the **rolling annualized volatility** for each stock, providing insight into the historical behavior of price fluctuations. It supports more informed decisions when choosing between using **rolling σ** vs. **implied volatility** in Part 2 and Part 3.

---

### Objective

> *“How volatile has this stock been over time, and how reliable is my volatility estimate?”*

This module computes and plots the **rolling standard deviation** of daily log returns (annualized), offering a clear view of volatility trends that impact option pricing and risk assumptions.

---

### How it works
1. Load and clean OHLC data for each ticker (from Reversal.xlsx, if not already in memory)
2. Compute log returns
3. Apply a rolling window (win days) to calculate daily volatility
4. Multiply by √252 to annualize
5. Plot the rolling σ lines for each ticker on the same chart

###  Sample Configuration

```python
rolling_window = 20  # Rolling window (in trading days)

plot_rolling_sigma(["TSLA", "SMCI", "SOXL"], win=rolling_window)
```
### Sample Output
<img width="815" height="403" alt="Screenshot 2025-07-23 at 1 29 25 PM" src="https://github.com/user-attachments/assets/24aafaee-dcfd-42e3-9de8-79a306e45d92" />

---

## Part 5: Stock Screener for Short-Term Reversal Candidates

This module helps filter U.S. stocks that are **suitable for short-term reversal strategies**, by applying customizable screening criteria such as P/E ratio, market cap, dividend yield, volatility, and price drops.

It screens across **S&P 500** and **NASDAQ-100** tickers in real-time using Yahoo Finance data.

I removed BF.B and BRK.B from the list as they consistently trigger Yahoo Finance errors due to their dot-in-symbol format

---

### How It Works

1. Loads ticker lists from Wikipedia (S&P 500 + NASDAQ-100).
2. *Fetches 1-month OHLCV data using `yfinance` for each ticker.
3. Computes:
   - Daily percentage price change
   - 20-day rolling volatility (annualized)
4. Pulls company fundamentals:
   - Market Cap
   - P/E Ratio (trailing)
   - Dividend Yield
   - Daily Volume
5. Applies user-defined filters:
   - `max_pe`: maximum acceptable P/E ratio
   - `min_market_cap`: minimum market cap in dollars (e.g., `1e10` for $10B)
   - `min_change_pct`: price change filter (e.g., `-3` for stocks dropping more than 3%)
   - `min_dividend_yield`: minimum yield in %
   - `min_volatility`: minimum annualized volatility (from 20D rolling σ)
   - `min_volume`: minimum daily trading volume

6. Returns a sorted DataFrame of matching tickers with relevant metrics.

---

###  Sample Inputs

```python
Maximum P/E Ratio:            45
Minimum Market Cap:           15e10
Minimum Daily Change %:      -4
Minimum Dividend Yield (%):   0
Minimum 20D Volatility:       0.5
Minimum Daily Volume:         2e7
```
### Sample Output

<img width="642" height="250" alt="Screenshot 2025-07-23 at 2 37 02 PM" src="https://github.com/user-attachments/assets/7267cddf-344d-4f78-9411-eb456cb4767f" />

---

## Repository Contents

The following files are included in this repository:

| File Name         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `README.md`       | Full documentation and usage guide for the reversal strategy toolkit.       |
| `Reversal.ipynb`  | Interactive Jupyter Notebook containing all analysis code across Parts 1–4. |
| `Reversal.xlsx`   | Input data file containing historical OHLC prices for selected tickers.     |

### Data Coverage

As of July 23, 2025, the `Reversal.xlsx` file includes the following tickers:

- `TQQQ`
- `SMCI`
- `SOXL`
- `COIN`
- `MSTR`
- `HOOD`
- `PLTR`

Each ticker is saved as a separate worksheet (tab) within the Excel file. Users may manually append additional tickers to this file using the same format (with columns like `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`).

###  Data Currency Note

- The `Reversal.xlsx` file includes stock data **up to July 23, 2025**.
- Users can **manually update or append new data** to this file using [Yahoo Finance](https://finance.yahoo.com/) or `yfinance`, as long as they **maintain the same column structure and sheet naming convention** (e.g., one ticker per sheet with columns like `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`).

### To run this project

Make sure Python 3.9+ is installed, and install dependencies:

```bash
pip install -r requirements.txt

