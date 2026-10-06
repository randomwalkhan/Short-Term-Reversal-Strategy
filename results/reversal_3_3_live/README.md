# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 12:05:06 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           84.00               25            2.04              0.88         61.29                49.40         0.537            pass              0.287              9.0                           0.198               -5.05             -0.188                                 ok            True                  False
  ASML           80.00               30            0.88             11.44       1854.96                40.48         0.535            pass              0.267             26.8                           0.327                5.47              0.781                                 ok            True                  False
  ABNB           80.95               21            1.60              1.84        163.28                40.56         0.529            pass              0.193             13.7                           0.233               -0.23              0.578                                 ok            True                  False
  TMUS           87.88               33            0.51              0.59        164.39                30.04         0.507            pass              0.558             47.8                           0.465                0.85             -0.072                                 ok            True                  False
  MPWR           91.18               34            0.47              4.91       1477.78                53.63         0.580            pass              0.746             76.5                           0.548                6.84              0.827                                 ok           False                  False
  QCOM           90.24               41            0.07              0.09        180.75                57.17         0.571            pass              0.805             91.4                           0.651               -8.88             -1.080 downtrend_blocked_slope_and_streak           False                  False
  INTC           86.21               29            2.38              1.93        115.36                74.54         0.539            pass              0.346              0.0                           0.043               -8.42             -0.786 downtrend_blocked_slope_and_streak           False                  False
  AMAT           82.76               29            1.98              7.52        539.06                48.32         0.497 below_threshold              0.306             18.7                           0.351               12.50              1.580                                 ok           False                  False
  TEAM          100.00               39            0.69              0.95        196.24                55.00         0.490 below_threshold              0.825             60.9                           0.459                3.52              0.143                                 ok           False                  False
  MCHP           92.86               42            0.23              0.13         81.43                36.65         0.482 below_threshold              0.694             34.5                           0.188                7.23              0.819                                 ok           False                  False
  DXCM          100.00                5            2.65              1.61         86.21                23.46         0.478 below_threshold              0.517             23.1                           0.428               -5.51             -0.371 downtrend_blocked_slope_and_streak           False                  False
  CTSH           94.29               35            0.60              0.25         58.06                45.68         0.476 below_threshold              0.847             83.9                           0.404               -1.47              0.056                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-06T12:00:05.410645-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:55:05.274079-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:50:04.350583-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:45:06.217443-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:40:04.013409-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006120506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006120506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006120506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006120506)

</details>
