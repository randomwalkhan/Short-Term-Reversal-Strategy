# Reversal 2.3

`Reversal2.3.ipynb` is the current research notebook for short-term reversal analysis and option profitability confidence estimation.

`Reversal2.3.ipynb` 是当前版本的研究型 notebook，用于短期反转研究和期权盈利概率评估。

`Reversal2.2.1.ipynb`、`Reversal2.1.ipynb` and `Reversal2.0.ipynb` are preserved as earlier version snapshots.

`Reversal2.2.1.ipynb`、`Reversal2.1.ipynb` 和 `Reversal2.0.ipynb` 作为更早版本快照保留。

## Overview | 项目简介

This project focuses on identifying large intraday drawdowns, evaluating whether prices reverse over the next few trading days, and estimating the return distribution of related call-option trades.

本项目主要研究三件事：识别日内大幅下跌、评估未来几个交易日内的价格反转概率，以及估计相关看涨期权交易的收益分布。

The notebook works from CSV files stored under `reversal_data/`, and Reversal 2.3 also adds a dynamic Nasdaq + SPY universe builder backed by an official Nasdaq screener feed plus local SPY holdings.

Notebook 通过 `reversal_data/` 目录下的 CSV 数据运行；Reversal 2.3 还新增了一个基于 Nasdaq 官方 screener 数据和本地 SPY 成分股文件的动态股票池构建器。

Before running the main analysis notebook, you can use `update_reversal_csv.ipynb` to download and refresh the input CSV files.

在运行主分析 notebook 之前，可以先使用 `update_reversal_csv.ipynb` 下载并更新输入用的 CSV 数据。

## Workflow | 推荐流程

1. Run `update_reversal_csv.ipynb` to download or refresh market data into `reversal_data/`.  
   先运行 `update_reversal_csv.ipynb`，把市场数据下载或更新到 `reversal_data/`。
2. Run `Reversal2.3.ipynb` for reversal success analysis, Nasdaq + SPY universe construction, live setup screening, call-entry planning, option confidence intervals, GBM simulation, and rolling sigma plots.  
   再运行 `Reversal2.3.ipynb`，完成反转成功率分析、Nasdaq + SPY 股票池构建、实时 setup 筛选、call 入场规划、期权置信区间、GBM 模拟和滚动波动率可视化。

## Notebook Contents | Notebook 内容

1. `Probability of Success Reversal`  
   Measures how often a ticker recovers after a large intraday drop using CSV data under `reversal_data/`.  
   使用 `reversal_data/` 中的 CSV 数据，统计个股在出现较大日内跌幅后，未来若干交易日内发生反弹的成功率。

2. `Nasdaq + SPY Universe Builder`  
   Builds a broader candidate pool from current Nasdaq listings plus SPY constituents, filtered by minimum market cap and price.  
   从当前 Nasdaq 上市股票和 SPY 成分股中构建更大的候选池，并按最小市值和股价进行过滤。

3. `Live Reversal Setup Screener`  
   Uses today's near-real-time price to infer the current intraday drawdown for each ticker, then measures how often similar or worse historical drops recovered a user-defined fraction of the signal-day drawdown within the next N trading days.  
   使用当日近实时价格推断每个 ticker 当前的日内跌幅，再回看过去一段观察窗口内“至少同等严重”的历史下跌日，统计未来 N 个交易日内回补 signal-day 跌幅指定比例的成功率。

4. `Option Execution Planner for Call Entries`  
   Pulls option chains for the chosen ticker, filters toward near-ATM calls in the 21-40 trading-day range, and translates the strategy into reference entry, take-profit, and stop-loss levels.  
   拉取所选 ticker 的期权链，筛选 21-40 个交易日范围内、接近 ATM 的 call，并把策略转成参考入场价、止盈价和止损价。

5. `Black Scholes Methods for Profitability Confidence Interval`  
   Estimates option profitability confidence with a Black-Scholes pricing framework and bootstrap simulations.  
   结合 Black-Scholes 定价框架和 bootstrap 模拟，估计期权策略收益区间及其置信水平。

