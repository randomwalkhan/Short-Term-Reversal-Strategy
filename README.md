# Reversal 3.2.1

<!-- reversal-3.2-live:start -->
## Reversal 3.2.2 Live Paper Test

- Latest checkpoint (ET): `2026-04-14 01:40:06 EDT`
- Equity: `$13,188.00` | Realized: `$3,145.00` | Unrealized: `$43.00` | Open positions: `1`
- Today closed trades: `0`
- Current slot: `share_ext_0140`
- Universe: `qqq_plus_leverage_etfs`
- Chart windows: `Overall / 1D / 1W / 1M` (default open panel: `Overall`)

### Current Open Positions

```text
ticker asset_type execution_mode instrument  units  cash_spent  current_position_value  current_price  unrealized_pnl  unrealized_return_pct  business_days_held
  REGN      share share_fallback       REGN      8      5916.0                  5959.0         744.88            43.0                   0.73                   1
```

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](assets/reversal_3_2_1_live_equity_overall.png?v=20260414014006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](assets/reversal_3_2_1_live_equity_1d.png?v=20260414014006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](assets/reversal_3_2_1_live_equity.png?v=20260414014006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](assets/reversal_3_2_1_live_equity_1m.png?v=20260414014006)

</details>

- [Full live dashboard](results/reversal_3_2_1_live/README.md)
- [Live trades csv](results/reversal_3_2_1_live/live_trades.csv)
- [Live equity csv](results/reversal_3_2_1_live/live_equity.csv)
<!-- reversal-3.2-live:end -->

`Reversal3.2.1.ipynb` is the current research notebook for short-term reversal analysis and option profitability confidence estimation.

`Reversal3.2.1.ipynb` 是当前版本的研究型 notebook，用于短期反转研究和期权盈利概率评估。

## Strategy Summary | 策略总结

This repository studies a short-term reversal call-buying setup built around large intraday drawdowns, historical recovery probability, and staged optimization. The current official version is `Reversal 3.2.1`.

本仓库研究的是一套基于“日内大跌后短期反转”的 call 策略，通过历史反弹成功率和逐阶段优化来推进。目前官方版本是 `Reversal 3.2.1`。

- Official universe: `qqq_plus_leverage_etfs = qqq_only_filtered + SOXL + UPRO`
- Official filters: `60d` lookback, `matched_signals >= 10`, `minimum current drop > 0.5%`
- Trade framing: near-ATM calls, ~`30` DTE in backtests, `+10% / +15% / -10%` exit ladder
- Live paper test: no-lookahead scheduled scans with an option-liquidity gate, share fallback, and GitHub-published dashboard output
- Research discipline: `RESEARCH_GUARDRAILS.md`

## Research Journey | 研究历程

This project started from something I kept seeing on my screen: after a sharp down day, some stocks would rebound surprisingly quickly over the next few sessions. I wanted to know which names actually behaved that way consistently, and whether that pattern was strong enough to support short-term reversal option trades rather than just a good-looking anecdote.

这个项目最开始其实是一个很朴素的观察：我发现有些股票在大跌后的几天里，经常会出现比较快的反弹。我当时想弄清楚，到底是哪些股票更容易出现这种走势，这种现象到底只是偶然，还是能被系统化地验证，并进一步转化成 short-term reversal option trades。

In the earliest `Reversal 1.x` style work and the preserved early notebooks such as `versions/notebooks/Reversal2.0.ipynb` and `versions/notebooks/Reversal2.1.ipynb`, I started with a very small legacy watchlist of roughly ten names. The scripts pulled one year of Yahoo Finance `Close`, `High`, and `Low` data, computed daily `Max Drop`, and then let me set three simple inputs: a same-day drop threshold, a recovery target, and a lookahead window. Once those were set, the code would tell me which tickers had the tendency to rebound by `x%` of the drop within `t + lookahead` trading days after a qualifying drawdown.

在最早的 `Reversal 1.x` 思路和现在仓库里保留下来的早期 notebook，例如 `versions/notebooks/Reversal2.0.ipynb`、`versions/notebooks/Reversal2.1.ipynb` 中，我一开始只研究大约十只左右的股票，也就是后面保留下来的 `legacy_watchlist_11` 这条线。那时的脚本会先从 Yahoo Finance 下载过去一年的 `Close`、`High`、`Low`，再计算每日的 `Max Drop`。然后我可以手动设定三个核心参数：当日跌幅阈值、反弹比例、以及 lookahead day。脚本跑完之后，会直接输出哪些 ticker 在满足当日跌幅条件后，能在 `t + lookahead` 的窗口里完成我设定的反弹比例。

After identifying the names that exhibited this behavior, I added an option layer. In those earlier versions, I could input expiry, implied volatility, entry price, risk-free rate, and related assumptions, then use Black-Scholes and GBM-based simulations to estimate day-by-day call PnL confidence intervals. That part was important because it moved the project from “which names bounce” to “what the option trade might actually look like.”

