# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:15:04 EST`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   APP           93.75               16            3.06              8.90        411.41               119.50         0.799          pass              0.513              9.0                           0.157               63.95              4.167                                 ok            True                  False
  FTNT           81.08               37            1.04              0.90        122.89                92.89         0.677          pass              0.368             30.4                           0.199               -4.78             -0.098                                 ok            True                  False
   ROP           84.21               19            1.27              4.32        481.87                41.88         0.602          pass              0.346             37.9                           0.526                0.84             -0.071                                 ok            True                  False
  QCOM           84.00               25            1.54              1.82        167.74                68.75         0.601          pass              0.345             26.1                           0.233                0.91              0.354                                 ok            True                  False
   CSX           80.95               21            0.98              0.36         51.88                34.26         0.576          pass              0.223             22.1                           0.225                1.58              0.277                                 ok            True                  False
   CEG           90.62               32            1.30              2.53        276.73                60.48         0.569          pass              0.586             33.1                           0.237                4.26              1.285                                 ok            True                  False
   ADP           87.50               24            0.79              1.73        312.69                28.40         0.549          pass              0.495             49.0                           0.635                5.05              0.405                                 ok            True                  False
  SOXL           68.75               32            1.34              0.46         48.56               265.45         0.949          pass              0.447             68.4                           0.323              -34.21             -1.281 downtrend_blocked_slope_and_streak           False                  False
  INTC           70.97               31            1.69              0.66         55.16               143.34         0.823          pass              0.396             58.0                           0.479               -9.98             -0.096           downtrend_blocked_streak           False                  False
  ALNY           75.76               33            1.47              1.64        159.03               110.59         0.739          pass              0.315             29.3                           0.253               -1.57              0.067                                 ok           False                  False
  DRAM           58.33               24            2.01              0.55         39.03               109.09         0.717          pass              0.216             16.8                           0.219              -19.23             -0.848 downtrend_blocked_slope_and_streak           False                  False
  LRCX           67.50               40            0.64              0.94        210.43               105.03         0.698          pass              0.436             55.5                           0.292               -9.20              0.263           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-11-17T10:15:04.834585-05:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:05:06.251834-05:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:00:06.465677-05:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T09:50:06.673535-05:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "QCOM261218C00170000", "fill_price": 10.0125, "pnl": -5785.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "QCOM"}
2026-11-17T00:00:04.730535-05:00     data_refresh       data_refresh                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117101504)

</details>
