# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 12:25:04 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$65,421.80`
- Equity: `$136,049.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$-1,642.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 70627.5          1.1           1.08       44.42         44.46          bid_ask_mid                       1.08                bid_ask_mid                    True         -1642.5                  -2.27          80.0               15              0.97         20.09           21.19                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   ADP           84.62               13            1.25              2.65        303.02                24.93         0.544            pass              0.197              0.0                           0.198                9.70              1.099                      ok            True                  False
   KHC           90.00               30            0.52              0.09         24.76                34.81         0.535            pass              0.553             33.3                           0.359                9.89              1.090                      ok            True                  False
  TEAM          100.00               12            3.14              5.00        225.47                47.89         0.511            pass              0.486              7.3                           0.090                6.12              0.958                      ok            True                  False
  TMUS           81.48               27            0.73              0.75        146.22                64.13         0.645            pass              0.395             59.2                           0.327               -4.21             -0.399 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.25              0.56         63.56                25.23         0.579            pass              0.331             24.3                           0.408                1.97              0.327                      ok           False                  False
  CTSH          100.00                9            3.12              1.54         69.88                46.28         0.526            pass              0.457              1.3                           0.156               14.51              1.707                      ok           False                  False
   KDP           96.97               33            0.12              0.03         34.67                26.07         0.520            pass              0.866             86.9                           0.723                5.77              0.654                      ok           False                  False
  MSTR           88.00               25            2.52              2.58        144.91                68.80         0.506            pass              0.538             57.9                           0.448               -6.78             -0.357 downtrend_blocked_slope           False                  False
   PEP           83.87               31            0.16              0.15        135.70                25.03         0.502            pass              0.410             38.9                           0.242                7.00              0.841                      ok           False                  False
  VRTX           66.67                9            2.13              7.82        520.58                29.59         0.500            pass              0.120             23.5                           0.450                1.14              0.606                      ok           False                  False
 CMCSA          100.00                2            2.78              0.44         22.50                23.68         0.499 below_threshold              0.457              2.3                           0.126                6.67              0.863                      ok           False                  False
  AAPL           89.47               19            1.03              2.50        346.65                16.45         0.496 below_threshold              0.502             46.6                           0.306                0.93              0.152                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-26T12:00:05.800227-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:55:06.449404-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:50:05.011949-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:45:06.813895-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:40:04.884003-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:35:03.795292-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:30:06.493290-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:25:06.575832-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:20:06.988273-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:15:05.995279-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026122504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026122504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026122504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026122504)

</details>