在找出这些更容易反弹的股票之后，我又继续往期权端推进。早期版本里，我已经可以输入到期日、隐含波动率、买入成本、无风险利率等参数，然后用 Black-Scholes 和基于 GBM 的模拟去估计买入对应 call 之后，在未来每天的盈利区间和置信水平。对我来说，这一步很关键，因为它把问题从“哪些股票容易反弹”推进到了“如果真的买对应的 call，这笔交易可能长什么样”。

From there, the project became a sequence of research upgrades rather than a single script:

从那里开始，这个项目就逐步从一个小脚本，变成了一条连续推进的研究路径：

1. Formalize the base signal.  
   我先把“日内大跌” formalize 成 signal day，再把“未来几天是否回补 signal-day 跌幅的 `70%`”定义成最基础的成功标准。这条主线后来延续到 `Reversal3.2.1.ipynb` 和 `backtest_reversal_3_1_calls.py` 里。
2. Test where the effect is actually strongest.  
   然后我开始比较不同 universe，确认这个现象究竟在哪类股票池里最稳定。`compare_reversal_2_3_3_universes.py` 这一步告诉我，效果最强的不是越广越好，而是更精选的 `qqq_only_filtered`。
3. Improve the signal before scaling execution.  
   在 universe 固定下来之后，我继续测试更短的观察窗口、minimum current drop、以及少量 leveraged ETF overlay，逐步形成了 `60d` window、`minimum current drop > 0.5%`、以及 `SOXL + UPRO` 这套现在的官方路径。
4. Add regime awareness and execution controls.  
   再往后，我开始研究 regime filter、holiday handling、option-liquidity gating、share fallback，以及如何把整个流程接成 no-lookahead 的 live paper runner，并持续把结果写回 GitHub dashboard。

Representative research outputs I still keep in the repo:

我现在仍然保留在仓库里的代表性研究输出包括：

| Research question | Script / notebook | Representative output |
|---|---|---|
| Which universe best captures the reversal effect? | `compare_reversal_2_3_3_universes.py` | [`reversal_2_3_3_universe_comparison.csv`](results/reversal_2_3_3_universe_comparison/reversal_2_3_3_universe_comparison.csv), [`reversal_2_3_3_universe_comparison.png`](assets/reversal_2_3_3_universe_comparison.png) |
| Which factor refinement improves the base setup most? | `backtest_reversal_article_variants.py` | [`reversal_article_variants_summary.csv`](results/reversal_2_4_article_variants/reversal_article_variants_summary.csv), [`reversal_2_4_article_variants.png`](assets/reversal_2_4_article_variants.png) |
| Does a minimum-drop threshold improve trade quality? | `backtest_reversal_2_5_min_drop_experiment.py` | [`reversal_2_5_min_drop_summary.csv`](results/reversal_2_5_min_drop_experiment/reversal_2_5_min_drop_summary.csv), [`reversal_2_5_min_drop_experiment.png`](assets/reversal_2_5_min_drop_experiment.png) |
| Do a few leveraged ETFs improve the official setup? | `backtest_reversal_3_1_leveraged_etf_experiment.py` | [`reversal_3_1_leveraged_etf_summary.csv`](results/reversal_3_1_leveraged_etf_experiment/reversal_3_1_leveraged_etf_summary.csv), [`reversal_3_1_leveraged_etf_experiment.png`](assets/reversal_3_1_leveraged_etf_experiment.png) |
| Should the strategy be paused in hostile market regimes? | `analyze_reversal_3_1_regime_score.py`, `analyze_reversal_3_1_regime_predictive_power.py` | [`reversal_3_1_regime_score.png`](assets/reversal_3_1_regime_score.png), [`reversal_3_1_regime_gating_comparison.png`](assets/reversal_3_1_regime_gating_comparison.png) |

That is how the current live-paper implementation emerged. I did not begin with execution infrastructure first. I started with a repeatable rebound pattern, narrowed the universe, improved the signal path, tested option framing, and only then connected the research into a scheduled live process with execution constraints.

这也就是现在这套 live paper implementation 的来历。对我来说，顺序一直是先确认价格恢复现象是否真实存在，再判断它在哪些 universe 和参数下最稳定，然后再去讨论期权执行、流动性约束和 live monitoring。现在仓库里的执行层，就是这条研究路径自然延伸出来的结果。

## Current Version | 当前官方版本

Release notes (`3.2.1`)
- Keep the official `3.1` research setup unchanged.
- Preserve the `3.2` live execution layer: NYSE holiday protection, option-liquidity gate, share fallback, and the `spread <= 15%` entry threshold.
- Patch the live system so open positions continue to update after hours, and share-fallback positions keep scanning take-profit / stop loss during after-hours, overnight, and pre-market.

