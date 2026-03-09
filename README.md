# Reversal 2.0

`Reversal2.0.ipynb` is a research notebook for short-term reversal analysis and option profitability confidence estimation.

`Reversal2.0.ipynb` 是一个用于短期反转研究和期权盈利概率评估的研究型 notebook。

## Overview | 项目简介

This project focuses on identifying large intraday drawdowns, evaluating whether prices reverse over the next few trading days, and estimating the return distribution of related call-option trades.

本项目主要研究三件事：识别日内大幅下跌、评估未来几个交易日内的价格反转概率，以及估计相关看涨期权交易的收益分布。

The notebook works from CSV files stored under `reversal_data/` and uses configurable thresholds for signal detection, recovery measurement, volatility estimation, and option pricing.

Notebook 通过 `reversal_data/` 目录下的 CSV 数据运行，并允许用户自定义信号筛选阈值、反弹判定标准、波动率估计方式和期权定价参数。

## Notebook Contents | Notebook 内容

1. `Probability of Success Reversal`  
   Measures how often a ticker recovers after a large intraday drop using CSV data under `reversal_data/`.  
   使用 `reversal_data/` 中的 CSV 数据，统计个股在出现较大日内跌幅后，未来若干交易日内发生反弹的成功率。

2. `Black Scholes Methods for Profitability Confidence Interval`  
   Estimates option profitability confidence with a Black-Scholes pricing framework and bootstrap simulations.  
   结合 Black-Scholes 定价框架和 bootstrap 模拟，估计期权策略收益区间及其置信水平。

3. `Geometric Brownian Motion Methods for Profitability Confidence Interval`  
   Simulates option outcomes with GBM paths under configurable drift and volatility assumptions.  
   在可调的漂移率和波动率假设下，使用几何布朗运动模拟期权收益结果。

4. `Rolling Sigma`  
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
jupyter notebook Reversal2.0.ipynb
```

Update the user-config sections inside each code cell to change:

你可以在各代码单元的用户配置区修改以下参数：

- Tickers | 股票列表
- Drop threshold and recovery target | 下跌触发阈值与反弹目标
- Strike, call cost, expiry date | 行权价、期权成本、到期日
- Confidence level, risk-free rate, bootstrap count | 置信水平、无风险利率、bootstrap 次数
- GBM path count and volatility method | GBM 路径数与波动率设定方式

## Outputs | 输出结果

Depending on the cell settings, the notebook can generate:

根据不同单元格设置，notebook 可以输出：

- Reversal success-rate comparisons | 反转成功率对比结果
- Option profitability confidence intervals | 期权盈利置信区间
- Rolling sigma charts | 滚动波动率图表
- `success_rate_comparison.png`