6. `Geometric Brownian Motion Methods for Profitability Confidence Interval`  
   Simulates option outcomes with GBM paths under configurable drift and volatility assumptions.  
   在可调的漂移率和波动率假设下，使用几何布朗运动模拟期权收益结果。

7. `Rolling Sigma`  
   Plots rolling annualized volatility for selected tickers.  
   绘制所选股票的滚动年化波动率曲线。

## Data Layout | 数据结构

Place per-ticker CSV files in:

请将每个股票对应的 CSV 文件放在以下目录中：

```text
reversal_data/
  TQQQ.csv
  SOXL.csv
  ...
```

The notebook expects columns such as `Date`, `Open`, `High`, `Low`, `Adj Close`, and `Max Drop`.

Notebook 默认读取的主要字段包括 `Date`、`Open`、`High`、`Low`、`Adj Close` 和 `Max Drop`。

`update_reversal_csv.ipynb` is designed to generate these CSV files automatically from Yahoo Finance data.

`update_reversal_csv.ipynb` 的用途就是从 Yahoo Finance 自动生成这些 CSV 文件。

## Dependencies | 依赖环境

Install the Python packages used in the notebook:

安装 notebook 所需的 Python 包：

```bash
pip install numpy pandas matplotlib scipy yfinance notebook
```

## Usage | 使用方法

Open the notebook from the repository root so `Path.cwd()` resolves correctly:

请在仓库根目录打开 notebook，这样 `Path.cwd()` 才会正确指向项目目录：

```bash
jupyter notebook Reversal2.3.ipynb
```

To refresh the CSV data first, open:

如果你想先更新 CSV 数据，可以打开：

```bash
jupyter notebook update_reversal_csv.ipynb
```

Update the user-config sections inside each code cell to change:

你可以在各代码单元的用户配置区修改以下参数：

- Tickers | 股票列表
- Drop threshold and recovery target | 下跌触发阈值与反弹目标
- Strike, call cost, expiry date | 行权价、期权成本、到期日
- Confidence level, risk-free rate, bootstrap count | 置信水平、无风险利率、bootstrap 次数
- GBM path count and volatility method | GBM 路径数与波动率设定方式

For `update_reversal_csv.ipynb`, the main configurable inputs are:

对于 `update_reversal_csv.ipynb`，主要可调参数包括：

- Tickers | 股票列表
- Start date and end date | 数据起止日期
- Output directory | 输出目录

## Repository Files | 仓库文件

- `update_reversal_csv.ipynb` | Download and prepare CSV market data before analysis. | 在分析前下载并整理 CSV 市场数据。
- `Reversal2.3.ipynb` | Current main notebook with the new Nasdaq + SPY universe builder. | 当前主 notebook，包含新的 Nasdaq + SPY 股票池构建器。
- `Reversal2.2.1.ipynb` | Previous notebook snapshot. | 上一版本 notebook 快照。
- `Reversal2.1.ipynb` | Earlier notebook snapshot. | 更早版本 notebook 快照。
- `Reversal2.0.ipynb` | Earlier notebook snapshot. | 更早版本 notebook 快照。
- `backtest_reversal_2_3_calls.py` | Reversal 2.3 call backtest with top-2 daily ranking, weighted sizing, and broad universe selection. | Reversal 2.3 的 call 回测脚本，包含每日前二打分、加权仓位和广义股票池。
- `reversal_universe.py` | Shared Nasdaq + SPY universe builder used by the notebook and backtest. | notebook 和回测脚本共用的 Nasdaq + SPY 股票池构建模块。
- `spy_tickers.txt` | Local SPY constituents source used when building the broad universe. | 构建广义股票池时使用的本地 SPY 成分股文件。
- `README.md` | Project documentation. | 项目说明文件。

## Outputs | 输出结果

Depending on the cell settings, the notebook can generate:

根据不同单元格设置，notebook 可以输出：

- Reversal success-rate comparisons | 反转成功率对比结果
- Option profitability confidence intervals | 期权盈利置信区间
- Rolling sigma charts | 滚动波动率图表
- `success_rate_comparison.png`
