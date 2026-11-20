# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:55:04 EST`
Last processed slot: `manage_1100`

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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           91.67               24            1.68              2.97        250.49                49.35         0.507          pass              0.585             43.3                           0.379               -0.31             -0.341                                 ok            True                  False
  INTC           64.29               28            2.26              0.88         55.34               141.91         0.776          pass              0.383             61.8                           0.404               -3.23             -0.864 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.84             15.50        372.38               122.37         0.705          pass              0.507             12.1                           0.181               -8.78             -0.713 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.78               45            0.02              0.09        689.61                78.44         0.692          pass              0.948             92.9                           0.475                1.99             -0.020                                 ok           False                  False
  FTNT           76.92               26            2.15              1.98        130.61                96.17         0.659          pass              0.280             35.7                           0.360                8.24              0.697                                 ok           False                  False
  QCOM           84.00               25            1.60              1.81        161.23                69.46         0.586          pass              0.397             43.9                           0.308               -3.62             -0.749 downtrend_blocked_slope_and_streak           False                  False
  MCHP           78.95               19            2.67              1.09         58.00                78.21         0.574          pass              0.227             36.6                           0.306               -2.47             -0.460            downtrend_blocked_slope           False                  False
  UPRO           80.00                5            3.37              2.78        116.70                72.20         0.572          pass              0.106             16.3                           0.143              -11.65             -1.632 downtrend_blocked_slope_and_streak           False                  False
   BKR           66.67               12            2.52              0.82         46.32                56.86         0.561          pass              0.088              6.3                           0.085               -4.51             -0.446 downtrend_blocked_slope_and_streak           False                  False
  CSCO           70.00               20            1.44              0.96         94.29                50.60         0.549          pass              0.198             25.4                           0.173               -0.55             -0.375                                 ok           False                  False
   TXN          100.00                2            4.12              8.24        282.22                59.73         0.548          pass              0.512             19.0                           0.269               -1.22             -0.394                                 ok           False                  False
   ADI          100.00                5            4.19             11.07        372.70                64.58         0.546          pass              0.517             20.9                           0.286               -0.53             -0.443                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                           detail
2026-11-20T10:55:04.962322-05:00 early_entry_1055 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:50:06.269299-05:00 early_entry_1050 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:45:05.890117-05:00 early_entry_1045 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:40:06.786688-05:00 early_entry_1040 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:35:04.912768-05:00 early_entry_1035 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:30:06.085636-05:00 early_entry_1030 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:25:04.965468-05:00 early_entry_1025 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120105504)

</details>
