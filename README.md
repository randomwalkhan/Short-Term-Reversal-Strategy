# Reversal 2.3.3

`Reversal2.3.3.ipynb` is the current research notebook for short-term reversal analysis and option profitability confidence estimation.

`Reversal2.3.3.ipynb` 是当前版本的研究型 notebook，用于短期反转研究和期权盈利概率评估。

Update note: Reversal 2.3.3 filters out names with fewer than 10 historical samples and trims the notebook ranking outputs to the top 15 tickers.

更新说明：Reversal 2.3.3 过滤掉历史样本数少于 10 的 ticker，并把 notebook 的排名输出收敛到前 15 名。

`Reversal2.3.ipynb`、`Reversal2.2.1.ipynb`、`Reversal2.1.ipynb` and `Reversal2.0.ipynb` are preserved as earlier version snapshots.

`Reversal2.3.ipynb`、`Reversal2.2.1.ipynb`、`Reversal2.1.ipynb` 和 `Reversal2.0.ipynb` 作为更早版本快照保留。

![Reversal 2.3.3 Universe Comparison](assets/reversal_2_3_3_universe_comparison.png)

## Featured Result | 重点结果

The staged-entry Reversal 2.3.3 workflow currently defaults to `qqq_only_filtered`, and the latest five-universe comparison with a `signal_days > 10` filter still selects it as the best universe, with the highest win rate, strongest return, and a materially lower drawdown than the broader filtered universes.

分批建仓版 Reversal 2.3.3 工作流当前默认使用 `qqq_only_filtered`，而且在最新一轮加入 `signal_days > 10` 过滤的五组 universe 对比里，它依然是最优选择：胜率最高、收益最强，而且回撤显著低于更宽的 filtered universe。

Full comparison summary:

完整对比汇总：

- [reversal_2_3_3_universe_comparison.csv](results/reversal_2_3_3_universe_comparison/reversal_2_3_3_universe_comparison.csv)

| Universe | Signal-Filtered Size | Win Rate | Return | Max DD | Equity Output | Trade Output |
|---|---:|---:|---:|---:|---|---|
| `qqq_only_filtered` | `63` | `61.43%` | `+610.38%` | `-31.55%` | [equity](results/reversal_2_3_3_universe_comparison/qqq_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/qqq_only_filtered_trades.csv) |
| `nasdaq_only_filtered` | `650` | `55.19%` | `+147.30%` | `-65.59%` | [equity](results/reversal_2_3_3_universe_comparison/nasdaq_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/nasdaq_only_filtered_trades.csv) |
| `qqq_spy_filtered` | `249` | `55.07%` | `+125.54%` | `-42.87%` | [equity](results/reversal_2_3_3_universe_comparison/qqq_spy_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/qqq_spy_filtered_trades.csv) |
| `nasdaq_spy_filtered` | `796` | `54.92%` | `+128.43%` | `-60.48%` | [equity](results/reversal_2_3_3_universe_comparison/nasdaq_spy_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/nasdaq_spy_filtered_trades.csv) |
| `spy_only_filtered` | `239` | `53.81%` | `+62.64%` | `-51.67%` | [equity](results/reversal_2_3_3_universe_comparison/spy_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/spy_only_filtered_trades.csv) |

## License | 版权

This repository is released under an explicit `All Rights Reserved` copyright
notice. It is not an open-source project, and reuse, copying, modification,
distribution, or derivative work creation requires prior written permission.

本仓库采用明确的 `All Rights Reserved` 版权声明，并非开源项目；复制、修改、分发、
再发布或基于本仓库创建衍生作品，均需事先获得书面许可。

## Overview | 项目简介

This project focuses on identifying large intraday drawdowns, evaluating whether prices reverse over the next few trading days, and estimating the return distribution of related call-option trades.

本项目主要研究三件事：识别日内大幅下跌、评估未来几个交易日内的价格反转概率，以及估计相关看涨期权交易的收益分布。

The notebook works from CSV files stored under `reversal_data/`, Reversal 2.3 adds a dynamic universe builder, Reversal 2.3.1 adds a staged-entry options backtest plus universe-comparison scripts, Reversal 2.3.2 defaults the research flow to `qqq_only_filtered` with an in-notebook data-refresh step, and Reversal 2.3.3 adds minimum-sample filtering, top-15 ranked output, and an updated five-universe comparison under `signal_days > 10`.

Notebook 通过 `reversal_data/` 目录下的 CSV 数据运行；Reversal 2.3 新增了动态股票池构建器，Reversal 2.3.1 新增了分批建仓的回测和股票池横向比较脚本，Reversal 2.3.2 把默认研究流程切到 `qqq_only_filtered` 并在 notebook 内加入了数据刷新步骤，而 Reversal 2.3.3 则进一步加入了最小样本过滤、前 15 名输出，以及基于 `signal_days > 10` 的五组 universe 新对比。