版本说明（`3.2.1`）
- 官方研究口径仍沿用 `3.1`，不改 universe、lookback 和核心信号定义。
- live execution 继续沿用 `3.2`：NYSE 节假日保护、期权流动性门槛、share fallback，以及 `spread <= 15%` 的入场约束。
- 本次 patch 主要修复 live：收盘后若仍有持仓，净值曲线继续更新；若是 share fallback 持仓，则在 after-hours / overnight / pre-market 继续执行止盈与 stop loss 扫描。

## Featured Result | 重点结果

The official Reversal 3.2.1 backtest definition keeps the Reversal 3.1 research setup intact, including the dynamic trade-level filter `matched_signals >= 10`, the promoted `60d` historical lookback window, the `minimum current drop > 0.5%` entry filter, and the curated universe overlay `qqq_plus_leverage_etfs = qqq_only_filtered + SOXL + UPRO`. On the current data snapshot, the official Reversal 3.2.1 result remains `+1709.09%` total return, `-44.30%` max drawdown, `63.33%` win rate, and `4.28` Sharpe.

Reversal 3.2.1 的官方回测定义保留了 Reversal 3.1 的研究与执行口径不变，包括动态交易级过滤 `matched_signals >= 10`、提升后的 `60d` 历史观察窗口、`minimum current drop > 0.5%` 入场过滤，以及精选的 universe overlay：`qqq_plus_leverage_etfs = qqq_only_filtered + SOXL + UPRO`。在当前数据快照下，官方 Reversal 3.2.1 结果仍为：总收益 `+1709.09%`、最大回撤 `-44.30%`、胜率 `63.33%`、Sharpe `4.28`。

Backtest window: `2025-03-31` to `2026-03-31`.

回测区间：`2025-03-31` 至 `2026-03-31`。

Research discipline is documented in `RESEARCH_GUARDRAILS.md`; future upgrades
should be judged against those standards instead of curve quality alone.

研究纪律已写入 `RESEARCH_GUARDRAILS.md`；以后版本升级应按这些标准判断，而不是只看曲线是否更好看。

- [Reversal 3.2.1 equity](results/reversal_3_1/reversal_3_1_call_backtest_equity.csv)
- [Reversal 3.2.1 trades](results/reversal_3_1/reversal_3_1_call_backtest_trades.csv)
- [Reversal 3.2.1 plot](assets/reversal_3_1_call_backtest_equity.png)

![Reversal 3.2.1 Call Backtest](assets/reversal_3_1_call_backtest_equity.png)

## Optimization Path | 优化路径

The current strategy structure is intentionally sequential:

当前策略优化逻辑是明确分阶段推进的：

1. Select the best universe first.  
   先确定最优 universe。
2. Hold that universe fixed.  
   固定 universe，不再混入新的 universe 变化。
3. Compare factor / signal refinements on top of the chosen universe.  
   在选定 universe 之上比较新的因子或信号改造。
4. Promote the best-performing factor into the next official version.  
   把表现最好的因子升级为下一个正式版本。
5. Re-open the universe only when a controlled overlay experiment beats the official setup across more than one horizon.  
   只有当受控 overlay 实验在多个观察周期上都优于官方设定时，才重新打开 universe 层做升级。

### Stage 1: Universe Selection | 第一阶段：选 Universe

Reversal 2.3.3 compared five universes under the original dynamic `matched_signals >= 10` rule. The conclusion was clear: `qqq_only_filtered` remained the best universe and is therefore preserved in Reversal 2.5.3.

Reversal 2.3.3 在原始动态 `matched_signals >= 10` 规则下比较了五组 universe，结论非常明确：`qqq_only_filtered` 仍然最优，因此在 Reversal 2.5.3 中被保留。

Backtest window: `2025-03-17` to `2026-03-16`.

回测区间：`2025-03-17` 至 `2026-03-16`。

- [reversal_2_3_3_universe_comparison.csv](results/reversal_2_3_3_universe_comparison/reversal_2_3_3_universe_comparison.csv)
- Sharpe uses the U.S. 10Y Treasury yield on `2026-03-16` (`4.23%`) as the annual risk-free rate.

