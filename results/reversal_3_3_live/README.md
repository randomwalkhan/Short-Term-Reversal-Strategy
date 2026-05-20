# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 14:25:01 EDT`
Last processed slot: `manage_1430`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  FTNT     option         option FTNT260717C00125000     14          2026-05-20         2026-05-20        8.825       10.15 1855.0   15.014164 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.86               28            0.76              1.61        301.62                69.06         0.632            pass              0.768             80.7                           0.496                3.65              0.562                                 ok            True                  False
   KDP           88.89               27            0.81              0.16         28.78                34.80         0.528            pass              0.569             55.2                           0.331                0.19              0.118                                 ok            True                  False
  TEAM           91.30               46            0.15              0.09         86.58               114.61         0.650            pass              0.858             97.1                           0.835               -2.60             -0.461 downtrend_blocked_slope_and_streak           False                  False
   WMT          100.00                5            2.12              1.99        133.35                20.68         0.537            pass              0.565             37.1                           0.276                1.17              0.299                                 ok           False                  False
    EA           91.67               24            0.26              0.37        201.54                 2.97         0.504            pass              0.596             47.0                           0.469                0.19              0.039                                 ok           False                  False
  TMUS           80.95               21            1.59              2.15        192.50                36.70         0.497 below_threshold              0.251             34.1                           0.428               -1.45             -0.202                                 ok           False                  False
   TRI           69.23               13            2.26              1.38         86.76                57.28         0.494 below_threshold              0.226             52.2                           0.537               -6.94             -0.884 downtrend_blocked_slope_and_streak           False                  False
  CTSH           90.00               40            0.12              0.04         50.86                50.98         0.486 below_threshold              0.806             96.9                           0.739               -0.30             -0.171                                 ok           False                  False
  SNPS           97.14               35            0.77              2.65        492.74                41.71         0.483 below_threshold              0.858             81.2                           0.578               -2.84             -0.365 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.24               41            0.31              0.84        387.30                41.27         0.481 below_threshold              0.745             74.7                           0.746               -2.91             -0.187                                 ok           False                  False
  GOOG           89.19               37            0.53              1.42        384.29                41.08         0.480 below_threshold              0.649             58.5                           0.570               -3.11             -0.206           downtrend_blocked_streak           False                  False
  ADSK           90.32               31            0.95              1.62        243.47                38.52         0.475 below_threshold              0.700             78.9                           0.598               -0.51             -0.135                                 ok           False                   True
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-20T12:00:03.589849-04:00 early_entry_1200 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:55:04.978899-04:00 early_entry_1155 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:50:01.042142-04:00 early_entry_1150 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:45:06.973921-04:00 early_entry_1145 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00 early_entry_1140 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:40:04.008173-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "FTNT260717C00125000", "fill_price": 10.15, "pnl": 1855.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.01, "ticker": "FTNT"}
2026-05-20T11:35:01.033169-04:00 early_entry_1135 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:30:01.977277-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:25:06.020090-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520142501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520142501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520142501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520142501)

</details>