Before running the main analysis notebook, you can use `update_reversal_csv.ipynb` to download and refresh the input CSV files.

在运行主分析 notebook 之前，可以先使用 `update_reversal_csv.ipynb` 下载并更新输入用的 CSV 数据。

## Workflow | 推荐流程

1. Run `update_reversal_csv.ipynb` to download or refresh market data into `reversal_data/`.  
   先运行 `update_reversal_csv.ipynb`，把市场数据下载或更新到 `reversal_data/`。
2. Run `Reversal2.3.3.ipynb` for QQQ-only universe construction, reversal success analysis, in-notebook CSV refresh, live setup screening, call-entry planning, option confidence intervals, GBM simulation, and rolling sigma plots.  
   再运行 `Reversal2.3.3.ipynb`，完成 QQQ-only 股票池构建、反转成功率分析、notebook 内 CSV 刷新、实时 setup 筛选、call 入场规划、期权置信区间、GBM 模拟和滚动波动率可视化。
3. Run `compare_reversal_2_3_3_universes.py` if you want to compare backtest performance across the five filtered universes after applying the `signal_days > 10` gate.  
   如果你想在加上 `signal_days > 10` 过滤之后，比较五组 filtered universe 在当前分批 50% 建仓规则下的表现，再运行 `compare_reversal_2_3_3_universes.py`。

## Notebook Contents | Notebook 内容

1. `Probability of Success Reversal`  
   Measures how often a ticker recovers after a large intraday drop using CSV data under `reversal_data/`.  
   使用 `reversal_data/` 中的 CSV 数据，统计个股在出现较大日内跌幅后，未来若干交易日内发生反弹的成功率。

2. `QQQ-Only Universe Builder`  
   Builds the default `qqq_only_filtered` candidate pool from local QQQ constituents, filtered by minimum market cap and price.  
   基于本地 QQQ 成分股构建默认的 `qqq_only_filtered` 候选池，并按最小市值和股价进行过滤。

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
jupyter notebook Reversal2.3.3.ipynb
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
- `update_reversal_data.py` | Refresh `qqq_only_filtered` CSV datasets from Yahoo Finance. | 从 Yahoo Finance 刷新 `qqq_only_filtered` 所需的 CSV 数据。
- `Reversal2.3.3.ipynb` | Current main notebook. | 当前主 notebook。
- `Reversal2.3.ipynb` | Previous notebook snapshot with the Nasdaq + SPY universe builder. | 上一版本 notebook 快照，包含 Nasdaq + SPY 股票池构建器。
- `Reversal2.2.1.ipynb` | Previous notebook snapshot. | 上一版本 notebook 快照。
- `Reversal2.1.ipynb` | Earlier notebook snapshot. | 更早版本 notebook 快照。
- `Reversal2.0.ipynb` | Earlier notebook snapshot. | 更早版本 notebook 快照。
- `backtest_reversal_2_3_calls.py` | Reversal 2.3 call backtest with top-2 daily ranking, weighted sizing, and broad universe selection. | Reversal 2.3 的 call 回测脚本，包含每日前二打分、加权仓位和广义股票池。
- `backtest_reversal_2_3_1_calls.py` | Reversal 2.3.1 call backtest with staggered 50% entries and up to two concurrent positions. | Reversal 2.3.1 的 call 回测脚本，采用分批 50% 建仓和最多两个同时持仓。
- `backtest_reversal_2_3_3_calls.py` | Reversal 2.3.3 call backtest with `qqq_only_filtered` and a minimum 10-match signal gate. | Reversal 2.3.3 的 call 回测脚本，默认使用 `qqq_only_filtered`，并要求至少 10 个历史匹配样本。
- `compare_reversal_2_3_1_universes.py` | Compare Reversal 2.3.1 across multiple ticker-list universes. | 比较 Reversal 2.3.1 在多个股票池下的表现。
- `compare_reversal_2_3_3_universes.py` | Compare five filtered universes under Reversal 2.3.3 after applying `signal_days > 10`. | 在 `signal_days > 10` 过滤后，比较 Reversal 2.3.3 下五组 filtered universe 的表现。
- `reversal_universe.py` | Shared Nasdaq + SPY universe builder used by the notebook and backtest. | notebook 和回测脚本共用的 Nasdaq + SPY 股票池构建模块。
- `spy_tickers.txt` | Local SPY constituents source used when building the broad universe. | 构建广义股票池时使用的本地 SPY 成分股文件。
- `qqq_tickers.txt` | Local QQQ constituents source used for universe comparison. | 股票池比较时使用的本地 QQQ 成分股文件。
- `README.md` | Project documentation. | 项目说明文件。

## Outputs | 输出结果

Depending on the cell settings, the notebook can generate:

根据不同单元格设置，notebook 可以输出：

- Reversal success-rate comparisons | 反转成功率对比结果
- Option profitability confidence intervals | 期权盈利置信区间
- Rolling sigma charts | 滚动波动率图表
- `success_rate_comparison.png`