| Universe | Usable Tickers | Win Rate | Return | Max DD | Sharpe | Equity Output | Trade Output |
|---|---:|---:|---:|---:|---:|---|---|
| `qqq_only_filtered` | `97` | `59.02%` | `+552.91%` | `-32.46%` | `2.93` | [equity](results/reversal_2_3_3_universe_comparison/qqq_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/qqq_only_filtered_trades.csv) |
| `legacy_watchlist_11` | `10` | `54.15%` | `+81.27%` | `-31.57%` | `1.18` | [equity](results/reversal_2_3_3_universe_comparison/legacy_watchlist_11_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/legacy_watchlist_11_trades.csv) |
| `qqq_spy_filtered` | `501` | `53.53%` | `+54.38%` | `-43.24%` | `0.91` | [equity](results/reversal_2_3_3_universe_comparison/qqq_spy_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/qqq_spy_filtered_trades.csv) |
| `spy_only_filtered` | `491` | `52.92%` | `+36.28%` | `-43.26%` | `0.73` | [equity](results/reversal_2_3_3_universe_comparison/spy_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/spy_only_filtered_trades.csv) |
| `nasdaq_spy_filtered` | `1163` | `50.81%` | `-7.10%` | `-50.29%` | `0.23` | [equity](results/reversal_2_3_3_universe_comparison/nasdaq_spy_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/nasdaq_spy_filtered_trades.csv) |
| `nasdaq_only_filtered` | `830` | `49.59%` | `-30.21%` | `-50.51%` | `-0.15` | [equity](results/reversal_2_3_3_universe_comparison/nasdaq_only_filtered_equity.csv) | [trades](results/reversal_2_3_3_universe_comparison/nasdaq_only_filtered_trades.csv) |

![Reversal 2.3.3 Universe Comparison](assets/reversal_2_3_3_universe_comparison.png)

### Stage 2: Factor Selection | 第二阶段：选 Factor

After fixing the universe as `qqq_only_filtered`, the article-inspired comparison script tested volume rescaling, PCA de-factoring, kappa / s-score filtering, and shorter rolling windows. The `60d` window was the strongest factor upgrade and is therefore promoted into Reversal 2.4.

在把 universe 固定为 `qqq_only_filtered` 之后，论文启发的对比脚本继续测试了成交量 rescaling、PCA 去市场因素、kappa / s-score 过滤以及更短滚动窗口。最终 `60d` 窗口是最强的因子升级，因此被提升为 Reversal 2.4 的正式默认设置。

Backtest window: `2025-03-17` to `2026-03-16`.

回测区间：`2025-03-17` 至 `2026-03-16`。

Note: the stage 2 and stage 3 tables below use refreshed rerun results and include Sharpe ratios computed with the U.S. 10Y Treasury yield on `2026-03-16` (`4.23%`) as the annual risk-free rate.

说明：下面第二、第三阶段的表格都已经切换成最新重跑结果，并加入了 Sharpe ratio；Sharpe 统一使用 `2026-03-16` 的美国 10 年期国债收益率 `4.23%` 作为年化无风险利率。

- [article variants summary](results/reversal_2_4_article_variants/reversal_article_variants_summary.csv)
- [article variants equity](results/reversal_2_4_article_variants/reversal_article_variants_equity.csv)
- [article variants trades](results/reversal_2_4_article_variants/reversal_article_variants_trades.csv)

| Variant | Return | Max DD | Win Rate | Trades | Sharpe |
|---|---:|---:|---:|---:|---:|
| `Window 60d` | `+806.11%` | `-30.56%` | `61.00%` | `241` | `3.41` |
| `Original 2.3.3` | `+552.91%` | `-32.46%` | `59.02%` | `244` | `2.93` |
| `Add Volume` | `+364.25%` | `-37.58%` | `57.32%` | `239` | `2.44` |
| `Window 126d` | `+276.80%` | `-38.62%` | `56.83%` | `227` | `2.18` |
| `Window 252d + Recent Weight` | `+181.17%` | `-30.21%` | `56.31%` | `206` | `1.82` |
| `Kappa / s-score` | `+145.58%` | `-29.95%` | `55.61%` | `214` | `1.61` |
| `PCA Defactored` | `+23.89%` | `-42.39%` | `52.31%` | `216` | `0.60` |

![Reversal 2.4 Article Variants](assets/reversal_2_4_article_variants.png)

### Stage 3: Minimum Drop Filter | 第三阶段：选 Minimum Drop

After fixing both the universe and the `60d` factor, the next test was whether the live / backtest entry should require a minimum current drop. The `0.5%` threshold was the strongest improvement, so it is promoted into Reversal 2.5 as the new official execution filter.

在把 universe 和 `60d` 因子都固定下来之后，下一步测试的是是否要为 live / backtest 入场增加 minimum current drop 门槛。最终 `0.5%` 阈值表现最好，因此被提升为 Reversal 2.5 的正式执行过滤。

Backtest window: `2025-03-17` to `2026-03-16`.

回测区间：`2025-03-17` 至 `2026-03-16`。

- [minimum drop summary](results/reversal_2_5_min_drop_experiment/reversal_2_5_min_drop_summary.csv)
- [minimum drop equity](results/reversal_2_5_min_drop_experiment/reversal_2_5_min_drop_equity.csv)
- [minimum drop plot](assets/reversal_2_5_min_drop_experiment.png)

| Minimum Drop | Return | Max DD | Win Rate | Trades | Sharpe |
|---|---:|---:|---:|---:|---:|
| `0.0%` | `+806.11%` | `-30.56%` | `61.00%` | `241` | `3.41` |
| `0.5%` | `+1305.60%` | `-30.84%` | `62.08%` | `240` | `3.96` |
| `1.0%` | `+594.68%` | `-24.79%` | `60.44%` | `225` | `3.11` |
| `2.0%` | `+485.14%` | `-22.05%` | `62.13%` | `169` | `3.20` |
| `3.0%` | `+77.61%` | `-15.15%` | `60.00%` | `70` | `1.68` |
| `4.0%` | `+3.56%` | `-18.19%` | `52.38%` | `21` | `0.06` |

![Reversal 2.5 Minimum Drop Experiment](assets/reversal_2_5_min_drop_experiment.png)

### Stage 4: Leveraged ETF Overlay | 第四阶段：精选 Leveraged ETF Overlay

After fixing the `60d` factor and the `minimum current drop > 0.5%` filter, the next question was whether a very small number of leveraged ETFs should be allowed into the official universe. The research result was narrower than the original intuition: adding `SOXL` and `UPRO` consistently improved `1Y`, `2Y`, and `3Y` results, while `TQQQ` did not add stable incremental benefit once those two were already present. Reversal 3.1 therefore promotes a curated overlay, not a broad leveraged-ETF bucket.

在把 `60d` 因子和 `minimum current drop > 0.5%` 过滤都固定下来之后，下一步研究的问题是：是否应该允许极少数 leveraged ETF 进入官方 universe。结果比最初的直觉更窄：`SOXL` 和 `UPRO` 在 `1Y`、`2Y`、`3Y` 上都稳定改善了结果，而 `TQQQ` 在加入这两只之后并没有继续带来稳定增益。因此 Reversal 3.1 提升的是一个精选 overlay，而不是泛化的 leveraged ETF 大篮子。

Backtest window shown below (`1Y` comparison): `2025-03-31` to `2026-03-31`.

下图展示的回测区间（`1Y` 比较）：`2025-03-31` 至 `2026-03-31`。

- [leveraged ETF summary](results/reversal_3_1_leveraged_etf_experiment/reversal_3_1_leveraged_etf_summary.csv)
- [leveraged ETF robustness](results/reversal_3_1_leveraged_etf_experiment/reversal_3_1_leveraged_etf_robustness.csv)
- [leveraged ETF equity comparison](results/reversal_3_1_leveraged_etf_experiment/reversal_3_1_leveraged_etf_equity.csv)
- [leveraged ETF plot](assets/reversal_3_1_leveraged_etf_experiment.png)

| Variant | 1Y Return | 1Y Max DD | 1Y Win Rate | 1Y Sharpe |
|---|---:|---:|---:|---:|
| `baseline_qqq_only_filtered` | `+1136.44%` | `-44.17%` | `61.67%` | `3.76` |
| `plus_tqqq` | `+1148.88%` | `-44.13%` | `61.67%` | `3.78` |
| `plus_soxl` | `+1552.12%` | `-44.20%` | `62.92%` | `4.16` |
| `plus_upro` | `+1271.12%` | `-44.07%` | `62.08%` | `3.90` |
| `plus_soxl_upro` | `+1709.09%` | `-44.30%` | `63.33%` | `4.28` |
| `plus_tqqq_soxl_upro` | `+1707.90%` | `-44.30%` | `63.33%` | `4.28` |

![Reversal 3.1 Leveraged ETF Overlay Experiment](assets/reversal_3_1_leveraged_etf_experiment.png)

## Version History | 历代更新

The project keeps its optimization trail explicit rather than hiding earlier versions. The current path is:

本项目保留完整的优化路径，当前主线是：

Versioning rule: when the research definition changes materially, bump the main version; for smaller fixes or execution-only adjustments, increment the last segment only.

版本规则：研究口径发生实质变化时，提升主版本；若只是小修复或执行层微调，只增加最后一位。

- `2.3.3`: lock the best universe as `qqq_only_filtered`
- `2.4`: promote the `60d` observation window
- `2.5`: promote `minimum current drop > 0.5%`
- `3.1`: keep the `2.5` execution logic and upgrade the official universe to `qqq_plus_leverage_etfs`
- `3.2`: keep the `3.1` research configuration unchanged, add NYSE holiday protection, option-liquidity gating, share fallback execution, live position cash/value fields, the `spread <= 15%` option entry threshold, and the extended-hours take-profit / stop loss handling for share fallback
- `3.2.1`: keep the `3.2` strategy definition unchanged, but patch the live runner so off-hours checkpoints continue marking open positions and keep the dashboard/versioning flow consistent

Earlier notebook snapshots such as `versions/notebooks/Reversal2.5.3.ipynb`, `versions/notebooks/Reversal2.5.ipynb`, `versions/notebooks/Reversal2.4.ipynb`, `versions/notebooks/Reversal2.3.3.ipynb`, `versions/notebooks/Reversal2.3.2.ipynb`, and `versions/notebooks/Reversal2.3.1.ipynb` are retained for version-by-version review.

诸如 `versions/notebooks/Reversal2.5.3.ipynb`、`versions/notebooks/Reversal2.5.ipynb`、`versions/notebooks/Reversal2.4.ipynb`、`versions/notebooks/Reversal2.3.3.ipynb`、`versions/notebooks/Reversal2.3.2.ipynb`、`versions/notebooks/Reversal2.3.1.ipynb` 等旧版 notebook 都保留在仓库里，便于逐版本回看。

## License | 版权

This repository is released under an explicit `All Rights Reserved` copyright
notice. It is not an open-source project, and reuse, copying, modification,
distribution, or derivative work creation requires prior written permission.

本仓库采用明确的 `All Rights Reserved` 版权声明，并非开源项目；复制、修改、分发、
再发布或基于本仓库创建衍生作品，均需事先获得书面许可。

## Overview | 项目简介

This project focuses on identifying large intraday drawdowns, evaluating whether prices reverse over the next few trading days, and estimating the return distribution of related call-option trades.

本项目主要研究三件事：识别日内大幅下跌、评估未来几个交易日内的价格反转概率，以及估计相关看涨期权交易的收益分布。

The notebook works from CSV files stored under `reversal_data/`, Reversal 2.3 adds a dynamic universe builder, Reversal 2.3.1 adds a staged-entry options backtest plus universe-comparison scripts, Reversal 2.3.2 defaults the research flow to `qqq_only_filtered` with an in-notebook data-refresh step, Reversal 2.3.3 adds minimum-sample filtering plus top-15 ranked output, Reversal 2.4 promotes the `60d` observation window into the default research and official backtest setup, Reversal 2.5 adds the `minimum current drop > 0.5%` entry filter, Reversal 2.5.1 improves spot-price handling by preferring extended-hours prices when available, Reversal 2.5.2 adds current ATM call IV plus 20d rolling sigma to the live screener output, Reversal 2.5.3 consolidates that live screener into a cleaner single-table layout, Reversal 3.1 upgrades the official universe to `qqq_plus_leverage_etfs = qqq_only_filtered + SOXL + UPRO`, Reversal 3.2 adds NYSE holiday awareness to the live paper runner, and Reversal 3.2.1 relaxes the live option spread gate to `<= 15%` while extending share-fallback take-profit / stop loss scans into extended hours.

Notebook 通过 `reversal_data/` 目录下的 CSV 数据运行；Reversal 2.3 新增了动态股票池构建器，Reversal 2.3.1 新增了分批建仓的回测和股票池横向比较脚本，Reversal 2.3.2 把默认研究流程切到 `qqq_only_filtered` 并在 notebook 内加入了数据刷新步骤，Reversal 2.3.3 进一步加入了最小样本过滤和前 15 名输出，Reversal 2.4 把 `60d` 观察窗口正式提升为默认研究与官方回测设定，Reversal 2.5 加入了 `minimum current drop > 0.5%` 入场过滤，Reversal 2.5.1 把 spot 取价改成优先使用扩展时段价格，Reversal 2.5.2 把当前 ATM call IV 和 20d rolling sigma 接进了 live screener 输出，Reversal 2.5.3 把 live screener 的展示压缩成更清晰的单表布局，Reversal 3.1 把官方 universe 升级为 `qqq_plus_leverage_etfs = qqq_only_filtered + SOXL + UPRO`，Reversal 3.2 把 NYSE 节假日识别接进了 live paper runner，而 Reversal 3.2.1 则把 live option spread 门槛放宽到 `<= 15%`，并让 share fallback 在扩展时段继续执行止盈与止损扫描。

Before running the main analysis notebook, you can use `update_reversal_csv.ipynb` to download and refresh the input CSV files.

在运行主分析 notebook 之前，可以先使用 `update_reversal_csv.ipynb` 下载并更新输入用的 CSV 数据。

## Workflow | 推荐流程

1. Run `update_reversal_csv.ipynb` to download or refresh market data into `reversal_data/`.  
   先运行 `update_reversal_csv.ipynb`，把市场数据下载或更新到 `reversal_data/`。
2. Run `Reversal3.2.1.ipynb` for QQQ-plus-overlay universe construction, reversal success analysis, in-notebook CSV refresh, live setup screening, call-entry planning, option confidence intervals, GBM simulation, and rolling sigma plots.  
   再运行 `Reversal3.2.1.ipynb`，完成带精选 leveraged ETF overlay 的股票池构建、反转成功率分析、notebook 内 CSV 刷新、实时 setup 筛选、call 入场规划、期权置信区间、GBM 模拟和滚动波动率可视化。
3. Run `backtest_reversal_3_1_calls.py` for the official Reversal 3.2.1 call backtest under `qqq_plus_leverage_etfs + matched_signals >= 10 + 60d + minimum current drop > 0.5%`.  
   如果你想跑官方 Reversal 3.2.1 主回测，再运行 `backtest_reversal_3_1_calls.py`；这部分使用 `qqq_plus_leverage_etfs + matched_signals >= 10 + 60d + minimum current drop > 0.5%`。
4. Run `compare_reversal_2_3_3_universes.py` if you want to revisit the universe-selection stage under the original dynamic `matched_signals >= 10` filter.  
   如果你想回看 universe 选择阶段，再运行 `compare_reversal_2_3_3_universes.py`；这部分使用原始动态 `matched_signals >= 10` 过滤。
5. Run `backtest_reversal_article_variants.py` if you want to reproduce the article-inspired factor comparison that selected the `60d` window.  
   如果你想复现论文启发的因子对比并验证为什么最终选择 `60d` 窗口，再运行 `backtest_reversal_article_variants.py`。
6. Run `backtest_reversal_2_5_min_drop_experiment.py` if you want to reproduce the minimum-drop threshold sweep that selected the `0.5%` filter.  
   如果你想复现 minimum-drop 阈值比较，并验证为什么最终选择 `0.5%` 过滤，再运行 `backtest_reversal_2_5_min_drop_experiment.py`。
7. Read `RESEARCH_GUARDRAILS.md` before promoting any new factor, threshold, or story into an official version.  
   如果你想把新的因子、阈值或叙事升级成正式版本，先读 `RESEARCH_GUARDRAILS.md`。
8. Run `reversal_3_2_1_live.py` if you want the no-lookahead live paper-test pipeline with scheduled entry / exit scans and auto-generated GitHub dashboard files.  
   如果你想启用无未来函数的 live paper-test，并定时更新 GitHub dashboard，就运行 `reversal_3_2_1_live.py`。

## Notebook Contents | Notebook 内容

1. `Probability of Success Reversal`  
   Measures how often a ticker recovers after a large intraday drop using CSV data under `reversal_data/`.  
   使用 `reversal_data/` 中的 CSV 数据，统计个股在出现较大日内跌幅后，未来若干交易日内发生反弹的成功率。

2. `QQQ Plus Leveraged ETF Universe Builder`  
   Builds the default `qqq_plus_leverage_etfs` candidate pool from local QQQ constituents, filtered by minimum market cap and price, then adds the curated `SOXL + UPRO` overlay.  
   基于本地 QQQ 成分股构建默认的 `qqq_plus_leverage_etfs` 候选池，并在最小市值和股价过滤之后，加入精选的 `SOXL + UPRO` overlay。

3. `Live Reversal Setup Screener`  
   Uses today's near-real-time price to infer the current intraday drawdown for each ticker, applies an optional minimum current-drop filter, then measures how often similar or worse historical drops recovered a user-defined fraction of the signal-day drawdown within the next N trading days.  
   使用当日近实时价格推断每个 ticker 当前的日内跌幅，可选地叠加 minimum current-drop 过滤，再回看过去一段观察窗口内“至少同等严重”的历史下跌日，统计未来 N 个交易日内回补 signal-day 跌幅指定比例的成功率。

4. `Option Execution Planner for Call Entries`  
   Pulls option chains for the chosen ticker, filters toward near-ATM calls in the 21-40 trading-day range, and translates the strategy into reference entry, take-profit, and stop loss levels.  
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
  SOXL.csv
  UPRO.csv
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
jupyter notebook Reversal3.2.1.ipynb
```

To refresh the CSV data first, open:

如果你想先更新 CSV 数据，可以打开：

```bash
jupyter notebook update_reversal_csv.ipynb
```

Update the user-config sections inside each code cell to change:

你可以在各代码单元的用户配置区修改以下参数：

- Tickers | 股票列表
- Drop threshold, minimum current drop, and recovery target | 下跌触发阈值、minimum current drop 与反弹目标
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
- `update_reversal_data.py` | Refresh the default `qqq_plus_leverage_etfs` CSV datasets from Yahoo Finance. | 从 Yahoo Finance 刷新默认的 `qqq_plus_leverage_etfs` 所需 CSV 数据。
- `RESEARCH_GUARDRAILS.md` | Default research discipline for avoiding curve sculpting, weak narratives, and LLM-assisted overfitting. | 默认研究守则，用于避免曲线雕刻、伪机制叙事和 LLM 放大的过拟合。
- `reversal_3_2_1_live.py` | Reversal 3.2.1 live paper-test runner with scheduled entry/exit logic, state persistence, dashboard generation, optional GitHub publishing, the promoted `qqq_plus_leverage_etfs` live universe, NYSE holiday protection, and the current option-liquidity/share-fallback execution path. | Reversal 3.2.1 的 live paper-test 主脚本，包含定时入场/离场逻辑、状态持久化、dashboard 生成、可选的 GitHub 发布、升级后的 `qqq_plus_leverage_etfs` live universe、NYSE 节假日保护，以及当前的期权流动性门槛与 share fallback 执行路径。
- `Reversal3.2.1.ipynb` | Current main notebook with the official `qqq_plus_leverage_etfs` universe, the default `60d` observation window, `minimum current drop > 0.5%` live-screen filter, improved extended-hours spot pricing, ATM-IV versus rolling-sigma context, and a cleaner single-table live screener output. | 当前主 notebook，使用官方 `qqq_plus_leverage_etfs` universe，默认 `60d` 观察窗口，加入 `minimum current drop > 0.5%` 的 live-screen 过滤，优先使用扩展时段 spot 价格，并在 screener 输出中补充 ATM IV 与 rolling sigma 对照，同时把 live screener 压缩成更清晰的单表输出。
- `versions/notebooks/` | Archived notebook snapshots from `Reversal2.0` through `Reversal3.2`, kept for version-by-version review without cluttering the repo root. | 历史 notebook 快照目录，收纳从 `Reversal2.0` 到 `Reversal3.2` 的版本，便于逐版本回看，同时避免根目录混杂。
- `versions/notebooks/README.md` | Snapshot index for the archived notebook history. | 历史 notebook 快照索引。
- `backtest_reversal_2_3_calls.py` | Reversal 2.3 call backtest with top-2 daily ranking, weighted sizing, and broad universe selection. | Reversal 2.3 的 call 回测脚本，包含每日前二打分、加权仓位和广义股票池。
- `backtest_reversal_2_3_1_calls.py` | Reversal 2.3.1 call backtest with staggered 50% entries and up to two concurrent positions. | Reversal 2.3.1 的 call 回测脚本，采用分批 50% 建仓和最多两个同时持仓。
- `backtest_reversal_2_3_3_calls.py` | Official Reversal 2.3.3 call backtest with `qqq_only_filtered` and the original dynamic `matched_signals >= 10` trade gate. | Reversal 2.3.3 的官方 call 回测脚本，默认使用 `qqq_only_filtered`，并沿用最初的动态 `matched_signals >= 10` 交易门槛。
- `backtest_reversal_2_4_calls.py` | Official Reversal 2.4 call backtest with the promoted `60d` observation window. | Reversal 2.4 的官方 call 回测脚本，使用提升后的 `60d` 观察窗口。
- `backtest_reversal_2_5_calls.py` | Official Reversal 2.5 call backtest with the promoted `60d` observation window and `minimum current drop > 0.5%` filter. | Reversal 2.5 的官方 call 回测脚本，使用提升后的 `60d` 观察窗口和 `minimum current drop > 0.5%` 过滤。
- `backtest_reversal_3_1_calls.py` | Official Reversal 3.2.1 call backtest with the curated `qqq_plus_leverage_etfs` overlay, the promoted `60d` observation window, and the `minimum current drop > 0.5%` filter. | Reversal 3.2.1 的官方 call 回测脚本，使用精选的 `qqq_plus_leverage_etfs` overlay、提升后的 `60d` 观察窗口和 `minimum current drop > 0.5%` 过滤。
- `backtest_reversal_3_1_leveraged_etf_experiment.py` | Controlled leveraged-ETF overlay comparison across `TQQQ`, `SOXL`, `UPRO`, and their combinations on top of the official 2.5 setup. | 受控的 leveraged ETF overlay 比较脚本，在官方 2.5 设定之上测试 `TQQQ`、`SOXL`、`UPRO` 及其组合。
- `backtest_reversal_article_variants.py` | Article-inspired factor comparison across volume, PCA, kappa / s-score, and rolling-window variants. | 论文启发的因子比较脚本，横向测试成交量、PCA、kappa / s-score 和不同滚动窗口。
- `backtest_reversal_2_5_min_drop_experiment.py` | Minimum-drop threshold comparison that tests `0.0%` through `4.0%` filters on top of the `60d + qqq_only_filtered` setup. | minimum-drop 阈值比较脚本，在 `60d + qqq_only_filtered` 设定上测试 `0.0%` 到 `4.0%` 的过滤门槛。
- `compare_reversal_2_3_1_universes.py` | Compare Reversal 2.3.1 across multiple ticker-list universes. | 比较 Reversal 2.3.1 在多个股票池下的表现。
- `compare_reversal_2_3_3_universes.py` | Official five-universe comparison under Reversal 2.3.3 using the dynamic `matched_signals >= 10` filter. | Reversal 2.3.3 下的官方五组 universe 对比脚本，使用动态 `matched_signals >= 10` 过滤。
- `reversal_universe.py` | Shared universe builder used by notebook, backtest, and live paper trading, including the curated `qqq_plus_leverage_etfs` preset. | notebook、回测和 live paper trading 共用的 universe 构建模块，包含精选的 `qqq_plus_leverage_etfs` preset。
- `qqq_plus_leverage_etfs_tickers.csv` | Saved ticker list for the promoted Reversal 3.2.1 universe overlay. | Reversal 3.2.1 官方 overlay universe 的保存版 ticker 列表。
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
